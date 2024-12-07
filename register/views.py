#views is used to route different pages holy fucking shit django is actually interesting to learn
from django.shortcuts import render, redirect
from .forms import SignUp
from .models import Profile
def register(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user)
            return redirect('login')
    else:
        form = SignUp()
    return render(request, 'register/register.html', {'form': form})


# Create your views here.
