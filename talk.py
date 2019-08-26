f = open("KakaoTalk.txt", 'r',encoding = "utf-8")
lines = f.readlines()
data={}
for line in lines:
    try :
        if line[20]=='년' and line[0]=='-':
            line=line.split(' ')
            date=line[1]+' '+line[2]+' '+line[3]
        elif '[' in line and ']' in line and line[0]=='[':
            line=line.split(' ')
            id=line[0]
        if  id in data :
           del data[id]
           data[id]=date
        else :
            data[id] = date
    except :
        pass
for key, val in data.items() :
    print("ID= {key}, 마지막 접속 날짜={value}".format(key=key, value=val))
f.close()
