from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm # User Form import
from django.contrib.auth import login, logout, authenticate # 로그인 로그아웃 인증 import
from .forms import RegisterForm

# 회원가입 함수
def signup_view(request):
    if request.method == "POST": #  POST 방식일 때
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request.user)
            return redirect("main")
        else:
            return redirect("main")

    else: # GET 방식일 때
        form = RegisterForm()

    return render(request, 'signup.html', {'form' : form})

# 로그인 함수
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request= request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username = username, password = password)
            if user is not None :
                login(request, user)
            return redirect('main')
    else :
        form = AuthenticationForm()
        context = {
            'form' : form
        }
        return render(request, "login.html", context)

# 로그아웃
def logout_view(request):
    logout(request)
    return redirect("main")


            
