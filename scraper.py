import re
# import pprint #for pretty print

with open("data.txt") as file:
    content = file.read()
emailRegex  =  re.compile(r'[a-zA-Z0-9_.+]+@.*com')
emails = '\n'.join(emailRegex.findall(content))
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNums = '\n'.join(phoneRegex.findall(content))
# pprint.pprint(phoneNums)
# pprint.pprint(emails)

with open("emails.txt", 'w') as file:
    file.write(emails)

with open("phone_numbers.txt",'w') as file:
    file.write(phoneNums)