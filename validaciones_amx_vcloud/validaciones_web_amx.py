import time

from selenium import webdriver
from validaciones_amx_vcloud import constantes
from config_parameters import config_parameters_constants
from html_utils.html_utils import HtmlUtils
from html_utils.timer import Timer
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException


class ValidacionesWebAmx:

    @staticmethod
    def validation_enter_principal_page(web_driver: webdriver.Remote, json_result: dict):
        http_code = 0
        message_error = ''
        error_detected = 0

        Timer.start_time()
        try:
            http_code = HtmlUtils.get_http_code(config_parameters_constants.URL_PAGINA_PRINCIPAL_VCLOUD)
            web_driver.get(config_parameters_constants.URL_PAGINA_PRINCIPAL_VCLOUD)

            HtmlUtils.wait_until_element_is_visible(
                web_driver, 'usernameInput', config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML, By.ID)
        except WebDriverException as e:
            message_error = e.msg
            error_detected = 1
        except NoSuchElementException as e:
            message_error = e.msg
            error_detected = 1
        except TimeoutException as e:
            message_error = e.msg
            error_detected = 1

        Timer.stop_time()

        json_result[constantes.JSON_INGRESO_PAGINA_STATUS_VALIDACION] = error_detected
        json_result[constantes.JSON_INGRESO_PAGINA_MSG_ERROR] = message_error
        json_result[constantes.JSON_INGRESO_PAGINA_HTTP_CODE] = http_code
        json_result[constantes.JSON_INGRESO_PAGINA_TIEMPO_TOTAL_SEG] = Timer.get_time_in_seconds_float()

        return json_result

    @staticmethod
    def validation_login_session_vcloud(web_driver: webdriver.Remote, json_result: dict):
        message_error = ''
        error_detected = 0

        Timer.start_time()

        try:
            # busca el input del username y se establece
            input_login = HtmlUtils.wait_until_element_is_visible(
                web_driver, "usernameInput", config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML, By.ID)
            input_login.send_keys(config_parameters_constants.USERNAME)

            # busca el input del password y se establece
            input_password = HtmlUtils.wait_until_element_is_visible(
                web_driver, "passwordInput", config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML, By.ID)
            input_password.send_keys(config_parameters_constants.PASSWORD)

            # se da clic en el boton de inicio de sesion
            btn_login = HtmlUtils.wait_until_element_is_visible(
                web_driver, "loginButton", config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML, By.ID)
            btn_login.click()

            # busca un elemento renderizado del portal principal de la pagina
            HtmlUtils.wait_until_element_is_visible(
                web_driver, "tour-assistant-icon",
                config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML, By.CLASS_NAME)
        except WebDriverException as e:
            message_error = e.msg
            error_detected = 1
        except NoSuchElementException as e:
            message_error = e.msg
            error_detected = 1
        except ElementClickInterceptedException as e:
            message_error = e.msg
            error_detected = 1
        except TimeoutException as e:
            message_error = e.msg
            error_detected = 1

        Timer.stop_time()

        json_result[constantes.JSON_INICIO_SESION_STATUS_VALIDACION] = error_detected
        json_result[constantes.JSON_INICIO_SESION_MSG_ERROR] = message_error
        json_result[constantes.JSON_INICIO_SESION_TIEMPO_TOTAL_SEG] = Timer.get_time_in_seconds_float()

        return json_result

    @staticmethod
    def validation_libraries_section(web_driver: webdriver.Remote, json_result: dict):
        message_error = ''
        error_detected = 0

        Timer.start_time()

        try:
            btn_nav_libraries = HtmlUtils.wait_until_element_is_visible(
                web_driver, "//span[@class='nav-text'][text()=' Libraries ']",
                config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML, By.XPATH)

            btn_nav_libraries.click()

            HtmlUtils.wait_until_element_is_visible(
                web_driver, 'search-bar', config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML, By.CLASS_NAME)
        except WebDriverException as e:
            message_error = e.msg
            error_detected = 1
        except NoSuchElementException as e:
            message_error = e.msg
            error_detected = 1
        except ElementClickInterceptedException as e:
            message_error = e.msg
            error_detected = 1
        except TimeoutException as e:
            message_error = e.msg
            error_detected = 1

        Timer.stop_time()

        json_result[constantes.JSON_INGRESO_SECCION_LIBRARIES_STATUS_VALIDACION] = error_detected
        json_result[constantes.JSON_INGRESO_SECCION_LIBRARIES_MSG_ERROR] = message_error
        json_result[constantes.JSON_INGRESO_SECCION_LIBRARIES_TIEMPO_TOTAL_SEG] = Timer.get_time_in_seconds_float()

        return json_result

    @staticmethod
    def validation_access_section(web_driver: webdriver.Remote, json_result: dict):
        message_error = ''
        error_detected = 0

        Timer.start_time()

        try:
            btn_nav_administration = HtmlUtils.wait_until_element_is_visible(
                web_driver, "//span[@class='nav-text'][text()=' Administration ']",
                config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML, By.XPATH)

            btn_nav_administration.click()

            HtmlUtils.wait_until_element_is_visible(
                web_driver, "//button[text()='Export Users']",
                config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML, By.XPATH)
        except WebDriverException as e:
            message_error = e.msg
            error_detected = 1
        except NoSuchElementException as e:
            message_error = e.msg
            error_detected = 1
        except ElementClickInterceptedException as e:
            message_error = e.msg
            error_detected = 1
        except TimeoutException as e:
            message_error = e.msg
            error_detected = 1

        Timer.stop_time()

        json_result[constantes.JSON_INGRESO_SECCION_ADMINISTRATION_STATUS_VALIDACION] = error_detected
        json_result[constantes.JSON_INGRESO_SECCION_ADMINISTRATION_MSG_ERROR] = message_error
        json_result[constantes.JSON_INGRESO_SECCION_ADMINISTRATION_TIEMPO_TOTAL_SEG] = Timer.get_time_in_seconds_float()

        return json_result

    @staticmethod
    def validation_monitor_section(web_driver: webdriver.Remote, json_result: dict):
        message_error = ''
        error_detected = 0

        Timer.start_time()

        try:
            btn_nav_monitor = HtmlUtils.wait_until_element_is_visible(
                web_driver, "//span[@class='nav-text'][text()=' Monitor ']",
                config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML, By.XPATH)

            btn_nav_monitor.click()

            HtmlUtils.wait_until_element_is_visible(
                web_driver, "//button[text()='Export Tasks']",
                config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML, By.XPATH)
        except WebDriverException as e:
            message_error = e.msg
            error_detected = 1
        except NoSuchElementException as e:
            message_error = e.msg
            error_detected = 1
        except ElementClickInterceptedException as e:
            message_error = e.msg
            error_detected = 1
        except TimeoutException as e:
            message_error = e.msg
            error_detected = 1

        Timer.stop_time()

        json_result[constantes.JSON_INGRESO_SECCION_MONITOR_STATUS_VALIDACION] = error_detected
        json_result[constantes.JSON_INGRESO_SECCION_MONITOR_MSG_ERROR] = message_error
        json_result[constantes.JSON_INGRESO_SECCION_MONITOR_TIEMPO_TOTAL_SEG] = Timer.get_time_in_seconds_float()

        return json_result

    @staticmethod
    def validation_more_section(web_driver: webdriver.Remote, json_result: dict):
        message_error = ''
        error_detected = 0

        Timer.start_time()

        try:
            btn_nav_more = HtmlUtils.wait_until_element_is_visible(
                web_driver, "header-more-dropdown", config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML,
                By.CLASS_NAME)

            btn_nav_more.click()

            option_launchpad = HtmlUtils.wait_until_element_is_visible(
                web_driver, "//a[@class='more-items dropdown-item ng-star-inserted'][text()=' App Launchpad ']",
                config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML, By.XPATH)

            option_launchpad.click()

            content_wrapper = HtmlUtils.wait_until_element_is_visible(
                web_driver, "content-wrapper", config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML,
                By.CLASS_NAME)

            iframe_panel = HtmlUtils.wait_until_element_is_visible(
                content_wrapper, "iframe", config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML,
                By.TAG_NAME)

            web_driver.switch_to.frame(iframe_panel)

            HtmlUtils.wait_until_element_is_visible(
                web_driver, "//a[@class='nav-link active'][text()='Marketplace']",
                config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML, By.XPATH)

            web_driver.switch_to.parent_frame()
        except WebDriverException as e:
            message_error = e.msg
            error_detected = 1
        except NoSuchElementException as e:
            message_error = e.msg
            error_detected = 1
        except ElementClickInterceptedException as e:
            message_error = e.msg
            error_detected = 1
        except TimeoutException as e:
            message_error = e.msg
            error_detected = 1

        Timer.stop_time()

        json_result[constantes.JSON_INGRESO_SECCION_MORE_STATUS_VALIDACION] = error_detected
        json_result[constantes.JSON_INGRESO_SECCION_MORE_MSG_ERROR] = message_error
        json_result[constantes.JSON_INGRESO_SECCION_MORE_TIEMPO_TOTAL_SEG] = Timer.get_time_in_seconds_float()

        return json_result
