# step-1 intall required libraries 
from twilio.rest import Client
from datetime import datetime, timedelta
import time


#step2- twilio credentials
account_sid = "AC8a69911eee13522114d7bc930fc1873e"
auth_token = "ed00aa41aa120f1292fdc5df602440c5"

Client = Client(account_sid , auth_token)

#step-3 define send message function 
def send_whatsapp_message(recipient_number, message_body):
 try: 
     message = Client.messages.create(
         from_='whatsapp:+14155238886',
         body=message_body,
         to=f'whatsapp:{recipient_number}'
         )
       
     print(f'message sent successfully! message sid{message.sid}')
  
 except Exception as e:
     print('an error occured')
    
#step-4  user input 
name = input('Enter the recipient name = ')
recipient_number = input('Enter the recipient whatsapp number with country code (ex:+919313): ') 
message_body = input(f'Enter the message you want to send to  {name}:' )

#step-5 parse date/time and calulate delay
date_str = input('Enter the date to send message  (YYYY_MM_DD): ')
time_str = input('Enter the message time (HH:MM in  24 hour format): ')

#datetime 
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#calculate diffrence 
time_difference = current_datetime -schedule_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
     print("The specified time is in the past. please enter future date and time: ")
     
else:
    print(f"message scheduled to be sent to {name} at {schedule_datetime}. ")

#wait till scheduled time 
    time.sleep(delay_seconds)

#send the message

send_whatsapp_message(recipient_number, message_body)















  