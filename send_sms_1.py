from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_cell, my_twilio

client = TwilioRestClient(account_sid, auth_token)

my_msg =''.join(['hello stranger use www.twilio.com/referral/q87Lsk to have a free us number with this number your can call and receive messages freely.\n' for i in range(100)])

message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
