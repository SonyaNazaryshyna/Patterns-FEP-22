FROM python:3.12-slim as build
LABEL authors="yurti"

WORKDIR /app
COPY ./nba/requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./
FROM build as final
WORKDIR /app/nba
ENV DJANGO_SETTINGS_MODULE=web.settings
EXPOSE 8081
CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]
