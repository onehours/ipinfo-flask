FROM python:3.6


WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip3 config set install.trusted-host mirrors.aliyun.com
RUN pip install -r requirements.txt

COPY . /usr/src/app

EXPOSE 8000
CMD ["python", "app.py"]
