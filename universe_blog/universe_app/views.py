from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect  # , HttpResponse
from .models import Settings, NavbarModel, Footer, WorksSectionModel,\
    WorkModel, WorkImageModel,AboutModel, AboutImageModel,ContactModel, ContactAddressModel, ContactSocNetModel
from .forms import WorkCreateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


#@login_required(login_url='login_page')
def home_view(request):
    context={}
    '''
    settings_queryset = Settings.objects.all().first()
    navbar_queryset = NavbarModel.objects.all()
    footer_queryset = Footer.objects.all()
    context['settings_queryset']= settings_queryset
    context['navbar_queryset']= navbar_queryset
    context['footer_queryset']= footer_queryset
    '''
    return render(request,'index.html',context) #HttpResponse("home_page")

def works_view(request):
    context={}
    works_section_queryset=WorksSectionModel.objects.all().first()
    work_queryset= WorkModel.objects.filter(is_activated=True)
    context['works_section_queryset']= works_section_queryset
    context['work_queryset']= work_queryset
    return render(request,'works.html', context)

def about_view(request):
    context={}
    about_queryset=AboutModel.objects.all()
    about_image_queryset= AboutImageModel.objects.all().first()
    context['about_queryset']=about_queryset
    context['about_image_queryset']=about_image_queryset
    return render(request,'about_me.html', context)

def work_view(request, work_id):
    context={}
    work_queryset= WorkModel.objects.filter(id=work_id).first()
    work_image_queryset =WorkImageModel.objects.filter(work_id=work_id) #.first()
    context['work_queryset']= work_queryset
    context['work_image_queryset']= work_image_queryset
    return render(request,'work.html', context)

def contact_view(request):
    context={}
    if request.method== 'POST':
        subject=request.POST.get("subject",None)
        email=request.POST.get("email", None)
        message=request.POST.get("message", None)
        ContactModel.objects.create(
            subject=subject,
            email=email,
            message=message
        )
    address_queryset=ContactAddressModel.objects.all().first()
    social_network_queryset=ContactSocNetModel.objects.all()
    context['address_queryset']=address_queryset
    context['social_network_queryset']=social_network_queryset
    return render(request,'Contact.html', context)

def work_create_view(request):
    context={}
    form=WorkCreateForm()
    if request.method=='POST':
        form=WorkCreateForm(request.POST or None)
        if form.is_valid():
            forms=form.save(commit=False)
            forms.user_id=request.user
            forms.save()
            return redirect('works_page')
        else:
            context['form']=form
            return render(request,'work_create.html',context)
    context['form'] = form
    return render(request, 'work_create.html', context)

def register_view(request):
    context={}
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        else:
            form=UserCreationForm()
            context['form']=form
            return render(request,'register.html',context)
    else:
        form = UserCreationForm()
        context['form'] = form
    return render(request, 'register.html', context)

def login_view(request):
    context={}
    username=request.POST.get('username')
    raw_password=request.POST.get('password')
    user=authenticate(username=username,password=raw_password)
    if user:
        login(request,user)
        return redirect('home_page')
    else:
        context['error_message']='No such user'
        return render(request,'login.html', context)

    return render(request, 'login.html', context)

def logout_view(request):
    auth.logout(request)
    return redirect('home_page')

def components_view(request):
    return render(request,'components.html')