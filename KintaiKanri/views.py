from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import TKntiDtl
from .models import MPjKnr
from .forms import KintaiNyuryokuForm
from django.views.generic import ListView


def index(request):
    return HttpResponse("Hello, world. ")


class KintaiNyuryoku(CreateView):
    model = TKntiDtl
    form_class = KintaiNyuryokuForm
    
class PjKanriView(ListView):
    model = MPjKnr
 #  template_name = ".html"
