# send_email.py

import sys
import smtplib
from email.mime.text import MIMEText

status = sys.argv[1]
build_url = sys.argv[2]

sender = "your_email@gmail.com"
receiver = "recipient_email@gmail.com"
subject = f"Jenkins Build {status}"
body = f"Your Jenkins build has {status}.\n\nBuild URL: {build_url}"

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, os.environ['GMAIL_APP_PASSWORD'])
        server.sendmail(sender, receiver, msg.as_string())
    print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
    sys.exit(1)
