from email.mime.text import MIMEText
import smtplib

class EmailClient:
    def __init__(self, server):
        self._server = server

    def send(self, frm, to, subject, text):
        msg = MIMEText(text)
        msg['Subject'] = subject
        msg['From'] = frm
        msg['To'] = to

        s = smtplib.SMTP(self._server)
        s.send_message(msg)
        s.quit()
