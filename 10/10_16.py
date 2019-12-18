import re
html_data="<head><title>python</title></head>"
rs=re.match(r"<(?P<g1>.+)><(?P<g2>.+)>.+</(?P=g2)></(?P=g1)>",html_data)
print(rs)
html_data_err="<head><title>python</title></head>"
rs=re.match(r"<(?P<g1>.+)><(?P<g2>.+)>.+</(?P=g2)></(?P=g1)>",html_data_err)
print(rs)
