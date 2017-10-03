FROM python:3

WORKDIR /usr/src/app/

COPY requirements.txt.freeze .
RUN pip install --no-cache-dir -r requirements.txt.freeze

COPY . .

EXPOSE 8010
