from twilio.rest import Client
import requests, random, time
from datetime import datetime
r = requests.get('https://type.fit/api/quotes')
quotes = r.json()
while True:
    #Gets current time and formats it
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    account_sid = 'ACdfb2f5950ec76b6913dbdf7b10fff7d7'
    auth_token = 'a49bbc0f2b3c963e1bcc9595b5587f17'
    #Sends the message
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_='whatsapp:+14155238886',
    body=f"{quotes[random.randint(0,len(quotes))]['text']}",
    to='whatsapp:+447847889963'
    )

    print(message.sid)
    time.sleep(1800)

