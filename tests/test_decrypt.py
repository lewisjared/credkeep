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
