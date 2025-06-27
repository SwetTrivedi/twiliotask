from twilio.rest import Client
from dotenv import load_dotenv
import os


load_dotenv()

#  Get credentials from environment
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
to_number = os.getenv("TO_NUMBER")
from_number = os.getenv("FROM_NUMBER")

# Initialize Twilio Client
client = Client(account_sid, auth_token)

try:
    #  Make the call
    call = client.calls.create(
        to=to_number,
        from_=from_number,
        twiml='<Response><Say>This call is only testing purpose </Say></Response>'
    )
    print(f"Call initiated successfully. Call SID: {call.sid}")
except Exception as e:
    print(f"Error while initiating call: {e}")
