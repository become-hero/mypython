import re
rs=re.match("...","abc")
print(rs.group())
rs=re.match(".","\n")
print(rs.group())
#rs=re.match(".","abc")
#print(rs.group())
