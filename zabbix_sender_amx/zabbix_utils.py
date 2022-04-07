from pyzabbix import ZabbixSender, ZabbixMetric


class ZabbixSenderUtils:

    @staticmethod
    def generate_list_metrics(json_result: dict, hostname: str, host_key: str):
        metric_list = []

        for key, value in json_result.items():
            print(key)
            formated_host_key = '{}.{}'.format(host_key,key)
            metric_list.append(ZabbixMetric(host=hostname, key=formated_host_key, value=value))

        return metric_list

    @staticmethod
    def send_list_metrics_to_zabbix_server(zabbix_server_ip: str, metric_list: list):
        metrics_sended_correctly = True
        zabbix_sender = ZabbixSender(zabbix_server=zabbix_server_ip)

        try:
            resp = zabbix_sender.send(metric_list)
            print(resp)
        except ConnectionRefusedError:
            metrics_sended_correctly = False
        except TimeoutError:
            metrics_sended_correctly = False
            
        print('se enviaron?: {}'.format(metrics_sended_correctly))

        return metrics_sended_correctly

