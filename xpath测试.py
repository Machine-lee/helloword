# import smtplib

# server = smtplib.SMTP_SSL(smtp_server_domain_name, port, context=ssl_context)
# server.login(sender_email, password)
# server.sendmail(sender_mail, email, f"Subject: {subject}\n{content}")



import smtplib, ssl

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "starbrightlee08@gmail.com"
        self.password = "lmx7034562"

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        
        for email in emails:
            result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")

        service.quit()


if __name__ == '__main__':
    mails = '610238194@qq.com'
    subject = 'hello'
    content = '1'

    mail = Mail()
    mail.send(mails, subject, content)
