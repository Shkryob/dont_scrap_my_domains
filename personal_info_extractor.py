import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')
prompt = 'Please make answer short and structured.' \
        'Extract personal info (email, phone, addresses, names) from the following text:'
info_delimiter = '>>> Last update of WHOIS database'


def personal_info_extractor(text):
    if info_delimiter in text:
        text = text[:text.index(info_delimiter)]

    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': prompt + '\n' + text}
        ]
    )
    
    return completion.choices[0].message.content
