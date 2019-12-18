db_info=( "192.168.1.1",3306,"root","root123" ) 
ip=db_info[0]
port=db_info[1]
print("ip: {},port:{}".format(ip,port))
#for item in db_info:
#    print(item)
i=0
while i<len(db_info):
    print(db_info[i])
    i += 1
