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

class Profile(models.Model):
    image = models.ImageField(default = 'default.jpg',upload_to='images/')
    bio = models.CharField(max_length=150)
    email = models.EmailField()
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, related_name='profile') 
    
    def __str__(self):
            return self.user.username

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
class Item(models.Model):
    title =models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices = CATEGORY_CHOICES, max_length = 2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
            return self.title
    
    
    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })
    @classmethod
    def search_item(cls, name):
        items = cls.objects.filter(category__icontains=name)
        return items
    
class OrderItem(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    ordered = models.BooleanField(default=False)
    item =models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    
    def get_total_item_price(self):
        return self.quantity * self.item.price
    
class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,) 
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField ()
    ordered = models.BooleanField(default=False)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
   
    def __str__(self):
            return self.user.username
        
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
        