import re
from collections import Counter
import json


def test_check_log(path_to_file):
    with open(path_to_file, "r") as log:
        try:
            info = log.readlines(), "\n"
            for row in info:
                get = re.findall('GET', str(row))
                post = re.findall('POST', str(row))
                times = re.findall('(.*?) "-"', str(row))
                err_clients = re.findall('4\d\d', str(row))
                err_serv = re.findall('5\d\d', str(row))
                sb = []
                for i in times:
                    if i == "":
                        continue
                    sa = str(i).split()
                    s = sb.append(sa[-1])
                ba = sorted(sb, reverse=True)
                break
        except OSError:
            print('Не возможно обработать файл!')
    print(ba)
    print(times)

    with open("..//homework7//analysts1.json", "w") as json_log:
        try:
            sum_request = [json.dumps(len(row), indent=4)]
            sum_get = [json.dumps(len(get), indent=4)]
            sum_post = [json.dumps(len(post), indent=4)]
            long_t = [json.dumps(ba[0:10], indent=4)]
            cl_e = [json.dumps(err_clients[0:10], indent=4)]
            sr_e = [json.dumps(err_serv[0:10], indent=4)]
            for request, get, post, l, ce, se in zip(sum_request, sum_get, sum_post, long_t, cl_e, sr_e):
                json_log.write(f'Общее количество выполненных запросов - {request}' + '\n')
                json_log.write(f'Количество запросов по типу: GET - {get}' + '\n')
                json_log.write(f'Количество запросов по типу: POST -  {post}' + '\n')
                json_log.write(f'топ 10 самых долгих запросов - {l}' + '\n')
                json_log.write(f'топ 10 запросов, которые завершились клиентской ошибкой - {ce}' + '\n')
            # #     f.write(f'топ 10 запросов, которые завершились ошибкой со стороны сервера - {se}' + '\n')
            #     for ip, count in Counter(row).most_common(10):
            #         i = 1
            #         json_log.write(f'{i} IP адрес - {ip} , сделаны запросов - {count}' + '\n')
            #         i += 1
        except OSError:
            print('Не открывается файл!')