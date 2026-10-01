from ollama import chat

system_msg = "You are a heroine. Answer in rhymes. Answer in one sentence."
history = [{ "role" : "system", "content" : system_msg}]
question_counter = 0

print("WELCOME TO MY WORLD 🥳")
while True:
    question = input("You:")
    if question == " ":
        print("Lahari🦄: Please type something...")
        continue
    if question.lower().strip() == "/history":
        print("---- Your Conversation so far ----")
        if len(history) < 2:
            print("Nothing here so far!")
        for msg in history[1:]:
            if msg["role"] == "user":
                speaker = "You"
            else:
                speaker = "Lahari🦄"
            print(f"{speaker}: {msg['content']}")
        print("---------------------")
        print()
        continue
    if question.lower().strip() == "/clear":
        history = [{ "role" : "system", "content" : system_msg}]
        print("Your history is cleared. Start a fresh conversation.")
        print()
        continue

    if question.lower().strip() == "/help":
        print("----- Available commands -----")
        print("/history - displays conversation history")
        print("/clear - clears chat history")
        print("/help - displays this list")
        print("exit - quits the chatbot")
        print("----------------------")
        print()
        continue

    if question.lower().strip() == "bye":
        print("Lahari🦄:Goodbye Honey. Please come back soon . I will miss you!😭😭")
        print(f"You asked {question_counter} questions today. Good job!")
        break
    history.append({ "role" : "user", "content" :question})
    question_counter += 1
    try:
        response = chat(
                model="llama3.2",
                messages = history
            )
        reply = response.message.content
        history.append({ "role" : "assistant", "content" :reply})
        print(f"Lahari🦄 :{reply}")
        print()
        print("----------")
        print()
    except Exception as e:
        print("Unknown issue. Is Ollama running?")