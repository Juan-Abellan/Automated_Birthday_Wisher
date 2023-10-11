import pandas as pd
import smtplib
import datetime as dt
import os
import random

birthdays_dict = {
                "name": ["Papa", "Mama", "Brother", "Anna"],
                "email": ["mero_defondo@gmail.com",
                          "mojarra_deroca@yahoo.com",
                          "pez_limon@gmail.com",
                          "cabo_trafalgar@gmail.com"],
                "year": [1948, 1955, 1993, 1989],
                "month": [10, 10, 1, 9],
                "day": [11, 11, 1, 4],
                }
# TODO 1. Update the birthdays.csv
birthdays_df = pd.DataFrame.from_dict(data=birthdays_dict)
birthdays_df.to_csv(path_or_buf="birthdays.csv", index=False)
#
# print(f"""
# TESTING_TODO 1 -------------------------------------------------------------------------------------------------------
# {birthdays_df}
# {type(birthdays_df) = }
# TESTING_TODO 1 -------------------------------------------------------------------------------------------------------
# """)

# TODO 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month

months_to_check = list(birthdays_df["month"])
days_to_check = list(birthdays_df["day"])
persons_to_check = list(birthdays_df["name"])
emails_to_send = list(birthdays_df["email"])

# print(f"""
# TESTING_TODO 2 -------------------------------------------------------------------------------------------------------
# {now = }
# {type(now) = }
# ------------------------------
# {day = }
# {type(day) = }
# ------------------------------
# {month = }
# {type(month) = }
# ------------------------------
# {birthdays_df["month"]}
# {type(birthdays_df["month"]) = }
# ------------------------------
# {birthdays_df["day"]}
# {type(birthdays_df["day"]) = }
# TESTING_TODO 2 -------------------------------------------------------------------------------------------------------
# """)

lst = os.listdir("letter_templates")  # your directory path
number_files = len(lst)
random_letter = random.randint(a=1, b=number_files)

my_email = "kippilein@gmail.com"
my_password = "kiyc ppvb vfny 98li"  # This password is an app password not the pw of the mail.

for index, person in enumerate(persons_to_check):
    if month == months_to_check[index] and day == days_to_check[index]:
        # TODO 3. If step 2 is true,
        #  pick a random letter from letter templates and replace the [NAME]
        #  with the person's actual name from birthdays.csv
        with open(file=f"""letter_templates/letter_{random_letter}.txt""", mode="r") as text1:
            text = text1.read()
            # print(f"""
            # {text = }
            # {type(text) = }
            # """)

            text_replaced = text.replace("[NAME]", person)

            # print(f"""
            # {text_replaced = }
            # {type(text_replaced) = }
            # """)
        # TODO 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection_sec = connection.starttls()
            connection_login = connection.login(user=my_email, password=my_password)
            connection_send = connection.sendmail(from_addr=my_email,
                                                  to_addrs=emails_to_send[index],
                                                  msg=f"""Subject:Happy Birthday {person}!\n\n{text_replaced}"""
                                                  )


