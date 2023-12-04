from django.shortcuts import render
from .models import GroupsPumps, PumpStatus
from .forms import GroupPumpsForm

def index(request):
    unique_groups = set(GroupsPumps.objects.values_list('group__name', flat=True))  # Получение уникальных групп
    groups_with_pumps = {}
    
    for group_name in unique_groups:
        pumps = GroupsPumps.objects.filter(group__name=group_name).values_list('pumps__name', flat=True)
        statuses = PumpStatus.objects.filter(pumps__name__in=pumps)
        status_info = [(pump, status) for pump, status in zip(pumps, statuses)]
        groups_with_pumps[group_name] = status_info
    
    return render(request, 'pumpsapp/index.html', {'groups_with_pumps': groups_with_pumps})


def index1(request):
    grouppumps = GroupsPumps.objects.all()
    
    return render(request, 'pumpsapp/h.html', {'grouppumps': grouppumps})


