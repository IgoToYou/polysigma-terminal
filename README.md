# Polysigma Terminal - Deployment Guide

## Local Deployment

```bash
cd polysigma_backup
python3 server.py 8765
# Open http://localhost:8765
```

## Vercel Deployment

1. Go to https://vercel.com/new
2. Import from GitHub → select `IgoToYou/polysigma-terminal`
3. Click Deploy
4. Done! You get a `.vercel.app` URL

## Render Deployment

1. Go to https://render.com/static
2. Connect GitHub → select repo
3. Settings:
   - Build command: leave empty
   - Publish directory: /
4. Deploy

## Cloudflare Pages

1. Go to https://pages.cloudflare.com/
2. Create project → connect GitHub
3. Select repo `polysigma-terminal`
4. Build command: leave empty
5. Deploy

## How it works

- `polysigma_terminal_full.html` — the complete trading terminal (306KB)
- HTML contains `window.ENV_API_URL = 'https://terminal.polysigma.io'` — all API calls go directly to real terminal API
- No backend needed — pure static HTML
- Auth gate is hidden via CSS patch — works without login