NAME   := osakunta/django-sivusto
TAG    := $$(git log -1 --pretty=%h)
IMG    := ${NAME}:${TAG}
LATEST := ${NAME}:latest

build:
	docker build -t ${IMG} .
	docker tag ${IMG} ${LATEST}

test:
	docker run ${NAME} /bin/sh -c "python manage.py test"

push:
	docker push ${NAME}

login:
	echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin

populate:
	cat ~/django_database_backup.sql | docker exec -i django-sivusto-db psql -U postgres -d postgres
