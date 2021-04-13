from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        #check correct data
        if fm.is_valid():
            print('form validation')
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            # for showing data in terminal
            print(name)
            print(email)

        print('cleaned data',fm)
    else:
        fm= StudentRegistration()
        #print("ye get request se aya hai")

    return render(request,"form/makeform.html",{'form':fm})