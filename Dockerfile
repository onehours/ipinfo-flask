FROM python:3.6

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip3 config set install.trusted-host mirrors.aliyun.com
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "app.py", "0.0.0.0:8000"]
