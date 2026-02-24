#!/usr/bin/env python3
"""
x_search.py — Search X/Twitter using xAI Grok's native x_search tool via xai-sdk.

Usage:
    x_search.py "query" [flags...]

Outputs JSON by default. Use --text for plain text output.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone


def load_env_file(path):
    """Manually parse a .env file and set env vars (no python-dotenv needed)."""
    if not os.path.isfile(path):
        return
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip()
            # Strip surrounding quotes
            if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
                value = value[1:-1]
            # Only set if not already in environment
            if key not in os.environ:
                os.environ[key] = value


def parse_handles(raw):
    """Parse comma-separated handles, stripping @ prefix."""
    if not raw:
        return None
    handles = [h.strip().lstrip("@") for h in raw.split(",") if h.strip()]
    return handles if handles else None


def parse_date(raw):
    """Parse YYYY-MM-DD string to datetime."""
    if not raw:
        return None
    try:
        return datetime.strptime(raw, "%Y-%m-%d")
    except ValueError:
        print(f"Error: Invalid date format '{raw}'. Expected YYYY-MM-DD.", file=sys.stderr)
        sys.exit(1)


def build_args():
    parser = argparse.ArgumentParser(
        description="Search X/Twitter using xAI Grok's x_search tool (xai-sdk)."
    )
    parser.add_argument("query", help="Search query")
    parser.add_argument("--model", default="grok-4-1-fast", help="Model ID (default: grok-4-1-fast)")
    parser.add_argument("--handles", default=None, help="Allowed X handles, comma-separated")
    parser.add_argument("--exclude-handles", default=None, help="Excluded X handles, comma-separated")
    parser.add_argument("--from", dest="from_date", default=None, help="From date YYYY-MM-DD")
    parser.add_argument("--to", dest="to_date", default=None, help="To date YYYY-MM-DD")
    parser.add_argument("--days", type=int, default=None, help="Shorthand: from_date = today minus N days")
    parser.add_argument("--images", action="store_true", help="Enable image understanding")
    parser.add_argument("--videos", action="store_true", help="Enable video understanding")
    parser.add_argument("--raw", action="store_true", help="Dump raw response to stderr")
    parser.add_argument("--text", action="store_true", help="Output plain text instead of JSON")

    return parser.parse_args()


def main():
    # Load .env before anything else
    env_path = os.path.expanduser("~/.openclaw/.env")
    load_env_file(env_path)

    args = build_args()

    api_key = os.environ.get("XAI_API_KEY")
    if not api_key:
        print("Error: XAI_API_KEY not found in environment or ~/.openclaw/.env", file=sys.stderr)
        sys.exit(1)

    # Import SDK
    try:
        from xai_sdk import Client
        from xai_sdk.chat import user
        from xai_sdk.tools import x_search
    except ImportError as e:
        print(f"Error: Failed to import xai-sdk: {e}", file=sys.stderr)
        print("Make sure xai-sdk is installed in the venv.", file=sys.stderr)
        sys.exit(1)

    # Build x_search tool with filters
    try:
        tool_kwargs = {}

        # Handles
        handles = parse_handles(args.handles)
        if handles:
            tool_kwargs["allowed_x_handles"] = handles
        excluded = parse_handles(args.exclude_handles)
        if excluded:
            tool_kwargs["excluded_x_handles"] = excluded

        # Dates
        from_dt = parse_date(args.from_date)
        to_dt = parse_date(args.to_date)

        if args.days and not from_dt:
            from_dt = datetime.now(timezone.utc) - timedelta(days=args.days)

        if from_dt:
            tool_kwargs["from_date"] = from_dt
        if to_dt:
            tool_kwargs["to_date"] = to_dt

        # Image/video understanding
        if args.images:
            tool_kwargs["enable_image_understanding"] = True
        if args.videos:
            tool_kwargs["enable_video_understanding"] = True

        tool = x_search(**tool_kwargs)
    except Exception as e:
        print(f"Error building x_search tool: {e}", file=sys.stderr)
        sys.exit(1)

    # Create client and chat
    try:
        client = Client(api_key=api_key)
        chat = client.chat.create(
            model=args.model,
            tools=[tool],
        )
        chat.append(user(args.query))
    except Exception as e:
        print(f"Error creating chat: {e}", file=sys.stderr)
        sys.exit(1)

    # Stream response
    full_text = ""
    final_response = None
    try:
        for response, chunk in chat.stream():
            final_response = response
            if chunk.content:
                full_text += chunk.content
    except Exception as e:
        print(f"Error during streaming: {e}", file=sys.stderr)
        sys.exit(1)

    if final_response is None:
        print("Error: No response received from API.", file=sys.stderr)
        sys.exit(1)

    # Extract citations
    citations = list(final_response.citations) if final_response.citations else []

    # Raw debug output
    if args.raw:
        try:
            raw_data = {
                "id": getattr(final_response, "id", None),
                "role": getattr(final_response, "role", None),
                "content": getattr(final_response, "content", None),
                "finish_reason": getattr(final_response, "finish_reason", None),
                "citations": citations,
                "tool_calls": str(getattr(final_response, "tool_calls", None)),
                "tool_outputs": str(getattr(final_response, "tool_outputs", None)),
                "usage": str(getattr(final_response, "usage", None)),
            }
            print(json.dumps(raw_data, indent=2, default=str), file=sys.stderr)
        except Exception as e:
            print(f"[raw dump error: {e}]", file=sys.stderr)

    # Output
    if args.text:
        print(full_text)
    else:
        output = {
            "query": args.query,
            "response": full_text,
            "citations": citations,
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
