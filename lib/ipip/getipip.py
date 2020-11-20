# https://github.com/ipipdotnet/ipdb-python
from __future__ import unicode_literals
import ipdb
import os
import time

db_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ipipfree.ipdb')


def get_city(ip):
    db = ipdb.City(db_dir)
    # 是否支持ipv4,ipv6
    # print(db.is_ipv4(), db.is_ipv6())
    # 查看构建时间
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(db.build_time())))
    # print(db.languages())
    # print(db.fields())
    # print(db.build_time())
    # print(db.find(ip, "CN"))
    # print(db.find_map(ip, "CN"))
    # print(db.find_info(ip, 'CN').country_name)
    # print(db.find_info(ip, "CN").city_name)

    data_list = db.find(ip, "CN")

    country = data_list[0]

    if data_list[2] == '':
        region = data_list[1]
        city = None
        isp = None
    else:
        region = data_list[1]
        city = data_list[2]
        isp = None

    data_dict = {
        'country':country,
        'region':region,
        'city':city,
        'isp':isp
    }

    return data_dict


if __name__ == '__main__':
    print(get_city('103.214.85.217'))
    print(get_city('107.182.21.166'))
    testip = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'iplist.txt')
    with open(testip) as f:
        for i in f:
            print(get_city(i.strip()))
