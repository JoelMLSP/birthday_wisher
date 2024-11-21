##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import pandas
import smtplib
import random

df = pandas.read_csv("birthdays.csv")
today = dt.datetime.now()
filtered =  df[(df['day'] == today.day) & (df['month'] == today.month)]
filtered_dict = filtered.to_dict()
letter = ["letter_1.txt","letter_2.txt","letter_3.txt"]
my_email = "" #add email
password = "" #add app password
connection = smtplib.SMTP("smtp.gmail.com")
def random_letter():
    with open(f"letter_templates/{random.choice(letter)}", "r") as file:
        letter_opened = file.read()
        letter_edited = letter_opened.replace("[NAME]", value)
        return letter_edited


if not filtered.empty:
    connection.starttls()
    for index, value in filtered_dict["name"].items():
        letter_to_send = random_letter()
        email = filtered_dict["email"][index]
        message = f"Subject:Birthday Wishes\n\n{letter_to_send}"
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=message.encode('utf-8'))

else:
    print ("its noones birthday today")

connection.close()