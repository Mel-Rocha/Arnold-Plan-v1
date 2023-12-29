@login_required
def food_options_create(request):
    if request.method == 'POST':
        form = FoodOptionsForm(request.POST)
        if form.is_valid():
            food_options = form.save()
            return redirect('food_optionos:food_optionos_details', pk=food_options.pk)
    else:
        form = FoodOptionsForm()
    return render(request, 'food_options/food_options_create.html', {'form': form})