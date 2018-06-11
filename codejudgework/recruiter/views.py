from django.shortcuts import render
from recruiter.forms import UserForm,RecruiterForm
def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        recruiter_form = RecruiterForm(data=request.POST)

        if user_form.is_valid() and recruiter_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            recruiter = recruiter_form.save(commit=False)
            recruiter.user = user

            recruiter.save()
            registered = True

        else:
            print(user_form.errors,recruiter_form.errors)
    else:
        user_form = UserForm()
        recruiter_form = RecruiterForm()

    return render(request,'recruiter/index.html',
    {'user_form':user_form,
    'recruiter_form':recruiter_form,
    'registered':registered})


# Create your views here.
