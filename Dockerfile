# Базовый образ
FROM python:3-slim

# Установка зависимостей
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Копирование файлов проекта
COPY backend /django_app
WORKDIR /django_app

# Не позволяет Python генерировать файлы .pyc в контейнере
ENV PYTHONDONTWRITEBYTECODE=1

# Отключает буферизацию для упрощения ведения журнала контейнера
ENV PYTHONUNBUFFERED=1

# Открытие порта
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]