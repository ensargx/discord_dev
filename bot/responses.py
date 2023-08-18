def handle_response(message) -> str:
    p = message.lower()

    if p == "hi" or p == "hello":
        return "Hello there!"
        
    return "Bot works!, try 'hi' or 'hello'"