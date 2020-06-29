FROM python:alpine
WORKDIR /
ADD *.py /
ADD Pipfile /
ADD Pipfile.lock /
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install pipenv celery[redis] requests
RUN pipenv install
CMD pipenv run python main.py
