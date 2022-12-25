import random
import smtplib
from email.message import EmailMessage
import imghdr
from rand_pass_gen import generate_random_password,generate_2FA_code

EMAIL_ADDRESS='nihaltmdev@gmail.com'
EMAIL_PASSWORD='NihalwritesCode'

def welcome(a,b):
    global EMAIL_ADDRESS,EMAIL_PASSWORD,msg
    msg=EmailMessage()
    msg['Subject']='Welcome to Tic-Tac-Toe'
    msg['From']=EMAIL_ADDRESS
    msg['To']=a
    twofa=generate_2FA_code()
    msg.set_content(f'''Dear {b},\nRelive your childhood with a game that will give make you feel nostalgic and experience euphoria!
\nEnjoy the Game\nHere is your Confirmation code- {twofa}\nWith Warm Regards,\nNMV Team.''')
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)
            return twofa

def send_pass(a,b,c):
    global EMAIL_ADDRESS,EMAIL_PASSWORD,msg
    msg=EmailMessage()
    msg['Subject']='Tic Tac Toe password Reset'
    msg['From']=EMAIL_ADDRESS
    msg['To']=a
    new_pass=c
    msg.set_content(f'''Dear {b},\nWe realised that you wanted to login to your favourite game but could not as you had forgotten the password.
\nSo here is your password- {new_pass}\nPlease do not forget to delete this email once you have logged in\nEnjoy the Game\nWith Warm Regards,\nNMV Team.''')
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)
    return new_pass

def two_FA(a,b):
    global EMAIL_ADDRESS,EMAIL_PASSWORD,msg
    msg=EmailMessage()
    msg['Subject']='Tic Tac Toe 2FA'
    msg['From']=EMAIL_ADDRESS
    msg['To']=a
    twofa=generate_2FA_code()
    msg.set_content(f'''Dear {b},\nWe realised that you wanted to login to your favourite game.
\nSo here is the 2FA code- {twofa}\nEnjoy the Game\nWith Warm Regards,\nNMV Team.''')
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)
    return twofa





