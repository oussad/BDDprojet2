from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



@given("l'utlisateur ouvre le navigateur chrome")
def ouvrir_navigateur(context):

    print('le nom de la foction ouvrir le navigateur ')


@when("lors que l utlisateur ouvre l'application orange")
def lancer_orangeHRM(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    print('le nom de la foction lancer orange HRM')



@then("le logo s'affiché sur la page d accuille")
def valider_presence_logo(context):
    valeur=context.driver.find_element(By.XPATH,"(//img)[1]").is_displayed()
    assert valeur is False
    #assert valeur=='True'
    print('le nom de la foction valider presence logo ')
