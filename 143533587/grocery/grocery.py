groceries = {}
try:
    while True:
        grocery = input("").upper()
        in_list = False
        for i in range(len(groceries)):
            try:
                if grocery == groceries[grocery]:
                    print("True")
                if not in_list:
                    groceries[grocery] +=1
                    in_list = True
            except: pass
        if not in_list:
            groceries[grocery] = 1
        #print(groceries)
except EOFError:
    myKeys = list(groceries.keys())
    myKeys.sort()
    sorted_dict = {i: groceries[i] for i in myKeys}
    for item,num in enumerate(sorted_dict):
        print(groceries[num],num)