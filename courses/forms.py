from django import forms
from .models import ClassGroup
from datetime import date ,datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class ClassGroupForm(forms.ModelForm):

    def clean(self):

        start_date = self.cleaned_data.get('start_date')
        days = list(self.cleaned_data.get('days'))  
        print(start_date)
        print(days)
        daysarr = []
        for day in days:
            daysarr.append(day.days)
        startday = start_date.isoweekday()
        
        if startday not in daysarr :
            raise ValidationError({'start_date' :
                _('start day must be in session days')},
            )
        return self.cleaned_data
    class Meta:
        model = ClassGroup
        fields = '__all__'
