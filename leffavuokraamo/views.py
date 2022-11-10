from datetime import date
from django.db.models import Q
from django.shortcuts import redirect, render 
from django.views import generic
from .models import Film, Rental, Genre, Tag
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, CreateEditForm


def index(request):
    print(request.headers)
    return render(request, "leffavuokraamo/index.html",{})


@login_required(login_url='/leffavuokraamo/login_page')
def user_page(request):
    user = request.user
    rentals = Rental.objects.filter(customer=user).order_by('-rental_date')
    context = {"user": user, "rentals": rentals}
    return render(request, "leffavuokraamo/user_page.html", context)


def return_movie(request, rental_id):
    rental = Rental.objects.get(id=rental_id)
    return_date = date.today()
    setattr(rental, 'is_active', 'False')
    setattr(rental, 'date_returned', return_date)
    film = getattr(rental, 'film')
    setattr(film, 'is_loaned', 'False')
    film.save()
    rental.save()
    return render(request, "leffavuokraamo/return_success.html", {'film': film})


def movies(request):
    all_films = Film.objects.all().order_by('title')
    context = {"all_films":all_films}
    word = ''
    results = []
    if 'word' in request.GET:
        word = request.GET['word']
        if len(word)>0:
            genres = Genre.objects.filter(name__icontains=word)
            tags = Tag.objects.filter(tag__icontains=word)
            results = Film.objects.filter(Q(title__icontains=word) | Q(genres__in=genres) | Q(tags__in=tags))
        context = {'results': results}
    return render(request, 'leffavuokraamo/movies_page.html', context)


class MovieDetailsView(generic.DetailView):
    model = Film
    template_name = 'leffavuokraamo/moviedetails_page.html'


@login_required(login_url='/leffavuokraamo/login_page')
def rent_movie(request, film_id):
    film = Film.objects.get(id=film_id)
    setattr(film, 'is_loaned', 'True')
    film.save()
    customer = request.user
    rental = Rental(film=film, customer=customer)
    setattr(rental, 'is_active', 'True')
    rental.save()
    context = {"film": film, "customer": customer, "rental": rental}
    return render(request, 'leffavuokraamo/movierent_page.html', context)


def success(request):
    return render(request, 'leffavuokraamo/movierent_page.html',{})


# REKISTERÖITYMISSIVU
 
def registeration_page(request):
    form = CreateUserForm()
    
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Käyttäjätunnus luotu käyttäjälle " + user)
            return redirect('leffavuokraamo:login')
    context = {'form':form }
    
    return render(request, 'leffavuokraamo/registeration_page.html', context)

     
# KIRJAUTUMISSIVU
   
def login_page(request):
    if request.method == "POST":
        username = request.POST['käyttäjätunnus']
        password = request.POST['salasana']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('leffavuokraamo:user')
        else:
            messages.success(request, ("Virheellinen käyttäjätunnus tai salasana. Yritä uudelleen."))
            return redirect('leffavuokraamo:login')
    
    else:
    
       return render(request, "leffavuokraamo/login_page.html",{})


# MUOKKAA PROFIILIA

def edit_profile(request):
    form = CreateEditForm()
    
    if request.method =="POST":
        form = CreateEditForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, ("Käyttäjätietoja muokattu"))
            return redirect('leffavuokraamo:user')
            
            
    else:
        form = CreateEditForm(instance=request.user)
        context = {'form': form}
        return render(request, 'leffavuokraamo/edit_profile.html', context)

    context = {'form': form}
    return render(request, 'leffavuokraamo/edit_profile.html', context)


