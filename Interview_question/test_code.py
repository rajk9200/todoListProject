# # #code editor for python
# file_1 =['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'] #8
# file_2 = ['White', 'White', 'White', 'White', 'White', 'White', 'White', 'White', 'White', 'White', 'White'] #11
# # file_3 =["Red","White","Red",........"White","Red","White","White","White"]
#
# file_4 =[]
# for i in range(len(file_2)):
#     if len(file_1)>i:
#         file_4.append(file_1[i])
#     file_4.append(file_2[i])
# # print(file_4)
# # for i in range(len(file_2)):
# #     if i <len(file_1):
# #         file3.append(file_1[i])
# #     file3.append(file_2[i])
# # print(file3)
#
#
# a= ['a','b','b','c','a']
# b=list(set(a))
# b.sort()
# v=""
# for j in b:
#     v=v+f"{j}{a.count(j)}"
#
# print(v)
#
#
# # b=[]
# # for i in a:
# #     if i not in b:
# #         b.append(i)
# # for j in b:
# #     v =a.count(j),j
# #     print(v)
#
#
#
#
#
#
#
#
#
#
#
#
# # s=sorted(inp,key=lambda x:x[''])
# # print(s)
# # reversed order
# inp = [1,'asw3',4,'fdd453po','6756dsfsd']
# # out = ['wsa3','ssfdd7665','pofdd543',4,1]
# list1=[]
# list2=[]
# for i in inp:
#     if str(i).isdigit():
#         list2.append(i)
#     else:
#         v =[s for s in i]
#         v.sort(reverse=True)
#         list1.append("".join(v))
# list2.sort(reverse=True)
# list1.sort(reverse=True)
#
# list1.extend(list2)
# print(list1)
#
#
#
#
#
#
#
#
# # def mysort():
# #     pass
# #
# #
# # result = sorted(inp, key=mysort)
#
#
#
#
# # v1=[]
# # v2=[]
# # for i in inp:
# #     if str(i).isdigit():
# #         v1.append(i)
# #     else:
# #         s=str(i)[::-1]
# #         print(s)
#
#
#
#
#
#
# import random
# def fourDigitOtp(func):
#     def wrapper():
#         otp = random.randrange(1111, 9999)
#         return otp
#     return wrapper
#
#
# def sixDigitOtp():
#     otp =random.randrange(111111,999999)
#     return otp
#
# v =fourDigitOtp(sixDigitOtp)
#
# print(v())
from python_question import output

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# def removeInnerList(list1):
#     list2=[]
#     for i in list1:
#         if isinstance(i,list):
#             list2.extend(i)
#         else:
#             list2.append(i)
#     return list2
#
# list1 = [10, 20, [300, 400, [5000, 6000], 500,[5000, 6000]], 30,[5000, 6000], 40]
#


is_prime=True
v=19
for i in range(2,v):
    if v%i==0:
        is_prime=False
        break
if is_prime:
    print("value is prime")
else:
    print("value is not prime")

# user input
v=[0,1,1,2,3,5,8,13]
a,b=0,1
output=[]
for i in range(8):
    output.append(a)
    a,b=b,a+b
print(output)

def removeInnerList(list1):
    list2=[]
    for i in list1:
        if isinstance(i,list):
            list2.extend(removeInnerList(i))
        else:
            list2.append(i)
    return list2

list1 = [10, 20, [300, 400, [5000, 6000], 500,[5000, 6000]], 30,[5000, 6000], 40]

print(removeInnerList(list1))