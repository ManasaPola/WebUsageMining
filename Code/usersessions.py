import pymongo
import pickle
import math
import numpy as np
import csv

def file_to_db(location):

    file = open(location,encoding="utf8")
    lines = file.readlines()
    file.close()
    path=set()
    hour = -1
    startmin = 0
    user_urldict = {}
    user_sessiondict = {}
    flag1=0
    flag2=0
    with open("../Data/sessions.csv", 'a') as csvFile:
        for l in lines:
                splits = l.strip().split(",")
                host = splits[0]
                hrmin = splits[3].split(":")
                url = splits[6]
                path.add(url)

                if int(hrmin[1]) in range (31,61):
                    if(flag2==0):
                        flag1=0
                        startmin = 31
                        for key in user_urldict.keys():
                            session=0
                            if key in user_sessiondict.keys():
                                session = user_sessiondict[key]
                            user_sessiondict[key] = session + 1
                            list=[]
                            list.append(user_sessiondict[key])
                            list.append(host)
                            list.append(len(user_urldict[key]))
                            writer = csv.writer(csvFile)
                            writer.writerow(list)
                        user_urldict = {}
                        flag2=1

                if int(hrmin[1]) in range(0,31):
                    if(flag1==0):
                        flag2=0
                        startmin = 0
                        for key in user_urldict.keys():
                            session = 0
                            if key in user_sessiondict.keys():
                                session = user_sessiondict[key]
                            user_sessiondict[key] = session + 1
                            list=[]
                            list.append(user_sessiondict[key])
                            list.append(host)
                            list.append(len(user_urldict[key]))
                            writer = csv.writer(csvFile)
                            writer.writerow(list)
                        user_urldict = {}
                        if hour == 23:
                            hour=0
                        else:
                            hour=hour+1
                        flag1=1

                if int(hrmin[0])==hour and int(hrmin[1])>=startmin and int(hrmin[1])<=startmin+30 :
                    urls=[]

                    if host in user_urldict.keys():
                        urls=user_urldict[host]
                    urls.append(url)
                    user_urldict[host] = urls


    print("Files stored in DB")



def main():

    file_location = "julydata200.csv"

    file_to_db(file_location)

    # with open('paths.pickle', 'wb') as handle:
    #     pickle.dump(urls, handle, protocol=pickle.HIGHEST_PROTOCOL)



main()
