import smtplib
from email.mime.text import MIMEText
import sys
import os

# Read args: success/failure, build URL etc.
status = sys.argv[1] if len(sys.argv) > 1 else "SUCCESS"
build_url = sys.argv[2] if len(sys.argv) > 2 else ""

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "sadanki190@gmail.com"
smtp_password = "ewnj tlbw jaxr ijpr"  # Use Gmail app password for security

from_addr = smtp_user
to_addr = smtp_user
subject = f"{'✅ SUCCESS' if status == 'SUCCESS' else '❌ FAILURE'}: Jenkins Build Notification"
body = f"Build {status}. Check details here: {build_url}"

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = from_addr
msg['To'] = to_addr

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
    print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
    sys.exit(1)
