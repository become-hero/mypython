import re
html_data="<head><title>python</head></title>"
rs=re.match(r"<.+><.+>.+</.+></.+>",html_data)
print(rs)
