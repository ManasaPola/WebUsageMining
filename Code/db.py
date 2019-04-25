import pymongo
import pickle
import math
import numpy as np


db = pymongo.MongoClient().MWDB

# delete everything from MongoDB
def delete_all_db():
    db.bulk_write([pymongo.DeleteMany({})])

def file_to_db(location):
    delete_all_db()
    unique_hosts = set()
    unique_urls =set()

    file = open(location, encoding="utf8")
    lines = file.readlines()
    file.close()
   # root_count = len(lines)
    hour = -1
    startmin = 0
    user_sessiondict={}
    user_urldict = {}
    flag1=0
    flag2=0
    count=0
  #  userstranscations=[]
    for l in lines:
            splits = l.strip().split("\t")
            host = splits[0]
            datetime = splits[1].strip().split("T")
            time = datetime[1].split("+")
            hrmin=time[0].split(":")
            url = splits[2]

            unique_hosts.add(host)
            unique_urls.add(url)

            if int(hrmin[1]) in range (31,61):
                if(flag2==0):
                    flag1=0
                   # usertrans=[]
                    startmin = 31
                    for key in user_urldict.keys():
                        session=0
                        count=count+1

                    #    usertrans.extend(user_urldict[key])

                        if key in user_sessiondict.keys():
                            session=user_sessiondict[key]
                        user_sessiondict[key]=session+1
                        store_db(key, session+1, user_urldict[key],count)

                   # userstranscations.append(usertrans)
                    user_urldict = {}
                    flag2=1

            if int(hrmin[1]) in range(0,31):
                if(flag1==0):
                    flag2=0
                    startmin = 0
                   # usertrans=[]

                    for key in user_urldict.keys():
                        count=count+1
                        session = 0

                   #     usertrans.extend(user_urldict[key])

                        if key in user_sessiondict.keys():
                            session = user_sessiondict[key]
                        user_sessiondict[key] = session + 1
                        store_db(key, session+1, user_urldict[key],count)
                 #   if(len(user_urldict.keys())>0):
                  #      userstranscations.append(usertrans)
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
   # return userstranscations

# store host, time,url in MongoDB
def store_db(host, id, urls,count):

    db.insert_many(
        [{'host': host, 'session_id': id, 'sequence':len(urls)-i, 'url': urls[i],'session':count} for i in range(len(urls))])

# returns distinct values of a column
def get_distincts(column):
    return db.distinct(column)



def get_transcations(hosts):
    result = set()
    search_results = db.find()
    for request in search_results:
        result.add(str(hosts.index(request["host"]))+" "+str(request["session_id"]))
    return result

def get_col(transcation,hosts,urls):
    result=np.zeros(len(urls))
    user_sessionid=transcation.split(" ")
    search_results = db.find({"host":hosts[int(user_sessionid[0])],"session_id":int(user_sessionid[1])}).sort( [( "sequence", -1 )] )
    tran=[]
    for request in search_results:
        index =urls.index(request["url"])
        result[index]=int(request["sequence"])
        tran.append(index)
    return result,tran


def construct_matrix():
    hosts = get_distincts("host")
    urls = get_distincts("url")
    transcations = get_transcations(hosts)
    matrix = np.zeros((len(transcations), len(urls)))
    trans = []
    for i, transcation in enumerate(transcations):
        matrix[i],tran = get_col(transcation,hosts,urls)
        trans.append(tran)

    return hosts,urls,transcations,matrix,trans



def main():
    global db
    global file_location
    db = pymongo.MongoClient().swm.logs
    file_location = "nasa1.txt"

   # file_to_db(file_location)

    hosts,urls,transcations,matrix,trans = construct_matrix()
   # print(len(userstranscations[0]))
    with open('hosts.pickle', 'wb') as handle:
        pickle.dump(hosts, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('urls.pickle', 'wb') as handle:
        pickle.dump(urls, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('transcations.pickle', 'wb') as handle:
        pickle.dump(transcations, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('matrix.pickle', 'wb') as handle:
        pickle.dump(matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('usersessions.pickle', 'wb') as handle:
        pickle.dump(trans, handle, protocol=pickle.HIGHEST_PROTOCOL)


  #  with open('transcations.pickle', 'rb') as handle:
   #     transcations = pickle.load(handle)

   # with open('urls.pickle', 'rb') as handle:
   #     urls = pickle.load(handle)

   # with open('hosts.pickle', 'rb') as handle:
    #    hosts = pickle.load(handle)

   # hosts, urls, transcations, trans = construct_matrix(hosts,urls,transcations)

  #  with open('usersessions.pickle', 'wb') as handle:
  #      pickle.dump(trans, handle, protocol=pickle.HIGHEST_PROTOCOL)

 #   with open('usersessions.pickle', 'rb') as handle:
   #     usersessions = pickle.load(handle)

   # with open('matrix.pickle', 'rb') as handle:
   #     matrix = pickle.load(handle)

   # print(len(transcations))
   # print(len(urls))
   # print(len(usersessions))
   # print(len(matrix))
   # print(len(matrix[0]))


    #print(hosts)
    #print(urls)
    #print(transcations)
    #print(matrix[0][0])

main()



