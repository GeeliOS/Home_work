# Инструкция по развертыванию проекта

1. `python3 -m venv venv_name` - создание venv
2. `source venv_name/bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py runserver`

## Запуск терминала в контексте django

`python manage.py shell_plus --ipython`

-----------------
#Обязательное ДЗ: “Django Countries”

##Вступление
Для закрепления изученной информации рекомендуется самостоятельно пройти весь путь, от создания проекта, до отображения HTML в браузере, самостоятельно.

##Задания
##Выполнять после: <span style="color:red">Модуль-1</span>

- [x] <span style="color:blue">1.</span> Создайте новый проект **DjangoCountries**. 
<em>Создайте новое виртуальное окружение(venv), установите в него Django.</em>
**Рекомендация**: выполните все действия используя терминал Linux.
- [x] <span style="color:blue">2.</span> Главная страница должна быть доступна по корневому url’у.
На ней разместите произвольное приветствие c минимальным HTML оформлением.
- [x] <span style="color:blue">3.</span> Запустите проект и проверьте отображение главной страницы.
- [x] <span style="color:blue">4.</span> Загрузите ваш проект на GitHub
**Важно**: не забудьте в проект добавить .gitignore. Виртуальное окружение и настройки вашей IDE не должны быть частью репозитория.

##Выполнять после: <span style="color:red">Модуль-2</span>
- [x] <span style="color:blue">5.</span> Оформите главную страницу в виде полноценного html-документа
- [x] <span style="color:blue">6.</span> Список с данными для стран возьмите <a name="https://github.com/samayo/country-json/blob/master/src/country-by-languages.json">тут.</a>
**Примечание**: пока мы работаем без БД, скопируйте данные о странах в файл (разместите файл в корне проекта).
 Для получение информации из файла используйте <a name="https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html">работу с файлами в Python</a>, <a name="https://pyneng.readthedocs.io/ru/latest/book/17_serialization/json.html">работа с json-1</a> и <a name="https://dvmn.org/encyclopedia/modules/json/">работа с json-2</a>.
- [x] <span style="color:blue">7.</span> По url: **/countries-list/** отобразите нумерованный список всех стран, отобразив в списке только названия стран.
- [x] <span style="color:blue">8.</span> Название каждой страны сделайте гиперссылкой, которая ведет на персональную страницу данной страны. 
На персональной странице страны отобразите ее название(в виде заголовка) и список всех языков, на которых говорят в данной стране.
- [x] <span style="color:blue">9.</span> На главной странице добавьте еще одну ссылку “Языки”. По ссылке отобразите страницу со списком всех языков на котором говорят во всех странах.

##Выполнять после: <span style="color:red">Модуль-3</span>
- [x] <span style="color:blue">10.</span> Создайте модель-класс Country.
- [x] <span style="color:blue">11.</span> Перенесите все страны из <a name="https://github.com/samayo/country-json/blob/master/src/country-by-languages.json">исходного json</a> файла в базу данных(БД).
- [x] <span style="color:blue">12.</span> Измените работу вашего приложения на работу с БД
- [x] <span style="color:blue">13.</span> Выгрузите данные из БД в фикстуру(fixture) **countries.json**

##Выполнять после: <span style="color:red">Модуль-4</span>
- [x] <span style="color:blue">14.</span> Используя информацию с занятия, измените структуру БД, реализовав связь “многие-ко-многом” для стран и языков.
<em>Не забудьте</em>: выгрузить обновленные данные из БД fixture: **countries.json**
- [x] <span style="color:blue">15.</span> Добавьте в проект файл requirements.txt
- [x] <span style="color:blue">16.</span> Добавьте в проект файл README.md, добавив в него:
  - Информацию о запуске проекта после клонирования
  - Список всех заданий, пометив выполненные

##Выполнять после: <span style="color:red">Модуль-5</span>
**Примечание**: Модуль-5 “работа с формами”, в рамках проекта “Django Countries” мы не будем использовать формы, поэтому задания с формами не связаны.


- [ ] <span style="color:blue">17.</span> На главной странице добавьте еще одну ссылку “Языки”. По ссылке отобразите страницу со списком всех языков на котором говорят во всех странах.
- [ ] <span>18.</span> Все языки в списке сделайте гиперссылками, каждая ведет на отдельную страницу, на которой отображаются страны, которые говорят на выбранном языке.
##Выполнять после: <span style="color:red">Модуль-7(финальные задания)
- [ ] <span>19.</span> На верху страницы со списком стран добавьте алфавит, каждая буква которого является гиперссылкой. Каждая гиперссылка(на букве) ведет на страницу на которой отображаются только страны на выбранную букву. См. аналогию <a name="https://www.worldometers.info/geography/alphabetical-list-of-countries/">тут</a>.
- [ ] <span>20.</span> Внизу страницы со списком стран реализуйте <a name="https://blog.calltouch.ru/chto-takoe-paginatsiya/">пагинацию</a>. На каждой странице отобразите 10 стран.

Отправьте проект мне на почту: <a name="eyurchenko@specialist.ru">eyurchenko@specialist.ru</a> (ссылку на GitHub)

**Важно!** Для получения зачета по курсу, необходимо выполнить **все** задания <span style="color:blue">**выделенные синим цветом**</span>. Остальные задания - опциональные.