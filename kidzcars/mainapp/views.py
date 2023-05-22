from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, NewCarForm, NewBrandForm
from .models import Car, Brand
from django.contrib import messages
import wikipedia, joblib
from wikipedia.exceptions import PageError

# Create your views here.

def index(request):
	return render(request, 'index.html')

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('mainapp:profile')
			else:
				messages.error(request,"Invalid username or password")
		else:
			messages.error(request,"Invalid username or password")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out") 
	return redirect('mainapp:index')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful" )
			return redirect('mainapp:index')
		messages.error(request, "Unsuccessful registration : invalid information")
	form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form":form})

def profile(request):
    return render(request, 'profile.html')

def newcar(request):
	if request.method == "POST":
		form = NewCarForm(request.POST)
		if form.is_valid():
			car = form.save()
			messages.success(request, "Car register successful" )
			return redirect('mainapp:index')
		messages.error(request, "Unsuccessful registration : invalid information")
	form = NewCarForm()
	return render(request=request, template_name="newcar.html", context={"newcar_form":form})

def newbrand(request):
	if request.method == "POST":
		form = NewBrandForm(request.POST, request.FILES)
		if form.is_valid():
			brand = form.save(commit=False)
			brand.save()
			messages.success(request, "Brand register successful")
			return redirect('mainapp:index')
		messages.error(request, "Unsuccessful registration : invalid information")
	form = NewBrandForm()
	return render(request=request, template_name="newbrand.html", context={"newbrand_form":form})

def carlist(request):
    brands = Brand.objects.all()
    context = {
        'brands': brands,
    }
    return render(request, 'carlist.html', context)

def cardetail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    
    try:
        wikipedia_page = wikipedia.page(car.brand.name + " " + car.model + " " + car.generation, auto_suggest=False)
    except PageError:
        print("Error while fetching Wikipedia page, trying another page")
        try:
            wikipedia_page = wikipedia.page(car.brand.name + " " + car.model, auto_suggest=False)
        except PageError:
            print("Error while fetching Wikipedia page, trying another page")
            try:
                wikipedia_page = wikipedia.page(car.brand.name + " " + car.model.lower(), auto_suggest=False)
            except PageError:
                print("Error while fetching Wikipedia page for the brand")
                try:
                    wikipedia_page = wikipedia.page(car.brand.name + "car manufacturer", auto_suggest=False)
                except PageError:
                    print("Error while fetching Wikipedia page for the brand")
                    wikipedia_page = None
    
    if wikipedia_page:
        wikipedia_content = wikipedia_page.content
        wikipedia_url = wikipedia_page.url
        paragraphs = wikipedia_content.split('\n\n')
        wikipedia_intro = paragraphs[0].split('==')[0].strip() if paragraphs else ""
    else:
        wikipedia_intro = ""
        wikipedia_url = ""
    
    context = {
        'car': car,
        'wikipedia_intro': wikipedia_intro,
        'wikipedia_url': wikipedia_url,
    }
    
    return render(request, 'cardetail.html', context)


def branddetail(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    cars = brand.car_set.all()
    context = {
        'brand': brand,
        'cars': cars
    }
    return render(request, 'branddetail.html', context)

def savecars(request):
	cars_ready = joblib.load("mainapp/scripts/cars_ready.joblib")

	for car in cars_ready:
		model = car[1]
		generation = car[2]
		year = int(car[3])

		car_tosave = Car(brand=Brand.objects.get(name="Mercedes-Benz"), model=model, generation=generation, year=year)
		car_tosave.save()

		print(model, generation, year, 'saved')

	return render(request, 'index.html')