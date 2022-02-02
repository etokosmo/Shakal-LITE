<h1 align="center">Игра Shakal LITE</h1>
<h3>В проекте присутвует функция random.sample с аргументом counts, который доступен только с Python v3.9. Просьба перед началом установить данную версию или более новую.<br>
Bootstrap подключен через CDN. Для отображения стилей необходимо подключение к Интернет.
</h3>

## Описание

<p>Приветсвую!</p>
<p>Предлагаю тебе ознакомиться с моим первым проектом на Python Flask. Это игра наподобие настольной игры "Шакал". Только более облегченная версия.</p>

## Основные правила игры

<img src="https://github.com/etokosmo/Shakal-LITE/blob/main/static/img/readme/rules.png" width="100%">
<p>Чтобы более подробно изучить правила данной игры, есть специальный раздел в меню под именованием "Rules"</p>

## Обозначение клеток

<img src="https://github.com/etokosmo/Shakal-LITE/blob/main/static/img/readme/cards.png" width="100%">

## Игра

<p>Чтобы начать игру необходимо нажать на раздел в меню Play. Выбрать количество игроков (от 1 до 4). По желанию ввести им имена. И начать играть.</p>
<img src="https://github.com/etokosmo/Shakal-LITE/blob/main/static/img/readme/game1.gif" width="100%">

## Технологии в проекте

<p>Цель проекта ознакомиться с основами фреймворка Flask на языке программирования Python. Также, обособленно ознакомиться с языком разметки HTML, каскадными таблицами стилей CSS и языком программирования JavaScript.</p>

### Задачи, поставленные перед началом проекта
------

<p><b> Создать логически законченный проект с использованием маршрутизации, шаблонов, статических файлов, возможностями Jinja и расширением Flask-WTF.</b></p>
<ul>
<li>Проект должен запускаться и не выдавать критических ошибок во время работы.</li>
<li>Должен присутствовать базовый шаблон, примененный к другим страницам.</li>
<li>В проекте необходимо применить css. Например Bootstrap 3.</li>
<li>В программе должно использоваться расширение Flask-WTF и присутствовать как минимум одна форма, наследуемая от класса FlaskForm. </li>
<li>Необходимо применить как минимум 4 различных поля (SubmitField принимаем за одно из полей).</li>
<li>Должно присутствовать как минимум 2 разных валидатора и их применение должно быть обосновано.</li>
<li>В проекте должно находиться как минимум две функции представления: должен быть как статический, так и динамический маршруты.</li>
<li>Одна из функций представления должна иметь возможность срабатывать на POST-запрос.</li>
<li>Код в проекте цельный и логически завершенный.</li>
</ul>

------

<p>В проекте присутвуют две формы, наследуемые от класса FlaskForm.</p>
<p>Первая - для выбора количества игроков, и задании им имен. Для имен сделаны два валидатора: DataRequired и Length(max=15). Первый отвечает за то, чтобы было введено имя. Второй - за длину имени, чтобы в будущем не слетала верстка из-за длинного имени.</p>
<p>Вторая - для отправки отзыва. Она состоит из имени, выборки браузера, почты, текста отзыва и оценки. Валидаторы: DataRequired - чтобы поле не оставалось пустым; Email - для проверки почты.</p>
<p>
Присутвуют 5 функций представления. Четыре из них могут работать с POST запросами. Также одна из пяти имеет динамический адрес, принимающий имя отправителя отзыва и его оценку. Переданные данные подставляются в HTML шаблон.

## Установка и настройка проекта

<p>Для просмотра проекта необходимо скачать проект. Создать виртуальную среду. Загрузить библиотеки из requirements.txt. Запустить файл app.py. Открыть локальный сервер в браузере.</p>

### Личные впечатления
------

<p>Для первого своего проекта было весьма сложновато разбираться в работе сервера, фремворке Flask и верстке HTML, CSS. Также для улучшения проекта необходимо было написать несколько функций на JavaScript. Но проделанной работой я вполне доволен. Буду рад любому ревью о данном проекте.</p>
<p>Спасибо за внимание!</p>
