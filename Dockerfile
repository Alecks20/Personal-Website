FROM python:3.11-alpine

LABEL org.opencontainers.image.source=https://github.com/alecks20/personal-website
LABEL org.opencontainers.image.description="A stable version of my personal website, what currntly I use on my production deployment"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["python3","app.py"]