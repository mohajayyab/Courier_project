# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ONWKSZpxq3xZWTg4MZv3CpO5mLvvNO_H
"""

#the data is not in chronological order .
print('1. Read the data found in the utak.txt file and solve it using it')
Courier=[] 
fbe=open('utak.txt','r') 
for sor in fbe: 
    elem=sor.strip().split() 
    nap=int(elem[0])
    ut=int(elem[1])
    km=int(elem[2])
    
    Courier.append([nap,ut,km])
    
fbe.close()
print(Courier) 
    

#find the minimum day, including the length of the 1st road in km.

firstday=7 
for i in Courier:
    if i[0]<firstday:
        firstday=i[0]
#we are looking for the km for the 1st trip of the first day
for i in Courier:
    if i[0]==firstday and i[1]==1:
        print('The first ride of the week was %s km.' %(i[2]))



# how long the last trip of the week was in km!

lastday=1 
for i in Courier:
    if i[0]>lastday:
        lastday=i[0]

lasttrip Courier=1
for i in :
    if i[0]==lastday:
        if i[1]>lasttrip:
            lasttrip=i[1]
for i in Courier:
    if i[0]==lastday and i[1]==lasttrip:
        print('The last ride of the week was %s km.' %(i[2]))

#how many days of the week the courier did not work!

days={1,2,3,4,5,6,7}

workingday=set() 
for i in Courier:
    workingday.add(i[0]) 

offday=set() 
offday=days-workingday
print('Couriers days off:',end='') #end='': a print a végrehajtás után nem kerül új sorba
for i in offday:
    print(i,end=', ')
   
print()


#day of the week had the most rides!
maxride=1
for i in Courier:
    if i[1]>maxride:
        maxride=i[1]
print(maxride)
for i in Courier:
    if i[1]==maxride:
        print('The week %s. day had the most traffic.' %(i[0]))

#the total per day 
#how many kilometers was the road?

for day in days:
    dailykm=0 
    for i in Courier:
        if day==i[0]:
            dailykm+=i[2]
    print('%s. day: %s km' %(day,dailykm))



#The courier is paid for each trip depending on the length 
def paid(distance):
    if 1<=distance<=2:
        return 500
    if 3<=distance<=5:
        return 700    
    if 6<=distance<=10:
        return 900
    if 11<=distance<=20:
        return 1400
    else:
        return 2000

km=int(input('give me the distance  '))
print('%s payment is made for the requested distance.' %paid(km))

#Determine the payment for all recorded trips (payment received)!
Courier_rend=sorted(Courier)
weeklypaid=0
fki=open('remuneration.txt','w')
for i in Courier_rend:
    fki.write('%s. nap %s. út: %s Ft\n' %(i[0],i[1],paid(i[2])))
    weeklypaid+=paid(i[2])
fki.close()

print('The courier receives a total of %s HUF for his entire weeks work.' %(weeklypaid))