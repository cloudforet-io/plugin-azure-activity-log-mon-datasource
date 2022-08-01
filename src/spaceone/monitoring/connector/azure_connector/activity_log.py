import logging
from spaceone.core import utils
from spaceone.monitoring.libs.connector import AzureConnector

__all__ = ['ActivityLog']
_LOGGER = logging.getLogger(__name__)


class ActivityLog(AzureConnector):
    def __init__(self, client=None, **kwargs):
        super().__init__(**kwargs)

        if client:
            self.client = client

    def list_logs(self, filters):
        try:
            activity_logs = [log for log in self.client.activity_logs.list(filters)]
            return activity_logs
        except Exception as e:
            _LOGGER.error(f"[list_metrics]: {e}")
            return []

    @staticmethod
    def _convert_timestamp(metric_datetime):
        return utils.datetime_to_iso8601(metric_datetime)

    @staticmethod
    def _get_metric_data(metric_value):
        if metric_value:
            return metric_value
        else:
            return 0
