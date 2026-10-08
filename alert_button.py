import time
import os
import requests
import RPi.GPIO as GPIO
from dotenv import load_dotenv

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

try:
    while True:
        if GPIO.input(7) == GPIO.HIGH and not button_pressed:
            print("Someone pressed the alert button!")

            message = "🚨 ALERT! Someone pressed the button!"

            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

            data = {
                "chat_id": CHAT_ID,
                "text": message
            }

            requests.post(url, data=data)

            button_pressed = True

        elif GPIO.input(7) == GPIO.LOW:
            button_pressed = False

        time.sleep(0.1)


except KeyboardInterrupt:
    print("\nMonitoring stopped.")
