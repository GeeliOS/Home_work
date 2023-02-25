import json
from django.shortcuts import render, HttpResponse
from MainApp.models import countrys

with open('MainApp/sw_templates.json') as f:
    file_content = f.read()
    country_info = json.loads(file_content)

def home(request):
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
    context={
        "country_info":country_info
    }
    return render(request, 'languages-list.html', context)

def countrie(request, name):
    for countryin in country_info:

        if countryin['country']==name:
            context = {
                "country_info": countryin
            }
    return render(request, 'countrie.html', context)

# context={
#     "countryin": countryin['country'],
#     "languages": ', '.join(countryin['languages'])
# }