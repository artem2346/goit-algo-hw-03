from datetime import datetime
import random
import re

 #1


def get_days_from_today(date):
    try:
        date_input = datetime.strptime(date,"%Y-%m-%d").toordinal()
        date_now = datetime.now().toordinal()
        return int(date_now - date_input)
    except:
        print('please,check and correct your data')



print(get_days_from_today('2027-10-09'))



#2

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000:
        random_variables = set([random.randint(min,max) for x in range(quantity)])
        while True:
            if len(random_variables) != quantity:
                random_variables.add(random.randint(min,max))
            else:
                break
        random_choices_variables_sorted = sorted(list(random_variables))
        return random_choices_variables_sorted
    else:
        return []



print(get_numbers_ticket(10, 20, 5))



#3


def normalize_phone(phone_number):
    delete_gap = phone_number.strip()
    num = re.sub(r"[^0-9]","",delete_gap)

    if len(num) < 10:
        return 'Please enter a valid number'
    
    elif re.search(r"^0",num):
        if  len(num) != 10:
            return 'Please check your number'
        
        num = re.sub(r"^0","+380",num)
        return num
    elif re.search(r"^\d{3}",num).group() == '380':
        if len(num) != 12:
            return 'Please check your number'
        num = re.sub(r"^\d{3}","+380",num)
        return num
    else:
        return 'Please enter a valid number'


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
print(normalize_phone('ldlld23453'))
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)




