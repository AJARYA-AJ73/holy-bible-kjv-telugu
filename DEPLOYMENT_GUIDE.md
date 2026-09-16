# 24/7 Free Cloud Hosting Guide for AJARYA-AJ73

This guide explains step-by-step how your Holy Bible web platform is hosted on the cloud for free, running 24/7/365 under your own GitHub account: **`AJARYA-AJ73`**.

---

## ??? Step 1: Create an Empty Repository on GitHub

1. Open your browser and log into GitHub: [https://github.com/new](https://github.com/new)
2. In **Repository name**, type:
   ```
   holy-bible-kjv-telugu
   ```
3. Choose **Public** (or Private, both work).
4. **Important**: Leave "Add a README file", ".gitignore", and "Choose a license" **UNCHECKED** (we already created all of them).
5. Click the green button: **Create repository**.

---

## ?? Step 2: Push Your Code to Your GitHub Account

Open your terminal or PowerShell inside `C:\Users\ajaryapaul\OneDrive\Desktop\BIBLE` and run:

```bash
git remote add origin https://github.com/AJARYA-AJ73/holy-bible-kjv-telugu.git
git push -u origin main
```
*(Windows will pop up a quick GitHub browser login window once to authenticate you).*

---

## ?? Step 3: Deploy 24/7 on Render.com (100% Free)

1. Go to [https://dashboard.render.com](https://dashboard.render.com) and click **Sign in with GitHub**.
2. Click **New +** (top right) and select **Web Service**.
3. Choose **Build and deploy from a Git repository**, then select your repository:
   ```
   holy-bible-kjv-telugu
   ```
4. Render will auto-detect everything from `render.yaml` and `requirements.txt`:
   * **Name**: `holy-bible-kjv-telugu`
   * **Runtime**: `Python`
   * **Build Command**: `pip install -r requirements.txt`
   * **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   * **Instance Type**: **Free**
5. Click **Create Web Service**.

---

## ?? Step 4: Your Website is Live 24/7!

In about 2 minutes, Render will provide your permanent public HTTPS address:
```
https://holy-bible-kjv-telugu.onrender.com
```
* **Always Online**: Works 24/7 even when your laptop is completely turned off.
* **Worldwide Access**: You, your family, or anyone across the world can open it from any mobile phone, iPhone, Android, tablet, or PC!
