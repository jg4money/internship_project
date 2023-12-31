from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from support.logger import logger
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def browser_init(context):
    """
    :param context: Behave context
    """

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service) #- comment out for mobile emulation

    ##MOBILE EMULATION##
    # mobile_emulation = {
    #     "deviceName": "iPhone 12 Pro"
    #  }
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)

    ### OTHER BROWSERS
    # service = Service(executable_path= "/Users/jacobgrable/QA/python-selenium-automation/geckodriver")
    # context.driver = webdriver.Firefox(service=service)
    # context.driver = webdriver.Safari()

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'jacobgrable_02vm1G'
    # bs_key = 'qcMffBqrPwXHx1H7JwoH'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    # 'os': 'Windows',
    # 'osVersion': '11',
    # 'browserName': 'Chrome',
    # 'sessionName': 'Reelly.io'
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1920,1080")
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(
    # options=options,
    # service=service
    # )

    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)
    logger.info(f'\nStarted scenario: {scenario.name}')


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')

    def after_scenario(context, feature):
        context.driver.delete_all_cookies()
        context.driver.quit()
