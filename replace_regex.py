import re
str1= "9742-510-216 #phone number"
print re.sub(r'#.*$',"",str1)
a= re.sub(r'\D',"",str1)
print a
