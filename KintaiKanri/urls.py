from django.urls import path
from django.urls.resolvers import _PATH_PARAMETER_COMPONENT_RE

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.KintaiNyuryoku.as_view(), name="kintainyuryoku"),
    path('pjkanriview/', views.PjKanriView.as_view(), name="PjKanriView"),
]