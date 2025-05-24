# #code editor for python

#Question 1
file_1 =['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'] #8
file_2 = ['White', 'White', 'White', 'White', 'White', 'White', 'White', 'White', 'White', 'White', 'White'] #11
# output ["Red","White","Red",........"White","Red","White","White","White"]
output=[]
n=len(file_1)
for i in range(n):
    output.append(file_1[i])
    output.append(file_2[i])
output.extend(file_2[n:])

print(output)
#Question 2
a= ['a','b','b','c','a']
mydic={}
for i in a:
    mydic[i]=a.count(i)
print("".join([f"{k}{v}" for k,v in mydic.items() ]))
# output a2b2c1

#
# without count function
s = "aaaaabbbbcc"
# # output 2a4b2c
c = 1
output=""
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c+=1
    else:
        output +=f"{s[i-1]}{c}"
        c=1
output +=f"{s[-1]}{c}"
print(output,'o----------')



#Question 3 Sorting list when int and str both
inp= [1,'asw3',4,'fdd453po','6756dsfsd']
# output ['wsa3', 'ssfdd7665', 'pofdd543', 4, 1]
# number =sorted([i for i in inp if isinstance(i,int) ],reverse=True)
# letter=[i for i in inp if isinstance(i,str) ]
# letter.sort(reverse=True)
# print(letter)
# # number.extend(letter)
# print(number)


#Question 4 Sorting Json Data in python by id
json_data =[
    {'id':1,'title':"honesty is best policy.","status":True},
    {'id':3,'title':"Helth is welth.","status":True},
    {'id': 2, 'title': "Enjoying in Manali.", "status": False},
    {'id': 5, 'title': "Iphone 15 lunched.", "status": False},
    {'id': 4, 'title': "Sumsung S23 cemera is better then Iphone.", "status": False},
]

v=sorted(json_data, key=lambda a:a['id'])
print(v)
#output  arrange description data by id

# Question 5 remove blank element from list
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#output ['Mike', 'Emma', 'Kelly', 'Brad']
v=[i for i in list1 if i!=""]
print(v)

