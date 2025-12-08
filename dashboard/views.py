from django.shortcuts import render,redirect
from rest_framework.views import APIView

from .forms import LoginForm, RegisterForm


# Create your views here.
def login_view(request):
    context = {}
    form = LoginForm(request.POST or None)
    context['form'] = form
    return render(request,"login.html",context)


def register_view(request):
    context = {}
    form = RegisterForm(request.POST or None)
    context['form'] = form
    return render(request,"register.html",context)


def dashboard_view(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect("/login")
    return render(request,'index.html')

def admin_dashboard(request):
    context = {}
    # if not request.user.is_authenticated:
    #     return redirect("/login")
    # if not request.user.is_staff:
    #     return redirect('/')
    context={}
    # context['total_customer']=CustomerUser.objects.count()
    # context['total_product']=Product.objects.count()
    # context['total_order']=Order.objects.count()


    return render(request,'admin_dashboard.html',context)






