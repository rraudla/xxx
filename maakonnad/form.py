from django import forms
from .models import mk, vald, linn

class form_locator(forms.Form):
    valik_mk = forms.ModelChoiceField(queryset=mk.objects.all().order_by('maakond'),
                                   widget=forms.Select(attrs={'onchange': 'submit();'}), empty_label='- - maakond - -')
    valik_linn = forms.ModelChoiceField(queryset=linn.objects.all().order_by('linn'),
                                    widget=forms.Select(attrs={'onchange': 'submit();'}), empty_label='- - linn - -')
