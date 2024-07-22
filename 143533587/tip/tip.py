def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    ret = d[1:]
    ret = float(ret)
    return ret

def percent_to_float(p):
    ret = p [:-1]
    ret = int(ret)/100
    return ret

main()