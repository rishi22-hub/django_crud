from django.db import models

class Company(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    description=models.TextField()
    industry=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=100)
    est_date=models.DateTimeField()
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Employee(models.Model):
    cmp_name=models.ForeignKey(Company,on_delete=models.CASCADE)
    emp_name=models.CharField(max_length=100,default="abc")
    join_date=models.DateField()
    emp_address=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    def __str__(self):
        return self.emp_name

