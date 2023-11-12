from django.shortcuts import render,redirect
from .models import Person
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
def home(request):
    person_qry = Person.objects.all()
    context = {'person':person_qry}
    return render(request,'base.html',context) #ชื่อไฟล์ที่จะแสดง

def list(request): #ชื่อฟังชั่น
    person_qry = Person.objects.all()
    context = {'person':person_qry}
    return render(request,'list.html',context) #ชื่อไฟล์ที่จะแสดง

def add(request): #ชื่อฟังชั่น ต้องไม่ซ้ำใคร
    if request.method == 'POST':
        f_name = request.POST['firstname']
        l_name = request.POST['lastname']
        tel = request.POST['tel']
        year = request.POST['year']
        pic = request.FILES['picture']
        person = Person(p_firstname=f_name,p_lastname=l_name,p_tel=tel,p_regisyear = year,p_picture=pic)
        person.save()
        messages.success(request, 'เพิ่มข้อมูลสำเร็จ!!')
        return redirect('/list')
    
    return render(request,'add.html') #ชื่อไฟล์ที่จะแสดง

def manage(request): #ชื่อฟังชั่น
    return render(request,'manage.html') #ชื่อไฟล์ที่จะแสดง

def custom_login(request): #ชื่อฟังชั่น
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pswd']
        user = authenticate(request, username=username, password=password)
        if user is not None:#ถ้าไม่เป็นค่าว่าง user password ถูก
            login(request, user)
            messages.success(request, 'เข้าสู่ระบบสำเร็จ')
            return redirect('/list')
        else:
            messages.error(request, 'ไม่สำเร็จ กรุณาตรวจสอบข้อมูลอีกครั้ง')
            pass
    return render(request,'login.html') #ชื่อไฟล์ที่จะแสดง


def logout_view(request):
    logout(request)
    return render(request,'login.html')