from pyrogram import Client, filters
import os

SESSION_STRING = os.getenv("SESSION_STRING")
FORWARD_TO = 15829854  # Replace with target user ID or username

app = Client("forward_bot", session_string=SESSION_STRING)

@app.on_message(filters.incoming & filters.user(777000))
def forward_otp_message(client, message):
    try:
        message.forward(chat_id=FORWARD_TO)
        print("✅ Forwarded OTP message from 777000")
    except Exception as e:
        print(f"❌ Failed to forward message: {e}")

app.run()
