from django.shortcuts import render,redirect
import datetime
from Mobileapp.models import Mobile_Db,MobDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from webapp.models import Contact_Db,RegisterDb
from django.contrib import messages

# Create your views here.
def index_page(req):
    today=datetime.datetime.now()
    return render(req,"index.html",{'today':today})
def Add_company(req):
    return render(req,"Add_company.html")
def save_company(req):
    if req.method == "POST":
        na = req.POST.get('name')
        ds = req.POST.get('description')
        img = req.FILES['image']
        obj1=Mobile_Db(Company_Name=na, Description=ds, Company_Image=img)
        obj1.save()
        messages.success(req,"successfully saved...!")
        return redirect(Add_company)
def display_company(req):
    data=Mobile_Db.objects.all()
    return render(req,"display_company.html",{'data':data})
def Edit_Company(req,mob_id):
    data=Mobile_Db.objects.get(id=mob_id)
    return render(req,"Edit_company.html",{'data':data})
def update_comapny(req,mob_id):
    if req.method=="POST":
        na = req.POST.get('name')
        ds = req.POST.get('description')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = Mobile_Db.objects.get(id=mob_id).Company_Image
        Mobile_Db.objects.filter(id=mob_id).update(Company_Name=na, Description=ds, Company_Image=file)
        messages.success(req,"updated successfully...!")
        return redirect(display_company)
def delete_company(req,mob_id):
    x = Mobile_Db.objects.filter(id=mob_id)
    x.delete()
    messages.error(req,"Deleted successfully...")
    return redirect(display_company)
def Add_mobile(req):
    data=Mobile_Db.objects.all()
    return render(req,"Add_mobile.html",{'data':data})
def save_mobile(req):
    if req.method == "POST":
        a=req.POST.get('cname')
        b=req.POST.get('mname')
        c=req.POST.get('price')
        d=req.POST.get('description')
        img1= req.FILES['img1']
        img2=req.FILES['img2']
        img3=req.FILES['img3']
        obj3=MobDb(CompanyName=a,Mobile_Name=b,Price=c,Description=d,Mobile_Image1=img1,Mobile_Image2=img2,Mobile_Image3=img3)
        obj3.save()
        messages.success(req,"Saved Successfully...!")
        return redirect(Add_mobile)
def display_mobile(req):
    data = MobDb.objects.all()
    return render(req,"display_mobile.html",{'data':data})
def edit_mobile(req,mob_id):
    data = Mobile_Db.objects.all()
    cat=MobDb.objects.get(id=mob_id)
    return render(req,"edit_mobile.html",{'data':data,'cat':cat})
def delete_mobile(req,mob_id):
    x=MobDb.objects.filter(id=mob_id)
    x.delete()
    messages.error(req,"Deleted successfully...!")
    return redirect(display_mobile)
def update_mobile(req,mob_id):
    if req.method=="POST":
        a=req.POST.get('cname')
        b = req.POST.get('mname')
        c = req.POST.get('price')
        d = req.POST.get('description')
        try:
            img = req.FILES['img1']
            fs = FileSystemStorage()
            file1 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file1 = MobDb.objects.get(id=mob_id).Mobile_Image1
        try:
            img = req.FILES['img2']
            fs = FileSystemStorage()
            file2= fs.save(img.name, img)
        except MultiValueDictKeyError:
            file2 = MobDb.objects.get(id=mob_id).Mobile_Image2
        try:
            img = req.FILES['img3']
            fs = FileSystemStorage()
            file3 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file3= MobDb.objects.get(id=mob_id).Mobile_Image3
        MobDb.objects.filter(id=mob_id).update(CompanyName=a, Mobile_Name=b, Price=c, Description=d, Mobile_Image1=file1, Mobile_Image2=file2,
                     Mobile_Image3=file3)
        messages.success(req,"updated successfully..!")
        return redirect(display_mobile)
def admin_login(req):
    return render(req,"admin_login.html")
def admin_page(request):
    if request.method=="POST":
        un= request.POST.get('username')
        pwd =request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.info(request,"Welcome..!")
                return redirect(index_page)
            else:
                messages.warning(request,"Invalid user or password..!")
                return redirect(admin_login)
        else:
            messages.warning(request,"User not Found..!")
            return redirect(admin_login)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.error(request,"Logout successfully...!")
    return redirect(admin_login)
def contact_details(req):
    data=Contact_Db.objects.all()
    return render(req,"contact_details.html",{'data':data})
def delete_contact(req,cnt_id):
    x=Contact_Db.objects.filter(id=cnt_id)
    x.delete()
    messages.info(req,"Removed Successfully....!")
    return redirect(contact_details)
def register_details(req):
    data = RegisterDb.objects.all()
    return render(req,"register_details.html",{'data':data})
def delete_register(req,cn_id):
    x=RegisterDb.objects.filter(id=cn_id)
    x.delete()
    messages.error(req,"Removed user...!")
    return redirect(register_details)




