# NEON_VISION: OpenClaw × xAI Grok Imagine Skills Pack

![Cyberpunk banner placeholder - replace with your generated East La Mirada nightscape](https://via.placeholder.com/1200x400/0a0a0a/00ff9f?text=NEON+VISION+-+Grok+Imagine+for+OpenClaw)

**By CyberBitPunk2140**  
*East La Mirada Node • February 2026*

A **cyberpunk-grade** pair of native skills that turn your local OpenClaw agent into a full-powered xAI Grok Imagine studio.

Generate insane images and cinematic videos with native audio — right from your terminal, Telegram, or wherever your Claw runs. No cloud wrappers. No bullshit. Just pure Grok power.

---

## 🌌 Why These Skills Exist

You already know Grok Imagine (image) and Grok Imagine Video are some of the best creative models on the planet right now (Jan 28 2026 release).  

I wanted them **inside** my OpenClaw agent with:
- Zero extra dependencies
- Local saving (~/Pictures + ~/Videos)
- Full CLI arguments (duration, aspect, resolution)
- Automatic OpenClaw display/attachment
- Cyberpunk workflow baked in

So I built them. Now you have them.

---

## ✨ Features

### grok-imagine (Image Skill)
- Model: `grok-imagine-image`
- Text-to-image + multi-turn refinement
- Excellent text-in-image, uncensored style, fast
- Saves as high-quality JPG with timestamp
- Auto-folder: `~/Pictures/Grok-Images/`

### grok-imagine-video (Video Skill)
- Model: `grok-imagine-video` (official xAI)
- Text-to-video + native audio (SFX, music, voice, ambient)
- Image-to-video & video editing ready for v2
- Duration 1–15s, 480p/720p, 16:9 / 9:16 / 1:1
- Asynchronous polling + auto-download
- Saves as MP4 with timestamp
- Auto-folder: `~/Videos/Grok-Videos/`

**Both skills:**
- One shared `XAI_API_KEY`
- Full SKILL.md metadata for ClawHub compatibility
- Clean error handling & progress feedback
- Cyberpunk-flavored example prompts in the docs

---

## 🛠️ Prerequisites

1. **OpenClaw** installed and running (latest version)
2. **xAI API key** with image + video generation access:
   - Go to https://console.x.ai → API Keys → Create new key
   - Add to your OpenClaw config:
     ```bash
     # ~/.openclaw/openclaw.json or env
     {
       "env": {
         "XAI_API_KEY": "xai-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
       }
     }
