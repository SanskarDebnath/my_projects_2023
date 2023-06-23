from twilio.rest import Client
import openai



openai.api_key = "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"

# Twilio Account Sid and Auth Token
twilio_sid = 'AC4136fd223f146e2975305f1c664caeda'
twilio_token = '33aed237f3a00b28b70b330a180c362b'
client = Client(twilio_sid, twilio_token)

#Twilio WhatsApp sandbox number
from_whatsapp_number='whatsapp:+14155238886'
#WhatsApp group number
to_whatsapp_number='whatsapp:+918837418457'

def send_message(message):
    client.messages.create(body=message,
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)

def gpt_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']

def process_message(message):
    if message.startswith('/askgpt:'):
        prompt = message.split(':')[1]
        response = gpt_response(prompt)
        send_message(response)

# prompt
process_message('/askgpt:What is the capital of France?')
