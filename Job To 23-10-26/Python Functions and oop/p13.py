#Write a function using `**kwargs` to display student details.  

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


student_details(name="Jenil", age=22, course="Python")