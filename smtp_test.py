import smtplib
from email.message import EmailMessage
import os

# Replace with your SMTP server settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587

sender_email = 'haldafai1990@gmail.com'
receiver_email = 'h_aldafai@hotmail.com'
password = os.getenv('EMAIL_HOST_PASSWORD')  # Replace with your email password or use environment variables

message = EmailMessage()
message['Subject'] = 'Test Email'
message['From'] = sender_email
message['To'] = receiver_email
message.set_content('This is a test email.')

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)
        print('Email sent successfully!')
except Exception as e:
    print(f'Error sending email: {e}')
