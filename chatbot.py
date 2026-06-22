from groq import Groq

from config import GROQ_API_KEY
from prompts import SYSTEM_PROMPT, SUBJECT_PROMPTS

client = Groq(api_key=GROQ_API_KEY)


def get_ai_response(messages, subject):

    subject_prompt = SUBJECT_PROMPTS.get(subject, "")

    chat_messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "system",
            "content": subject_prompt
        }
    ]

    chat_messages.extend(messages)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=chat_messages,
        temperature=0.5,
        max_tokens=1024,
    )

    return response.choices[0].message.content