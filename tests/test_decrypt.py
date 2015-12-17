import credkeep
import mock
from . import encrypted_secrets, decrypted_secrets, CredkeepTestCase


def mock_decrypt(secret):
    values = {}
    for k in encrypted_secrets:
        values[encrypted_secrets[k]] = decrypted_secrets[k]

    return values[secret]


class TestDecrypt(CredkeepTestCase):
    def setUp(self):
        super(TestDecrypt, self).setUp()
        self.enc_fname = 'test.enc.json'
        self.create_temp(self.enc_fname, encrypted_secrets)

    @mock.patch('credkeep.decrypt.decrypt_secret')
    def test_decrypt(self, mock_decrypt_secret):
        mock_decrypt_secret.side_effect = mock_decrypt

        results = credkeep.decrypt_file(self.enc_fname, set_env=False)
        self.assertDictEqual(results, decrypted_secrets)


class TestDecryptCache(CredkeepTestCase):
    def setUp(self):
        super(TestDecryptCache, self).setUp()
        self.enc_fname = 'test.enc.json'
        self.create_temp(self.enc_fname, encrypted_secrets)

    @mock.patch('credkeep.decrypt.decrypt_file')
    def test_cache_hit(self, mock_decrypt):
        clear_fname = 'test.json'
        self.create_temp(clear_fname, decrypted_secrets)

        credkeep.decrypt_or_cache(self.enc_fname)
        mock_decrypt.assert_not_called()

    @mock.patch('credkeep.decrypt.decrypt_file')
    def test_cache_miss(self, mock_decrypt):
        credkeep.decrypt_or_cache(self.enc_fname)
        mock_decrypt.assert_called_with(self.enc_fname)
