import re

phNum = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #create re object
mo = phNum.findall("My numbers are 455-000-1234 and 785-125-5656") # create match object
print(mo)

#phNum.search()
#mo.group()
# mo.group(1), mo.group(2)...