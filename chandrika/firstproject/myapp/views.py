from django.shortcuts import render, get_object_or_404,redirect
from .models import index
from django.http import HttpResponseRedirect


# Create your views here.
def user(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['email']
        password = request.POST['password']
        data = index(i_name=name,i_email=mail,i_password=password)
        data.save()
        return render(request, 'index.html')
    return render(request,'index.html')

def getdata(request):
    if request.method == 'GET':
        a = index.objects.all()
        return render(request, 'getdata.html',{'userdata':a})
    elif request.method =='POST':
        return HttpResponseRedirect(request.path)
    
def Update_Record(request):
    if request.method == 'POST':

        id = request.POST['id']
        name = request.POST['name']
        mail = request.POST['email']
        password = request.POST['password']
        
        b = get_object_or_404(index,pk=id)
        
        b.i_name=name
        b.i_email = mail
        b.i_password = password
        b.save()
        return HttpResponseRedirect ("/getdata/")
def Delete_record(request,id):
    if request.method == 'POST':
        a=index.objects.get(pk=id)
        a.delete()
        return redirect('/getdata/')

