from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

# user kayıt olursa
def user_register(request):

    if request.method == 'POST':
        
        k_ad = request.POST.get('k_ad')
        k_email = request.POST.get('k_email')
        k_sifre = request.POST.get('k_sifre')

        if k_ad and k_email and k_sifre:
            # veritabanını sorgula
            try:
              User.objects.get(email = k_email)
              # böyle bir kullanıcı varsa hata mesajı döndür
              messages.error(request, message="Bu email adresine sahip bir hesap mevcut")
              return redirect('user-register')  
            except:
              # böyle bir kullanıcı yoktur o zaman kayıt et 
               User.objects.create_user(username=k_ad, email=k_email, password=k_sifre)
               #  başarılı measjı ver
               messages.success(request, 'Başarılı bir şekilde kayıt oldunuz. Lütfen giriş yapın.')
               return redirect('user-login')  
    
    else:
      return render(request, 'user-register.html')


# user giriş yaparsa
def user_login(request):

    if request.method == "POST":
        k_ad = request.POST.get('k_ad')
        k_sifre = request.POST.get('k_sifre')

        if k_ad and k_sifre:
           user = authenticate(request, username=k_ad, password=k_sifre)

           if user is not None:
              login(request, user)
              # ansayfaya yönlendir
              return redirect('anasayfa')
           else:
              # hata mesajı yazdır ve logine yönlendir
              messages.error(request, 'kullanıcı adı veya parola hatalı')
              return redirect('user-login')
    
    else:
       # get isteği geldiğinde sayfayı gönder
       return render(request, 'user-login.html')
    

# çıkış yapma
def user_logout(request):

        logout(request)
        # anasayfaya yönlendir
        return redirect('anasayfa')