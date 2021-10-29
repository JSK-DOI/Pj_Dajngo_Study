from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import TKntiDtl
from .forms import KintaiNyuryokuForm


def index(request):
    return HttpResponse("Hello, world. ")


class KintaiNyuryoku(CreateView):
    model = TKntiDtl
    form_class = KintaiNyuryokuForm
    
