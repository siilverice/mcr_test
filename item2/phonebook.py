def phone(phonebook, phone_no):
    if phonebook.count(phone_no) > 1:
        return "Error => Too many people: {}".format(phone_no)
    elif phonebook.count(phone_no) < 1:
        return "Error => Not found: {}".format(phone_no)

    # TODO:
    # split \n to array
    # find <*> to be name
    # find address
    return "Phone => {num}, Name => {name}, Address => {address}".format(num=phone_no, name="", address="")
