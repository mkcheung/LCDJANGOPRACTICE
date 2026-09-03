from django.urls import path

from .views import TwoSumView, ThreeSumView

urlpatterns = [
    path('two-sum/', TwoSumView.as_view(), name='two-sum'),
    path('three-sum/', ThreeSumView.as_view(), name='three-sum'),
]
