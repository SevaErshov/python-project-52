from django.urls import path
from users import views as uv


urlpatterns = [
    path('', uv.UsersPage.as_view()),
    path('create/', uv.Create.as_view()),
    path('<int:pk>/update/', uv.EditUser.as_view(), name='users_upd'),
    path('<int:pk>/delete/', uv.RemoveUser.as_view(), name='users_dlt')
]
