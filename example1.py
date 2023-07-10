from botfb import *
#When you modify a project, you must call the modify function, otherwise it will not be modified
edit=EditBot('mybot')
#function create bot
create=CreateBot('mybot')
#here token
create.tokenFb(
    "YOR_TOKEN_PAGE",
    "123456",)
#here add any code for event
create.event(
''' 
def mychat_fun(chat_me):
    import openai
    openai.api_key = "YOR_KEY"



    messages = [
        {"role": "system", "content": "You are an intelligent assistant."}
    ]

    if chat_me:
        messages.append(
            {"role": "user", "content": chat_me}
        )
    
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    
    reply = chat.choices[0].message.content
    return reply
    if 'error' in status.json() and 'code' in status.json()['error'] and status.json()['error']['code'] == 429:
        time.sleep(20)

'''    )
#Host must be set "None
create.getHost('38fe-105-108-152-194.ngrok-free.app')
create.chatBot('chat_me','reply','mychat_fun')
create.runbot()
