from twilio.rest import Client

account_sid = 'AC1c9eeaf88c45b4517989fe6c922bf99b'
auth_token = 'a3db08ee21186e2b17cf2f8e71e60d9b'
client = Client(account_sid, auth_token)

def automation_function():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='o kaleen bhai ....',
        #body='hey u ... whats up',
        to='whatsapp:+919014981664'
    )
    print(message.sid)
