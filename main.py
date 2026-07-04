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
    if min < 1 or max > 1000 or (max - min + 1)  < quantity:
        return []
    
    random_variables_unique = set([random.randint(min,max) for x in range(quantity)])

    while len(random_variables_unique) < quantity:

        random_variables_unique.add(random.randint(min,max))
       
        
    random_choices_variables_sorted = sorted(list(random_variables_unique))
    return random_choices_variables_sorted


print(get_numbers_ticket(10, 10, -1))



#3


def normalize_phone(phone_number):

    delete_gap = phone_number.strip()
    num = re.sub(r"[^0-9+]","",delete_gap)

    if re.search(r"^\+",num) and 7 <= len(num) <= 15:   

        if re.search(r"^\+\d{3}",num).group() == '+380' and len(num) != 13:
            return 'Please enter a valid number'
        
        return num
    
    elif len(num) == 12 and re.search(r"^\d{3}",num).group() == '380':
        num = re.sub(r"^\d{3}","+380",num)
        return num
    
    elif  len(num) == 10 and re.search(r"^0",num):
        num = re.sub(r"^0","+380",num)
        return num
    
    else:
        return 'Please enter a valid number'


print(normalize_phone("   +38(050)111-22-11   ")) 
print(normalize_phone('+3805012345673'))            
print(normalize_phone('0501234567'))                
print(normalize_phone('+331234567890'))             
print(normalize_phone('+380'))                       
print(normalize_phone('+79'))      
print(normalize_phone('+38050123456'))   
print(normalize_phone("48-12"))                
print(normalize_phone("481234567890"))        
print(normalize_phone("+86123456"))       



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
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)





