from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birthdate = input("Date of birth: ")
    try:
        year,month,day = check_birthday(birthdate)
    except:
        sys.exit("Invalid date")

    date_of_birth = date(int(year),int(month),int(day))
    date_of_today = date.today()
    diff = date_of_today - date_of_birth
    total_m = diff.days *24 *60
    output = p.number_to_words(total_m, andword = "" )
    print(output.capitalize()+ " minutes")


def check_birthday(birthdate):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birthdate):
        year,month,day = birthdate.split("-")
        return year,month,day


if __name__ == "__main__":
    main()