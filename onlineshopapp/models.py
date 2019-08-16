from django.db import models
from django.contrib.auth.models import User 



#a tupple 1st entry goes to db and s2n id displayed

CATEGORY_CHOICES = (
    ('F', 'Food'),
    ('D', 'Detergents' ),
    ('O', 'Others') 
)
LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary' ),
    ('D', 'danger')
)
class Item(models.Model):
    title =models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices = CATEGORY_CHOICES, max_length = 2)
    category = models.CharField(choices = LABEL_CHOICES, max_length = 2)

    def __str__(self):
            return self.title
    
class OrderItem(models.Model):
    item =models.ForeignKey(Item, on_delete=models.CASCADE)
    
    def __str__(self):
            return self.title
class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,) 
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField ()
    ordered = models.BooleanField(default=False)
   
    def __str__(self):
            return self.user.username
    
class Profile(models.Model):
    image = models.ImageField(default = 'default.jpg',upload_to='images/')
    bio = models.CharField(max_length=150)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, related_name='profile') 
    
    def __str__(self):
            return self.user.username

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
        