from django.shortcuts import render,HttpResponse,redirect # type: ignore
from .models import*
from .models import User # type: ignore
from .models import messages
from django.core.paginator import Paginator # type: ignore
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import Wishlist
import random
from django.core.mail import send_mail # type: ignore


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
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        dep_id=department.objects.all()
        pro_id=product.objects.all()
        col_id=colorfilter.objects.all()
        size_id=size.objects.all()
        wish_id=Wishlist.objects.filter(user=uid)
        l1=[]
        for i in wish_id:
            l1.append(i.product1)

        did=request.GET.get("did")
        cid=request.GET.get("color_name")
        sid=request.POST.get("name")

        if did:
            pro_id=product.objects.filter(department=did)
        else:
            pro_id=product.objects.all()

        paginator = Paginator(pro_id, 6)
        page_number = request.GET.get('page',1)
        try:
            page_number=int(page_number)
        except ValueError:
            page_number=1
        pro_id= paginator.get_page(page_number)
        # show_page=Paginator.get_elided_page_range(page_number,on_each_side=1,on_ends=1)
        show_page=paginator.get_elided_page_range(page_number,on_each_side=1,on_ends=1)

        contaxt={
            "dep_id":dep_id,
            "pro_id":pro_id,
            "did":did,
            "cid":cid,
            "col_id":col_id,
            "size_id":size_id,
            "sid":sid,
            "show_page":show_page,
            "wish_id":wish_id,
            "l1":l1
        }
        return render(request,"shopgrid.html",contaxt)
    else:
        return render(request,"shopgrid.html")


def shopingcart(request):
    # if 'email' in request.session:
    #     uid=User.objects.get(email=request.session['email'])
        cid=cart.objects.filter(user=User.objects.get(email=request.session['email']))
        subtotal=0
        for i in cid:
            subtotal+=i.total_price
        contaxt={
            "cid":cid,
            "subtotal":subtotal  
        }
        return render(request,"shopingcart.html",contaxt)

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
def details(request,id):
    uid=User.objects.all()
    col_id=colorfilter.objects.all()
    size_id=size.objects.all()
    pro_id=product.objects.get(id=id)
    contaxt={
        "uid":uid,
        "col_id":col_id,
        "size_id":size_id,
        "pro_id":pro_id
    }
    return render (request,"shopdetails.html",contaxt)

def add_wishlist(request,id):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        pro_id=product.objects.get(id=id)
        print(pro_id)
        pid=Wishlist.objects.filter(product1=id,user=uid).exists()
        if pid:
            pid=Wishlist.objects.get(product1=id)
            pid.delete()
        else:
            Wishlist.objects.create(pname=pro_id.pname,image=pro_id.image,price=pro_id.price,product1=pro_id,user=uid)
            
        return redirect(shopgrid)
    else:    
        return render (request,"shopgrid.html")
    
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

def add_to_cart(request,id):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        pro_id=product.objects.get(id=id)
        print(pro_id)
        pid=cart.objects.filter(product1=id,user=uid).exists()
        if pid:
            pid=cart.objects.get(product1=id)
            pid.qty=pid.qty + 1
            pid.total_price=pid.price * pid.qty
            pid.save()
            return redirect(shopingcart)
        else:
            cart.objects.create(name=pro_id.pname,image=pro_id.image,price=pro_id.price,total_price=pro_id.price,product1=pro_id,user=uid)  

        return redirect(shopingcart)
    else:
        return render (request,"shopingcart.html")
    
def pluscart(request,id):
    pid=cart.objects.get(id=id)
    print(pid)
    pid.qty=pid.qty + 1
    pid.total_price=pid.price * pid.qty
    pid.save()  
    return redirect(shopingcart)
    
def minuscart(request,id):
    pid=cart.objects.get(id=id)
    print(pid)
    if pid:
        pid.qty > 1
        pid.qty -= 1
        pid.total_price=pid.price * pid.qty         
        pid.save()
        return redirect(shopingcart)  
    else:   
        pid.delete()
        return render (request,"shopingcart.html")  
    
def forgot_password(request):
    if request.POST:
        email=request.POST['email']
        otp=random.randint(1000,9999)
        print(otp)
        try:    
            uid=User.objects.get(email=email)
            uid.forgot_password=otp
            uid.save()
            send_mail(
                'Forgot Password OTP',
                f'Your OTP for password reset is {otp}.',
                'nencyp694@gmail.com',
                [email],
                )
            contaxt = {
                "msg": "OTP sent to your email"
            }
            return render(request, "forgot.html", contaxt)
        except User.DoesNotExist:
            contaxt = {
                "msg": "Invalid Email"
            }
            return render(request, "forgot.html", contaxt)
    else:
        return render(request, "forgot.html")

def forgot_password(request):
    if request.method == "POST":
        identifier = request.POST.get('identifier')
        try:
            # Try email first, then phone
            if '@' in identifier:
                user = User.objects.get(email=identifier)
            else:
                user = User.objects.get(phone=identifier)
            otp = random.randint(1000, 9999)
            user.forgot_password = otp
            user.save()
            # Send OTP via email or SMS (here, only email example)
            if '@' in identifier:
                send_mail(
                    'Forgot Password OTP',
                    f'Your OTP for password reset is {otp}.',
                    'your_email@example.com',
                    [user.email],
                    fail_silently=False,
                )
            # For SMS, integrate with an SMS API here if needed
            request.session['reset_user_id'] = user.id
            return redirect('otp_verify')
        except User.DoesNotExist:
            return render(request, "forgot.html", {"msg": "User not found"})
    return render(request, "forgot.html")

def otp_verify(request):
    user_id = request.session.get('reset_user_id')
    if not user_id:
        return redirect('forgot_password')
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        otp = request.POST.get('otp')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if str(user.forgot_password) == otp:
            if password == confirm_password:
                user.password = password
                user.forgot_password = None
                user.save()
                del request.session['reset_user_id']
                return redirect('login')
            else:
                return render(request, "forgot.html", {"msg": "Passwords do not match"})
        else:
            return render(request, "forgot.html", {"msg": "Invalid OTP"})
    return render(request, "login.html")

