from django.contrib import admin
from django.urls import path

from main.views import (
    index,
    create_user,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('user/create/', create_user)
]


# 2 эндпоинта
# 1) /index/home -> возвращает ваше имя КРАСНОГО ЦВЕТА
# 2) /cals -> возвращает ссылку на 1-ю старницу
