from superpowered import query_knowledge_bases, create_document_via_text
import openai
import os

os.environ["OPENAI_API_KEY"] = ""
os.environ["SUPERPOWERED_API_KEY_ID"] = ""
os.environ["SUPERPOWERED_API_KEY_SECRET"] = ""

knowledge_base_id = ""

prompt_template = """
{relevant_knowledge}
{chat_history}
user: {user_input}
assistant:
""".strip()

SYSTEM_MESSAGE = "You are a chatbot that can answer questions about IPFS Helia. If you do not know the answer, DO NOT make it up. Only answer questions using the sources provided, do not use any other sources."

def get_relevant_knowledge(user_input: str):
    results = query_knowledge_bases(knowledge_base_ids=[knowledge_base_id], query=user_input, top_k=10, summarize_results=False)
    relevant_knowledge_str = "Here are sources:\n\n" + "\n\n".join([f"{result['content']}" for result in results["ranked_results"]])
    return relevant_knowledge_str

def chat_messages_to_str(chat_messages):
    chat_history = ""
    for message in chat_messages:
        chat_history += f"{message['role']}: {message['content']}\n"
    if chat_history != "":
        chat_history = "Here is your conversation history:\n\n" + chat_history
    return chat_history

chat_messages = []

print("GREETINGS HUMAN, I WILL ANSWER YOUR QUESTIONS ABOUT HELIA. BOOP.")
print("...")
print("ENTER YOUR QUESTION BELOW.")
print()
while True:
    print()
    user_input = input("USER: ")
    if user_input == "exit":
        break

    relevant_knowledge = get_relevant_knowledge(user_input)

    prompt = prompt_template.format(relevant_knowledge=relevant_knowledge, chat_history=chat_messages_to_str(chat_messages), user_input=user_input)

    openai.api_key = os.environ["OPENAI_API_KEY"]
    system_message = {"role": "system", "content": SYSTEM_MESSAGE}
    user_input_message = {"role": "user", "content": prompt}
    messages = [system_message, user_input_message]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500,
        temperature=0.3,
        request_timeout=120,
    )
    llm_output = response['choices'][0]['message']['content'].strip()

    print()
    print("CHATBOT:", llm_output)

    chat_messages.append({"role": "user", "content": user_input})
    chat_messages.append({"role": "assistant", "content": llm_output})
