from django.urls import include, path

from .views import MyView

urlpatterns = [
  path('t', MyView.as_view({'get': 'test'})),
]