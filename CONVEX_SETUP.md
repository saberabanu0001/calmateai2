# Using Convex as the database for CalmMateAI

When **CONVEX_URL** is set in your environment, the app stores user data in [Convex](https://convex.dev) instead of SQLite.

---

## Why Convex?

- **Hosted** – No database server to run; data lives in Convex’s cloud.
- **Real-time** – Convex can push live updates (handy for future features).
- **Same app code** – Registration, login, and profile updates work the same; only the backend (Convex vs SQLite) changes.

---

## One-time setup

### 1. Install Node.js

Convex’s backend (schema + functions) is defined with the Convex CLI, which uses Node.  
Install from [nodejs.org](https://nodejs.org) if you don’t have it.

### 2. Install Convex backend and Python client

```bash
# From project root
npm init -y
npm install convex

pip install convex
```

### 3. Log in and create a Convex project

```bash
npx convex dev
```

- Log in (e.g. with GitHub) if prompted.
- Create a new project and pick a name.
- This will create a `convex/` folder and a **deployment URL** (e.g. `https://happy-otter-123.convex.cloud`).

### 4. Set your deployment URL

After `npx convex dev` runs once, it will write a Convex URL into `.env.local` (or you can copy it from the Convex dashboard).

Add the same URL to your app’s `.env`:

```env
CONVEX_URL=https://your-deployment-name.convex.cloud
```

Use the **deployment URL** from the Convex dashboard or from the `npx convex dev` output.

### 5. Run the Convex backend (when developing)

Keep the Convex backend in sync while you develop:

```bash
npx convex dev
```

Leave this running in a terminal. It pushes your `convex/` schema and functions to Convex.

### 6. Run the Flask app

In another terminal:

```bash
source venv/bin/activate
python app.py
```

With **CONVEX_URL** set, the app will use Convex for user storage (registration, login, profile).

---

## What’s in `convex/`

- **convex/schema.js** – Defines the `users` table (email, name, password).
- **convex/users.js** – Convex functions:
  - `users:getByEmail` – get one user by email
  - `users:list` – list all users
  - `users:create` – create user (password must be hashed in Python)
  - `users:update` – update name/password

The Python code in **convex_db.py** calls these from Flask (same interface as **database.py**).

---

## Switching back to SQLite

Remove or comment out **CONVEX_URL** in `.env` and restart the app. It will use **database.py** and the local `calmateai.db` file again.

---

## Production (e.g. Render)

1. Create a Convex project and run `npx convex deploy` (or use the same project as dev).
2. In your host’s environment variables, set **CONVEX_URL** to your Convex deployment URL.
3. Do **not** run `npx convex dev` in production; use `npx convex deploy` once to push your schema and functions.
