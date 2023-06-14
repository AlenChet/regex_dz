from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    #pprint(contacts_list)


def get_normal_name(rows):
    result = [' '.join(employee[0:3]).split(' ')[0:3] + employee[3:7] for employee in rows]
    return result


def delete_duplicate(new_name):
    not_duplicate = []
    for new in new_name:
        for employee in new_name:
            if new[0:2] == employee[0:2]:
                list_employee = new
                new = list_employee[0:2]
                for i in range(2, 7):
                    if list_employee[i] == '':
                        new.append(employee[i])
                    else:
                        new.append(list_employee[i])
        if new not in not_duplicate:
            not_duplicate.append(new)
    return not_duplicate


def update_numbers(rows, reg, new):
    pat = re.compile(reg)
    book_phone = [[pat.sub(new, string) for string in strings] for strings in rows]
    return book_phone


name_list = get_normal_name(contacts_list)
not_duplicate_list = delete_duplicate(name_list)
reg = r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})'
list_correct = update_numbers(not_duplicate_list, reg, r'+7(\2)\3-\4-\5')
reg_2 = r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s]*[(доб.\s]*(\d+)[)]*'
new_phonebook = update_numbers(list_correct, reg_2, r'+7(\2)\3-\4-\5 доб.\6')


with open("new_phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_phonebook)