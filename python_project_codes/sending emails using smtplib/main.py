# import smtplib
#
# my_email = 'ktmcodebrewery@gmail.com'
# # password = "5eJXsMtp@yah"
# app_password = "jcfboqrovkuvezdu"
#
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=app_password)
#     # connection.send_message(from_addr=my_email, to_addr='ronadorapper@gmail.com', msg="Subject:Happy Birthday\n\nHappy birthday Rapper. Wish you a wonderful year ahead.")
#     connection.sendmail(
#         msg='Subject:Happy Birthday\n\nHappy birthday Rapper. Wish you a wonderful year ahead.',
#         from_addr=my_email,
#         to_addrs='ktmcodebrewery@yahoo.com'
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# # print(month)
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year= , day= , )

import smtplib
import datetime as dt
import random

MY_EMAIL = "ktmcodebrewery@gmail.com"
RECEIVER = ["ktmcodebrewery@yahoo.com", "swornimstha31@gmail.com", "ktmcodebrewery@gmail.com", "rammaniganesh28@gmail.com"]
APP_PASSWORD = "jcfboqrovkuvezdu"


now = dt.datetime.now()
weekday = now.weekday()


with open('quotes.txt') as quote_file:
    quote_list = quote_file.readlines()
    quote = random.choice(quote_list)
    print(quote)

with smtplib.SMTP(host='smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=APP_PASSWORD)
    for mail in RECEIVER:
    	connection.sendmail(from_addr=MY_EMAIL, to_addrs=mail, msg=f"Subject: Daily Quotes\n\n{quote}")
    print("Message Sent")













