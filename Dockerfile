# syntax=docker/dockerfile:1

FROM python:3.12-alpine

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Install gunicorn
RUN pip3 install gunicorn

# Command to run the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "Flask:app"]
