# Write your solution here
import urllib.request
import json
from math import floor

def retrieve_all():
    link =  "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    my_request = urllib.request.urlopen(link)
    course_list = json.loads(my_request.read())
    active_course = []

    for course in course_list:
        if course["enabled"] == True:
            active_course.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))

    return active_course

def retrieve_course(course_name: str):
    link = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    my_request = urllib.request.urlopen(link)
    course_info = json.loads(my_request.read())
    course_details = {}

    max_student = 0
    total_hour = 0
    exercises = 0

    for weeks, value in course_info.items():
        nbr_student = value["students"]
        total_hour += value["hour_total"]
        if nbr_student > max_student:
            max_student = nbr_student
        exercises += value['exercise_total']
    hours_average = floor(total_hour/max_student)
    exercises_average = floor(exercises/max_student)

    course_details["students"] = max_student
    course_details["weeks"] = len(course_info)
    course_details["hours"] = total_hour
    course_details["hours_average"] = hours_average 
    course_details["exercises"] = exercises 
    course_details["exercises_average"] = exercises_average 

    return course_details

if __name__ == "__main__":
    active_course = retrieve_all()
    single_course_info = retrieve_course("docker2019")
    print(single_course_info)