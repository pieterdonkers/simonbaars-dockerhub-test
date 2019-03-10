# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.errorunknown import ERRORUNKNOWN  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.models.persons import Persons  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_images_image_id_get(self):
        """Test case for images_image_id_get

        Gets an image
        """
        headers = [('User_Agent', 'User_Agent_example')]
        response = self.client.open(
            '/openapi101/images/{imageId}'.format(imageId='imageId_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_images_post(self):
        """Test case for images_post

        Uploads an image
        """
        headers = [('User_Agent', 'User_Agent_example')]
        data = dict(image=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/openapi101/images',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_get(self):
        """Test case for persons_get

        Gets some persons
        """
        query_string = [('pageSize', 100),
                        ('PageNumber', 1)]
        headers = [('User_Agent', 'User_Agent_example')]
        response = self.client.open(
            '/openapi101/persons',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_post(self):
        """Test case for persons_post

        Creates a person
        """
        person = Person()
        headers = [('User_Agent', 'User_Agent_example')]
        response = self.client.open(
            '/openapi101/persons',
            method='POST',
            data=json.dumps(person),
            content_type='application/json',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_username_delete(self):
        """Test case for persons_username_delete

        Deletes a person
        """
        response = self.client.open(
            '/openapi101/persons/{username}'.format(username='username_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_username_friends_get(self):
        """Test case for persons_username_friends_get

        Gets a person's friends
        """
        query_string = [('pageSize', 100),
                        ('PageNumber', 1)]
        response = self.client.open(
            '/openapi101/persons/{username}/friends'.format(username='username_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_username_get(self):
        """Test case for persons_username_get

        Gets a person
        """
        response = self.client.open(
            '/openapi101/persons/{username}'.format(username='username_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
