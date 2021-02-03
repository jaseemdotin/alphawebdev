from django.shortcuts import render,redirect
from .forms import *
from .models import *
from .filters import filters
from reportlab.pdfgen import canvas
import io
from django.http import FileResponse
# Create your views here.
def home(request):
    uid=request.user.id
    request.session['Userid']=uid
    pname = alphaproducts1.objects.order_by('-discount')[:2]
    ptop = alphaproducts1.objects.order_by('-sell')[:3]
    signup=alpha_signup.objects.all()
    searchproduct = alphaproducts1.objects.all()
    cat=alpha_category.objects.all()
    myfilte=filters(request.GET,queryset=searchproduct)
    searchproduct=myfilte.qs

    return render(request,'Alphahome.html',{'pname':pname,'username':signup,'cat':cat,'ptop':ptop,'flt':myfilte,'srch':searchproduct,'uid':uid})
def usersignup(request):
    return render(request,'User_Signup.html')
def productadd(request):
    return render(request,'Product_Add.html')
def catadd(request):
    return render(request,'Add_Category.html')
def alphasignup(request):
    form=alphasignupform()
    if request.method=='POST':
        form=alphasignupform(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'User_Signup.html',{'form':form})
def catadd(request):
    form = alphacategoryform()
    if request.method == 'POST':
        form = alphacategoryform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(catadd(request))
    return render(request, 'Add_Category.html')

def alphaproductadd(request):
    productcat=alpha_category.objects.all()
    useridnew = request.session['Userid']
    if request.method=='POST':
        uid=request.session['Userid']
        catid=request.POST.get("catname")
        catname=alpha_category.objects.get(id=catid)
        Userid=alpha_signup.objects.get(id=uid)
        productname=request.POST.get("productname")
        pimage1 = request.FILES.get("pimage1")
        pimage2 = request.FILES.get("pimage2")
        pimage3 = request.FILES.get("pimage3")
        prize = request.POST.get("prize")
        sell = request.POST.get("sell")
        discount = request.POST.get("discount")
        brand = request.POST.get("brand")
        pdisc = request.POST.get("pdisc")
        spec_status = request.POST.get("spec_status")
        alphaproducts1.objects.create(
            Userid=Userid,
            catname=catname,
            productname=productname,
            pimage1=pimage1,
            pimage2=pimage2,
            pimage3=pimage3,
            prize=prize,
            sell=sell,
            discount=discount,
            brand=brand,
            pdisc=pdisc,
            spec_status=spec_status,
        )

        return adminadd(request)
    else:
        return render(request,'Product_Add.html',{'a':productcat,'uid':useridnew})


def base(request):
    pr = alphaproducts1.objects.order_by('-discount')[:3]
    return render(request,'base.html',{'b':pr})
def adminview(request):
    return render(request,'Myprofile.html')
def adminpage(request):
    return render(request,'Myprofile.html')
def productdview(requset,pk):
    ins = alphaproducts1.objects.get(pk=pk)
    return render(requset,'productdview.html',{'ins':ins})
def productview(request,pk):
    pview = alphaproducts1.objects.get(pk=pk)
    return render(request,'base.html',{'pview':pview})
def profileview(request):
    return render(request,'base.html',)
def adminadd(request):
    ram=alphaproducts1.objects.filter(catname=1,spec_status=0).count()
    cam = alphaproducts1.objects.filter(catname=3,spec_status=0).count()
    lap = alphaproducts1.objects.filter(catname=2,spec_status=0).count()

    return render(request,'adminadd.html',{'ram':ram,'lap':lap,'cam':cam})
def ramspecadd(request):
    cat_type = 1
    productname=alphaproducts1.objects.filter(catname=1,spec_status=0)
    if request.method == 'POST':

        product=request.POST.get("pid")
        b = alphaproducts1.objects.get(id=product)
        form=productstatusform(request.POST,instance=b)
        productid=alphaproducts1.objects.get(id=product)
        ramtype = request.POST.get("ramtype")
        ramsize=request.POST.get("ramsize")
        ptotal=request.POST.get("ptotal")
        ramspec.objects.create(
            productid=productid,
            ramtype=ramtype,
            ramsize=ramsize,
            ptotal=ptotal,
        )
        form.save()

        return home(request)
    else:
        return render(request,'specadd.html',{'productname':productname,'cat_type':cat_type})

def lapspecadd(request):
    cat_type=2
    productname=alphaproducts1.objects.filter(catname=2,spec_status=0)
    if request.method == 'POST':
        product=request.POST.get("pid")
        productid=alphaproducts1.objects.get(id=product)
        ramtype = request.POST.get("ramtype")
        ramsize = request.POST.get("ramsize")
        ptotal = request.POST.get("ptotal")
        graphicsdisc = request.FILES.get("graphicsdisc")
        graphicssize = request.POST.get("graphicssize")
        screensize = request.POST.get("screensize")
        motherboard = request.POST.get("motherboard")
        hdd = request.POST.get("hdd")
        sdd = request.POST.get("sdd")
        systemos = request.POST.get("systemos")
        processor = request.POST.get("processor")
        lapspec.objects.create(
            productid=productid,
            ramtype=ramtype,
            ramsize=ramsize,
            ptotal=ptotal,
            graphicsdisc=graphicsdisc,
            graphicssize=graphicssize,
            screensize=screensize,
            hdd=hdd,
            motherboard=motherboard,
            sdd=sdd,
            systemos=systemos,
            processor=processor,

        )

        return home(request)
    else:
        return render(request,'specadd.html',{'productname':productname,'cat_type':cat_type})

def camspecadd(request):
    cat_type = 3
    productname=alphaproducts1.objects.filter(catname=3,spec_status=0)
    if request.method == 'POST':
        product=request.POST.get("pid")
        productid=alphaproducts1.objects.get(id=product)
        camresalution = request.POST.get("camresalution")
        camtype=request.POST.get("camtype")
        ptotal=request.POST.get("ptotal")
        cameraspec.objects.create(
            productid=productid,
            camresalution=camresalution,
            camtype=camtype,
            ptotal=ptotal,
        )

        return home(request)
    else:
        return render(request,'specadd.html',{'productname':productname,'cat_type':cat_type})

def printpdf(request):
    buffer=io.BytesIO()
    p=canvas.Canvas(buffer)
    p.drawString(100,100)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')