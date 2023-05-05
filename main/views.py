from django.shortcuts import render, redirect
from .forms import CreateUserForm

def home(request):
    return render(request, 'main/index.html')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'main/register.html', context)