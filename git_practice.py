
"""
1. Что такое система контроля версий

Это система, записывающая изменения в файл
или набор файлов в течение времени

Позволяет вернуть к состоянию до изменения
также вернуть проект к исходному состоянию
увидеть изменения и кто последний внес изменения

    Существует три вида систем контроля версий:

1. Локальные

представляют систему с простой базой данных
которые хранит записи о всех изменениях в файлах
осуществляя тем самым контроль ревизий

2. Централизованные



3. Распределенные

не просто скачивают, а полностью копируют
и каждая копия репозиторий является полным бэкапом всех данных

"""

###

"""
2. Что такое git и какова его работа

Git - это распрделенная система контроля версий,
записывающая изменения в файл или набор
файлов в течение времени и позволяющая вернуться
позже к определенной версии

    У Git есть три основных состояния,
в которых могут находиться файлы:

1. Зафиксированное(committed)

Файл уже сохранен в вашей локальной базе

2. Измененное (modified)

Это файлы, которые поменялись, но еще не были зафиксированы

3. Подготовленное (staged)

Это измененные файлы, отмеченные для включения в следующий коммит

"""

###

"""
3. 3 состояния git

Git Директория - Гит хранит метаданные и базу объектов проекта

Рабочая директория - Снимок версии проекта

Область подготовленных файлов

"""

###

"""
4. Отличие git от github

git - это система управления версиями

Github - это онлайн сервис

"""

# git commands

# git init  -> .git
# -> отвечает за инициализацию и при вызове создается папка

# git remote add name url 
# -> добавляет удаленный репозиторий, к-й находится на каком-нибудь сервере(github)

# git pull -> стягиваем изменения с какой-либо ветки
# git pull origin master  -> хочу стянуть все изменения с ветки мастера

# git status -> показывают статус файлов проекта
# -> то есть какие файлы у нас изменены, не добавлены, какие ожидают коммита

# git add -> добавляет файлы в рабочей папке в индекс для дальнейшего коммита
# git add name file 
# git add . -> добавит все файлы которые были изменены в индекс

# git commit -> добавляет все файлы которые находятся в индексе 
# и сохраняет их состояние на данный момент 
# git commit -m "comment" -> комментарий обязательно должен описывать коммит

# git branch -> можно посмотреть список веток и выбрать необходимую ветку

# git branch name branch -> можно создать новую ветку с name branch

# git checkout name branch  -> переход на другую ветку

# git push name branch -> отвечает за отправку в удаленный репозиторий
# git push origin master -> то, что будем чаще использовать

# git reset filename -> удаляет файл с таким именем из индекса

