from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.macros.macros_planner.models import MacrosPlanner


def statistics_view(request, pk):
    macros_planner = MacrosPlanner.objects.get(pk=pk)

    context = {'macros_planner': macros_planner}
    return render(request, 'statistics_/statistics.html', context)


@login_required
def statistics_list(request):
    profile = request.user.profile
    macros_planners = MacrosPlanner.objects.filter(profile__user=request.user)

    return render(
        request,
        'statistics_/statistics_list.html',
        {'profile': profile, 'macros_planners': macros_planners}
    )
