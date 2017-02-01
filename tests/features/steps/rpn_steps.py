from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox()


@given(u'I have entered "{expression}"')
def step_impl(context, expression):
    driver.get("http://csd-team.co.in:8000/calculate/")
    elem = driver.find_element_by_name("expression")
    elem.send_keys(expression)


@when(u'click on "Evaluate"')
def step_impl(context):
    elem = driver.find_element_by_name("evaluate")
    elem.click()

@then(u'System display message "{result}"')
def step_impl(context, result):
    try:
        element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "result")))
        actual_result = element.get_attribute("value")
        assert result == actual_result
    except Exception:
        assert False
    finally:
        driver.close()
