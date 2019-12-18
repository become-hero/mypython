import re
str="\python"
rs=re.match("\\\\\w+",str)
print(str)
rs=re.match(r"\\\w+",str)
print(str)
