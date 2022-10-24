FROM  svizor/zoomcamp-model:3.9.12-slim

# RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile","Pipfile.lock", "./"]

# RUN pipenv lock
# RUN pipenv install --system --deploy  --ignore-pipfile
# RUN pipenv install --deploy  --ignore-pipfile
RUN pipenv install --system --deploy

COPY ["docker_predict_credit.py", "./"]

EXPOSE 9000
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9000", "docker_predict_credit:app" ]