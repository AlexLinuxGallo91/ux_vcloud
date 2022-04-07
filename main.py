import json

from selenium import webdriver
from html_utils.timer import Timer
from validaciones_amx_vcloud import constantes
from config_parameters import config_parameters_constants
from validaciones_amx_vcloud.validaciones_web_amx import ValidacionesWebAmx
from urllib3.exceptions import MaxRetryError
from zabbix_sender_amx.zabbix_utils import ZabbixSenderUtils
from config_parameters.config_utils import ConfigUtils


def init_web_remote_driver(headless: bool):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')

    if headless:
        chrome_options.add_argument('--headless')

    return webdriver.Remote(
        options=chrome_options,
        command_executor=config_parameters_constants.COMMAND_EXECUTOR)


def experience_user_execution(web_driver: webdriver.Remote, json_result: dict):
    init_time = Timer.get_actual_time()

    json_result = ValidacionesWebAmx.validation_enter_principal_page(web_driver, json_result)

    json_result = ValidacionesWebAmx.validation_login_session_vcloud(web_driver, json_result)

    json_result = ValidacionesWebAmx.validation_libraries_section(web_driver, json_result)

    json_result = ValidacionesWebAmx.validation_access_section(web_driver, json_result)

    json_result = ValidacionesWebAmx.validation_monitor_section(web_driver, json_result)

    json_result = ValidacionesWebAmx.validation_more_section(web_driver, json_result)

    final_time = Timer.get_actual_time()
    total_time_ux = Timer.get_diff_total_time(final_time, init_time)

    json_result['total_execution_ux'] = round(total_time_ux, 2)

    return json_result


def main():
    ConfigUtils.load_config_parameters_from_json_file()
    web_driver = init_web_remote_driver(headless=config_parameters_constants.SELENIUM_HEADLESS_EXECUTION)

    constantes.FINAL_RESULT_JSON = experience_user_execution(web_driver, constantes.FINAL_RESULT_JSON)
    json_final = json.dumps(constantes.FINAL_RESULT_JSON, indent=4)

    web_driver.close()
    web_driver.quit()

    print(json_final)

    # se realiza el envio de los datos/metricas al servidor del zabbix
    metric_list = ZabbixSenderUtils.generate_list_metrics(
        constantes.FINAL_RESULT_JSON, config_parameters_constants.ZABBIX_HOST_MONITORING,
        config_parameters_constants.ZABBIX_HOST_KEY)

    print(metric_list)

    ZabbixSenderUtils.send_list_metrics_to_zabbix_server(config_parameters_constants.ZABBIX_IP_SERVER, metric_list)


if __name__ == '__main__':
    try:
        main()
    except MaxRetryError:
        print('Sucedio un error al ejecutar el script, favor de revisar que '
              'el contenedor Docker se encuente en estado de ejecucion.')
