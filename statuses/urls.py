from django.urls import path
from statuses import views as sv


urlpatterns = [
    path('', sv.StatusesList.as_view()),
    path('create/', sv.StatuseCreate.as_view()),
    path('<int:pk>/update/', sv.StatuseUpdate.as_view(), name='statuses_upd'),
    path('<int:pk>/delete/', sv.StatuseDelete.as_view(), name='statuses_dlt'),
]