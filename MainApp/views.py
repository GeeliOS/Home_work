import json
from django.shortcuts import render, HttpResponse
from MainApp.models import Countrys, Languages
# TODO: нужно убрать чтение из файла, информация теперь в БД
with open('MainApp/sw_templates.json') as f:
    file_content = f.read()
    country_info = json.loads(file_content)

def home(request):

    return render(request, 'home.html')


def countries_list(request):


    country = Countrys.objects.all()
    context={
        "country_info":country
    }
    return render(request, 'countries-list.html', context)


def languages_list(request):
    # new_y = set()
    # for i in range(len(country_info)):
    #     for j in range(len(country_info[i]['languages'])):
    #         new_y.add(country_info[i]['languages'][j])
    language=Languages.objects.all()
    context={
        "country_info":language
    }
    return render(request, 'languages-list.html', context)


def countrie(request, name):
    # for countryin in country_info:
    #
    #     if countryin['country']==name:
    country = Countrys.objects.get(name=name)
    language=Countrys.objects.get(id=country.id).languages_id.all()
    context = {
    "country_info": country,
    "language_info": language
    }
    return render(request, 'countrie.html', context)

# context={
#     "countryin": countryin['country'],
#     "languages": ', '.join(countryin['languages'])
# }