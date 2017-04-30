import json
import os
from random import randint

home = os.path.expanduser("~")
CONFIG_FILE_PATH = home + '/.exercise_generator/config.json'
KEY_NAME = 'name'
KEY_EXERCISES = 'exercises'


def read_json(file_path):
    with open(file_path) as json_file:
        json_object = json.load(json_file)
        return json_object


def handle_num(num, prefix_str):
    rand_int = randint(1, num)
    prefix_str += str(rand_int)
    return prefix_str


def handle_list(lizt, prefix_str):
    rand_int = randint(1, len(lizt))
    ele = lizt[rand_int - 1]
    if isinstance(ele, dict):
        return handle_dict(ele, prefix_str)
    elif isinstance(ele, int):
        prefix_str += '{}, '.format(rand_int)
        return handle_num(ele, prefix_str)
    else:
        assert False


def handle_int(num, prefix_str):
    rand_num = randint(1, num)
    prefix_str += str(rand_num)
    return prefix_str


def handle_dict(dictionary, prefix_str=''):
    if KEY_NAME in dictionary:
        prefix_str += '{}, '.format(dictionary[KEY_NAME].encode('utf-8'))
    exercises_value = dictionary[KEY_EXERCISES]
    if isinstance(exercises_value, list):
        return handle_list(exercises_value, prefix_str)
    elif isinstance(exercises_value, int):
        return handle_int(exercises_value, prefix_str)
    else:
        assert False


def test():
    json_object = read_json(CONFIG_FILE_PATH)
    result = handle_dict(json_object)
    print result


if __name__ == '__main__':
    test()
