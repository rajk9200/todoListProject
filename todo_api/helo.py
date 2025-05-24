from rest_framework.serializers import ModelSerializer

d={'ids':[1,2,3,4,5,6], 'id':7 }
# drive =7
# c=[1,2,3,4,5,6]


# out="Driver:"+d['id']+"co-driver"
print("driver:",d['id'], end=" ")
print("co-driver:",",".join([str(i) for i in d['ids']]))

n=5
for i in range(n):
    print(" "*(n-i),end="")
    print("* "*i, )




# bls =Blog.objects.all()
# BloglSerializer(bls,many=True)
# import asyncio

# employee
# id,name,salary,dep_id
# departmet_name
# dep_id,dep_name
#
# SELECT name,dep_name
# form employee e1
# WHERE e1dep_id =e2.dep_id
# inner join on departmet_name e2


d={'ids':[1,2,3,4,5,6], 'id':7 }
# drive =7
# c=[1,2,3,4,5,6]


out="driver {d['id]} co-drivers- {d['ids']} "
print(out)










