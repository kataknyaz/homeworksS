import logging
from datetime import datetime

logging.basicConfig(filemode='notification.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def send_sms(message):
    print(f'SMS sent: {message}')
    logging.info(f'SMS sent: {message}')


def send_email(message):
    print(f'Email sent: {message}')
    logging.info(f'Email sent: {message}')



def send_notification(notification_type, callback, message):
    try:
        if notification_type not in ['email','sms']:
            raise ValueError('Unknown notificatio type')
        callback(message)
    except ValueError as err:
        print(f'Error: {err}')   
        logging.error(f'Error: {err}')  


send_notification('sms', send_sms, 'Hello, world! As email')  
send_notification('email', send_sms, 'Hello, world! As SMS')    
send_notification('push', None, 'This will trigger an error')      



