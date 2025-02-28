from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect("products:list")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})
