from django.shortcuts import render
from .models import Tittle,Header,Banner,Feature,Trending,Trending_object,MostPlayed,MostPlayed_object,Category,Category_object,Shop,Newsletter,Shop_header,Section_trending,Section_trending_object,Product_header,Single_product,More_info,Related,Related_object,Contact_header,Contact
# Create your views here.

def index(request):
    tittle = Tittle.objects.all()[0]
    header = Header.objects.all()[0]
    banner = Banner.objects.all()[0]
    feature = Feature.objects.all()
    trending = Trending.objects.all()[0]
    trending_object = Trending_object.objects.all()
    mostplayed = MostPlayed.objects.all()[0]
    mostplayed_object = MostPlayed_object.objects.all()
    category = Category.objects.all()[0]
    category_object = Category_object.objects.all()
    shop = Shop.objects.all()[0]
    newsletter = Newsletter.objects.all()[0]
    return render(request,'main/index.html',context={
        'tittle':tittle,
        'header':header,
        'banner':banner,
        'feature':feature,
        'trending':trending,
        'trending_object':trending_object,
        'mostplayed':mostplayed,
        'mostplayed_object':mostplayed_object,
        'category':category,
        'category_object':category_object,
        'shop':shop,
        'newsletter':newsletter
    })

def contact(request):
    tittle = Tittle.objects.all()[0]
    header = Header.objects.all()[0]
    contact_header = Contact_header.objects.all()[0]
    contact = Contact.objects.all()[0]
    return render(request,'main/contact.html',context={
        'tittle':tittle,
        'header':header,
        'contact_header':contact_header,
        'contact':contact
    })

def product_details(request):
    tittle = Tittle.objects.all()[0]
    header = Header.objects.all()[0]
    product_header = Product_header.objects.all()[0]
    single_product = Single_product.objects.all()[0]
    more_info = More_info.objects.all()[0]
    related = Related.objects.all()[0]
    related_object = Related_object.objects.all()
    return render(request,'main/product-details.html',context={
        'tittle':tittle,
        'header':header,
        'product_header':product_header,
        'single_product':single_product,
        'more_info':more_info,
        'related':related,
        'related_object':related_object
    })

def shop(request):
    tittle = Tittle.objects.all()[0]
    header = Header.objects.all()[0]
    shop_header = Shop_header.objects.all()[0]
    section_trending = Section_trending.objects.all()[0]
    section_trending_object = Section_trending_object.objects.all()
    return render(request,'main/shop.html',context={
        'tittle':tittle,
        'header':header,
        'shop_header':shop_header,
        'section_trending':section_trending,
        'section_trending_object':section_trending_object
    })