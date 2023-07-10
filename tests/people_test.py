import requests
from assertpy.assertpy import assert_that

BASE_URI = 'http://0.0.0.0:5000/api/ui/#/'


def test_read_all_has_kent():
    # User requests.get() with url to make a get request
    response = requests.get(BASE_URI)

    # Response from requests has many userful properties
    # we can assert on the response status code
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

    # We can get python dictionaries as response by using .json() method
    response_text = response.json()
    first_name = [people['fname'] for people in response_text]
    assert_that(first_name).contains('Kent')
