from django.shortcuts import render
from my_django_app.models import hellow
from django.contrib import messages
from my_django_app.forms import crform

def display(request):
    results = hellow.objects.all()
    return render(request, "index.html", {"hellow": results})


def insert(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('date') and request.POST.get('fir') and request.POST.get('punishment') and request.POST.get('location'):
            criminal = hellow()
            criminal.name = request.POST.get('name')
            criminal.date = request.POST.get('date')
            criminal.fir = request.POST.get('fir')
            criminal.punishment = request.POST.get('punishment')
            criminal.location = request.POST.get('location')
            criminal.save()
            messages.success(request, "The Recode" +
                             criminal.name+"is saved successfully!!!")
            return render(request, "create.html")
    else:
        return render(request, "create.html")
def update(request,id):
    getcriminaldetails= hellow.objects.get(id=id)
    return render(request,'update.html',{"hellow":getcriminaldetails})

def requpdate(request,id):
    updatereq=hellow.objects.get(id=id)
    form=crform(request.POST,instance=requpdate)
    if form.is_valid():
        form.save()
        messages.success(request,"Criminal recode is updated successfully...!!!!!!!!!!!")
        return render(request,"update.html",{"hellow":requpdate})
    else:
         messages.success(request,"Criminal recode is updated  is not successful")
def crdel(request,id):
    delcriminal=hellow.objects.get(id=id) 
    delcriminal.delete()
    results = hellow.objects.all()
    return render(request, "index.html", {"hellow": results})