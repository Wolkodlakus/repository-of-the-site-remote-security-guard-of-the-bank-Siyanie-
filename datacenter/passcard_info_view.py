from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime, now


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    
    this_passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits_context = []
    for this_passcard_visit in this_passcard_visits:
        selected_characteristics = {
            'entered_at': localtime(this_passcard_visit.entered_at),
            'duration': this_passcard_visit.format_duration(this_passcard_visit.get_duration()),
            'is_strange': this_passcard_visit.is_long(),
        }
        this_passcard_visits_context.append(selected_characteristics)
    
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits_context
    }
    return render(request, 'passcard_info.html', context)
