from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User

from .forms import RegisterForm, IngredientForm
from .models import ingredientDb, recipeDb

from openai import OpenAI
import os
import json
from dotenv import load_dotenv


load_dotenv()

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
    ingredients = ingredientDb.objects.order_by('-ingredientId')[:5]    # Descending order and top 5 rows
    recipes = recipeDb.objects.order_by('-recipeId')[:5]                # Descending order and top 5 rows
    return render(request, 'home.html', {'ingredients':ingredients, 'recipes':recipes})

@login_required
def newmeal_view(request):
    ai_response = None
    json_response= None
    if request.method == "POST":
        ingredients_data = request.POST.get('ingredients', '')
        ingredients = ingredients_data.split(',')
        for ingredient_name in ingredients:
            if ingredient_name.strip():
                ingredientDb.objects.create(
                    ingredientName=ingredient_name.strip(),
                    userName=request.user
                )
        calories = request.POST.get('calorieCount')
        cuisine = request.POST.get('cuisine')

        print("Ingredients :", ingredients, " ;Calories :", calories, " ;Cuisine :", cuisine)
        
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that should only answer questions related to recipes, ingredients, calories, and cuisines. Any other topics prompted, respond with 'Invalid question.'"},
                {
                    "role": "user",
                    "content": f"Give me a 3 {cuisine} recipes that can be made with {ingredients} that are close to about {calories} calories. Give me a short description, ingredient list, calorie count, and instructions to cook the recipe strictly in a pure valid json format without any introduction message starting and ending with curly brackets. For the 3 recipes, the JSON Keys should be : name, description, ingredients, calories, instructions"
                }
            ]
        )

        ai_response = completion.choices[0].message.content
        print('GPT Response -', ai_response)
        startIndex, endIndex = 0, 0
        try:
            for i in range(len(ai_response)):
                if ai_response[i] == '{':
                    startIndex = i
                    break
                    
            for i in range(len(ai_response)-1, 0, -1):
                if ai_response[i] == '}':
                    endIndex = i
                    break
            json_response = json.loads(ai_response[startIndex:endIndex+1])

            for i in range(3):
                recipeDb.objects.create(recipeName=json_response["recipes"][i]["name"], calories=json_response["recipes"][i]["calories"], userName=request.user)
        except:
            print("An error occured !")      
            json_response = "Invalid question."  

    return render(request, 'newmeal.html', {'yourRecipes':json_response})