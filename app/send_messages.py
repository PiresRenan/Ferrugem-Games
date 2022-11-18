from twilio.rest import Client

VERIFIED_NUMBER = "+5511993597029"
TWILIO_SID = "AC5404fd88d6fcf6051bfc893da6cad530"
TWILIO_AUTH_TOKEN = "725c692a550723dae227220432bafb1f"

def sendMessage(body):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create( 
                from_='whatsapp:+14155238886',  
                body=body,      
                to=f'whatsapp:{VERIFIED_NUMBER}' 
                ) 
    