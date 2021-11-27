from django import forms
from django.forms import fields
from .models import TKntiDtl
 
class KintaiNyuryokuForm(forms.ModelForm):
    class Meta:
        model = TKntiDtl
        fields = ('syn_cd', 'knti_dt', 'pj_no', 'wrk_st_time', 'wrk_ed_time', 'act_hrs', 'rst_hrs', 'mdnght_wrk_hrs', 'nn_rglr_wrk_hrs', )

class KintaiListTopForm(forms.ModelForm):
    class Meta:
        model = TKntiDtl
        fields = ['syn_cd', 'knti_dt', 'pj_no']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['knti_dt'].widget = forms.DateInput(attrs={'type':'date'})



