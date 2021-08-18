# sms_sender_twilio

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC42c3b0dac480c2bf504f403704742f89"
# Your Auth Token from twilio.com/console
auth_token  = "42f2a0846d5e66bb0edc7880a99d93ca"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5562985481850", 
    from_="+14152363566",
    body="Hello from Python!")

print(message.sid)