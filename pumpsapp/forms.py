from django import forms
from .models import GroupsPumps
from .models import Pumps

class GroupPumpsForm(forms.ModelForm):
    pump = forms.ModelMultipleChoiceField(queryset=Pumps.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = GroupsPumps
        fields = ['group', 'pump']

