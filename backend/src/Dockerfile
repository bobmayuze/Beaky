FROM python:3.5-jessie

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -i https://pypi.doubanio.com/simple -r requirements.txt
COPY . /usr/src/app

EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]