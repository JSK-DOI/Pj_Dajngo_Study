from django.views import generic
from django.db.models import fields
from django.http import HttpResponse
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import TKntiDtl, MUsr, MPjKnr, MClndr
from .forms import KintaiNyuryokuForm, KintaiListTopForm, PjKanriNyuryokuForm, CalendarNyuryokuForm, OtameshiForm
from .mixins import MonthCalendarMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from urllib.parse import urlencode
from datetime import datetime, date
from django.db.models import Q 
from django.shortcuts import render,redirect
from . import mixins
import MySQLdb
from django.db import connection
from django.db.utils import IntegrityError

def mainmenu(request):
  return render(request, 'KintaiKanri/Mainmenu.html')

class KintaiNyuryoku(FormView):
    model = TKntiDtl
    form_class = KintaiNyuryokuForm
    template_name = 'KintaiKanri/tkntidtl_form.html'
    

class KintaiListTop(FormView):
    form_class = KintaiListTopForm
    template_name = 'KintaiKanri/kintailisttop.html'

    def get(self, request, *args, **kwargs):
        if "action" in self.request.GET:
            # 文字列⇒日付型に変更
            knti_dt = datetime.strptime(self.request.GET.get('knti_dt'),'%Y-%m-%d')
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

    def get_queryset(self):
        # パラメータ
        v_month  = self.kwargs.get('month')
        v_year   = self.kwargs.get('year')
        v_syn_cd = self.request.GET.get('syn_cd')
        v_pj_no  = self.request.GET.get('pj_no')
        # 当月1日
        if v_month and v_year:
            dt1 = date(year=int(v_year), month=int(v_month), day=1)
        else:
            dt1 = date.today().replace(day=1)
        # 次月1日
        if dt1.month == 12:
            dt2 = dt1.replace(year=dt1.year+1, month=1, day=1)
        else:
            dt2 = dt1.replace(month=dt1.month+1, day=1)
        # 勤怠明細テーブル
        queryset = TKntiDtl.objects.filter(
            syn_cd       = v_syn_cd, 
            pj_no        = v_pj_no,
            knti_dt__gte = dt1,
            knti_dt__lt  = dt2,
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 月間カレンダーフォーム取得
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        context['syn_cd'] = self.request.GET.get('syn_cd')
        context['pj_no'] = self.request.GET.get('pj_no')
        context['new_list'] = self._set_list(context=context)
        return context
    
    def _set_list(self, context: dict):
        dic   = dict()
        # データ取得
        data1=list(context['TKntiDtl_list'].values())
        data2=context['month_days']
        curr=context['month_current']
        # 勤怠明細QuerySet ⇒ 辞書に変換
        for rec in data1:
            dic[rec['knti_dt']] = rec
        # カレンダー日付リストより、データなしの日付を辞書に追加
        for week in data2:
            for day in week:
                if day.month == curr.month:
                    if dic.get(day) is None:
                        dic[day] = {'syn_cd':'','knti_dt':day}
        # ソート ※itemsを使用するのでソート後はタプルになる
        dic_sort = sorted(dic.items(), key=lambda x:x[0])
        # 再度、辞書に変換
        dic_new  = dict((x,y) for x, y in dic_sort)

        return dic_new

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
 # MUserCreate   
class MUserCreate(CreateView) :
    model = MUsr
    template_name = 'KintaiKanri/muser_create.html'
    # 画面上に表示させる項目の指定
    fields = ('syn_cd','syn_nm_s_kj','syn_nm_n_kj','syn_nm_s_kn','syn_nm_n_kn','nysy_dt','pj_add_dt','pj_del_dt','e_mail_adr','syn_kngn','lgn_pss','syn_kbn')

# カレンダー管理画面
class CalendarNyuryoku(mixins.MonthWithFormsMixin, generic.View):
    """フォーム付きの月間カレンダーを表示するビュー"""
    template_name = 'KintaiKanri/CalendarNyuryoku.html'
    model = MClndr
    date_field = 'clndr_dt'
    form_class = CalendarNyuryokuForm

    def get(self, request, **kwargs):
        context = self.get_month_calendar()
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        context = self.get_month_calendar()
        formset = context['month_formset']
        if formset.is_valid():
            formset.save()
            return redirect('calendarnyuryoku')

        return render(request, self.template_name, context)

 # ユーザ編集画面
 # MUsrUpdate    
class MUsrUpdate(UpdateView):
    model = MUsr
    template_name = "KintaiKanri/muser_update.html"
    # 画面上に表示させる項目の指定
    fields = ('syn_cd','syn_nm_s_kj','syn_nm_n_kj','syn_nm_s_kn','syn_nm_n_kn','nysy_dt','pj_add_dt','pj_del_dt','e_mail_adr','syn_kngn','lgn_pss','syn_kbn')
    # ---
    success_url = reverse_lazy('muserlist')


class otameshi(generic.View):
    form = OtameshiForm()
    template_name = 'KintaiKanri/otameshi.html'

    def get(self, request, **kwargs):
        context = {'form': self.form}
        return render(request, self.template_name, context)
    def post(self, request, **kwargs):
        if request.method == 'POST':
            form = OtameshiForm(request.POST)
            if form.is_valid():
                syn_cd = request.POST["syn_cd"]
                knti_dt = request.POST["knti_dt"]
                pj_no = request.POST["pj_no"]
                knti_dt = str(knti_dt).replace('-', '/')

                sqlxx = "INSERT INTO t_knti_dtl VALUES ('" + syn_cd + "', '" + knti_dt + "', '"+ pj_no +"', null, null, null, null, null, null) "
                print(sqlxx)
                #TKntiDtl.objects.raw(sqlxx)
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(sqlxx)
                except IntegrityError:
                    print('プライマリキー重複')
                    return HttpResponseRedirect('http://127.0.0.1:8000/primalyerror/')

                return mainmenu(request)
            else:
                print('ERROR FORM INVALID')

        context = {'form': form}
        return render(request, self.template_name, context)


def primalyerror(request):
  return render(request, 'KintaiKanri/primalyerror.html')