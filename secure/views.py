from django.shortcuts import render, redirect
from .models import Vault
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    all_passwords = Vault.objects.filter(user=request.user)
    context = {'passwords': all_passwords}
    return render(request, 'index.html', context)

@login_required
def add_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_password = Vault(user=request.user, username=username, password=password)
        new_password.save()
        return redirect('index')
    return render(request, 'add.html')