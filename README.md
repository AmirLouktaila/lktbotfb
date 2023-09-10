# lktbotfb
<code>pip install lktbotfb</code>

بالنسبة لإضافة مثال لهذا الكود في ملف README على GitHub، يمكنك اتباع الخطوات التي تم ذكرها سابقًا وإضافة الكود داخل علامات البرمجة ثلاثية الجمل (```).

هذا هو كيف يمكنك تنسيق الكود في ملف README:

\```python
from botfb import *

# When you modify a project, you must call the modify function, otherwise it will not be modified
edit = EditBot('mybot')

# Function to create bot
create = CreateBot('mybot')

# Provide your Facebook token here
create.tokenFb("YOUR_TOKEN_PAGE", "123456")

# Add your event code here
create.event('''
def mychat_fun(chat_me):
    import openai
    openai.api_key = "YOUR_KEY"

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
''')

# Get the host information
create.getHost('YOUR_NGROK_HOST')

# Start the chat bot
create.chatBot('chat_me', 'reply', 'mychat_fun')

# Run the bot
create.runbot()
\```

يمكنك استبدال `YOUR_TOKEN_PAGE` و`YOUR_KEY` و`YOUR_NGROK_HOST` بالقيم الفعلية التي تستخدمها في مشروعك. بعد ذلك، قم بحفظ ملف README.md وقم بالتزامن مع مستودع GitHub الخاص بك. سيتم عرض الكود بشكل مناسب في ملف README على GitHub، وسيمكن للآخرين نسخه إذا رغبوا في ذلك.
