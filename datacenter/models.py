from django.db import models
from django.utils.timezone import localtime, now


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def format_duration(self, duration):
        sday = ''
        if duration.days > 0:
            sday = str(duration.days)+'д '
        shour = str(duration.seconds // 3600)+'ч '
        sminute = str((duration.seconds % 3600) // 60)+'мин '
        ssecond = str(duration.seconds % 60)+'сек'

        return sday+shour+sminute+ssecond

    def get_duration(self):
        if self.leaved_at is None:
            return localtime() - localtime(self.entered_at)
        else:
            return localtime(self.leaved_at) - localtime(self.entered_at)
    
    def is_long(self, minutes=60):
        return self.get_duration().total_seconds() >= minutes*60

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved='leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )
