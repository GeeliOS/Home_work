import json
from django.shortcuts import render, HttpResponse

# TODO: использование абсолютных путей недопустимо, используйте пути относительно корня проекта
with open('/home/student/Projets/DjangoCountries/MainApp/sw_templates.json') as f:
    file_content = f.read()
    country_info = json.loads(file_content)

# TODO: директория виртуального окружения(venv) не должна быть часть git проекта.
#  Исправите файл .gitignore и удалите виртуальное окружение из под репозитория

def about(request):
    result = f"""
  <center> <a  href='/countries-list'>Страны</a><br>
   <a  href='/languages-list'>Языки</a></center>
    """
    return HttpResponse(result)

def countries_list(request):
    context={
        "country_info":country_info
    }
    return render(request, 'countries-list.html', context)


def languages_list(request):
    # TODO: тут вам нужно создать список языков, исключив дубликаты и передать в шаблон. А в шаблоне отобразить языки
    context={
        "country_info":country_info
    }
    return render(request, 'languages-list.html', context)

def countrie(request, name):
    for countryin in country_info:
        if countryin['country']==name:
            context={
                "countryin":countryin
            }
    return render(request, 'countrie.html', context)