# Basic Rule-Based Chatbot

def chatbot_response(user_input):
    """
    Returns a predefined response based on user input.
    """

    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "I'm a simple Python chatbot."

    elif user_input == "what can you do":
        return "I can respond to some basic messages."

    elif user_input == "thank you" or user_input == "thanks":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that."


def main():
    print("=" * 45)
    print("          BASIC CHATBOT")
    print("=" * 45)
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)

        print("Bot:", response)

        # Stop the chatbot when user says bye
        if user_input.lower().strip() == "bye":
            break


# Start the chatbot
main()