from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.daily_records.forms import DailyRecordsForm
from apps.daily_records.models import DailyRecords

@login_required
def create_daily_records(request):
    if request.method == 'POST':
        form = DailyRecordsForm(request.POST)
        if form.is_valid():
            daily_record = form.save(commit=False)
            daily_record.profile = request.user.profile
            daily_record.save()
            return redirect('daily_records:daily_records_list')
    else:
        form = DailyRecordsForm()
    return render(request, 'daily_records/daily_records_form.html', {'form': form})

@login_required
def daily_records_list(request):
    profile = request.user.profile
    records = DailyRecords.objects.filter(profile=profile)
    return render(request, 'daily_records/daily_records_list.html', {'records': records})
