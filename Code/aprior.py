import pickle
from efficient_apriori import apriori
import csv
import pandas as pd

from itertools import combinations


# with open('usersessions.pickle', 'rb') as handle:
#     usersessions = pickle.load(handle)
#
#
# print(len(usersessions))
#
# with open('usersessions.csv','rb') as f:
#     reader=csv.reader(f)
#     usersessions = list(reader)
# f.close()

usersessions=[]
location="../Data/usersessions.csv"
file = open(location,encoding="utf8")
lines = file.readlines()
file.close()

for l in lines:
    l=l.replace("\n",'')
    l=l.replace('"','')
    usersessions.append(tuple(l.split(",")))


print(usersessions[0])
itemsets, rules = apriori(usersessions,min_support=0.05,  min_confidence=0.5)

for rule in sorted(rules, key=lambda rule: rule.confidence,reverse=True):
  print(rule)

#print(itemsets[2])
#print(list(rules))
