from behave import given, when, then
from pages.wikipedia_page import WikipediaPage

@given('el usuario está en la página principal de Wikipedia')
def step_impl(context):
    context.page = WikipediaPage(context.driver)
    context.page.open()

@when('busca "{term}"')
def step_impl(context, term):
    context.page.search(term)

@then('el título del artículo debe ser "{expected_title}"')
def step_impl(context, expected_title):
    actual_title = context.page.get_article_title()
    assert actual_title == expected_title, f"Expected title '{expected_title}' but got '{actual_title}'"
