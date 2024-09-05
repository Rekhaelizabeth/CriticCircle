from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Director, Movie

# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def seller(request):
    return render(request,'seller.html')
def sellerpage(request):
    return render(request,'sellerpage.html')
def movies(request):
    
    movie_list = Movie.objects.all()  # Fetch only 3 movies
    return render(request, 'movies.html', {'movies': movie_list})

def directors(request):
    
    directorslist = Director.objects.all()  # Fetch only 3 movies
    return render(request, 'directors.html', {'directorslist': directorslist})
def director_movies(request, director_id):
    # Fetch the director based on the ID
    director = get_object_or_404(Director, id=director_id)
    # Fetch all movies by this director
    movies = Movie.objects.filter(director=director)
    context = {
        'director': director,
        'movies': movies,
    }
    return render(request, 'director_movies.html', context)


# def addproductadmin(request):
    # user = request.user
    # userid = user.id
    # stdata = Category.objects.all()
    # if request.method == 'POST':
    #     # Create a new Category instance and assign values
    #     newproduct = Product(
    #     product_name = request.POST.get('product_name'),
    #     product_description = request.POST.get('product_description'),
    #     price = request.POST.get('price'),
    #     product_images1 = request.FILES.get('product_images1'),
    #     product_images2 = request.FILES.get('product_images2'),
    #     product_images3 = request.FILES.get('product_images3'),
    #     category = request.POST.get('category'),
    #     brand_name = request.POST.get('brand_name'),
    #     sizeQuantity = request.POST.get('sizeQuantity'),
    #     petCompatibility = request.POST.get('petCompatibility'),
    #     agesizesuitability = request.POST.get('agesizesuitability'),
    #     colorsVariations = request.POST.get('colorsVariations'),
    #     user_id=userid
    #     )
    #     newproduct.save()   
        
    #     return redirect("viewproduct")
    # return render(request, "addproductadmin.html")




def admindashboard(request):
    return render(request,'admindashboard.html')
# def viewproduct(request):
#     stdata = Product.objects.filter(status=False)
#     return render(request, "viewproduct.html", {'stdata': stdata})


def customerproduct(request):
    # stdata = Product.objects.filter(status=False)
    return render(request, "customerproduct.html")


def displayDog(request):
    return render(request,'displayDog.html')

def displayCat(request):
    return render(request,'displayCat.html')

def displayBird(request):
    return render(request,'displayBird.html')
