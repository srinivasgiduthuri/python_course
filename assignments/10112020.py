# Create a class to represent an employee with employee name, job, and salary. Job can be Programmer, Tester or DBA.
# Provide constructor(__init__) and methods net_salary(...) should calculate salary along with hra
# change_job(...) which takes new job and changes job of the employee
# hra is based on the job programmer - 30%, tester - 25%, dba - 40%
class Employee:
    job_hra_dict = {"programmer": 30, "tester": 25, "dba": 40}

    def __init__(self, name, job, salary):
        Employee.validate_job(job)
        self.name = name
        self.job = job
        self.salary = salary

    @staticmethod
    def validate_job(job):
        if job not in Employee.job_hra_dict.keys():
            raise ValueError(F"Invalid job : {job}")

    def net_salary(self):
        return self.salary * (1 + Employee.job_hra_dict[self.job] / 100)

    def change_job(self, new_job):
        Employee.validate_job(new_job)
        self.job = new_job

    def print_details(self):
        return self.name + " - " + self.job + " - " + str(self.salary) + " - " + str(self.net_salary())


employee1 = Employee("Steve", "dba", 10000)
print(employee1.print_details())
employee2 = Employee("John", "programmer", 10000)
print(employee2.print_details())
employee3 = Employee("John", "tester", 10000)
print(employee3.print_details())
# employee1.change_job("sse")
employee1.change_job("programmer")
print(employee1.print_details())
