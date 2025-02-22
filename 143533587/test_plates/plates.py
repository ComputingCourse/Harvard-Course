def main():
    plate = input("Enter your plate: ")
    print(is_valid(plate))


def is_valid(plate):
    valid = True
    ret = False
    if len(plate) >= 2 and len(plate) <= 6:
        if plate[0].isalpha() and plate[1].isalpha():
            num = False
            for letter in plate:
                if letter.isnumeric():
                    if not num:
                        if letter == "0":
                            valid = False
                    num = True
                elif not letter.isalpha():
                    valid = False
                else:
                    if num:
                        valid = False
            ret = True
    if not valid and ret:
        ret = False
    return ret


if __name__ == "__main__":
    main()