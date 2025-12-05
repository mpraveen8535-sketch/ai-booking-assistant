"""
AI Booking Assistant
Extracts service, day, and time from customer booking messages.
"""

import anthropic
import json


def extract_booking_details(message: str) -> dict:
    """
    Extract booking details from a customer message.
    
    Args:
        message: Natural language booking request (e.g., "I want a haircut Friday at 3pm")
    
    Returns:
        dict with service, day, and time extracted from the message
    """
    client = anthropic.Anthropic()
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=256,
        messages=[
            {
                "role": "user",
                "content": f"""Extract booking details from this customer message. Return ONLY valid JSON with these fields:
- service: the service requested (e.g., "haircut", "color", "trim", "styling")
- day: the day mentioned (e.g., "Friday", "Monday", "tomorrow")
- time: the time mentioned (e.g., "3pm", "10:30am", "afternoon")

If any field is not mentioned, use null.

Customer message: "{message}"

JSON:"""
            }
        ]
    )
    
    # Parse the response
    response_text = response.content[0].text.strip()
    
    # Handle potential markdown code blocks
    if response_text.startswith("```"):
        response_text = response_text.split("```")[1]
        if response_text.startswith("json"):
            response_text = response_text[4:]
        response_text = response_text.strip()
    
    return json.loads(response_text)


def main():
    # Test messages
    test_messages = [
        "I want a haircut Friday at 3pm",
        "Can I book a color treatment for Monday morning around 10?",
        "Need a trim tomorrow at 2:30pm please",
        "Hi, I'd like to schedule a blowout for Saturday",
        "Haircut and beard trim on Wednesday at 4pm",
    ]
    
    print("=" * 60)
    print("AI BOOKING ASSISTANT")
    print("=" * 60)
    
    for msg in test_messages:
        print(f"\nCustomer: \"{msg}\"")
        print("-" * 40)
        
        try:
            result = extract_booking_details(msg)
            print(json.dumps(result, indent=2))
        except Exception as e:
            print(f"Error: {e}")
        
        print()


if __name__ == "__main__":
    main()
