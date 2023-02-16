def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d2 = float(d.replace('$',''))
    return d2

def percent_to_float(p):
    p2 = float(p.replace('%',''))
    return p2/100


main()