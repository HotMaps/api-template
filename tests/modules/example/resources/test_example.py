import json
import requests
import os

# def test_example_post():
#     """
#     This is an example method on how to do unit test on your API, you need to execute this using py.test in order to work
#     It will query the app and compare it with an already existing JSON file located in payload.txt
#     """
#     # TODO: set up the URL of your localhost (specially the port)
#     url = "http://localhost:9005/api/v1/example/hello/world"
#
#     payload = "{\r\n  \"payload\": {\r\n    \"text\": \"This is a test\"\r\n  }\r\n}"
#     headers = {
#         'content-type': "application/json",
#         'cache-control': "no-cache",
#         'postman-token': "d188c7bd-5556-d8e0-33e2-f4c1d1abd817"
#     }
#
#     output = requests.request("POST", url, data=payload, headers=headers)
#
#     json_file = os.path.join(os.path.dirname(__file__), "payload.txt")
#
#     json_str = open(json_file).read()
#
#     expected_output = json.loads(json_str)
#
#     assert output.json() == expected_output

def get(lst, index, default=None):
    try:
        return lst[index]
    except IndexError:
        return default

import pytest

@pytest.yield_fixture()
def a_list():

    print('Before')

    yield ('apple', 'vanilla', 'chocolate')

    print ('after')

def test_get_element(a_list):
    element = get(a_list, 0, 'nothing')
    assert element == 'apple'

def test_get_element_missing(a_list):
    element = get(a_list, 1000, 'nothing')
    assert element == 'nothing'

def test_get_element_failure(a_list):
    element = get(a_list, 1000)
    assert element == 'This will not work'