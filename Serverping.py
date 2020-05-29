import os
import time, os
import smtplib, ssl
import imghdr
from email.message import EmailMessage

#you need to run this as admin and use python3


#In position 0 is Server One. In position 1 is Server Two. Change these to what you need
IP_Addr = ["192.168.1.1", "192.168.1.2"]        

Email = input("Email:")
Password = input("Password:")
RecvEmail = input("Where Am I Sending This to?:")
print("\n")

#The Email Function
def email():
    msg = EmailMessage()
    msg['Subject'] = 'Server is Down'
    msg['From'] = Email
    msg['To'] = RecvEmail
    msg.set_content('   Server is Down  ')


#Html body of email
    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:red;">Server is Down</h1>
        </body>
    </html>
    """, subtype='html')

#Sending The Email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Email, Password)
        smtp.send_message(msg)
        print("Email Successfully Sent")
        time.sleep(300)
        test()
        

#Ping the servers and send email only if one is down. 
#Loops for 300 seconds
def test():
    print("Attempting to Ping:", IP_Addr[0])
    response = os.system("ping -c 1 " + IP_Addr[0] + " > log.txt")
    time.sleep(1)
    print("Attempting to Ping:", IP_Addr[1])
    response_two = os.system("ping -c 1 " + IP_Addr[1] + " > log.txt") 
    if response == 0:
        print(IP_Addr[0], "Is Up")
    else:
        print(IP_Addr[0], "Is down")
        email()
        
    if response_two == 0:
        print(IP_Addr[1], "Is Up")
        print("####################")
    else:
        print(IP_Addr[1], "Is Down")
        email()
        
    time.sleep(300)
    test()
    
        
test()
