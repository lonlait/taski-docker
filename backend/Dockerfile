# Создать образ на основе базового слоя,
# который содержит файлы ОС и интерпретатор Python 3.12.
FROM python:3.12-slim

# вернуть distutils + собрать компилируемые пакеты, если нужны
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      python3-distutils \
      build-essential \
      libpq-dev \
 && rm -rf /var/lib/apt/lists/* 

# Переходим в образе в директорию /app: в ней будем хранить код проекта.
# Если директории с указанным именем нет, она будет создана.
# Название директории может быть любым.
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
WORKDIR /app
# Дальнейшие инструкции будут выполняться в директории /app

# Установить setuptools (включает distutils) и gunicorn
RUN pip install --upgrade pip setuptools gunicorn==23.0.0

# Скопировать с локального компьютера файл зависимостей
# в текущую директорию (текущая директория — это /app).
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Скопировать всё содержимое директории backend (manage.py, backend/, api/ и т.д.)
COPY . .

# Создать скрипт запуска
RUN echo '#!/bin/bash\npython manage.py migrate\npython manage.py collectstatic --noinput\nexec gunicorn --bind 0.0.0.0:8000 backend.wsgi:application' > /app/start.sh && chmod +x /app/start.sh

# При старте контейнера запустить скрипт запуска
CMD ["/app/start.sh"]