from django import forms
from django.forms import fields
from .models import TKntiDtl, MPjKnr, MClndr
 
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

class PjKanriNyuryokuForm(forms.ModelForm):
    class Meta:
        model = MPjKnr
        fields = ('pj_no', 'pj_nm', 'pj_st_time', 'rst_st_time', 'rst_ed_time', 'pj_ed_time', 'act_hrs')

class CalendarNyuryokuForm(forms.ModelForm):
    """シンプルなスケジュール登録用フォーム"""
    class Meta:
        model = MClndr
        fields = ('clndr_dt', 'pj_no', 'wrk_dt_kbn',)
        labels = {
           'clndr_dt':'年月日',
           'pj_no':'プロジェクト番号',
           'wrk_dt_kbn':'稼働区分',
           }
        widgets = {
            'clndr_dt': forms.HiddenInput,
        }



class OtameshiForm(forms.Form):
    syn_cd = forms.CharField(
        label = '社員CD',
        required = False,
        max_length = 6,
        widget = forms.TextInput(attrs={'size':10}),
    )
    knti_dt = forms.DateField(
        label = '勤怠日付',
        required = False,
        widget = forms.DateInput(attrs={'type':'date'}),
        input_formats = ['%Y-%m-%d'],  
        error_messages={
            'invalid': '報告日を正しく入力してください。',
        },
    )
    pj_no = forms.CharField(
        label = 'プロジェクトNo',
        required = False,
        max_length = 8,
    )