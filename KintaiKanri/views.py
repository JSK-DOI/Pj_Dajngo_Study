from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import TKntiDtl
from .models import MPjKnr
from .forms import KintaiNyuryokuForm
from django.views.generic import ListView
from django.db.models import Q  


def index(request):
    return HttpResponse("Hello, world. ")


class KintaiNyuryoku(CreateView):
    model = TKntiDtl
    form_class = KintaiNyuryokuForm
    
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
    