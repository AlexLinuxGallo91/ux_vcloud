from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import requests


class HtmlUtils:

    @staticmethod
    def get_http_code(url: str):
        resp = requests.get(url)
        return resp.status_code

    @staticmethod
    def wait_until_element_is_visible(selenium_web_driver: webdriver.Remote, css_locator: str,
                                      time_in_seconds: int, identificador):
        try:
            web_element = WebDriverWait(selenium_web_driver, time_in_seconds).until(
                EC.visibility_of_element_located((identificador, css_locator)))
            return web_element
        except TimeoutException:
            raise TimeoutException('Problema de carga en pagina en lapso de espera de {} segundos. No fue '
                                   'posible localizar el elemento {} mediante {}'.format(
                time_in_seconds, css_locator, identificador))
