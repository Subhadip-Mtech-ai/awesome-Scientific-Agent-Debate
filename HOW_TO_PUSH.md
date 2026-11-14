# How to Push to GitHub

## Step 1: Create a GitHub repository

1. Go to https://github.com/new
2. Repository name: `hypothesis-ablation`
3. Description: `Controlled ablation study: Single-LLM vs Multi-Agent Debate for scientific hypothesis generation (IIITA AI Tools for Research)`
4. Set to **Public**
5. Do NOT initialize with README (we already have one)
6. Click **Create repository**

## Step 2: Create a Personal Access Token (PAT)

1. Go to https://github.com/settings/tokens/new
2. Note: `hypothesis-ablation push`
3. Expiration: 7 days
4. Scopes: check `repo`
5. Click **Generate token**
6. Copy the token (starts with `ghp_...`)

## Step 3: Add remote and push

Open a terminal in:
`C:\Users\hp\.gemini\antigravity\scratch\hypothesis-ablation`

Then run:
```powershell
# Replace YOUR_USERNAME and YOUR_TOKEN with actual values
git remote add origin https://YOUR_USERNAME:YOUR_TOKEN@github.com/YOUR_USERNAME/hypothesis-ablation.git
git branch -M main
git push -u origin main
```

## Expected output
```
Enumerating objects: 24, done.
Counting objects: 100% (24/24), done.
Writing objects: 100% (24/24), done.
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

## Alternative: Use GitHub Desktop

1. Download GitHub Desktop: https://desktop.github.com/
2. File > Add Local Repository
3. Navigate to `C:\Users\hp\.gemini\antigravity\scratch\hypothesis-ablation`
4. Click Publish repository
