from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from apps.diet.meal.models import Meal
from apps.diet.diet.models import Diet
from apps.diet.meal.forms import MealForm
from apps.diet.meal_general_info.forms import MealGeneralInfoForm


@login_required
def meal_list(request):
    profile = request.user.profile

    diets = profile.diet_set.all()
    meals = Meal.objects.filter(diet__in=diets)

    return render(request, 'meal/meal_list.html', {'profile': profile, 'meals': meals})


@login_required
def meal_create(request, diet_id):
    diet = Diet.objects.get(pk=diet_id)

    if request.method == 'POST':
        meal_general_info_form = MealGeneralInfoForm(request.POST)
        if meal_general_info_form.is_valid():
            meal_general_info = meal_general_info_form.save(commit=False)

            # Crie uma nova instância de Meal associada à dieta
            meal = Meal(diet=diet)
            meal.save()

            meal_general_info.meal = meal
            meal_general_info.save()

            return redirect('meal:meal_details', pk=meal.pk)
    else:
        meal_general_info_form = MealGeneralInfoForm()

    return render(request, 'meal/meal_create.html', {'meal_general_info_form': meal_general_info_form, 'diet': diet})


@login_required
def meal_update(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('meal/meal_details', pk=meal.pk)
    else:
        form = MealForm(instance=meal)
    return render(request, 'meal/meal_update.html', {'form': form, 'diet': meal})


@login_required
def meal_delete(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        diet_pk = meal.diet.pk
        meal.delete()
        return redirect('diet:diet_details', pk=diet_pk)
    return render(request, 'meal/meal_delete.html', {'meal': meal})


@login_required
def meal_details(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    meal_general_info = meal.mealgeneralinfo
    food_optionss = meal.foodoptions_set.all()

    context = {'meal': meal, 'meal_general_info': meal_general_info, 'food_optionss': food_optionss}
    return render(request, 'meal/meal_details.html', context)
