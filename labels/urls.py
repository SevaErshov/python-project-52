from django.urls import path
from labels import views as lv


urlpatterns = [
    path('', lv.LabelsList.as_view()),
    path('create/', lv.LabelCreate.as_view()),
    path('<int:pk>/update/', lv.LabelUpdate.as_view(), name='labels_upd'),
    path('<int:pk>/delete/', lv.LabelDelete.as_view(), name='labels_dlt'),
]