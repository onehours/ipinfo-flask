import requests


def ipip(ip):
    url = 'http://freeapi.ipip.net/'

    ret = requests.get(url=url + ip)
    if not ret:
        return 'error !'
    return ret.json()


if __name__ == '__main__':
    print(' '.join(ipip('223.5.5.5')))
