FROM python:3.9.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /BE-assignment
WORKDIR /BE-assignment
COPY . /BE-assignment/
RUN pip install -r requirements.txt