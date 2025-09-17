from django.shortcuts import render

def home(request):
    return render(request, 'bookmodule/home.html')  # تأكد من المسار الكامل هنا
