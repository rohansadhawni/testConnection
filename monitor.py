# monitor.py

import requests
import logging

# Configuration
API_URL = (
    "http://localhost:3000/testConnection"  # Replace with your actual API URL and port
)
DISCORD_WEBHOOK_URL = "https://discordapp.com/api/webhooks/xxxxxxxxxx/yyyyyyyyyyyyyyyyyyy_"  # Replace with your Discord webhook URL

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def check_connection():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200 and response.json().get("status") == "OK":
            logging.info("API is up and running")
        else:
            logging.error("API responded with an unexpected status")
            send_discord_notification(
                "API is down",
                f"Status code: {response.status_code}\nResponse: {response.text}",
            )
    except Exception as e:
        logging.error("Error checking API connection: %s", str(e))
        send_discord_notification("API is down", f"Error: {str(e)}")


def send_discord_notification(title, description):
    try:
        data = {
            "embeds": [
                {
                    "title": title,
                    "description": description,
                    "color": 15158332,  # Optional: red color for errors
                }
            ]
        }
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        if response.status_code == 204:
            logging.info("Discord notification sent successfully")
        else:
            logging.error(
                "Failed to send Discord notification. Status code: %d",
                response.status_code,
            )
    except Exception as e:
        logging.error("Error sending Discord notification: %s", str(e))


if __name__ == "__main__":
    check_connection()
