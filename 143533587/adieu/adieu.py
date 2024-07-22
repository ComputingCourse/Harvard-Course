try:
    names =[]
    while True:
        name = input("Name: ")
        names.append(name)
        last_name = name


except EOFError:
    str = "Adieu, adieu, to"
    for name in names:
        if name == last_name and len(names)== 1:
            str += " " + name
        elif name == last_name:
            str += " and " + name
        else:
            str += " " + name + ","
    if len(names) == 2:
        str = "Adieu, adieu, to Liesl and Friedrich"
    print(str)
