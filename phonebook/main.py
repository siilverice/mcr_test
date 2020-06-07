import re


def phone(phonebook, phone_no):
    count_occurs = phonebook.count(phone_no)
    if count_occurs > 1:
        return "Error => Too many people: {}".format(phone_no)
    elif count_occurs < 1:
        return "Error => Not found: {}".format(phone_no)

    name = ""
    address = ""
    pb_arr = phonebook.split("\n")
    for record in pb_arr:
        if record.find(phone_no) > 0:
            # find name
            name = record[record.find("<") + 1:record.find(">")]
            # find address
            mess_address = record.replace(phone_no, "").replace(name, "")
            clean_address = "".join(ch for ch in mess_address if ch.isalnum() or ch in [".", "-", " ", "_"]).strip()
            address = re.sub("( +)|_", " ", clean_address)

    return "Phone => {num}, Name => {name}, Address => {address}".format(num=phone_no, name=name, address=address)
