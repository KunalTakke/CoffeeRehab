from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=30)
    desc=models.CharField(max_length=300)
    pub_data=models.DateField()
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='coffee/images',default='')

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=40,default='')
    phone=models.CharField(max_length=30,default='')
    msg=models.CharField(max_length=500,default='')
   

    def __str__(self):
        return self.name

