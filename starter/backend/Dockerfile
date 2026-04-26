FROM public.ecr.aws/docker/library/python:3.10-slim
ENV FLASK_RUN_HOST=0.0.0.0
WORKDIR /app

RUN apt-get update && apt-get install -y \
  gcc \
  libpcre3 \
  libpcre3-dev \
  && pip install pipenv \
  && rm -rf /var/lib/apt/lists/*

COPY Pipfile* /app/
RUN pipenv install --system --skip-lock

COPY . /app

CMD ["python", "-m", "flask", "--app", ".", "run", "--host=0.0.0.0", "--port=5000"]