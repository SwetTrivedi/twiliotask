# from twilio.rest import Client
# from dotenv import load_dotenv
# import os


# load_dotenv()
# # 
# # #  Get credentials from environment
# account_sid = os.getenv("TWILIO_ACCOUNT_SID")
# auth_token = os.getenv("TWILIO_AUTH_TOKEN")
# to_number = os.getenv("TO_NUMBER")
# from_number = os.getenv("FROM_NUMBER")

# # Initialize Twilio Client
# client = Client(account_sid, auth_token)

# try:
#     #  Make the call
#     call = client.calls.create(
#         to=to_number,
#         from_=from_number,
#         twiml='<Response><Say>This call is only testing purpose </Say></Response>'
#     )
#     print(f"Call initiated successfully. Call SID: {call.sid}")
# except Exception as e:
#     print(f"Error while initiating call: {e}")



from fastapi import FastAPI, Form, Response
from twilio.twiml.voice_response import VoiceResponse

app = FastAPI()

@app.post("/voice")
async def voice():
    resp = VoiceResponse()
    gather = resp.gather(
        input="speech",
        action="/process",
        method="POST",
        language="hi-IN",
        speech_timeout="auto"
    )
    gather.say("नमस्ते! कृपया अपनी बात बताएं।", language="hi-IN")
    # resp.play("https://github.com/SwetTrivedi/twiliotask/raw/refs/heads/main/Recording%20(2).m4a")
    return Response(content=str(resp), media_type="application/xml")

@app.post("/process")
async def process(SpeechResult: str = Form("")):
    print("User said:", SpeechResult)
    resp = VoiceResponse()

    user_input = SpeechResult.lower()

    if "नमस्ते" in user_input or "hello" in user_input:
        resp.say("नमस्ते! मैं आपकी क्या मदद कर सकता हूँ?", language="hi-IN")
    elif "पानी" in user_input:
        resp.say("पानी की जानकारी के लिए धन्यवाद।", language="hi-IN")
    elif "कैसे" in user_input:
        resp.say("मैं ठीक हूँ, आपका धन्यवाद!", language="hi-IN")
    else:
        resp.say("माफ़ करें, मैं आपको समझ नहीं पाया। कृपया दोबारा बोलें।", language="hi-IN")


    gather = resp.gather(
        input="speech",
        action="/process",
        method="POST",
        language="hi-IN",
        speech_timeout="auto"
    )
    gather.say("कृपया अगला सवाल बोलें।", language="hi-IN")

    return Response(content=str(resp), media_type="application/xml")
