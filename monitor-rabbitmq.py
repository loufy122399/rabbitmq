#!/usr/bin/env python
import subprocess

running_list = []
error_list = []
false = "false"
true = "true"


def get_status():
    obj = subprocess.Popen(("curl -s -u guest:guest  http://localhost:15672/api/nodes &> /dev/null"), shell=True,
                           stdout=subprocess.PIPE)
    data = obj.stdout.read()
    data1 = eval(data)
    #print(data1)
    for i in data1:
        if i.get("running") == "true":
            running_list.append(i.get("name"))
        else:
            error_list.append(i.get("name"))


def count_server():
    if len(running_list) < 3:  # 可以判断错误列表大于0或者运行列表小于3，3未总计的节点数量
        print(100)  # 100就是集群内有节点运行不正常了
    else:
        print(50)  # 50为所有节点全部运行正常


def main():
    get_status()
    count_server()


if __name__ == "__main__":
    main()
