from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



@given('ouvrir  application orange sur chrome')
def ouvrir_navigateur(context):

    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
@When('saisir le nom utlisateur "{user}" et mot de passe "{password}"')
def saisir_user_pass(context,user,password):
    context.driver.find_element(By.NAME,"username").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(password)

@When('cliquer sur le botoun login')
def cliquer_botoun(context):
    context.driver.find_element(By.XPATH, "//button").click()

@Then('valider que le message d erreur s affiche')
def saisir_user_pass(context):
    text_erreur=context.driver.find_element(By.XPATH,"//p[text()='Invalid credentials']").text
    assert text_erreur=='Invalid credentials'

@then('valider que le mode deashbord s affiche sur l accuille')
def valider_deashbord(context):
    text_deashbord=context.driver.find_element(By.XPATH, "//h6").text
    assert text_deashbord=='Dashboard'

