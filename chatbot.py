print("=== Welcome to AlphaBot ===")
print("Type 'bye' or 'exit' whenever you want to quit.\n")

while True:
    # Get user message and convert it to lowercase
    user_input = input("You: ").strip().lower()

    # Rule-based conditions
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("AlphaBot: Hello! How can I help you today?")
    
    elif "how are you" in user_input:
        print("AlphaBot: I am doing great! Thanks for asking.")
        
    elif "your name" in user_input:
        print("AlphaBot: My name is AlphaBot, your virtual assistant.")
        
    elif "help" in user_input:
        print("AlphaBot: You can say hello, ask my name, or say bye.")
        
    elif "bye" in user_input or "exit" in user_input:
        print("AlphaBot: Goodbye! Have a wonderful day!")
        break  # Exits the while loop and ends the program
        
    else:
        print("AlphaBot: Sorry, I don't understand that. Type 'help' for ideas.")