from twilio.rest import TwilioRestClient
import RPi.GPIO as GPIO
import pyzmail
import time

#Setting up Raspberry Pi
ir_input = 14
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(ir_input, gpio.IN, gpio.PUD_DOWN)

#SENDING SMS
def send_sms():
        ACCOUNT_SID = "ACe800b4b8dc5fd3b52ed1c9f75a27addf"
        AUTH_TOKEN = "e3acdb6caf894a1e99f4bc6be6a4bbb7"
        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
        client.messages.create(from_="(520) 217-7571", to="+919962663625", body="This is a test message.")

#SENDING EMAIL
def send_email:
        sender = (u'Security Force', 'securiityforce001@gmail.com')
        recipients = [(u'Boss', 'benatarajan@gmail.com')]
        '''
        subject = u'Notification of a security breach'
        text_content = u'You have been alerted of an alleged security breach of your safe. Stay protected.'
        '''
        subject = u'Test message'
        text_content = u'This is a test message.'
        prefered_encoding = 'iso-8859-1'
        text_encoding = 'iso-8859-1'

        payload, mail_from, rcpt_to, msg_id = pyzmail.compose_mail(\
                sender, \
                recipients, \
                subject, \
                prefered_encoding, \
                (text_content, text_encoding), \
                html=None)#, \
                #attachments=[('attached content', 'text', 'plain', 'text.txt', \
                #		'us-ascii')])
        print payload

        print "------------------------------------------------------------"

        print 'Sender address: ', mail_from
        print 'Recipients: ', rcpt_to

        print "------------------------------------------------------------"

        smtp_host = "smtp.gmail.com"
        smtp_port = 587
        smtp_mode = 'tls'
        smtp_login = 'securiityforce001@gmail.com'
        smtp_password = 'gurkaprotectingme'
        ret = pyzmail.send_mail(payload, mail_from, rcpt_to, smtp_host, \
                smtp_port=smtp_port, smtp_mode=smtp_mode, \
                smtp_login=smtp_login, smtp_password=smtp_password)

        if isinstance(ret, dict):
                if ret:
                        print 'failed recipients: ', ', '.join(ret.keys())
                else:
                        print 'Boss has been alerted about the situation.'
        else:
                print 'error: ', ret

if __name__ == '__main__':
        while(True):
            ir_state = gpio.input(ir_input)
            if ir_state == gpio.HIGH:
                print("HIGH")
                send_sms()
                send_email()
            else:
                print("LOW")
            time.sleep(0.5)
