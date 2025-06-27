# Twilio Call Project (Python)

This project demonstrates how to make outgoing voice calls using the Twilio Python SDK in a secure and professional way.

## Features

- Make outgoing calls using Twilio
- Secure credential handling via `.env` file
- Error handling for failed calls
- Clean and professional structure

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables

Create a `.env` file in the root directory:

```env
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
FROM_NUMBER=your_verified_number
TO_NUMBER=verified_target_number
```

### 3. Run the Script

```bash
python make_call.py
```

## Example TwiML Message

```xml
<Response>
  <Say>Hello, this is a test call from my personal number via Twilio trial.</Say>
</Response>
```

##  Notes

- Twilio trial accounts can only call verified numbers.
- Always keep your credentials secure.
- You can extend this project to support dynamic messages, logs, etc.

##  Helpful Links

- [Twilio Console](https://www.twilio.com/console)
- [Twilio Python Docs](https://www.twilio.com/docs/voice/quickstart/python)
- [TwiML Reference](https://www.twilio.com/docs/voice/twiml)
