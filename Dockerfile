FROM python:3.7

WORKDIR /app

COPY Pipfile* ./

RUN pip install pipenv && \
    pipenv install --system --deploy

COPY . .

CMD exec gunicorn sato.wsgi:application \
    --bind 0.0.0.0:8010 \
    --workers 3 \
    -t 120

EXPOSE 8010
