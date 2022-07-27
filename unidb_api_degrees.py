import requests
import json
from pprint import pprint as pp

degrees = ['Archaeology', 'Architecture', 'Art', 'Business', 'Chemistry', 'Engineering', 'History', 'Computer Science',
           'Creative Writing', 'Criminology', 'Dentistry', 'Drama', 'Dance', 'Economics', 'Education', 'Electrical Engineering',
           'Biology', 'Mathematics', 'English', 'French'] # to be completed, https://www.britishuni.com/subject-guide/subject-list

valid_degrees = []

def degree_endpoint(degree):
    endpoint = "https://unidbapi.com/api/degree/read_demographics?d={}&key=56d0b15602".format(degree)
    return endpoint


def get_valid_degrees():
    for degree in degrees:
        response = requests.get(degree_endpoint(degree))
        if json.dumps(response.json()) != "{\"error\": \"Invalid Query\"}":
            valid_degrees.append(degree)


if __name__ == "__main__":
    get_valid_degrees()
    for degree in valid_degrees:
        endpoint = "https://unidbapi.com/api/degree/read_demographics?d={}&key=56d0b15602".format(degree)

        response = requests.get(endpoint)
        pp(response.json())
