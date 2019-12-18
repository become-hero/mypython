import re
rs=re.match("[Hh]","hello")
print(rs)
rs=re.match("[Hh]","Hello")
print(rs)
rs=re.match("[0123456789]","3")
print(rs)
rs=re.match("[0-9]","3")
print(rs)
