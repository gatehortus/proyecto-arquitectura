import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Proveedor


class ServicioJsonPublicoTests(TestCase):
    def test_endpoint_proveedores_publicos_devuelve_json_para_equipo_siguiente(self):
        get_user_model().objects.create_user(username='tester', password='secret123')
        self.client.login(username='tester', password='secret123')
        Proveedor.objects.create(nombre='Alfa SA', nit='111')
        Proveedor.objects.create(nombre='Zeta SA', nit='222')

        response = self.client.get(reverse('proveedores_publicos_api'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        data = json.loads(response.content)
        self.assertEqual([item['nombre'] for item in data], ['Alfa SA', 'Zeta SA'])
        self.assertIn('nit', data[0])
        self.assertIn('email', data[0])
