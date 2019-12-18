import re
html_data="<head><title>python</title></head>"
rs=re.match(r"<(.+)><(.+)>.+</\2></\1>",html_data)
print(rs)
html_data="<head><title>python</head></title>"
rs=re.match(r"<(.+)><(.+)>.+</\2></\1>",html_data)
print(rs)
