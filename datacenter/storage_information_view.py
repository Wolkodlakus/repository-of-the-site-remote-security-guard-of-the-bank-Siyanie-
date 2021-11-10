from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime, now



def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at = None)
    non_closed_visits_list = []    
    for non_closed_visit in non_closed_visits:
        
        dict_visit = {
            'who_entered' : non_closed_visit.passcard.owner_name,
            'entered_at' : localtime(non_closed_visit.entered_at),
            'duration' : non_closed_visit.format_duration(non_closed_visit.get_duration()),
            'is_strange' : non_closed_visit.is_long,
        }       
        non_closed_visits_list.append(dict_visit)
    
    context = {
        'non_closed_visits': non_closed_visits_list,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
