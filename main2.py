from datetime import datetime
import pandas
import random
import smtplib


my_mail = "gabrielkelvin184@gmail.com"
password = "yoipmchuowhtemjc"

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthday = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday:
    birthday_person = birthday[today]
    file_path = f"letter_templates/letter{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        birthday_letter = contents.replace("[NAME]", birthday_person["name"])

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(from_addr=my_mail,
                        to_addrs="gabriel_kelvin@myyahoo.com",
                        msg=f"Subject: Happy Birthday! \n\n {birthday_letter}")