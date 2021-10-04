from django.shortcuts import render
from django.http import HttpResponse


def form(request):
    return render(request,'form.html')
def status(request):
    dh=dash.objects.all()
    return render(request,'status.html',{'dh':dh})
def about(request):
    return render(request,'about.html')
def index(request):
    return render(request,'index.html')
def showformdata(request):
    if request.method=='POST':
        fm=ReqForm(request.POST)
        if fm.is_valid():
            em=fm.cleaned_data['email']
            cn=fm.cleaned_data['ClubName']
            rn=fm.cleaned_data['RepresentativeName']
            cn=fm.cleaned_data['Contact']
            df=fm.cleaned_data['req_date_from']
            dt=fm.cleaned_data['req_date_to']
            rt=fm.cleaned_data['req_type']
            rp=fm.cleaned_data['req_purpose']
            profile = fm.save(commit=False)
            profile.user = request.user
            profile.save()
            fm.save()    
            fm=ReqForm()   
            print(em)    
            print(rn) 
    else:
        fm=ReqForm()
    return render(request,'form.html',{'frm':fm})
    
def reqInfo(request):
    u=request.user
    if u.groups.filter(name='Managers').exists():
        req = Form.objects.all()
        print(req)
        print("this is a manager")
        context={
        'form':form,
        'req': req
         }
    else:
        req = Form.objects.filter(user=request.user)
        print(req)
        print("normal user")
        context={
            'form':form,
            'req': req
        }
    return render(request,'status.html',context)

def reqInfoManagement(request):
    req = Form.objects.all()
    print(req)
    context={
        'form':form,
        'req': req
    }
    return render(request,'status.html',context)

def student_approve(request,user_id):
    val=Form.objects.get(id=user_id)
    val.allocation_status=1
    val.save()
    return HttpResponseRedirect(reverse("status.html"))
def student_disapprove(request,user_id):
    val=Form.objects.get(id=user_id)
    Form.allocation_status=2
    Form.save()
    return HttpResponseRedirect(reverse("status.html"))
def student_reset(request,user_id):
    val=Form.objects.get(id=user_id)
    val.alloted=0
    val.save()
    return HttpResponse("reset successfully")
def write_view(request, *args, **kwargs):
    val=Form.objects.get(id=user_id)
    if request.is_ajax() and request.method == "POST":
        texteditor = request.POST['TextEntered']
        val.Management_Comments='texteditor'
        print(texteditor)
##      Don't forget to do validation and cleanup on texteditor to avoid security hassles  
##      Do your logic here
        SuccessAcknowledgment = {"Acknowledged":"Acknowledged"}
        return HttpResponse(json.dumps(SuccessAcknowledgment))
    else:
        return render(request, "write.html")

def showmess(request):
    if request.method=='POST':
        fm=mess(request.POST)
        if fm.is_valid():
            ms=fm.cleaned_data['Management_Comments']
            profile = fm.save(commit=False)
            profile.user = request.user
            profile.save()
            fm.save()    
            fm=mess()   
            print(ms) 
    else:
        fm=mess()
    return render(request,'status.html',{'mess':fm})
