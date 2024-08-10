from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from apps.diet.diet.models import Diet
from apps.diet.diet.forms import DietForm
from apps.diet.food_options.models import FoodOptions
from apps.diet.diet_general_info.forms import DietGeneralInfoForm
from apps.diet.meal_general_info.models import MealGeneralInfo


@login_required
def diet_list(request):
    profile = request.user.profile
    diets = Diet.objects.filter(profile__user=request.user)
    return render(request, 'diet/diet_list.html', {'profile': profile, 'diets': diets})


@login_required
def diet_create(request):
    if request.method == 'POST':
        diet_general_info_form = DietGeneralInfoForm(request.POST)
        if diet_general_info_form.is_valid():
            diet_general_info = diet_general_info_form.save(commit=False)

            # Associe a instância de Diet ao perfil do usuário
            diet = Diet.objects.create(profile=request.user.profile)
            diet_general_info.diet = diet
            diet_general_info.save()

            # Redirecione para os detalhes da nova dieta
            return redirect('diet:diet_details', pk=diet.pk)
    else:
        diet_general_info_form = DietGeneralInfoForm()
    
    return render(request, 'diet/diet_create.html', {'diet_general_info_form': diet_general_info_form})


@login_required
def diet_update(request, pk):
    diet = get_object_or_404(Diet, pk=pk)
    if request.method == 'POST':
        form = DietForm(request.POST, instance=diet)
        if form.is_valid():
            form.save()
            return redirect('diet/diet_details', pk=diet.pk)
    else:
        form = DietForm(instance=diet)
    return render(request, 'diet/diet_update.html', {'form': form, 'diet': diet})


@login_required
def diet_delete(request, pk):
    diet = get_object_or_404(Diet, pk=pk)
    if request.method == 'POST':
        diet.delete()
        return redirect('diet:diet_list')
    return render(request, 'diet/diet_delete.html', {'diet': diet})


@login_required
def diet_details(request, pk):
    diet = get_object_or_404(Diet, pk=pk)
    diet_general_info = diet.dietgeneralinfo
    meals = diet.meal_set.all()
    meal_general_infos = MealGeneralInfo.objects.filter(meal__in=meals)
    food_optionss = FoodOptions.objects.filter(meal__in=meals)

    context = {'diet': diet, 'diet_general_info': diet_general_info, 'meals': meals, 'meal_general_infos': meal_general_infos, 'food_optionss': food_optionss}
    return render(request, 'diet/diet_details.html', context)
