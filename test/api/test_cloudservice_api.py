import os
import unittest
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.core import utils
from spaceone.tester import TestCase, print_json


class TestCollector(TestCase):

    @classmethod
    def setUpClass(cls):
        azure_cred = os.environ.get('AZURE_CRED')
        test_config = utils.load_yaml_from_file(azure_cred)

        cls.schema = 'azure_client_secret'
        cls.azure_credentials = test_config.get('AZURE_CREDENTIALS', {})
        super().setUpClass()

    def test_init(self):
        v_info = self.monitoring.DataSource.init({'options': {}})
        print_json(v_info)

    def test_verify(self):
        options = {
        }
        v_info = self.monitoring.DataSource.verify({'options': options, 'secret_data': self.azure_credentials})
        print_json(v_info)

    def test_collect(self):
        query = {'resource_uri': '/subscriptions/3ec64e1e-1ce8-4f2c-82a0-a7f6db0899ca/resourceGroups/jhsong-rg/providers/Microsoft.Compute/virtualMachines/jhsong-active-log-test'}
        start = '2022-07-25T06:00:53.873Z'
        end = '2022-08-01T06:00:53.873Z'

        resource_stream = self.monitoring.Log.list({'options': {},
                                                    'secret_data': self.azure_credentials,
                                                    'query': query,
                                                    'start': start,
                                                    'end': end})

        for res in resource_stream:
            print_json(res)


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
