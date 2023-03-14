import allure
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context,driver):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)
def after_scenario(context,driver):
    context.driver.quit()

def after_step(context,step):
    if step.status=="failed":
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',attachment_type=allure.attachment_type.PNG)







#behave -f allure_behave.formatter:AllureFormatter -o allure_rapports features gener des rapport allure
#behave -f allure_behave.formatter:AllureFormatter -o allure_rapports features --tags=smoke

#$ allure  serve allure_rapports converir les ficheir json en html
