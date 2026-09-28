def chatbot_response(user_input: str) -> str:
    """Return a deterministic response for aa user message."""
    message = user_input.strip().lower()
    
    if message in {'hello', 'hi'}:
        return "Hi!"
    if message in "how are you":
        return "I'm fine, thanks! What about you?"
    if message in "fine":
        return "Good"
    if message in "bye":
        return "Goodbye!"
    if message in "what is your name":
        return "I'm a simple rule-based chatbot."
    if message in {"thanks", "thank you"}:
        return "You're welcome!"
    if "what is artificial intelligence" in message:
        return "Artificial Intelligence is a branch of computer science that aims to create software or machines that exhibit human-like intelligence."
    if message in {"ok thanks", "ok"}:
        return "Thankyou!"
    if message in "help":
        return "Try saying hello, asking how I am, or saying bye."
    return "Sorry, I don't understand."