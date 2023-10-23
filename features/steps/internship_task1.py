from behave import given, when, then
from time import sleep

@given('Open the main page')
def open_main(context):
    context.app.login_page.open_main()

@then('Log in to the page')
def login(context):
    context.app.login_page.login()


@then('Change the language of the page to Russian')
def change_languange(context):
    sleep(5)
    context.app.home_page.change_lang()


@then ('Verify the language has changed')
def verify_lang(context):
    context.app.home_page.verify_lang()
