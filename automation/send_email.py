#!/usr/bin/env python3
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# === CONFIGURE THESE SETTINGS ===
sender_email = "zacharyflores5@gmail.com"
# For Gmail, you need an "App Password", NOT your regular password
# Generate one here: https://myaccount.google.com/apppasswords
sender_password = "meszrhoydrmbqbji"
receiver_email = "joeledward949@gmail.com"
subject = "Test Email from Python"
body = "Hello! This email was sent using Python's built-in smtplib."

# === CREATE THE EMAIL ===
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# === SEND THE EMAIL ===
try:
    # Create a secure SSL context
    context = ssl.create_default_context()
    
    # Connect to Gmail's SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    
    print("✅ Email sent successfully!")
    
except Exception as e:
    print(f"❌ Failed to send email. Error: {e}")
