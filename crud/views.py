from django.shortcuts import render
from crud.form import EmpForm
def index(request):
    if request.method=='POST':
        stu=EmpForm(request.POST)
        if stu.is_valid():
            try:
                stu.save()
            except:
                pass
    else:
        stu=EmpForm()
    return render(request,"index.html",{'form':stu})