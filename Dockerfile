FROM python:3.7

WORKDIR /app

COPY Pip* /app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --deploy --system

COPY . /app/

EXPOSE 6000

CMD ["python", "routes.py"]