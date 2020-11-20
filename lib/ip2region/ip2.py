from lib.ip2region.ip2Region import Ip2Region
import os

dbFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ip2region.db')


def ip2region(line):
    searcher = Ip2Region(dbFile)
    algorithm = 'memory'

    line = line.strip()

    if line == "":
        print("[Error]: Invalid ip address.")

    if line == "quit":
        print("[Info]: Thanks for your use, Bye.")

    if not searcher.isip(line):
        print("[Error]: Invalid ip address.")

    try:

        if algorithm == "binary":
            data = searcher.binarySearch(line)
        elif algorithm == "memory":
            data = searcher.memorySearch(line)
        else:
            data = searcher.btreeSearch(line)
        # print("%s|%s in %5f millseconds" % (data["city_id"], data["region"].decode('utf-8')))
    except Exception as e:
        print("[Error]: %s" % e)

    searcher.close()

    data_list = data['region'].decode('utf-8').split('|')

    country = data_list[0]

    if data_list[3] == '0' :
        region = data_list[2]
        city = None
        isp = None
    else:
        region = data_list[2]
        city = data_list[3]
        isp = data_list[4]

    data_dict = {
        'country':country,
        'region':region,
        'city':city,
        'isp':isp
    }

    return data_dict


if __name__ == '__main__':
    # print(ip2region('107.182.21.166'))
    # print(ip2region('39.106.4.32'))
    testip = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'iplist.txt')
    with open(testip) as f:
        for i in f:
            print(ip2region(i))

