from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    b = ("b", "B")
    m = ("m", "M")
    ph = ("ph", "PH")

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Role, default=Role.b)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

