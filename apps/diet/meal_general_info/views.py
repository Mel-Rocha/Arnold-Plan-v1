from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from apps.diet.food_options.models import FoodOptions
from apps.diet.meal_general_info.models import MealGeneralInfo
from apps.diet.meal_general_info.forms import MealGeneralInfoForm


@login_required
def meal_general_info_create(request):
    if request.method == 'POST':
        form = MealGeneralInfoForm(request.POST)
        if form.is_valid():
            meal_general_info = form.save()
            return redirect('meal_general_info:meal_general_info_details', pk=meal_general_info.pk)
    else:
        form = MealGeneralInfoForm()
    return render(request, 'meal_general_info/meal_general_info_create.html', {'form': form})


@login_required
def meal_general_info_update(request, pk):
    meal_general_info = get_object_or_404(MealGeneralInfo, pk=pk)

    if request.method == 'POST':
        form = MealGeneralInfoForm(request.POST, instance=meal_general_info)
        if form.is_valid():
            meal_general_info = form.save()
            return redirect('meal_general_info:meal_general_info_details', pk=meal_general_info.pk)
    else:
        form = MealGeneralInfoForm(instance=meal_general_info)

    return render(request, 'meal_general_info/meal_general_info_update.html',
                  {'form': form, 'meal_general_info': meal_general_info})


@login_required
def meal_general_info_delete(request, pk):
    meal_general_info = get_object_or_404(MealGeneralInfo, pk=pk)
    if request.method == 'POST':
        meal_general_info.delete()
        return redirect('meal_general_info:meal_general_info_list')
    return render(request, 'meal_general_info/meal_general_info_delete.html', {'meal_general_info': meal_general_info})


@login_required
def meal_general_info_details(request, pk):
    meal_general_info = get_object_or_404(MealGeneralInfo, pk=pk)
    meal = meal_general_info.meal

    food_optionss = FoodOptions.objects.filter(meal=meal)

    context = {'meal_general_info': meal_general_info, 'food_optionss': food_optionss, 'meal': meal}

    return render(request, 'meal_general_info/meal_general_info_details.html', context)
