import pytest
import allure
import requests
import allure_engine as engine


@allure.title("title")
@allure.label("owner")
@allure.tag("tag")
@allure.description("description")
@allure.testcase("TMS-456")
@allure.issue("AUTH-123")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://jsonplaceholder.typicode.com/posts", name="name")
def test_assert():
    assert engine.discount(100, 50) == 50.0

@allure.title("title")
@allure.label("owner")
@allure.tag("tag")
@allure.description("description")
@allure.testcase("TMS-456")
@allure.issue("AUTH-123")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://jsonplaceholder.typicode.com/posts", name="name")
def test_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200

@allure.title("title")
@allure.label("owner")
@allure.tag("tag")
@allure.description("description")
@allure.testcase("TMS-456")
@allure.issue("AUTH-123")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://jsonplaceholder.typicode.com/posts", name="name")
def test_post_length():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert len(response.json()) == 100
    

