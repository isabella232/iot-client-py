# coding: utf-8

"""
    Iot API

    Collection of all public API endpoints.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import iot_api_client
from iot_api_client.api.things_v1_api import ThingsV1Api  # noqa: E501
from iot_api_client.rest import ApiException


class TestThingsV1Api(unittest.TestCase):
    """ThingsV1Api unit test stubs"""

    def setUp(self):
        self.api = iot_api_client.api.things_v1_api.ThingsV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_things_v1_create(self):
        """Test case for things_v1_create

        create things_v1  # noqa: E501
        """
        pass

    def test_things_v1_create_sketch(self):
        """Test case for things_v1_create_sketch

        createSketch things_v1  # noqa: E501
        """
        pass

    def test_things_v1_delete(self):
        """Test case for things_v1_delete

        delete things_v1  # noqa: E501
        """
        pass

    def test_things_v1_delete_sketch(self):
        """Test case for things_v1_delete_sketch

        deleteSketch things_v1  # noqa: E501
        """
        pass

    def test_things_v1_layout(self):
        """Test case for things_v1_layout

        layout things_v1  # noqa: E501
        """
        pass

    def test_things_v1_list(self):
        """Test case for things_v1_list

        list things_v1  # noqa: E501
        """
        pass

    def test_things_v1_show(self):
        """Test case for things_v1_show

        show things_v1  # noqa: E501
        """
        pass

    def test_things_v1_update(self):
        """Test case for things_v1_update

        update things_v1  # noqa: E501
        """
        pass

    def test_things_v1_update_sketch(self):
        """Test case for things_v1_update_sketch

        updateSketch things_v1  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
