# ipinfo-flask
```
flask编写
IP地理位置查询
```

## 使用方式

### 1.直接python执行
```shell
pip install -r requirements.txt
python app.py
```

### 2.docker运行
```shell
docker build -t ipinfo-flask:1.1 .
docker run -d --name ipinfo -p 8000:8000 --restart=always ipinfo-flask:1.1
```


### 3.docker-compose运行
```shell
docker-compose -f docker-compose-build.yml up -d
```
