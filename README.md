# Сайт музыкальной группы Sabaton
На информационном сайте представлено несколько разделов - общая информация о группе, участники и т.д.

![image](https://user-images.githubusercontent.com/78861235/187300378-3ad36733-34e5-4d6b-8d77-b9dcec36fcdf.png)

Для того, чтобы запустить сайт на своем компьютере, необходимо выполнить следующие команды (в примере командная строка Windows 10):
```C:\...\> git clone https://github.com/musicgroup/sabaton
C:\...\> cd sabaton
C:\...\> python -m venv venv
C:\...\> venv\Scripts\activate
C:\...\> pip install -r requirments.txt
```
И сам запуск:

```C:\...\> python manage.py runserver```