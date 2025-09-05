def chatbot():
    print("🤖 Basic Chatbot (CodeAlpha Task 4) — type 'bye' to exit")
    while True:
        user = input("You: ").strip().lower()
        if user in {"hello", "hi"}:
            print("Bot: Hi!")
        elif user in {"how are you", "how are you?"}:
            print("Bot: I'm fine, thanks!")
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
