from django.urls import path
from tasks import views as tv


urlpatterns = [
    path('', tv.TasksList.as_view()),
    path('create/', tv.CreateTask.as_view()),
    path('<int:pk>/update/', tv.EditTask.as_view(), name='tasks_upd'),
    path('<int:pk>/delete/', tv.RemoveTask.as_view(), name='tasks_dlt'),
    path('<int:pk>/', tv.TaskPage.as_view(), name='tasks_get'),
]