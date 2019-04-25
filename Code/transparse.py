import csv


location="../Data/usertranscations.csv"
file = open(location,encoding="utf8")
lines = file.readlines()
file.close()

# leng=0
# for l in lines:
#     splits = l.split(",")
#     len_temp=len(splits)
#     if(len_temp>leng):
#         leng=len_temp
#
# print(leng)
with open("../Data/usersessions.csv", 'a') as csvFile:
    for l in lines:
        list=[]
        splits=l.split(",")
        le=len(splits)
        for i in range(0,le-1):
            if not splits[i]=="":
                list.append(splits[i])
        str=splits[-1].replace("\n",'')
        str=str.replace('"','')
        list.append(str)
        writer = csv.writer(csvFile)
        writer.writerow(list)
