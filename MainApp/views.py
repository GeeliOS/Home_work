import json
from django.shortcuts import render, HttpResponse
from MainApp.models import Countrys, Languages
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
    language=Languages.objects.all()
    context={
        "country_info":language
    }
    return render(request, 'languages-list.html', context)


def countrie(request, name):
    country = Countrys.objects.get(name=name)
    language=Countrys.objects.get(id=country.id).languages_id.all()
    context = {
    "country_info": country,
    "language_info": language
    }
    return render(request, 'countrie.html', context)




def language_countrys(request, name):
    languages = Languages.objects.get(name=name)
    country = Countrys.objects.filter(languages_id__name=languages.name)
    context = {
    "country_info": country,
    "language_info": languages
    }
    return render(request, 'language_countrys.html', context)


