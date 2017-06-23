# coding: utf-8
from unittest import TestCase
from models.models import Client, ClientAttributeError


class TestClient(TestCase):

    def test_instance(self):
        client0 = Client('Pedro', 'Rua José Mendes da Silva, 326', '082.960.826-59', 20, '!Q@W#E$R%T')
        # must accept
        self.assertEqual(client0.instance.name, 'Pedro')
        self.assertEqual(client0.instance.address, 'Rua José Mendes da Silva, 326')
        self.assertEqual(client0.instance.cpf, '082.960.826-59')
        self.assertEqual(client0.instance.age, 20)
        self.assertEqual(client0.instance.password, '!Q@W#E$R%T')
        self.assertIsInstance(client0, Client)
        # must except
        try:
            client0.name
        except ClientAttributeError:
            self.assertTrue("Access denied to 'Client' attribute 'name'", True)
        try:
            client0.address
        except ClientAttributeError:
            self.assertTrue("Access denied to 'Client' attribute 'address'", True)
        try:
            client0.cpf
        except ClientAttributeError:
            self.assertTrue("Access denied to 'Client' attribute 'cpf'", True)
        try:
            client0.age
        except ClientAttributeError:
            self.assertTrue("Access denied to 'Client' attribute 'age'", True)
        try:
            client0.password
        except ClientAttributeError:
            self.assertTrue("Access denied to 'Client' attribute 'password'", True)

    def test_singleton(self):

        client0 = Client('Pedro', 'Rua José Mendes da Silva, 326', '082.960.826-59', 20, '!Q@W#E$R%T')
        client1 = Client('Ordep', '623 ,avliS ad sedneM ésoJ auR', '956.280.692-80', 02, 'T%R$E#W@Q!')
        # must accept
        # equal
        self.assertEqual(client0.instance.name, 'Ordep')
        self.assertEqual(client0.instance.address, '623 ,avliS ad sedneM ésoJ auR')
        self.assertEqual(client0.instance.cpf, '956.280.692-80')
        self.assertEqual(client0.instance.age, 02)
        self.assertEqual(client0.instance.password, 'T%R$E#W@Q!')
        self.assertIsInstance(client0, Client)
        self.assertIsInstance(client1, Client)
        # not equal
        self.assertNotEqual(client0.instance.name, 'Pedro')
        self.assertNotEqual(client0.instance.address, 'Rua José Mendes da Silva, 326')
        self.assertNotEqual(client0.instance.cpf, '082.960.826-59')
        self.assertNotEqual(client0.instance.age, 20)
        self.assertNotEqual(client0.instance.password, '!Q@W#E$R%T')
