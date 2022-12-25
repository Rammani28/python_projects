##################### Extra Hard Starting Project ######################
# Completed in maybe 1 hour and 30 minutes
import datetime as dt
import pandas
import random
import smtplib

SENDER = 'Rammani'
MY_EMAIL = 'ktmcodebrewery@gmail.com'
APP_PASSWORD = 'jcfboqrovkuvezdu'

now = dt.datetime.now()
file = pandas.read_csv('birthdays.csv')

for row in file.iterrows():
    if row[1]['month'] == now.month and row[1]['day'] == now.day:

        path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
        with open(path) as letter:
            temp_letter = letter.read()

        letter_to_name = temp_letter.replace('[NAME]', row[1]['name'])
        letter_to_name = letter_to_name.replace('Angela', SENDER)
        print(letter_to_name)

        receiver_email = row[1]['email']
        with smtplib.SMTP(host='smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=receiver_email,
                                msg=f"Subject:Birthday Wish\n\n{letter_to_name}")
