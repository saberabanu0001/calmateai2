# Deploy CalmMateAI to Render.com

Use this when setting up your **Web Service** on Render.

---

## 1. Region

- **What it is:** The physical location of the server (data center) where your app runs.
- **What it affects:** 
  - **Latency:** Users closer to that region get slightly faster responses.
  - **Data residency:** Your app and its traffic are processed in that country/region.
- **Your choice (Oregon, US West):** Good default. Anyone in the world can use the app; US West is a common choice. You can leave it as is.

You can change region later in **Settings** if you want.

---

## 2. Root Directory

- **Leave blank** if your repo root is the project root (i.e. `app.py`, `requirements.txt`, `Procfile` are at the top level of the repo).
- Only set a root directory if your Flask app lives in a subfolder (e.g. `backend/`). For CalmMateAI, leave it **empty**.

---

## 3. Build & Start Commands

Render can auto-detect from your **Procfile**. If you set them manually:

| Field | Value |
|-------|--------|
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app --bind 0.0.0.0:$PORT` |

Note: **gunicorn** (not “unicorn”). If you typed “unicorn”, change it to **gunicorn**.

Your existing `Procfile` is:
```
web: gunicorn app:app --workers 2 --threads 4 --timeout 120 --bind 0.0.0.0:$PORT
```
Render uses this when you choose “Procfile” as the start command. Otherwise use the start command in the table above (single worker is fine for free tier).

---

## 4. Environment Variables (Required)

Add these in Render: **Dashboard → Your Service → Environment** (or during creation).

| Key | Value | Notes |
|-----|--------|------|
| `FLASK_SECRET_KEY` | (any long random string) | e.g. generate one: 32+ random characters. Used for sessions. |
| `CONVEX_URL` | `https://brazen-camel-323.convex.cloud` | **Production Convex backend.** Use this exact URL so production uses Convex in the cloud. |
| `GROQ_API_KEY` | (your Groq API key) | Needed for AI chat. Copy from your local `.env` if you use Groq. |

Optional (add if you use them):

| Key | Value |
|-----|--------|
| `GEMINI_API_KEY` | (your Gemini key, or leave empty) |
| `PORT` | Do **not** set. Render sets this automatically. |

**Important:** Do **not** copy your whole `.env` or `.env.local` into Render. Add only the variables above. Never commit real keys to GitHub.

---

## 5. Advanced – Secret Files

- **What it is:** For uploading whole *files* that contain secrets (e.g. a JSON key file for Google Cloud).
- **For this project:** You don’t have any secret *files*. All secrets are in **environment variables** (step 4). So you can **leave “Secret Files” empty**.

---

## 6. After Deploy

1. Open the URL Render gives you (e.g. `https://calmateai-xxxx.onrender.com`).
2. Register a test user and log in.
3. In Convex Dashboard → **Data** → **users**, you should see the new user (production uses `brazen-camel-323.convex.cloud`).

---

## 7. If the App Crashes or Doesn’t Start

- Check **Logs** in the Render dashboard for errors.
- Typical issues:
  - Wrong **Start Command** (e.g. “unicorn” instead of “gunicorn”).
  - Missing **CONVEX_URL** or wrong value (must be `https://brazen-camel-323.convex.cloud` for production).
  - Missing **FLASK_SECRET_KEY**.
