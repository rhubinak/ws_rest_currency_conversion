FROM python:3
ADD *.py /
ADD Pipfile /
ADD Pipfile.lock /
RUN pip install pipenv
RUN pipenv install
CMD [ "redis" ]
CMD [ "pipenv", "run", "./celery.py" ]
CMD [ "pipenv", "run", "./main.py" ]
