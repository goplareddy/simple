from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Person
from testapp.forms import PersonForm,PersonUpdateForm,PasswordChangeForm
import datetime

# Create your views here
def createform(request):
    model=Person()
    if(request.method=='GET'):
            #form=PersonForm()
            print("-- get call invoked")
            return render(request,'testapp/form.html',{'model':model})
    print("post call invoked")
    form=PersonForm(request.POST)

    if form.is_valid():
        model.firstname=form.cleaned_data['firstname']
        #print(model.firstname)
        model.lastname=form.cleaned_data['lastname']
        model.email=form.cleaned_data['email']
        model.loginname=form.cleaned_data['loginname']
        model.password=form.cleaned_data['password']
        model.gender=form.cleaned_data['gender']
        model.address=form.cleaned_data['address']
        model.country=form.cleaned_data['country']
        model.proof=form.cleaned_data['proof']
        model.type=form.cleaned_data['type']
        model.status=form.cleaned_data['status']
        model.attempt=0
        model.date=datetime.datetime.now()

        result=Person.objects.filter(loginname__exact=model.loginname)
        if(result.exists()):
           return render(request,'testapp/form.html',{'model':model,'msg':'login name already exists'})
            #return render(request,'testapp/form.html',{'model':model,'msg':'login name already exists'})

    #    print(result)
        result=Person.objects.filter(email__exact=model.email)
        if(result.exists()):
            return render(request,'testapp/form.html',{'model':model,'msg':'email already exists'})

        model.save()
        return render(request,'testapp/form.html',{'model':model,'msg':'registration success'})
    return render(request,'testapp/form.html',{'msg':'registration fail'})


def login(request):
    return render(request,'testapp/login.html')

def profile(request):
    #print(request.session["myData"])
    userId = request.session["myData"]
    data=Person.objects.get(id=userId)
    print(data)
    return render(request,'testapp/data.html',{'result':data})


def user_name(request):
    loginname=request.POST.get("loginname")
    password=request.POST.get("password")
    #type=request.POST.get("type")
    result=Person.objects.filter(loginname__exact=loginname,password__exact=password)
    modelObj = result.first()
    if (result.first()):
        print("login successful")
        request.session["myData"] = modelObj.id
        request.session["mytype"] = modelObj.type

        return render(request,'testapp/data.html',{'result':modelObj})
    else:
        return render(request,'testapp/login.html',{'msg':'login is failed '})
def update(request):
    return render(request,'testapp/update.html')
def updation(request):
    form=PersonUpdateForm(request.POST)
    userId = request.session["myData"]
    print(userId)
    model=Person.objects.get(id=userId)
    print(model)
    if form.is_valid():
        model.firstname=form.cleaned_data['firstname']
        print(model.firstname)
        model.lastname=form.cleaned_data['lastname']
        model.loginname=form.cleaned_data['loginname']

        model.gender=form.cleaned_data['gender']
        model.address=form.cleaned_data['address']
        model.country=form.cleaned_data['country']
        model.proof=form.cleaned_data['proof']
        model.type=form.cleaned_data['type']
        model.status=form.cleaned_data['status']
        model.attempt=0
        model.date=datetime.datetime.now()

        if(model.email!=form.cleaned_data['email']):
            result=Person.objects.filter(email__exact=model.email)
            if(result.exists()):
                return render(request,'testapp/update.html',{'result':result,'result':model,'msg':'email already exists'})
            model.email=form.cleaned_data['email']
        #    return render(request,'testapp/update.html',{'result':result}
        model.save()
        return render(request,'testapp/data.html',{'result':model,'msg':'updation is success'})
    return render(request,'testapp/update.html',{'form':form,'result':model})

def get(request):
    return render(request,'testapp/get1.html')
def getbyid(request):
    id = request.GET['id']
    try:
        result=Person.objects.get(id=id)
        print(result)
        form=PersonUpdateForm(request.POST)
        return render(request,'testapp/get1.html',{'result':result})
    except Person.DoesNotExist:
        return render(request,'testapp/get1.html',{'msg':'id not found'})

def delete(request):
  return render(request,'testapp/delete.html')

def delete_person(request):
    id= request.GET['id']
    try:
        object=Person.objects.get(id=id)
        object.delete()
        return render(request,'testapp/delete.html',{'object':object,'msg':'person data deleted successfully'})

    except Person.DoesNotExist:
        return render(request,'testapp/delete.html',{'msg':'person id not found'})

def profile_data(request):
    #print(request.session["myData"])
    userId = request.session["myData"]
    data=Person.objects.get(id=userId)
    print(data)
    return render(request,'testapp/data1.html',{'result':data})
def update1(request):
    return render(request,'testapp/update1.html')
def updation1(request):
    form=PersonUpdateForm(request.POST)
    userId = request.GET["id"]
    userId = request.session["myData"]
    print(userId)
    model=Person.objects.get(id=userId)
    print(model)
    if form.is_valid():
        model.firstname=form.cleaned_data['firstname']
        print(model.firstname)
        model.lastname=form.cleaned_data['lastname']
        model.loginname=form.cleaned_data['loginname']

        model.gender=form.cleaned_data['gender']
        model.address=form.cleaned_data['address']
        model.country=form.cleaned_data['country']
        model.proof=form.cleaned_data['proof']
        model.type=form.cleaned_data['type']
        model.status=form.cleaned_data['status']
        model.attempt=0
        model.date=datetime.datetime.now()



        if(model.email!=form.cleaned_data['email']):
            result=Person.objects.filter(email__exact=model.email)
            if(result.exists()):
                return render(request,'testapp/update1.html',{'result':result,'result':model,'msg':'email already exists'})
            model.email=form.cleaned_data['email']
        #    return render(request,'testapp/update.html',{'result':result}
        model.save()
        return render(request,'testapp/data1.html',{'result':model,'msg':'updation is success'})
    return render(request,'testapp/update1.html',{'form':form,'result':model})

    # loginstr="loginname='{}'".format(loginname)
    # pwdstr="password='{}'.fomat(password)
    # result=Person.objects.exact(where=[loginstr,pwdstr])
    # print(result)

def form1(request):
    loginname=request.POST.get('loginname')
    password=request.POST.get('oldpassword')
    print(password)

    data=Person.objects.filter(loginname__exact=loginname)
    print("data= ",data)
    print(password)
    if(data is None):
        return render(request,'testapp/login.html',{'msg':'login failure'})
    else:
        print(password)
        if(data.password!=password):
            print(password)
            data.attempt=attempt
            attempt=attempt+1
            data.save()
            print(data)
            return render(request,'testapp/login.html',{'msg':'login failure'})



        if(data.attempt==3):
            data.status=0
        data.save()
        return render(request,'testapp/login.html')

def getall(request):
    person=Person.objects.all()
    myType=request.session["mytype"]
    print("type",myType)
    print(person)
    return render(request,'testapp/getall.html',{'person':person,'type':myType})
def changepassword(request):
    return render(request,'testapp/password.html')
def newpassword(request):
    oldpassword=request.POST.get("oldpassword")
    print(oldpassword)
    userId = request.session["myData"]
    data=Person.objects.get(id=userId)
    if (oldpassword!=data.password):
        return render(request,'testapp/password.html',{'msg':'password is wrong'})
    newpassword=request.POST.get("newpassword")
    print(newpassword)
    confirmpassword=request.POST.get("confirmpassword")
    if (newpassword!=confirmpassword):
        return render(request,'testapp/password.html',{'msg':'password is not matched'})

    data.password=newpassword
    data.save()
    return render(request,'testapp/password.html',{'msg':'password updated successfully'})
