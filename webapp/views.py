from django.shortcuts import render,redirect
from webapp.models import Contact_Db,RegisterDb,CartDb,checkout_DB
from Mobileapp.models import Mobile_Db,MobDb
from django.contrib import messages
import razorpay
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage


# Create your views here.
def Home_page(req):
    cat = Mobile_Db.objects.all()
    product = MobDb.objects.all()
    return render(req,"Home_page.html",{'cat':cat,'product':product})
def About_page(req):
    cat = Mobile_Db.objects.all()
    return render(req,"About_us.html",{'cat':cat})
def Contact_page(req):
    cat = Mobile_Db.objects.all()
    return render(req,"Contact.html",{'cat':cat})
def save_contact(req):
    if req.method == "POST":
        na = req.POST.get('name')
        em =  req.POST.get('email')
        ms =  req.POST.get('msg')
        obj5 = Contact_Db(Name=na, Email=em, Message=ms)
        obj5.save()
        messages.success(req,"message sent successfully..!")
        return redirect(Contact_page)
def All_products(req):
    cat = Mobile_Db.objects.all()
    product=MobDb.objects.all()
    return render(req,"All_products.html",{'product':product,'cat':cat})
def mobile_details(req,pro_id):
    cat = Mobile_Db.objects.all()
    products=MobDb.objects.get(id=pro_id)
    return render(req,"mobile_details.html",{'products':products,'cat':cat})
def filtered_product(req, mob_name):
    cat = Mobile_Db.objects.all()
    data = MobDb.objects.filter(CompanyName=mob_name)
    return render(req, "filtered_product.html", {'data': data,'cat':cat})
def Register_page(req):
    return render(req,"Register_page.html")
def save_register(req):
    if req.method=="POST":
        un=req.POST.get('name')
        em=req.POST.get('email')
        ps=req.POST.get('pass')
        cp=req.POST.get('cpass')
        obj6=RegisterDb(User_Name=un,Email=em,Password=ps,Cpassword=cp)
        obj6.save()
        messages.info(req,"registered successfully..!")
        return redirect(Register_page)

def User_login(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        ps = request.POST.get('upass')
        if RegisterDb.objects.filter(User_Name=un,Password=ps).exists():
            request.session['User_Name']=un
            request.session['Password']=ps
            messages.success(request,"welcome..!")
            return redirect(Home_page)
        else:
            messages.warning(request,"Invalid user or password..!")
            return redirect(Register_page)
    else:
        # messages.warning(request,"User not found..!")
        return redirect(Register_page)
def User_logout(request):
    del request.session['User_Name']
    del request.session['Password']
    messages.info(request,"logout Successfully...!")
    return redirect(Home_page)
def save_cart(request):
    if request.method=="POST":
        un = request.POST.get('name')
        pn= request.POST.get('mobilename')
        qn= request.POST.get('quantity')
        ps= request.POST.get('price')
        tp= request.POST.get('totalprice')
        obj = CartDb(User_Name=un,Mobile_Name=pn,Quantity=qn,Price=ps,Totalprice=tp)
        obj.save()
        messages.info(request, "added to cart..!")
        return redirect(Home_page)
def cart_page(request):
    cat=Mobile_Db.objects.all()
    data=CartDb.objects.filter(User_Name=request.session['User_Name'])
    sub_total=0
    shipping=0
    total=0
    for i in data:
        sub_total += i.Totalprice
    if sub_total>10000:
        shipping=150
    else:
        shipping=250
    total = sub_total+shipping
    return render(request,"cart.html",{'data':data,'cat':cat,'sub_total':sub_total,'shipping':shipping,'total':total})
def delete_cart(req,cart_id):
    x = CartDb.objects.filter(id=cart_id)
    x.delete()
    messages.info(req,"Item removed from cart...!")
    return redirect(cart_page)
def checkout_page(request):
    cat=Mobile_Db.objects.all()
    data=CartDb.objects.filter(User_Name=request.session['User_Name'])
    sub_total = 0
    shipping = 0
    total = 0
    for i in data:
        sub_total += i.Totalprice
    if sub_total > 10000:
        shipping = 150
    else:
        shipping = 250
    total = sub_total + shipping
    return render(request,"checkout.html",{'data':data,'sub_total':sub_total,'shipping':shipping,'total':total,'cat':cat})

def Payment_page(request):
    customer = checkout_DB.objects.order_by('-id').first()
    payy = customer.Total_price
    amount = int(payy * 100)
    payy_str = str(amount)

    for i in payy_str:
        print(i)

    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_oVF8wJ5V3HMhtw', 'dJzANZczPrdD0sYFoztgOpS8'))
        payment = client.order.create({'amount': amount, 'currency': order_currency})
    return render(request,"Payment.html",{'customer':customer,'payy_str':payy_str})
def save_checkout(request):
    if request.method=="POST":
        un = request.POST.get('name')
        em = request.POST.get('email')
        pl= request.POST.get('place')
        ad = request.POST.get('address')
        mb= request.POST.get('mobile')
        ms= request.POST.get('message')
        tp=request.POST.get('price')
        obj7 = checkout_DB(User_Name=un,Email=em,Place=pl,Address=ad,Mobile=mb,Message=ms,Total_price=tp)
        obj7.save()
        return redirect(Payment_page)
# def whishlist(request):
#     data = CartDb.objects.filter(User_Name=request.session['User_Name'])
#     return render(request,"whishlist.html",{'data':data})

# def save_whishlist(request):
#         if request.method == "POST":
#             un = request.POST.get('name')
#             pn = request.POST.get('mobilename')
#             qn = request.POST.get('quantity')
#             ps = request.POST.get('price')
#             tp = request.POST.get('totalprice')
#             # img1= request.FILES['image']
#             objj = whishlistDb(User_Name=un, Mobile_Name=pn, Quantity=qn, Price=ps, Totalprice=tp)
#             objj.save()
#             messages.info(request, "added to cart..!")
#             return redirect(Home_page)



