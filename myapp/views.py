from django.shortcuts import render,HttpResponse,redirect # type: ignore
from .models import*
from .models import User # type: ignore
from .models import messages


# Create your views here.
def home(request):
    return HttpResponse("welcome..home")

def crud(request):
    eid=Employee.objects.all()
    contaxt={
        "eid":eid
    }
    return render(request,"crud.html",contaxt)

def create(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        department=request.POST['department']
        phone=request.POST['phone']
        Employee.objects.create(
            name=name,
            email=email,
            department=department,
            phone=phone
        )
        return redirect(crud) 
    else: 
        return render(request,"crud.html")
    
def update(request,id):
    eid=Employee.objects.get(id=id)
    print(eid)

    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        department=request.POST['department']
        phone=request.POST['phone']

        eid.name=name
        eid.email=email
        eid.department=department
        eid.phone=phone
        eid.save()
        return redirect(crud)
    
    else:
        return render(request,"crud.html")
    
def delete(request,id):
    eid=Employee.objects.get(id=id)
    eid.delete()
    return redirect(crud)

def register(request):
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
    
        if password == confirm_password:
            User.objects.create(username=username,email=email,password=password,confirm_password=confirm_password)

            return render(request, 'login.html')
        
        else:
            contaxt={
                "msg":"password do not match"
            }
        return render(request, 'register.html',contaxt)

    else:
        return render(request, 'register.html')
    
def login(request):
    if 'email' in request.session:
        return render(request,"index.html")
    try:
        if request.POST:
            email=request.POST['email']
            password=request.POST['password']

            uid=User.objects.get(email=email)
            print(uid)
            if uid.email == email:

                request.session['email']=uid.email
                if uid.password == password:
                    return redirect("index")
                else:
                    contaxt={
                        "msg":"Invalid password"
               }
                    return render(request,"login.html",contaxt)
            else:
                return render(request,"login.html")

    except User.DoesNotExist:
        contaxt={
            "msg":"Invalid Email"
        }
        return render(request,"register.html",contaxt)
    else:
        return render(request, 'login.html')

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request,"login.html")
    else:
        return render(request,"login.html")

    
def index(request):
    username = request.session.get('username')
    contaxt={
        "username":username
    }
    return render(request,"index.html",contaxt)


def blogdetails(request):
    return render(request,"blogdetails.html")  

def blog(request):
    return render(request,"blog.html")  

def checkout(request):
    return render (request,"checkout.html")

def contact(request):
    return render(request,"contact.html")   

def main(request):
    return render(request,"main.html")

def shopdetails(request):
    return render(request,"shopdetails.html")

def shopgrid(request):
    dep_id=department.objects.all()
    pro_id=product.objects.all()
    col_id=colorfilter.objects.all()
    size_id=size.objects.all()


    did=request.GET.get("did")
    cid=request.GET.get("color_name")
    sid=request.POST.get("name")

    if did:
        pro_id=product.objects.filter(department=did)
    else:
        pro_id=product.objects.all()

    contaxt={
        "dep_id":dep_id,
        "pro_id":pro_id,
        "did":did,
        "cid":cid,
        "col_id":col_id,
        "size_id":size_id,
        "sid":sid,

    }
    return render(request,"shopgrid.html",contaxt)

def shopingcart(request):
    return render(request,"shopingcart.html")

def department1(request):
    dep_id=department.objects.all()
    contaxt={
        "dep_id":dep_id
    }
    return render(request,"index.html",contaxt)

def color(request):
    col_id=colorfilter.objects.all()
    size_id=size.objects.all()
    print(col_id)
    cid=request.POST.get("color_name")
    print(cid)
    l1=[]

    if cid:
        pro_id=product.objects.filter(colorfilter__color_name=cid)
        l1.extend(pro_id)
    else:
        pro_id=product.objects.order_by("-id")
    contaxt={
        "col_id":col_id,
        "cid":cid,
        "pro_id":l1,
        "size_id":size_id

    }
    return render(request,"shopgrid.html",contaxt) 

def pro(request):
    pro_id=product.objects.all()
    print(pro_id)
    contaxt={
        "pro_id":pro_id
    }
    return render(request,"shopgrid.html",contaxt) 

def size1(request):
    size_id=size.objects.all()
    col_id=colorfilter.objects.all()
    sid=request.POST.get("name")
    l1=[]

    if sid:
        pro_id=product.objects.filter(size__name=sid)
        l1.extend(pro_id)
    else:
        pro_id=product.objects.order_by("-id")

    contaxt={
        "size_id":size_id,
        "sid":sid,
        "pro_id":l1,
        "col_id":col_id 
        
    }
    return render(request,"shopgrid.html",contaxt) 

def price(request):
    col_id=colorfilter.objects.all()
    size_id=size.objects.all()
    if request.POST:
        min1=request.POST['min1']
        print(min1)
        max1=request.POST['max1']
        print(max1)

        pro_id=product.objects.filter(price__lte=max1[1:],price__gte=min1[1:])
        print(pro_id)
        contaxt={
            "pro_id":pro_id,
            "min1":min1,
            "max1":max1,
            "col_id":col_id,
            "size_id":size_id
        }
        return render (request,"shopgrid.html",contaxt)
    else:
        contaxt={
            "min1":None,
            "max1":None
        }
        return render (request,"shopgrid.html",contaxt)
def shopdetails(request):
    col_id=colorfilter.objects.all()
    size_id=size.objects.all()
    pro_id=product.objects.all()

    contaxt={
        "col_id":col_id,
        "size_id":size_id,
        "pro_id":pro_id
    }
