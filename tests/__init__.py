from unittest import TestCase
from os.path import exists
from os import remove
from json import dump

decrypted_secrets = {
    "SECRET_API_KEY": "thisismysecretkey",
    "ANOTHER_API_KEY": "anotherkey"
}
encrypted_secrets = {
    "SECRET_API_KEY": "CiAr4gKwrApZNibuqh1YKjlIGMj4A4GSHArF+0lCqBnqOxKfAQEBAgB4K+ICsKwKWTYm7qodWCo5SBjI+AOBkhwKxftJQqgZ6jsAAAB2MHQGCSqGSIb3DQEHBqBnMGUCAQAwYAYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAzGyPmdgqEbxzvnjKICARCAMzOd+DIaI/rUbc8dYQTxGS8aQQNjgXPt6Or0rxo7fFn0rA5/Kf6zpnui0q9XXtUatL4D3Q==",
    "ANOTHER_API_KEY": "CiAr4gKwrApZNibuqh1YKjlIGMj4A4GSHArF+0lCqBnqOxKXAQEBAgB4K+ICsKwKWTYm7qodWCo5SBjI+AOBkhwKxftJQqgZ6jsAAABuMGwGCSqGSIb3DQEHBqBfMF0CAQAwWAYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAxgB3p/zbVarLd/5a4CARCAK4w48/dCK7EvwTDELb11bpBe8TpaIhcCalfOqACQzoLoqgciAY8DuczOvRs="
}


class CredkeepTestCase(TestCase):
    def setUp(self):
        self.added_files = []

    def tearDown(self):
        for fname in self.added_files:
            self.assertExists(fname)
            remove(fname)

    def add_temp(self, fname):
        """
        Add a temporary file generated from the test case

        This file *must* exist at the completion of the test or an assertion will be raised.
        :param fname: filename of temporary file
        """
        self.added_files.append(fname)

    def create_temp(self, fname, data={}):
        """
        Creates a new temporary file and registers it with the TestCase

        Created files will be cleaned up at the completion of the test

        :param fname: filename of temporary file
        :param data: Data that can be written using json.dump
        """
        self.assertNotExists(fname)
        dump(data, open(fname, 'w'))
        self.add_temp(fname)

    def assertExists(self, fname):
        """
        Asserts that a file exists
        :param fname: filename to test
        :return: The result of the assertion
        """
        return self.assertTrue(exists(fname))

    def assertNotExists(self, fname):
        """
        Asserts that a file does not already exist.
        :param fname: filename to test
        :return: The result of the assertion
        """
        return self.assertFalse(exists(fname))
