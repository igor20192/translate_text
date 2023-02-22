## Консольный переводчик
#### Монтаж приложения.
Клонировать репозиторий

    git clone https://github.com/igor20192/translate_text.git

    cd translate_text
Создать Создать виртуальное окружение
    
    python3 -m venv venv_translate

Активировать виртуальное окружение
    
    . venv_translate/bin/activate

Установить зависимости
    
    pip install -r requirements.txt

Текст для перевода поместить в файл input.txt
В терминале запустить команду
    
    python text_translate.py -tr  ru y

Первый аргумент 'ru' язык перевода
Возможные варианты смотреть здесь https://pypi.org/project/pygoogletranslation/
Второй аргумент 'y' необязательный, используется для очистки текста перед переводом
В консоли открывается редактор vim c переведенным текстом 
Переведенный текст находиться в файле translate.txt