from django.shortcuts import render,HttpResponseRedirect, redirect
from .models import Filldetails,CustomUser
from django.contrib.auth.models import User 
from django.contrib.auth import login,logout,authenticate
from django.views import View
from django.contrib import messages
# Create your views here.

################Home
def home(request):
        return render(request,'VRmaker/home.html')


###############login
class Login(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return render(request,'VRmaker/login.html')
        else:    
            return HttpResponseRedirect('/ResumeForm/')
        
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user=authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successfully')
            return HttpResponseRedirect('/ResumeForm/')
        else:
            messages.warning(request, 'Invalid Email!!!! LogIn Again')
            return HttpResponseRedirect('/login/')









##############signupform
class UserSignup(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return render(request,'VRmaker/signup.html')
        else:    
            return HttpResponseRedirect('/ResumeForm/')
    def post(self,request):
        user = CustomUser()
        first_name = request.POST.get('first_name')
        print(first_name)
        last_name = request.POST.get('last_name')
        us_email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        con_password = request.POST.get('con_password')

        if password == con_password:
            if CustomUser.objects.filter(email = us_email).exists(): ### filter the user email
                messages.error(request, 'Email id  Already Exist...? Use Diffrent Email id to Create Account.' )
            else:    
                user = CustomUser()
                pas = user.set_password(password)
                user.first_name = first_name
                user.last_name = last_name
                user.email = us_email
                user.phone_number = phone_number
                user.save()
                messages.success(request,"Thank You !" 'User Registered Successfully..!!')
                return HttpResponseRedirect('/signup/')
        return render(request,'VRmaker/signup.html')


#######Fill Resume
class ResumeForm(View):
    
        def get(self,request):
            if request.user.is_authenticated:
                data=Filldetails.objects.all()
                return render(request,'VRmaker/fillup.html',{'datas':data})
            return HttpResponseRedirect('/login/')
        def post(self,request):
                name=request.POST.get('name')
                dob=request.POST.get('dob')
                email=request.POST.get('email')
                gender=request.POST.get('gender')
                locality=request.POST.get('locality')
                city=request.POST.get('city')
                pincode=request.POST.get('pincode')
                state=request.POST.get('state')
                contact=request.POST.get('contact')
                preferredJL=request.POST.get('preferredJL')
                image=request.FILES.get('image')
                Filldetails.objects.create(name=name,dob=dob,email=email,gender=gender,locality=locality,city=city,pincode=pincode,state=state,contact=contact,preferredJL=preferredJL,image=image)
                messages.success(request,'Resume Create Succesfully')
                return redirect ('fillup')
########################logout#######
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


##########show Details
class Showup(View):
    def get(self,request,id):
        candidate=Filldetails.objects.get(pk=id)
        return render(request,'VRmaker/showup.html',{'candidates':candidate})