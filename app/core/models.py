from django.db import models
import string
import random
# Create your models here.

def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Member.objects.filter(code=code).count() == 0:
            break
    return code

    

class Member(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    booking_count = models.IntegerField()
    date_joined = models.DateField()
    
    def __str__(self):
        return self.name + ' '+ self.surname

class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    
    def __str__(self):
        return f"File Name: {self.file_name}"
    
    
    
class Inventory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    remaining_count = models.IntegerField()
    expiration_date = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    

class Booking(models.Model):
    booking_ref = models.CharField(max_length=8, default=generate_unique_code, unique=True)
    member = models.ForeignKey('Member', related_name='member', on_delete=models.CASCADE)
    item = models.ForeignKey('Inventory', related_name='items', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.booking_ref
    
    