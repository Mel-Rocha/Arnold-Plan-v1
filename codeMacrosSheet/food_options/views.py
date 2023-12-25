from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodOptions
from .forms import FoodOptionsForm
from meal.models import Meal
from django.contrib.auth.decorators import login_required



@login_required
def food_options_create(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)

    if request.method == 'POST':
        form = FoodOptionsForm(request.POST)
        if form.is_valid():
            food_options = form.save(commit=False)
            food_options.meal = meal
            food_options.save()
            return redirect('food_options:food_options_details', pk=food_options.pk)
    else:
        form = FoodOptionsForm()

    return render(request, 'food_options/food_options_create.html', {'form': form, 'meal': meal})


@login_required
def food_options_update(request, pk):
    food_options = get_object_or_404(FoodOptions, pk=pk)

    if request.method == 'POST':
        form = FoodOptionsForm(request.POST, instance=food_options)
        if form.is_valid():
            food_options = form.save()
            return redirect('food_options:food_options_details', pk=food_options.pk)
    else:
        form = FoodOptionsForm(instance=food_options)
    
    return render(request, 'food_options/food_options_update.html', {'form': form, 'food_options': food_options})


@login_required
def food_options_delete(request, pk):
    food_options = get_object_or_404(FoodOptions, pk=pk)
    if request.method == 'POST':
        food_options.delete()
        return redirect('food_options:food_options_list')
    return render(request, 'food_options/food_options_delete.html', {'food_options': food_options})


@login_required
def food_options_details(request, pk):
    food_options = get_object_or_404(FoodOptions, pk=pk)
    return render(request, 'food_options/food_options_details.html', {'food_options': food_options})


@login_required
def food_options_list(request):
    food_options = FoodOptions.objects.all()
    return render(request, 'food_options/food_options_list.html', {'food_options': food_options})