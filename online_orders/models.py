from django.db import models
from django.contrib.auth.models import User
import random
# from .tests import UniqueCheck
# Create your models here.
User_type=(
    ('ADMIN','ADMIN'),
    ('SUPPLIER','SUPPLIER'),
    ('CONSUMER', 'CONSUMER'),
)
class UserType(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # username = models.CharField(max_length=40,default='',blank=True)
    # password = models.CharField(max_length=300,default='',blank=True)   
    user_type = models.CharField(max_length=15,choices=User_type,blank=True)
    def __str__(self):
        return f'{self.user}-{self.user_type}' 
    
class Product_type(models.Model):
    product_name = models.CharField(max_length=40,default='',blank=True)
    cipher = models.CharField(max_length=60,default='',blank=True)                                                                           

class Cipher(models.Model):
    name=models.CharField(max_length=20,default='',null=True)
    inp6=models.CharField(max_length=20,default='',null=True)
    inp7=models.CharField(max_length=20,default='',null=True)
    def __str__(self):
        return self.name
       
class Calculation(models.Model):
    calc_name=models.CharField(max_length=20,default='',null=True)
    inp1=models.CharField(max_length=20,default='',null=True)
    inp2=models.CharField(max_length=20,default='',null=True)
    inp3=models.CharField(max_length=20,default='',null=True)
    inp4=models.CharField(max_length=20,default='',null=True)
    inp5=models.CharField(max_length=20,default='',null=True)
    cipher = models.ForeignKey(Cipher, on_delete=models.SET_NULL, null=True)
    Code_it_calc=models.BooleanField('',default=True) 
    def __str__(self):
        return self.calc_name



class Product(models.Model):
            
    def create_new_unique_no():
        not_unique = True
        while not_unique:
            unique_ref = random.randint(111111,999999)
            if not Product.objects.filter(unique_no=unique_ref):
                not_unique = False
        return str(unique_ref)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    unique_no = models.CharField(max_length=8,blank=True,default=create_new_unique_no)  
    product = models.CharField(max_length=100,default='',blank=True)  
    price = models.FloatField(blank=True) 
    quantity = models.FloatField(blank=True) 
    productType = models.ForeignKey(Product_type,on_delete=models.SET_NULL,blank=True,null=True)
    

    def __str__(self):
        return f'{self.user}-{self.product}' 

class PrimaryImageAttachment(models.Model): 
    product = models.OneToOneField(Product,on_delete=models.CASCADE,blank=True,null=True)
    file = models.FileField(upload_to ='product\primaryImages')                                                                   
    def __str__(self):
        return f'{self.product}  -  {self.file.url}' 
class SecondaryImageAttachment(models.Model): 
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    file = models.FileField(upload_to ='product\secondaryImages')   
    def __str__(self):
        return f'{self.product}  -  {self.file.url}'    






        