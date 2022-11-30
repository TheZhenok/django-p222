from django.shortcuts import (
    render,
    HttpResponse,
)
from django.http.request import HttpRequest


def index(request):
    print(request.__dir__())
    return HttpResponse("""
        <form action="/user/create/" method="POST">
            <input type="text" name="login" id="login" placeholder="Login">
            <input type="password" name="password" id="password" placeholder="Password">
            <input type="submit" value="Enter">
        </form>
    """)

def create_user(request: HttpRequest):
    if request.method == "POST":
        print(request.POST.get("login"))
        print(request.POST.get("password"))
        return HttpResponse("Hello {}. Welcome to site".format(
            request.POST.get("login")
        ))

    return HttpResponse("This endpoint only POST method")


# Вводит номер квартиры, пароль, повторите пароль
# Если пароли не совпадают, то выходит красная ошибка "НЕ ВЕРНЫЙ ЛОГИН И БЛА-БЛА-БЛА. Попробуйте
# БЛА-БЛА-БЛА"
# Если же вверно, то мы покажем, на каком этаже он живёт. На одном этаже может быть 4
# квартиры, где нумерация начианатся с 1
