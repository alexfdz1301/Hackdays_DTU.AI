import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def fetch_and_download(limit=5):
    """Fetches latest Telegram docs and downloads them locally."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    response = requests.get(url)
    data = response.json()

    docs = []
    for result in data.get("result", []):
        msg = result.get("message", {})
        doc = msg.get("document")
        if doc:
            file_id = doc["file_id"]
            file_name = doc["file_name"]
            file_info = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id={file_id}").json()
            file_path = file_info["result"]["file_path"]
            file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"

            local_path = os.path.join(DOWNLOAD_DIR, file_name)
            with open(local_path, "wb") as f:
                f.write(requests.get(file_url).content)

            docs.append({
                "name": file_name,
                "url": file_url,
                "path": local_path
            })

            if len(docs) >= limit:
                break

    return docs
