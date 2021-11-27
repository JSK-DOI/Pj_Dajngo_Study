from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.KintaiNyuryoku.as_view(), name="kintainyuryoku"),
    path('kintailisttop/', views.KintaiListTop.as_view(), name="kintailisttop"),
    path('kintailist/<int:year>/<int:month>/', views.KintaiList.as_view(), name = 'kintailist'),
    path('kintailist/', views.KintaiList.as_view(), name = 'kintailist'),
]