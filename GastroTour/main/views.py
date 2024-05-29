from django.shortcuts import render, get_object_or_404, redirect
from.models import Restaurant,Cart
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import uuid

def index(request):
    try:
        geranium = Restaurant.objects.get(name='Шиокара')
    except Restaurant.DoesNotExist:
        geranium = None

    return render(request, 'main/index.html', {'geranium': geranium})

def aboutus(request):
    return render(request, 'main/aboutus.html')


def tourInfo(request):
    return render(request, 'main/tourInfo.html')

def cart(request):
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart_items = Cart.objects.filter(session_id=cart_id)
    else:
        cart_items = []

    return render(request, 'main/cart.html', {'cart_items': cart_items})

def pay(request, restaurant_name):
    restaurant = get_object_or_404(Restaurant, name=restaurant_name)
    cost = restaurant.price
    
    context = {
        'cost': cost,
    }
    
    return render(request, 'main/pay.html', context)

def determine_continent(country):
    europe_countries = ['Франция', 'Германия', 'Италия', 'Дания']
    asia_countries = ['Китай', 'Индия', 'Япония']
    north_america_countries = ['США', 'Канада']
    south_america_countries = ['Бразилия', 'Аргентина']

    if country in europe_countries:
        return 'Европа'
    elif country in asia_countries:
        return 'Азия'
    elif country in north_america_countries:
        return 'Северная Америка'
    elif country in south_america_countries:
        return 'Южная Америка'
    else:
        return 'Другие'
    
def tours(request):
    restaurants = Restaurant.objects.all()  

    return render(request, 'main/tours.html', {'continents': restaurants})


def tour_info(request, tour_id):
    tour = Restaurant.objects.get(id=tour_id)
    context = {
        'title': tour.title,
        'country': tour.country,
        'rate': tour.rate,
        'cost': tour.cost,
        'description': tour.description,
    }
    return render(request, 'tourInfo.html', context)

def tourInfo(request, tour_name):
    restaurant = get_object_or_404(Restaurant, name=tour_name)
    
    context = {
        'restaurant': restaurant,
    }
    
    return render(request, 'main/tourInfo.html', context)

@csrf_exempt
def add_to_cart(request, restaurant_name):
    try:
        # Сначала получаем объект ресторана по имени
        restaurant = Restaurant.objects.get(name=restaurant_name)
    except Restaurant.DoesNotExist:
        return JsonResponse({'error': 'Ресторан не найден'}, status=404)

    cart_id = request.session.get('cart_id')
    if not cart_id:
        cart_id = str(uuid.uuid4())
        request.session['cart_id'] = cart_id

    # Теперь, когда у нас есть объект ресторана, мы можем создать объект Cart
    Cart.objects.create(restaurant=restaurant, session_id=cart_id)

    return redirect('cart')