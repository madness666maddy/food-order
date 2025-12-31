from django.shortcuts import render
from .models import Food, Combo

def menu_view(request):
    foods = Food.objects.all()
    combos = Combo.objects.all()

    return render(request, 'menu/menu.html', {
        'foods': foods,
        'combos': combos
    })
