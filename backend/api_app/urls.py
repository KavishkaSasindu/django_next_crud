from django.urls import path
from . import views


urlpatterns = [
    path('user/',views.listData.as_view()),
    path('get/<int:pk>/',views.RetrieveData.as_view()),
    path('update/<int:pk>/',views.UpdateData.as_view()),
    path('delete/<int:pk>/',views.DeleteData.as_view()),

]
