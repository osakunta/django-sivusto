FROM python:3

WORKDIR /usr/src/app/

COPY Pipfile.lock .
RUN pip install pipenv
RUN pipenv install

COPY . .

EXPOSE 8010
