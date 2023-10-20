import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_api_response(prompt:str)->str|None:
    text:str|None = None
    try:
        response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" You:", " Serenity:"]
        )
        choices:dict= response.get("choices")[0]
        text=choices.get("text")

    except Exception as e:
        print("Error!",e)
    return text   
def update_list(message:str, pl:list[str]):
    pl.append(message)

def creat_prompt(message:str, pl:list[str])->str:
    p_message:str=f"\nYou: {message}"
    update_list(p_message,pl)
    prompt:str="".join(pl)
    return prompt

def get_bot_response(message:str, pl:list[str])->str:
    prompt:str=creat_prompt(message,pl)
    bot_response:str=get_api_response(prompt)

    if bot_response:
        update_list(bot_response,pl)
        pos:int=bot_response.find("\nSerenity: ")
        bot_response=bot_response[pos+5:]
    else:
        bot_response="Something went wrong..."

    return bot_response

def main():
    prompt_list: list[str] = ["The following is a conversation with a mental health chatbot. The chatbot is here to provide support, guidance, and be a listening ear.",
                            "\nYou: I'm feeling really stressed out and overwhelmed lately. I don't know how to cope with it.",
                            "\nSerenity: I am really sorry to hear that. Can you tell me a few reasons why you might be feeling so stressed out?"]

    while True:
        user_input:str=input("You: ")
        response:str=get_bot_response(user_input,prompt_list)
        print(f"Serenity: {response}")

main()import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_api_response(prompt:str)->str|None:
    text:str|None = None
    try:
        response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" You:", " Serenity:"]
        )
        choices:dict= response.get("choices")[0]
        text=choices.get("text")

    except Exception as e:
        print("Error!",e)
    return text   
def update_list(message:str, pl:list[str]):
    pl.append(message)

def creat_prompt(message:str, pl:list[str])->str:
    p_message:str=f"\nYou: {message}"
    update_list(p_message,pl)
    prompt:str="".join(pl)
    return prompt

def get_bot_response(message:str, pl:list[str])->str:
    prompt:str=creat_prompt(message,pl)
    bot_response:str=get_api_response(prompt)

    if bot_response:
        update_list(bot_response,pl)
        pos:int=bot_response.find("\nSerenity: ")
        bot_response=bot_response[pos+5:]
    else:
        bot_response="Something went wrong..."

    return bot_response

def main():
    prompt_list: list[str] = ["The following is a conversation with a mental health chatbot. The chatbot is here to provide support, guidance, and be a listening ear.",
                            "\nYou: I'm feeling really stressed out and overwhelmed lately. I don't know how to cope with it.",
                            "\nSerenity: I am really sorry to hear that. Can you tell me a few reasons why you might be feeling so stressed out?"]

    while True:
        user_input:str=input("You: ")
        response:str=get_bot_response(user_input,prompt_list)
        print(f"Serenity: {response}")

main()
