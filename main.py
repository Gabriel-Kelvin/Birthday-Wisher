from datetime import datetime
import pandas
import random
import smtplib

my_mail = "gabrielkelvin184@gmail.com"
password = "yoipmchuowhtemjc"

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    random_number = random.randint(1,3)
    file_path = fr"letter_templates\letter{random_number}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        message_body = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday \n\n {message_body}")




