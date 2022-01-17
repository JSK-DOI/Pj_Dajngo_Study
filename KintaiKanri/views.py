from django.views import generic
from django.db.models import fields
from django.http import HttpResponse
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import TKntiDtl, TKntiDtl, MPjKnr
from .forms import KintaiNyuryokuForm, KintaiListTopForm, PjKanriNyuryokuForm   
from .mixins import MonthCalendarMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlencode
from datetime import datetime as dt
from django.db.models import Q 
from django.shortcuts import render
from .models import MUsr

def mainmenu(request):
  return render(request, 'KintaiKanri/Mainmenu.html')

class KintaiNyuryoku(CreateView):
    model = TKntiDtl
    form_class = KintaiNyuryokuForm

class KintaiListTop(FormView):
    form_class = KintaiListTopForm
    template_name = 'KintaiKanri/kintailisttop.html'

    def get(self, request, *args, **kwargs):
        if "action" in self.request.GET:
            # 文字列⇒日付型に変更
            knti_dt = dt.strptime(self.request.GET.get('knti_dt'),'%Y-%m-%d')
            # パラメータをdict型でセット
            paras = {
                'syn_cd' : self.request.GET.get('syn_cd'),
                'pj_no' : self.request.GET.get('pj_no'),
            }
            # パラメータをurlencode
            parameters = urlencode(paras)
            # リダイレクト先のURLパス
            redirect_url = reverse('kintailist', args = (knti_dt.year, knti_dt.month,))
            # URLにパラメータを付与
            url = f'{redirect_url}?{parameters}'
            return HttpResponseRedirect(url)
        else:
            return super().get(request, *args, **kwargs)


class KintaiList(MonthCalendarMixin, ListView):
    first_weekday = 6
    template_name = 'KintaiKanri/KintaiList.html'
    model = TKntiDtl
    context_object_name = 'TKntiDtl_list'
    #queryset = TKntiDtl.objects.none()
    #queryset = TKntiDtl.objects.filter(syn_cd='21850',pj_no='72018021')
    #paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 月間カレンダーフォーム取得
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        context['syn_cd'] = self.request.GET.get('syn_cd')
        context['pj_no'] = self.request.GET.get('pj_no')
        return context

#----------------------------------------
#--- プロジェクト管理画面
#----------------------------------------
class PjKanriView(ListView):
    # model = MPjKnr
 #  template_name = ".html"
    def get_queryset(self):
        strFind_Key = self.request.GET.get('PJknr_list_Find')

        if strFind_Key:
            object_list = MPjKnr.objects.filter(
                # Q(pj_no=strFind_Key) | Q(pj_nm=strFind_Key)
                Q(pj_no__icontains=strFind_Key) | Q(pj_nm__icontains=strFind_Key) | Q(act_hrs__icontains=strFind_Key)
            )
        else:
            object_list = MPjKnr.objects.all()

        # return super().get_queryset()
        return object_list

class PjKanriNyuryoku(CreateView):
    model = MPjKnr
    form_class = PjKanriNyuryokuForm
    template_name = "KintaiKanri/PjKanriNyuryoku.html"

class SearchView(ListView):
    model = TKntiDtl
    template_name = 'KintaiKanri/searchview.html'
    def get_queryset(self):
        q_word = self.request.GET.get('query')
 
        if q_word:
            object_list = TKntiDtl.objects.filter(
                Q(syn_cd__icontains=q_word) | Q(knti_dt__icontains=q_word))
        else:
            object_list = TKntiDtl.objects.all()
        return object_list

#----------------------------------------
#--- ユーザ管理画面
#----------------------------------------
class MUserList(generic.ListView):
    model = MUsr
    template_name = 'KintaiKanri/muser_list.html'

    # ユーザ管理一覧に表示する項目をゲット
    def get_queryset(self) :
## とりあえず全件出力
        users = MUsr.objects.all()
        return users

 # ユーザ詳細画面
 # MUserDetail
class MUserDetail(DetailView) :
    model = MUsr
    template_name = 'KintaiKanri/muser_detail.html'
    
   
 # ユーザ登録画面   
class MUserCreate(CreateView) :
    model = MUsr
    template_name = 'KintaiKanri/muser_create.html'
    # 画面上に表示させる項目の指定
    fields = ('syn_cd','syn_nm_s_kj','syn_nm_n_kj','syn_nm_s_kn','syn_nm_n_kn','nysy_dt','pj_add_dt','pj_del_dt','e_mail_adr','syn_kngn','lgn_pss','syn_kbn')
