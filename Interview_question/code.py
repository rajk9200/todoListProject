# #data
#
# # s="aaaabbbbcc"
# # # output 4a4b2c
# # s1=""
# # ns=[]
# # for i in s:
# #     if i not in ns:
# #         ns.append(i)
# # for v in ns:
# #     c =s.count(v)
# #     s1=s1+str(s.count(v))+v
# #


# # print(s1)
#
# print(chr(ord('A')+32))

# s = "aaaabbbbccabffd"
# output = ""
# count = 1
# for i in range(1,len(s)):
#     if s[i]==s[i-1]:
#         count +=1
#     else:
#         output += str(count)+s[i-1]
#         count=1
# output += str(count) + s[-1]
# print(output)
# # for i in range(1, len(s)):
# #     if s[i] == s[i - 1]:
# #         print(s[i - 1])
# #         count += 1
# #     else:
# #         output += str(count) + s[i - 1]
# #         count = 1
# #
# # # Add the count and the last character
# # output += str(count) + s[-1]
# #
# # print(output)




# s = "abbbbcca"
# # output 2a4b2c
# output = ""
# count=1
# for i in range(1,len(s)):
#     if s[i]==s[i-1]:
#         count +=1
#     else:
#         output += str(count)+s[i-1]
#         count=1
# output += str(count)+s[-1]
# print(output)
count=1
output = ""
s = "abbbbcca"
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count +=1
    else:
        output+=str(count)+s[i-1]
        count = 1
output+=str(count)+s[-1]
print(output)







# s = "abbbbcca"
# output = ""
# count = 1
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         count += 1
#     else:
#         output += str(count) + s[i - 1]
#         count = 1
# # Add the count and the last character
# output += str(count) + s[-1]
# print(output)



# class A:
#     def zyx(self):
#         print("A called")
#
# class B(A):
#     pass
#
#
# b=B()
# b.zyx()


# json_data=[
#     {'id':1,'name':"aman"},
#     {'id':3,'name':"Suresh"},
#     {'id':4,'name':"Arvind"},
#     {'id':2,'name':"Ameena"}
# ]
#
# sorted_data = sorted(json_data, key=lambda x: x['name'])
