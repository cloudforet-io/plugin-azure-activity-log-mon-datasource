import logging
from spaceone.core.manager import BaseManager
from spaceone.monitoring.conf.monitoring_conf import *
from spaceone.monitoring.connector.azure_connector.activity_log import ActivityLog
from spaceone.monitoring.model.log_model import Log, ActivityLogInfo

_LOGGER = logging.getLogger(__name__)


class MonitoringManager(BaseManager):
    def __init__(self, transaction):
        super().__init__(transaction)

    def list_logs(self, params):
        activity_log_connector: ActivityLog = self.locator.get_connector('ActivityLog', **params)
        activity_log_connector.set_connect(params.get('scheme'), params.get('options'), params.get('secret_data'))

        filters = self.set_filter(params)
        _LOGGER.debug(f'[list_logs] filter: {filters}')

        logs = activity_log_connector.list_logs(filters)
        # import pprint
        # pprint.pprint(logs)

        logs = [ActivityLogInfo(self.convert_nested_dictionary(log), strict=False) for log in logs]
        yield Log({'results': logs})

    @staticmethod
    def set_filter(params):
        filters = f"eventTimestamp ge '{params['start']}' and eventTimestamp le '{params['end']}'"

        query = params.get('query', {})
        if 'resource_uri' in query:
            filters = f"{filters} and resourceURI eq '{query['resource_uri']}'"

        return filters

    def convert_nested_dictionary(self, azure_obj):
        cloud_svc_dict = self.convert_dictionary(azure_obj)
        for k, v in cloud_svc_dict.items():
            if isinstance(v, object):  # object
                if 'azure' in str(type(v)):  # 1) if cloud_svc_object is azure defined model class
                    cloud_svc_dict[k] = self.convert_nested_dictionary(v)
                elif isinstance(v, list):  # 2) if cloud_svc_object is list
                    cloud_svc_converse_list = list()
                    for list_obj in v:  # if cloud_svc object's child value is Azure defined model class or dict class
                        if hasattr(list_obj, '__dict__') or 'azure' in str(type(list_obj)):
                            cloud_svc_converse_dict = self.convert_nested_dictionary(list_obj)
                            cloud_svc_converse_list.append(cloud_svc_converse_dict)
                        else:  # if cloud_svc_object's child value is simple list
                            cloud_svc_converse_list.append(list_obj)

                        cloud_svc_dict[k] = cloud_svc_converse_list

                elif hasattr(v, '__dict__'):  # if cloud_svc_object is not a list type, just a dict
                    cloud_svc_converse_dict = self.convert_nested_dictionary(v)
                    cloud_svc_dict[k] = cloud_svc_converse_dict

        return cloud_svc_dict

    @staticmethod
    def convert_dictionary(obj):
        return vars(obj)
