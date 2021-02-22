import unittest
import CipherText as ciph

class Cipher_method_testers(unittest.TestCase):
    def test_sample(self):
        pass

    def test_encrypt_result(self):
        self.assertEqual(ciph.encrypt('hello',10),'rovvy')
        self.assertEqual(ciph.encrypt('hello world',15),'wtaadldgas')
        self.assertEqual(ciph.encrypt('hello my world',20),'byffigsqilfx')

    def test_decrypt_result(self):
        self.assertEqual(ciph.decrypt('rovvy',10),'hello')
        self.assertEqual(ciph.decrypt('wtaadldgas',15),'helloworld')
        self.assertEqual(ciph.decrypt('byffigsqilfx',20),'hellomyworld')
    

if __name__ == "__main__":
    unittest.main()