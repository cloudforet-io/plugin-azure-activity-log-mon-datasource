import unittest
import os
from datetime import datetime, timedelta
from unittest.mock import patch

from spaceone.core.unittest.result import print_data
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.core import config
from spaceone.core import utils
from spaceone.core.transaction import Transaction
from spaceone.inventory.connector.snapshot import SnapshotConnector


class TestSnapshotConnector(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        config.init_conf(package='spaceone.monitoring')
        config_path = os.environ.get('TEST_CONFIG')
        test_config = utils.load_yaml_from_file(config_path)

        cls.schema = 'azure_client_secret'
        cls.azure_credentials = {
            'secret_data': test_config.get('AZURE_CREDENTIALS', {})
        }

        cls.azure_connector = SnapshotConnector(transaction=Transaction(), config={},
                                                secret_data=test_config.get('AZURE_CREDENTIALS', {}))
        # cls.azure_connector = DiskConnector(transaction=Transaction(), config={}, secret_data=cls.azure_credentials['secret_data'])
        super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def test_list_snapshots(self):
        # self.azure_connector.set_connect(self.azure_credentials)
        snapshots = self.azure_connector.list_snapshots()

        for snapshot in snapshots:
            print('=====')
            print(snapshot)
            print('=====')


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
