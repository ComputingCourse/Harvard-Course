months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
month = "00"
finished = False
while not finished:
    try:
        date = input("Date: ")
        date = date.replace(" ","")
        if date[0].isnumeric():#mm/dd/yyyy
            year = date[-4:]
            if date[1].isnumeric():
                month = date[0] + date[1]
                if date[4].isnumeric():
                    day = date[3]+ date[4]
                else:
                    day = "0" + date[3]
            else:
                month = "0" + date[0]
                if date[3].isnumeric():
                    day = date[2]+date[3]
                else:
                    day = "0" + date[2]
        else:#month dd, yyyy
            year = date[-4:]
            done = False
            for i in range(len(date)):
                if not done:
                    if date[i].isnumeric():
                        month = date[:i]
                        month = months.index(month) + 1
                        #month = "0" + month if len(month) == 1 else month
                        if date[i+1].isnumeric():
                            day = date[i] + date[i+1]
                        else:
                            day = "0" + date[i]
                        done = True
        if int(day) < 32 and int(month) < 13:
            print(f"{year}-{int(month):02d}-{int(day):02d}")
            finished = True
    except: pass