file_1 =['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'] #8
file_2 = ['White', 'White', 'White', 'White', 'White', 'White', 'White', 'White', 'White', 'White', 'White'] #11
# file_3 =["Red","White","Red",........"White","Red","White","White","White"]
output=[]
for i in range(len(file_1)):
    output.append(file_1[i])
    output.append(file_2[i])
output.extend(file_2[len(file_1):])
print(output)













list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#output ['Mike', 'Emma', 'Kelly', 'Brad']

# sort data by id
json_data =[
    {'id':1,'title':"honesty is best policy.","status":True},
    {'id':3,'title':"Helth is welth.","status":True},
    {'id': 2, 'title': "Enjoying in Manali.", "status": False},
    {'id': 5, 'title': "Iphone 15 lunched.", "status": False},
    {'id': 4, 'title': "Sumsung S23 cemera is better then Iphone.", "status": False},
]

# Convert into one list
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]


def one_list(your_list):
    mylist = []
    for i in your_list:
        if isinstance(i,list):
            mylist.extend(one_list(i))
        else:
            mylist.append(i)
    return mylist

print(one_list(list1))

#find missing number
v=[1,2,3,4,6]

n =len(v)+1
missing_number =n*(n+1) //2 -sum(v)
print(missing_number)

#ans 5

# Exercise: 1
#find index posiion
v=[2,5,7,8,3]
target=9

def getTarget(nums,target):
    mydic={}
    for i,num in enumerate(nums):
        diff = target-num
        if diff in mydic:
            return [mydic[diff],i]
        mydic[num]=i
    return []
print(getTarget(v,target),"helloooooooooo")


#answer 0,2

# without count function
s = "aaaaabbbbcc"
# # output 2a4b2c

# Exercise: 2 : Arrange list in a order without inbuilt python function
input : [8,6,9,1,5,4,8,2]
# output : [1,2,4,5,6,8,9]

# Exercise: 2 : Remove duplicate without  inbuilt python function
input= [1,2,1,4,2,8,5,9,7,8,4,8]

# Exercise: 2 : How to swap dict
original_dict = {'a': 1, 'b': 2, 'c': 1}
## output   {1: 'a', 2: 'b', 3: 'c'}


