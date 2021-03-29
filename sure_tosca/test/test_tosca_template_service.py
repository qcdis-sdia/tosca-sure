import os
import tempfile
from unittest import TestCase

import requests
from six import BytesIO
from werkzeug.datastructures import FileStorage
import logging

from sure_tosca.models import ToscaTemplateModel
from sure_tosca.service import tosca_template_service

logger = logging.getLogger(__name__)
if not getattr(logger, 'handler_set', None):
    logger.setLevel(logging.INFO)
h = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
h.setFormatter(formatter)
logger.addHandler(h)
logger.handler_set = True

class Test(TestCase):
    def download_file(self,url):
        f = tempfile.NamedTemporaryFile(delete=False)
        r = requests.get(url)
        with open(f.name, 'wb') as f:
            f.write(r.content)
        return f.name

    def test_upload(self):
        base_url = 'https://raw.githubusercontent.com/qcdis-sdia/sdia-tosca/master/examples/'
        file_names = ['application_example_outputs.yaml','application_example_2_topologies.yaml',
                      'application_example_updated.yaml','compute.yaml','application_example_provisioned.yaml',
                      'topology.yaml',
                      'os_provision_workflow.yaml']

        for file_name in file_names:
            path = self.download_file(base_url+file_name)
            logger.info("Testing : " + str(file_name))
            doc_id = tosca_template_service.save(self.upload_file(path))
            logger.info("doc_id : " + str(doc_id))
            self.assertTrue (doc_id >= 0)


    def test_workflow(self):
        base_url = 'https://raw.githubusercontent.com/qcdis-sdia/sdia-tosca/master/examples/'
        path = self.download_file(base_url + 'os_provision_workflow.yaml')
        doc_id = tosca_template_service.save(self.upload_file(path))
        tosca_template_dict = tosca_template_service.get_tosca_template_dict_by_id(doc_id)
        tosca_template_model = ToscaTemplateModel.from_dict(tosca_template_dict)

        self.assertIsNotNone(tosca_template_model)
        self.assertIsNotNone(tosca_template_model.topology_template)
        self.assertIsNotNone(tosca_template_model.topology_template.node_templates)


    def test_get_tosca_template_model_by_id(self):
        base_url = 'https://raw.githubusercontent.com/qcdis-sdia/sdia-tosca/master/examples/'
        path = self.download_file(base_url + 'application_example_updated.yaml')
        doc_id = tosca_template_service.save(self.upload_file(path))
        tosca_template_dict = tosca_template_service.get_tosca_template_dict_by_id(doc_id)
        tosca_template_model = ToscaTemplateModel.from_dict(tosca_template_dict)

        self.assertIsNotNone(tosca_template_model)
        self.assertIsNotNone(tosca_template_model.topology_template)
        self.assertIsNotNone(tosca_template_model.topology_template.node_templates)


    def test_get_tosca_template_model_by_id(self):
        base_url = 'https://raw.githubusercontent.com/qcdis-sdia/sdia-tosca/master/examples/'
        path = self.download_file(base_url + 'application_example_updated.yaml')
        doc_id = tosca_template_service.save(self.upload_file(path))
        tosca_template_dict = tosca_template_service.get_tosca_template_dict_by_id(doc_id)
        tosca_template_model = ToscaTemplateModel.from_dict(tosca_template_dict)

        self.assertIsNotNone(tosca_template_model)
        self.assertIsNotNone(tosca_template_model.topology_template)
        self.assertIsNotNone(tosca_template_model.topology_template.node_templates)

    def upload_file(self, path):
        input_tosca_file_path = path

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.assertEqual(True, os.path.exists(input_tosca_file_path),
                         'Starting from: ' + dir_path + ' Input TOSCA file: ' + input_tosca_file_path + ' not found')

        file = open(input_tosca_file_path, "r")
        # with open(input_tosca_file_path, 'r') as file:
        #     contents = file.read()
        # byte_contents = bytes(contents, 'utf8')

        with open(input_tosca_file_path, 'r') as file:
            contents = file.read()
        byte_contents = bytes(contents, 'utf8')
        # data = dict(file=(BytesIO(byte_contents), input_tosca_file_path))

        return FileStorage(stream=BytesIO(byte_contents), filename=input_tosca_file_path, name=input_tosca_file_path,
                           content_type=None,
                           content_length=None, headers=None)
