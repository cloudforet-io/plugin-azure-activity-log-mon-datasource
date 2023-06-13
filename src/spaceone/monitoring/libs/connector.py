import os
import logging
from spaceone.core.connector import BaseConnector
from spaceone.monitoring.error.azure import *
from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient

__all__ = ['AzureConnector']
_LOGGER = logging.getLogger(__name__)


class AzureConnector(BaseConnector):
    def __init__(self, *args, **kwargs):
        """
        kwargs
            - schema
            - options
            - secret_data
        """

        super().__init__(*args, **kwargs)
        self.client = None

    def set_connect(self, schema, options: dict, secret_data: dict):
        """
        cred(dict)
            - type: ..
            - tenant_id: ...
            - client_id: ...
            - client_secret: ...
            - subscription_id: ...
        """
        try:
            subscription_id = secret_data['subscription_id']

            os.environ["AZURE_SUBSCRIPTION_ID"] = subscription_id
            os.environ["AZURE_TENANT_ID"] = secret_data['tenant_id']
            os.environ["AZURE_CLIENT_ID"] = secret_data['client_id']
            os.environ["AZURE_CLIENT_SECRET"] = secret_data['client_secret']

            credential = DefaultAzureCredential()
            self.client = MonitorManagementClient(credential, subscription_id)

        except Exception as e:
            print(e)
            raise ERROR_INVALID_CREDENTIALS()
