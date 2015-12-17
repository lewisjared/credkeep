import unittest
import mock
import credkeep
import json
import os

from . import encrypted_secrets, decrypted_secrets, CredkeepTestCase


def mock_encrypt(secret, key):
    values = {}
    for k in encrypted_secrets:
        values[decrypted_secrets[k]] = encrypted_secrets[k]

    return values[secret]


class TestEncrypt(CredkeepTestCase):
    def setUp(self):
        super(TestEncrypt, self).setUp()
        self.clear_fname = 'test.json'
        self.create_temp(self.clear_fname, decrypted_secrets)

    @mock.patch('credkeep.encrypt.encrypt_secret')
    def test_encrypt(self, mock_encrypt_secret):
        mock_encrypt_secret.side_effect = mock_encrypt

        results = credkeep.encrypt_file(self.clear_fname)
        self.assertDictEqual(results, encrypted_secrets)


    @mock.patch('credkeep.encrypt.encrypt_secret')
    def test_custom_key(self, mock_encrypt_secret):
        mock_encrypt_secret.side_effect = mock_encrypt
        credkeep.encrypt_file(self.clear_fname, key='alias/test-key')
        for call in mock_encrypt_secret.call_args_list:
            args, kwargs = call
            self.assertEqual(kwargs['key'], 'alias/test-key')

    @mock.patch('credkeep.encrypt.encrypt_secret')
    def test_default_key(self, mock_encrypt_secret):
        mock_encrypt_secret.side_effect = mock_encrypt
        credkeep.encrypt_file(self.clear_fname)
        for call in mock_encrypt_secret.call_args_list:
            args, kwargs = call
            self.assertEqual(kwargs['key'], 'alias/credkeep')

    @mock.patch('credkeep.encrypt.encrypt_secret')
    def test_output_file(self, mock_encrypt_secret):
        mock_encrypt_secret.side_effect = mock_encrypt

        output = 'test.enc.json'
        self.assertNotExists(output)

        credkeep.encrypt_file(self.clear_fname, output_filename=output)
        self.add_temp(output)
        self.assertExists(output)
        results = json.load(open(output))
        self.assertDictEqual(results, encrypted_secrets)
