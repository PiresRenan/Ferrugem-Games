from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "+5511993597029"

TWILIO_SID = "AC5404fd88d6fcf6051bfc893da6cad530"
TWILIO_AUTH_TOKEN = "afcdacd66ac8e899884b4fa080ccefb2"

def sendMessage(body):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create( 
                from_='whatsapp:+14155238886',  
                body=body,      
                to='whatsapp:+5511993597029' 
                ) 
    print(message.sid)
    