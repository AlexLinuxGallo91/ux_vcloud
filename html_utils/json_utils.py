from validaciones_amx_vcloud import constantes

class JsonUtils:

    @staticmethod
    def init_json_empty_result():
        result = {}

        result[constantes.JSON_INGRESO_PAGINA_HTTP_CODE] = ''
        result[constantes.JSON_INGRESO_PAGINA_TIEMPO_TOTAL_SEG] = ''
        result[constantes.JSON_INGRESO_PAGINA_STATUS_VALIDACION] = ''
        result[constantes.JSON_INGRESO_PAGINA_MSG_ERROR] = ''

        result[constantes.JSON_INICIO_SESION_TIEMPO_TOTAL_SEG] = ''
        result[constantes.JSON_INICIO_SESION_STATUS_VALIDACION] = ''
        result[constantes.JSON_INICIO_SESION_MSG_ERROR] = ''

        result[constantes.JSON_INGRESO_SECCION_LIBRARIES_TIEMPO_TOTAL_SEG] = ''
        result[constantes.JSON_INGRESO_SECCION_LIBRARIES_STATUS_VALIDACION] = ''
        result[constantes.JSON_INGRESO_SECCION_LIBRARIES_MSG_ERROR] = ''

        result[constantes.JSON_INGRESO_SECCION_ADMINISTRATION_TIEMPO_TOTAL_SEG] = ''
        result[constantes.JSON_INGRESO_SECCION_ADMINISTRATION_STATUS_VALIDACION] = ''
        result[constantes.JSON_INGRESO_SECCION_ADMINISTRATION_MSG_ERROR] = ''

        result[constantes.JSON_INGRESO_SECCION_MONITOR_TIEMPO_TOTAL_SEG] = ''
        result[constantes.JSON_INGRESO_SECCION_MONITOR_STATUS_VALIDACION] = ''
        result[constantes.JSON_INGRESO_SECCION_MONITOR_MSG_ERROR] = ''

        return result
