#testing here

text="""
To obtain a challenging position that utilizes my skills and abilities in the Information Technology Industry
this offers professional growth while being resourceful, innovative and flexible
"""
# text =text.lower()
# d=text.count("in")
# print(d)
# import datetime
# text="2021-12-25"
# datetime.datetime.day()


emp = [("Sam", 111, "HR"), ("John", 112, "IT")]
column = ['Name', 'Emp_id', 'Dept']

dept = [("IT", "Info Tech"), ("HR", "Human Resources")]
column_dept = ['Dept_Name', 'Desc']

df_emp = pd.DataFrame(emp, columns=column)
print(df_emp)

df_dept = pd.DataFrame(emp, columns=column_dept)
print(df_dept)







