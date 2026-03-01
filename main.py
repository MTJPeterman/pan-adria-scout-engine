import os
import json
import datetime
import gspread
from google.oauth2.service_account import Credentials

SHEET_ID = "1iwPuwvGVTza3DYvVZMrbjOORer4Pxr20Xrax9oA3ndg"

def connect():
    creds_json = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT"])
    creds = Credentials.from_service_account_info(
        creds_json,
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ],
    )
    return gspread.authorize(creds)

def run():
    gc = connect()
    sh = gc.open_by_key(SHEET_ID)

    ws = sh.worksheet("Signal Inbox")

    today = datetime.date.today().isoformat()

    ws.append_row([
        "Test startup",
        "AI infrastructure",
        "Slovenia",
        "GitHub",
        "https://github.com",
        today
    ])

if __name__ == "__main__":
    run()
