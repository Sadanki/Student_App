import sys
import os
import smtplib
from email.mime.text import MIMEText

status = sys.argv[1] if len(sys.argv) > 1 else "SUCCESS"
build_url = sys.argv[2] if len(sys.argv) > 2 else ""

sender = "sadanki190@gmail.com"  # your Gmail address
receiver = sender  # send to yourself (or change)
subject = f"{'✅ SUCCESS' if status == 'SUCCESS' else '❌ FAILURE'}: Jenkins Build Notification"
body = f"Build {status}. Check details here: {build_url}"

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, os.environ['GMAIL_APP_PASSWORD'])  # use env var for password
        server.sendmail(sender, receiver, msg.as_string())
    print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
    sys.exit(1)

