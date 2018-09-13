FROM python:3.6

WORKDIR /usr/src/app/

COPY Pipfile* manage.py ./
RUN pip install pipenv
RUN pipenv install --system --deploy

COPY cmsplugin_raw_html/ cmsplugin_raw_html/
COPY hallituspalaute/ hallituspalaute/
COPY gallery/ gallery/
COPY ilmo_app/ ilmo_app/
COPY sato/ sato/

CMD exec gunicorn sato.wsgi:application \
    --bind 0.0.0.0:8010 \
    --workers 3 \
    -t 120

EXPOSE 8010
