class employees:
    def __init__(self,fullname,education,domain,department,salary,experience):
        self.name = fullname
        self.education = education
        self.domain = domain
        self.department = department
        self.salary = salary
        self.experience = experience   

def add_employees():
    print("Add new employees in database")

    fullname = (input("enter the name of emp: "))
    education = (input("enter the education of emp: "))
    domain = (input("enter the domain of emp: "))
    department = (input("enter the working department of emp: "))
    salary = float(input("enter the salary of emp:"))
    experience = (input("enter the years of experience of emp : "))


    E1 = employees(fullname,education,domain,department,salary,experience)

    print ("\n ----Employees detail----")


    print("Name = ", E1.name)
    print("Education = ", E1.education)
    print("Domain = ",E1.domain)
    print("Department = ", E1.department)
    print("Salary = ",E1.salary)
    print("Experience = ",E1.experience)



add_employees()

#  Output:
# Add new employees in database
# enter the name of emp: Mohd monis
# enter the education of emp: BCA + MCA from TMU
# enter the domain of emp: Data Analytics + AI ML
# enter the working department of emp: Information Technology
# enter the salary of emp:60000.0
# enter the years of experience of emp : 2 years of Experience

#  ----Employees detail----
# Name =  Mohd monis
# Education =  BCA + MCA from TMU
# Domain =  Data Analytics + AI ML
# Department =  Information Technology
# Salary =  60000.0
# Experience =  2 years of Experience