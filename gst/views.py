from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.
import  time
from gst.models import Product
def index(request):

    price = 0
    nam = ''
    gst=0
    totalPrice=0
    if request.POST:

        print("Form will be submited here")
        nam = request.POST['name']
        price = request.POST['price']
        gst = request.POST['gst']
        te = time.time()

        totalPrice = requests.get("http://api.mathjs.org/v4/?expr=("+str(price)+"*"+str(gst)+")%2F100%2B"+str(price)).text

        product = Product(product_name=nam, product_price=price, gst=gst, totalPrice=totalPrice, timestamp=te)
        product.save()
        print(nam, price, gst, totalPrice)
        print("---------------")

    gst5 = Product.objects.filter(gst=5).count()
    gst12 = Product.objects.filter(gst=12).count()
    gst18 = Product.objects.filter(gst=18).count()
    gst28 = Product.objects.filter(gst=28).count()

    data=Product.objects.all()
    dataCount = data.count()
    gst5p = (gst5/dataCount)*100
    gst12p = (gst12/dataCount)*100
    gst18p = (gst18/dataCount)*100
    gst28p = (gst28/dataCount)*100

    print(gst28p)
    context = {
        "data": data,
        "gst5p": gst5p,
        "gst12p": gst12p,
        "gst18p": gst18p,
        "gst28p": gst28p,
        "nam": nam,
        "price": price,
        "gst": gst,
        "totalPrice": totalPrice,

    }
    return render(request,'gst/index.html', context)


# noinspection PyInterpreter
def add_product(request):



    data = Product.objects.all()
    return render(request, 'gst/index.html', {'data':data})
