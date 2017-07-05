FROM python:3

WORKDIR /usr/src/app/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD . .

EXPOSE 8010

CMD ["python", "manage.py", "runserver", "0.0.0.0:8010"]
