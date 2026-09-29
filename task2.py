def chatbot():

    print("🤖 Simple Chatbot")
    print("Type 'bye' to exit.")

    while True:

        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! 👋")

        elif user == "how are you":
            print("Bot: I am fine. Thank you!")

        elif user == "thanks":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! 👋")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()