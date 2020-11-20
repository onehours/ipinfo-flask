import requests


def taobaoip(ip):
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip='

    ret = requests.get(url=url + ip)
    if  not ret:
        return 'error !'
    return ret.json()

if __name__ == '__main__':

    print(taobaoip('223.5.5.5'))
