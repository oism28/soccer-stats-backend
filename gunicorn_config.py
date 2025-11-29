import os

port = os.environ.get("WEBSITES_PORT") or os.environ.get("PORT") or "10000"
bind = f"0.0.0.0:{port}"
workers = int(os.environ.get("GUNICORN_WORKERS", "3"))
timeout = int(os.environ.get("GUNICORN_TIMEOUT", "120"))
