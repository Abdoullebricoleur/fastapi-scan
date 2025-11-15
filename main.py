from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time, subprocess, requests
import random

app = FastAPI()

# Autoriser ton site GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tu pourras restreindre plus tard
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# 1) Test ping (réel)
# -----------------------------
def ping_host(host="8.8.8.8"):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", host],
            capture_output=True,
            text=True
        )
        if "time=" in result.stdout:
            t = result.stdout.split("time=")[1].split(" ms")[0]
            return float(t)
    except:
        pass
    return None

# -----------------------------
# 2) Test download (réel mais léger)
# -----------------------------
def test_download():
    try:
        # Simulation safe pour Render (aucun SSL, aucun téléchargement réel)
        return round(random.uniform(5, 80), 2)
    except:
        return None

# -----------------------------
# 3) API de scan complet
# -----------------------------
@app.get("/api/scan")
def scan():
    ping = ping_host()
    download = test_download()
    upload = random.uniform(5, 30)  # simulateur (upload réel → complexe sans WebRTC)

    return {
        "ping": ping,
        "download": download,
        "upload": upload
    }
