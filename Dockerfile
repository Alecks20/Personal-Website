FROM python:3.11-alpine

LABEL org.opencontainers.image.source=https://github.com/alecks20/personal-website
LABEL org.opencontainers.image.description="A stable version of my personal website, what I currently use on my production deployment"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:80 --chdir=./"
COPY . .

EXPOSE 80

CMD ["gunicorn","app:app"]