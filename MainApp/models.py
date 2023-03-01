from django.db import models


class Languages(models.Model):
   name = models.CharField(max_length=100)
   def __repr__(self):
      return f"Language: {self.id}"

class Countrys(models.Model):
   name  = models.CharField(max_length=100)
   languages_id = models.ManyToManyField(to=Languages)

   def __repr__(self):
      return f"Country: {self.id} | {self.languages_id}"

# ЯЗЫКИ ЗАПОЛНЕНИЕ ТАБЛИЦЫ
# class Languages(models.Model):
# import json
# with open('MainApp/sw_templates.json') as f:
#     file_content = f.read()
#     country_info = json.loads(file_content)
#     new_y = set()
#     for i in range(len(country_info)):
#         for j in range(len(country_info[i]['languages'])):
#              new_y.add(country_info[i]['languages'][j])
#
#     for country_in in new_y:
#       color=Languages(name=country_in)
#       color.save()



# СТРАНЫ ЗАПОЛНЕНИЕ ТАБЛИЦЫ
# class Countrys(models.Model):
# import json
# with open('MainApp/sw_templates.json') as f:
#     file_content = f.read()
#     country_info = json.loads(file_content)
# for i in range(len(country_info)):
#      color=Countrys(name=country_info[i]['country'])
#      color.save()




# МНОГИЕ КО МНОГИ ЗАПОЛНЕНИЕ ТАБЛИЦЫ
# import json
# from MainApp.models import Countrys
# with open('MainApp/sw_templates.json') as f:
#     file_content = f.read()
#     country_info = json.loads(file_content)
#
# for i in range(len(country_info)):
#     item1 = Countrys.objects.get(name=country_info[i]['country'])
#     country_id=Countrys(name=item1.id)
#     country_id = Countrys(name=item1.name)
#     for j in range(len(country_info[i]['languages'])):
#         item2 = Languages.objects.get(name=country_info[i]['languages'][j])
#         item1.languages_id.add(item2)