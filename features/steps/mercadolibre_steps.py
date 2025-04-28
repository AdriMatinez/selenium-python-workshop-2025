from behave import given, when, then
from selenium import webdriver
from pages.mercadolibre_page import SearchPage

@given('el usuario se encuentra en la pagina mercado libre')
def step_given_mercadolibre(context):  
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.mercadolibre.com.co/")
    context.mercadolibre_page = SearchPage(context.driver)

@when('el usuario escribe el nombre del producto')

def step_when_user_search_product(context):
    context.mercadolibre_page.search_product("Iphone 13")

    
    
@then('visualiza las coincidencias del producto')
def step_then_user_see_product(context):
  assert "Iphone 13" in context.driver.title

    
