from config_parameters import config_parameters_constants
import json
import os
import sys

class ConfigUtils:

    @staticmethod
    def load_config_parameters_from_json_file():
        try:
            root_project_dir = os.path.dirname(os.path.dirname(__file__))
            path_json_file = os.path.join(root_project_dir, 'config.json')

            json_file = open(path_json_file)
            json_data = json.load(json_file)
            json_file.close()

            # credenciales y url del portal principal de VCloud
            config_parameters_constants.URL_PAGINA_PRINCIPAL_VCLOUD = \
                json_data['parametros_portal_vcloud']['url_portal_principal']

            config_parameters_constants.USERNAME = json_data['parametros_portal_vcloud']['user']
            config_parameters_constants.PASSWORD = json_data['parametros_portal_vcloud']['password']

            # datos del servidor y contenedor Docker
            config_parameters_constants.IP_DOCKER_HOST_SELENIUM = \
                json_data['parametros_selenium_docker']['ip_docker_host_selenium']

            config_parameters_constants.PORT_DOCKER_HOST_SELENIUM = \
                json_data['parametros_selenium_docker']['port_docker_host_selenium']

            config_parameters_constants.COMMAND_EXECUTOR = 'http://{}:{}/wd/hub'.\
                format(config_parameters_constants.IP_DOCKER_HOST_SELENIUM,
                       config_parameters_constants.PORT_DOCKER_HOST_SELENIUM)

            # datos del servidor zabbix a donde se enviaran las metricas
            config_parameters_constants.ZABBIX_IP_SERVER = json_data['parametros_zabbix']['ip_server_zabbix']

            config_parameters_constants.ZABBIX_HOST_MONITORING = \
                json_data['parametros_zabbix']['zabbix_host_monitoring']

            config_parameters_constants.ZABBIX_HOST_KEY = json_data['parametros_zabbix']['zabbix_host_key']

            # timeouts de renderizado de elementos html en el portal
            config_parameters_constants.TIME_OUT_RENDERIZADO_ELEMENTO_HTML = \
                json_data['parametros_timeouts']['timeout_render_html_inputs']

            # configuracion selenium
            config_parameters_constants.SELENIUM_HEADLESS_EXECUTION = json_data['parametros_selenium']['headless']

        except FileNotFoundError as e:
            print('Sucedio un error al cargar el archivo de configuracion json: {}'.format(e))
            sys.exit(1)
        except KeyError as e:
            print('Sucedio un error al leer el archivo de configuracion json, no existe la llave: {}'.format(e))
            sys.exit(1)
