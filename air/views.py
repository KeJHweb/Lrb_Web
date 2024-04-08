from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django import forms
from air import  models

class LoginForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["username", "password"]
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }


class SignForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["username", "password","email"]
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }

def login(request):
    ''' 用户登录 '''
    if request.method == 'GET':
        form = LoginForm()
        return render(request, "login.html", {'form': form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        form.cleaned_data
        user_obj = models.UserInfo.objects.filter(username=form.cleaned_data["username"], password=form.cleaned_data["password"]).first()
        if user_obj:
            request.session["info"] = {"id": user_obj.id, "name": user_obj.username}# 获取一个cookie
            request.session.set_expiry(60*60*24*7) # session存在的时间
            return redirect("/index")
        else:
            return render(request, 'login.html', {'form': form, 'error': "用户名或密码错误"})
    else:
        return render(request, 'login.html', {'form': form})

def sign(request):
    '''用户注册'''
    if request.method == 'GET':
        form = SignForm()
        return render(request, "signup.html", {'form': form})
    form = SignForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/login/")
    else:
        return render(request, "signup.html", {"form": form})
    return render(request, 'signup.html', {'form': form})




def introduce(request):
    return render(request, 'introduce.html')

def train_location(request):
    return render(request,'train_location.html')
def index(request):
    return render(request, "index.html")
def list(request):
    return render(request,'class_list.html')
def more(request):
    return render(request,'more.html')
def enroll(request):
    return render(request,'enroll.html')
def service(request):
    return render(request, 'service_1.html')
def service2(request):
    return render(request, 'service_2.html')
def service3(request):
    return render(request, 'service_3.html')
def contact(request):
    return render(request,'contact.html')

def my_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # password = request.POST.get('password')

        # 在这里验证用户名和密码是否正确，假设验证成功了

        return JsonResponse({'username': username})  # 渲染成功的登录页面
