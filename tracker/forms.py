from django.forms import ModelForm
from .models import Trackerdata

class TrackerdataForm(ModelForm):
    class Meta:
        model =Trackerdata
        fields=['automation','task','stardate','enddate','status','blockers','spoc','finished']
        #exclude = ()
