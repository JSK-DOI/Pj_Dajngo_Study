from django.urls import path
from django.urls.resolvers import _PATH_PARAMETER_COMPONENT_RE

from . import views

urlpatterns = [
    path('', views.mainmenu,  name='mainnenu'),
    path('kintainyuryoku/', views.KintaiNyuryoku.as_view(), name="kintainyuryoku"),
    path('kintailisttop/', views.KintaiListTop.as_view(), name="kintailisttop"),
    path('kintailist/<int:year>/<int:month>/', views.KintaiList.as_view(), name = 'kintailist'),
    path('kintailist/', views.KintaiList.as_view(), name = 'kintailist'),
    path('pjkanriview/', views.PjKanriView.as_view(), name="PjKanriView"),
    path('pjkanrinyuryoku/', views.PjKanriNyuryoku.as_view(), name="PjKanriNyuryoku"),
    path('search/', views.SearchView.as_view(), name='searchview'),
]