import re


def phone(phonebook, phone_no):

    if phonebook.count(phone_no) > 1:
        return "Error => Too many people: {}".format(phone_no)
    elif phonebook.count(phone_no) < 1:
        return "Error => Not found: {}".format(phone_no)

    name = ""
    address = ""
    pb_arr = phonebook.split("\n")
    for record in pb_arr:
        if record.find(phone_no) > 0:
            name = record[record.find("<") + 1:record.find(">")]
            mess_address = record.replace(phone_no, "").replace(name, "")
            clean_address = re.sub(r"[()\"#/@;:<>{}`+=~|!?,$]", "", mess_address).strip()
            address = re.sub("( +)|_", " ", clean_address)

    return "Phone => {num}, Name => {name}, Address => {address}".format(num=phone_no, name=name, address=address)
