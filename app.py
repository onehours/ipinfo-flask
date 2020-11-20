from lib.qqwry import qqwry
from lib.ip2region import ip2
from flask import Flask,request,jsonify,render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    print(request.environ)
    print(request.remote_addr)
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    if not ip:
        ip = '223.5.5.5'
    ip_dict = ip2.ip2region(ip)
    print(ip_dict)
    czip = qqwry.CzIp()
    ip_dict2 = czip.getip(ip)
    print(ip_dict2)
    if 'curl' in request.environ.get('HTTP_USER_AGENT'):
        msg = f"""IP	: {ip}
地址    : {ip_dict['country']} | {ip_dict['region']}| {ip_dict['city']}
运营商  : {ip_dict['isp']}
数据二  : {ip_dict2['city']} | {ip_dict2['isp']}
"""
    else:
        dic = {
            'ip': ip,
            'add': f"{ip_dict['country']} | {ip_dict['region']}| {ip_dict['city']}",
            'isp': ip_dict['isp'],
            'data2': f"{ip_dict2['city']} | {ip_dict2['isp']}"
        }
        return render_template('index.html',dic=dic)
    return msg

@app.route('/ip')
def getip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    if not ip:
        ip = '223.5.5.5'
    if ',' in ip:
        ip = ip.split(',')[0]

    ip_dict = ip2.ip2region(ip)
    czip = qqwry.CzIp()
    ip_dict2 = czip.getip(ip)
    msg = f"{ip}  {ip_dict2['city']}  {ip_dict2['isp']}"
    return msg


from werkzeug.routing import  BaseConverter
class RegexConverter(BaseConverter):
    def __init__(self,url_map,*items):
        super(RegexConverter,self).__init__(url_map)
        self.regex=items[0]
app.url_map.converters['regex'] = RegexConverter


# 匹配三位长度的字符串
@app.route('/<regex("(\d+.\d+.\d+.\d+)"):ip>')
def user(ip):
    if not ip:
        ip = '223.5.5.5'
    ip_dict = ip2.ip2region(ip)
    czip = qqwry.CzIp()
    ip_dict2 = czip.getip(ip)
    if 'curl' in request.environ.get('HTTP_USER_AGENT'):
        msg = f"""IP	: {ip}
地址    : {ip_dict['country']} | {ip_dict['region']}| {ip_dict['city']}
运营商  : {ip_dict['isp']}
数据二  : {ip_dict2['city']} | {ip_dict2['isp']}
"""
    else:
        dic = {
            'ip': ip,
            'add': f"{ip_dict['country']} | {ip_dict['region']}| {ip_dict['city']}",
            'isp': ip_dict['isp'],
            'data2': f"{ip_dict2['city']} | {ip_dict2['isp']}"
        }
        return render_template('index.html',dic=dic)
    return msg


@app.errorhandler(500)
def error500(e):
    return render_template('500.html'), 500


@app.errorhandler(404)
def error404(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000')



