import re
str="python java python c++"
rs=re.match("python",str)
print(rs.group())
