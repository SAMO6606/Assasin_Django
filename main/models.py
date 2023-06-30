from django.db import models

# Create your models here.


class Tittle(models.Model):
    tittle_name = models.CharField('Tittle Name', max_length=60)

class Header(models.Model):
    logo = models.ImageField('Site Logo', upload_to='images')
    page1 = models.CharField('Page1', max_length=30)
    page2 = models.CharField('Page2', max_length=30)
    page3 = models.CharField('Page3', max_length=30)
    page4 = models.CharField('Page4', max_length=30)

class Banner(models.Model):
    name1 = models.CharField('name1',max_length=60)
    name2 = models.CharField('name2',max_length=60)
    text = models.TextField('Text')
    button_name = models.CharField('Button Name', max_length=60)
    img = models.ImageField('image', upload_to='images')
    price = models.CharField('Price', max_length=60)
    offer = models.CharField('Offer', max_length=60)

class Feature(models.Model):
    name = models.CharField('Feature name', max_length=30)
    img = models.ImageField('image', upload_to='images')

class Trending(models.Model):
    name1 = models.CharField('name1',max_length=60)
    name2 = models.CharField('name2',max_length=60)
    button_name = models.CharField('Button Name', max_length=60)

class Trending_object(models.Model):
    img = models.ImageField('image', upload_to='images')
    price1 = models.CharField('Price1', max_length=60)
    price2 = models.CharField('Price2', max_length=60)
    category = models.CharField('Category ', max_length=30)
    name = models.CharField(' name', max_length=30)

class MostPlayed(models.Model):
    name1 = models.CharField('name1',max_length=60)
    name2 = models.CharField('name2',max_length=60)
    button_name = models.CharField('Button Name', max_length=60)

class MostPlayed_object(models.Model):
    img = models.ImageField('image', upload_to='images')
    category = models.CharField('Category ', max_length=30)
    name = models.CharField(' name', max_length=30)
    button_name = models.CharField('Button Name', max_length=60)

class Category(models.Model):
    name1 = models.CharField('name1',max_length=60)
    name2 = models.CharField('name2',max_length=60)

class Category_object(models.Model):
    name = models.CharField(' name', max_length=30)
    img = models.ImageField('image', upload_to='images')

class Shop(models.Model):
    name1 = models.CharField('name1',max_length=60)
    name2 = models.CharField('name2',max_length=60)
    name3_blue = models.CharField('name3 Blue',max_length=60)
    text = models.TextField('Text')
    button_name = models.CharField('Button Name', max_length=60)


class Newsletter(models.Model):
    name1 = models.CharField('name1',max_length=60)
    name2 = models.CharField('name2',max_length=60)
    name3_blue = models.CharField('name3 Blue',max_length=60)
    name4 = models.CharField('name4',max_length=60)
    text = models.TextField('Text')
    button_name = models.CharField('Button Name', max_length=60)

class Shop_header(models.Model):
    name1 = models.CharField('name1',max_length=60)
    name2 = models.CharField('name2',max_length=60)
    name3 = models.CharField('name3',max_length=60)

class Section_trending(models.Model):
    name1 = models.CharField('name1',max_length=60)
    name2 = models.CharField('name2',max_length=60)
    name3 = models.CharField('name3',max_length=60)
    name4 = models.CharField('name4',max_length=60)

class Section_trending_object(models.Model):
    img = models.ImageField('image', upload_to='images')
    price1 = models.CharField('Price1', max_length=60)
    price2 = models.CharField('Price2', max_length=60)
    category = models.CharField('Category ', max_length=30)
    name = models.CharField(' name', max_length=30)

class Product_header(models.Model):
    name1 = models.CharField('name1',max_length=60)
    name2 = models.CharField('name2',max_length=60)
    name3 = models.CharField('name3',max_length=60)
    name4 = models.CharField('name4',max_length=60)

class Single_product(models.Model):
    img = models.ImageField('imge', upload_to='images')
    name = models.CharField('name',max_length=60)
    price1 = models.CharField('Price1', max_length=60)
    price2 = models.CharField('Price2', max_length=60)
    text = models.TextField('Text')
    button_name = models.CharField('Button Name', max_length=60)
    category1 = models.CharField('category1',max_length=60)
    category1_a = models.CharField('category1_a',max_length=60)
    category2 = models.CharField('category2',max_length=60)
    category2_a = models.CharField('category2_a',max_length=60)
    category3 = models.CharField('category3',max_length=60)
    category3_a = models.CharField('category3_a',max_length=60)

class More_info(models.Model):
    button_name1 = models.CharField('Button Name 1', max_length=60)
    button_name2= models.CharField('Button Name 2', max_length=60)
    text1 = models.TextField('Text1')
    text2 = models.TextField('Text2')
    text3 = models.TextField('Text3')
    text4 = models.TextField('Text4')

class Related(models.Model):
    name1 = models.CharField('name1',max_length=60)
    name2 = models.CharField('name2',max_length=60)
    button_name = models.CharField('Button Name', max_length=60)

class Related_object(models.Model):
    img = models.ImageField('imge', upload_to='images')
    name = models.CharField('name',max_length=60)

class Contact_header(models.Model):
    name1 = models.CharField('name1',max_length=60)
    name2 = models.CharField('name2',max_length=60)
    name3 = models.CharField('name3',max_length=60)

class Contact(models.Model):
    name1 = models.CharField('name1',max_length=60)
    name2 = models.CharField('name2',max_length=60)
    text = models.TextField('Text')
    addres = models.CharField('adress', max_length=60)
    phone = models.CharField('phone', max_length=60)
    email = models.EmailField('email')
    




    
    













    





    





    













    

    




