Grok Imagine Skills for OpenClaw
This repository contains two skills that add xAI Grok Imagine image and video generation to OpenClaw.

grok-imagine — text-to-image generation
grok-imagine-video — text-to-video generation with audio

Prerequisites

xAI API key with image and video generation access
Get it at: https://console.x.ai
Set the key in ~/.openclaw/.env:
XAI_API_KEY="api-key"
Add it to OpenClaw config (example in ~/.openclaw/openclaw.json):
{
  "env": {
    "XAI_API_KEY": "$X_API_KEY"
  }
}

Python requests package (pip install requests if missing)

Installation

Clone or download the repository.
Copy the two skill folders into your OpenClaw skills directory:
cp -r grok-imagine ~/.openclaw/skills/
cp -r grok-imagine-video ~/.openclaw/skills/
Reload skills:
openclaw reload skills
(or restart OpenClaw)

Usage
Once loaded, trigger the skills naturally in chat:
Image example:
Generate an image of a cyberpunk city at night
Use grok-imagine to create [your prompt]
Video example:
Generate a 10-second video of East La Mirada at midnight, neon rain
Use grok-imagine-video: [prompt] --duration 10 --aspect 16:9
Each folder contains a SKILL.md with full instructions and the Python helper script.

Repository Structure
.
├── grok-imagine/
│   ├── SKILL.md
│   └── generate_image.py
├── grok-imagine-video/
│   ├── SKILL.md
│   └── generate_video.py
└── README.md

Troubleshooting
"XAI_API_KEY not found" → check your openclaw.json and reload
Video generation takes time → normal (30–180 seconds)
Skill not appearing → run openclaw reload skills or restart

License
MIT License — free to use, modify, and distribute.
