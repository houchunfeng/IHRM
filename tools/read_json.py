"""读取数据方法"""
import json

from config import BASE_DIR


def read_login(filename):
    """读取登录的json数据"""
    with open(BASE_DIR+"/data/" + filename, "r") as f:
        test_data = []
        for data in json.load(f).values():
            test_data.append(tuple(data.values()))
        return test_data

if __name__ == '__main__':
    print(read_login("login.json"))