import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    """"""
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '75542d4eed3476'
    password = '32e0c3152aa63e'
    message = f' <h3>New Feedback Submission</h3><ul><li>Customer:{customer}</l1><li>Dealer:{dealer}</l1> <li>Rating:{rating}</l1><li>Comments:{comments}</l1><ul>'
    sender_email = 'email1@example.com'
    reciever_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = reciever_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())
