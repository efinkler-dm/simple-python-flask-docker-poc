FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
