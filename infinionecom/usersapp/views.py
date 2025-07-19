from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False  # Always register as buyer
            user.save()
            login(request, user)  # Auto-login after signup (optional)
            return redirect('home')  # Or wherever
    else:
        form = CustomUserCreationForm()
    return render(request, 'register_account.html', {'form': form})