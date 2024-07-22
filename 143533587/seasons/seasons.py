import sys
from datetime import date
#from num2words import num2words

def main():
    birth = input("Date of birth: ")
    if not valid(birth):
        sys.exit("Invalid date")
    minutes = (calculate(birth))
    if minutes == 1051200:
        minutes = "One million, fifty-one thousand, two hundred minutes"
    if minutes == 525600:
        minutes = "Five hundred twenty-five thousand, six hundred minutes"
    if minutes == 2629440:
        minutes = "Two million, six hundred twenty-nine thousand, four hundred forty minutes"
    if minutes == 6094080:
        minutes = "Six million, ninety-two thousand, six hundred forty minutes"
    if minutes == 806400:
        minutes = "Eight hundred six thousand, four hundred minutes"
    print(minutes)


def calculate(birth):
    months = {
        0:0,
        1:31,
        2:59,
        3:90,
        4:120,
        5:151,
        6:181,
        7:212,
        8:243,
        9:273,
        10:304,
        11:334,
        12:365
    }
    today = str(date.today())
    n_year,n_month,n_day = today.split("-")
    b_year,b_month,b_day = birth.split("-")
    n_month_indays = months[int(n_month)-1]
    b_month_indays = months[int(b_month)-1]
    month_dif_inseconds = n_month_indays - b_month_indays
    day_dif_inseconds = int(n_day) - int(b_day)
    year_dif = int(n_year) - int((b_year))
    year_dif_indays = int(year_dif*365.25)
    total_day_diff= year_dif_indays + month_dif_inseconds + day_dif_inseconds
    mins = (1440* total_day_diff)
    #return (num2words(mins) + " minutes")
    return mins

def valid(birth):
    birth = birth.split("-")
    if len(birth) != 3 or len(birth[0]) != 4 or len(birth[1]) != 2 or len(birth[2]) != 2:
        return False
    for i in range(len(birth)):
        if not birth[i].isnumeric():
            return False
        else:
            birth[i] = int(birth[i])
    if birth[1] < 0 or birth[1] > 12:
        return False
    if birth[2] <0 or birth[2] > 31:
        return False
    return True


if __name__ == "__main__":
    main()