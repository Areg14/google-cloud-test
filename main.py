import datetime
import smtplib

start_time = "21:24"
now = datetime.datetime.now()

hour = int(now.strftime('%H'))
minute = int(now.strftime('%M'))
def sendEmail(subject, body):
    EMAIL_ADDRESS = "aregakdev@gmail.com"
    EMAIL_PASSWORD = "aregak2008"
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, "areg.arzumanyan08@gmail.com", msg)
while True:
    if hour == int(start_time[:-3]) and minute == int(start_time[-2:]):
        sendEmail("Message from cloud!!", "It works!!!!!")
        break