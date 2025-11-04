import smtplib
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self):
        self.smtp_host = "smtp.gmail.com"
        self.smtp_port = 587
        self.username = "admin@company.com"
        self.password = "MyPassword123"
    
    def send_email(self, to_address, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = to_address
        
        server = smtplib.SMTP(self.smtp_host, self.smtp_port)
        server.starttls()
        server.login(self.username, self.password)
        server.send_message(msg)
        server.quit()
    
    def send_bulk_emails(self, recipients, subject, body):
        for email in recipients:
            self.send_email(email, subject, body)
    
    def validate_email(self, email):
        return '@' in email