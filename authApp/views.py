from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User

from .forms import RegisterForm, IngredientForm
from .models import ingredientDb, recipeDb

# Landing Page View
def landing_view(request):
    return render(request, 'landingpage.html')

# Register View
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login View
def login_view(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            print('Authentication Failed')
            error_message = 'Invalid Credentials!'
    return render(request, 'login.html', {'error': error_message})

# Logout View
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('landingpage')
    else:
        return redirect('landingpage')
    
# Home View
# Using the decorator
@login_required
def home_view(request):
    ingredients = ingredientDb.objects.all()
    recipes = recipeDb.objects.all()
    return render(request, 'home.html', {'ingredients':ingredients, 'recipes':recipes})

@login_required
def newmeal_view(request):
    if request.method == "POST":
        ingredients_data = request.POST.get('ingredients', '')
        ingredients = ingredients_data.split(',')
        for ingredient_name in ingredients:
            if ingredient_name.strip():
                ingredientDb.objects.create(
                    ingredientName=ingredient_name.strip(),
                    userName=request.user
                )

    return render(request, 'newmeal.html')