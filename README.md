# AI Booking Assistant

An AI-powered tool that extracts booking details from natural language customer messages. Built for service businesses like salons, barbershops, and spas.

## What it does

Customer sends: *"I want a haircut Friday at 3pm"*

AI extracts:
```json
{
  "service": "haircut",
  "day": "Friday",
  "time": "3pm"
}
```

## Tech Stack

- Python 3
- Anthropic Claude API

## Setup

1. Clone the repo
```bash
git clone https://github.com/mpraveen8535-sketch/ai-booking-assistant.git
cd ai-booking-assistant
```

2. Install dependencies
```bash
pip install anthropic
```

3. Set your API key
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

4. Run it
```bash
python booking_assistant.py
```

## Example Output
```
Customer: "I want a haircut Friday at 3pm"
----------------------------------------
{
  "service": "haircut",
  "day": "Friday",
  "time": "3pm"
}
```

## Future Improvements

- Connect to Google Calendar for actual booking
- Add support for multiple services in one message
- Build a simple web interface

## Author

Monishka Praveen Wannakuwatte
Bachelor of AI Student | Deakin University
