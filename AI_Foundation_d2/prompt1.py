from  ollama import chat
response = chat(
    model = "llama3.2",
    messages=[
        {
            "role":"user",
            "contzent":"write me a whatapp message to my friend geetha asking her to meet me at the bus  stop. keep the answer under 2 lines."
        }
    ]
)
print(response.message.content) 