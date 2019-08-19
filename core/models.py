from datetime import datetime
from decimal import Decimal
from django.db import models
from django.shortcuts import reverse
from core.utils import unique_slug_generator
from django.db.models.signals import post_save, pre_save
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


# Create your models here.
DISPONIBILITE_CHOICES = (
    ('Disponible en Stock', 'Disponible en Stock'),
    ('Plus Disponible', 'Plus Disponible'),
    ('Stock Limité', 'Stock Limité')
)

DEVICE_CHOICES = (
    ('FCFA', 'FCFA'),
    ('US', 'US'),
)

class UserProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20, blank=True)

    def __str__(self):
         return "%s %s" % (self.user.first_name, self.user.last_name)
    
    class Meta:
        verbose_name = "User Profil"
        verbose_name_plural = "User Profil"

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfil.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)



class BaseModel(models.Model):
    name = models.CharField(max_length=225, verbose_name="Name")
    reference = models.CharField(max_length=225, verbose_name="Reference", blank=True)
    created_at = models.DateField(auto_now=True, verbose_name="Created at")
    updated_at = models.DateField(auto_now=False,blank=True, null=True)
    status = models.BooleanField(verbose_name="Status", default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        ordering = ['name']
        abstract = True
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(BaseModel, self).save(*args, **kwargs)




class Category(BaseModel):
    def __str__(self):
        return self.name


class Item(BaseModel):
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True, blank=True)
    disponibilite = models.CharField(choices=DISPONIBILITE_CHOICES, max_length=255)
    image = models.ImageField(upload_to='articles')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Prix', default=0.00,
                                validators=[MinValueValidator(Decimal('0.00'))])
    discount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Discount', default='',
                                validators=[MinValueValidator(Decimal('0.00'))], blank=True, null=True)
    device = models.CharField(choices=DEVICE_CHOICES, max_length=10, default="FCFA")
    percentage_reduction = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)


    class Meta:
        verbose_name_plural = "Articles"
        ordering = ['-created_at']

    def get_detail_from_article_url(self):
        return reverse("article-detail", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })

    @property
    def title(self):
        return self.name


def slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()

pre_save.connect(slug_pre_save_receiver, sender=Item)

# post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)






class Message(models.Model):
    sender_fullname = models.CharField(max_length=255)
    sender_email = models.EmailField()
    content = models.TextField()
    created_at = models.DateField(auto_now=True, verbose_name="Created at")
    reference = models.CharField(max_length=255)

    def __str__(self):
        return self.sender_fullname
    
    class Meta:
        verbose_name_plural = "Messages"
        ordering = ['-created_at']


class Header(models.Model):
    text = models.TextField()
    rank = models.IntegerField()
    image = models.ImageField(upload_to='header')
    second_image = models.ImageField(upload_to='header', blank=True)
    created_at = models.DateField(auto_now=True, verbose_name="Created at")
    updated_at = models.DateField(auto_now=False,blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Headers"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(Header, self).save(*args, **kwargs)


class ContactType(BaseModel):
    def __repr__(self):
        return self.name
    
    class Meta:
        verbose_name = "Contact Type"
        verbose_name_plural = "Contact Types"
        ordering = ['-created_at']


class Contact(models.Model):
    type_contact = models.ForeignKey(ContactType, on_delete=models.CASCADE)
    reference = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    created_at = models.DateField(auto_now=True, verbose_name="Created at")
    updated_at = models.DateField(auto_now=False,blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.reference

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(Contact, self).save(*args, **kwargs)


class Nesletter(models.Model):
    reference = models.CharField(max_length=255, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.reference

    class Meta:
        verbose_name_plural = "Newsletters"


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False, verbose_name="Commandé")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Article")
    quantity = models.IntegerField(default=1, verbose_name="Quantité")
    created_at = models.DateField(auto_now=True, verbose_name="Created at")

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
        ordering = ['-created_at']


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True, verbose_name="Created at")
    updated_at = models.DateField(auto_now=False,blank=True, null=True)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Order"
        ordering = ['-created_at']


class BlogPost(BaseModel):
    content = models.TextField()

    class Meta:
        verbose_name = "Blog Post"
    


class Comment(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now=True, verbose_name="Created at")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.blogpost.name


class Brand(models.Model):
    name = models.CharField(max_length=225, verbose_name="Name")
    reference = models.CharField(max_length=225, verbose_name="Reference")
    created_at = models.DateField(auto_now=True, verbose_name="Created at")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Banner(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    image = models.ImageField(upload_to="Banner")
    status = models.BooleanField(default=True, verbose_name="Status")

    def __str__(self):
        return self.name




