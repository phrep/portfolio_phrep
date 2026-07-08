import json
from unittest.mock import patch

from django.core.cache import cache
from django.test import TestCase

from .models import ChatLog


class PageViewsTests(TestCase):
    def test_home_carrega(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_lista_projetos_carrega(self):
        response = self.client.get('/lista_projetos/')
        self.assertEqual(response.status_code, 200)

    def test_detalhe_projeto_existente_carrega(self):
        response = self.client.get('/projeto/projeto1/')
        self.assertEqual(response.status_code, 200)


class ChatApiTests(TestCase):
    def setUp(self):
        cache.clear()

    def test_mensagem_vazia_retorna_400(self):
        response = self.client.post(
            '/api/chat/', data=json.dumps({'message': ''}), content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_mensagem_muito_longa_retorna_400(self):
        response = self.client.post(
            '/api/chat/', data=json.dumps({'message': 'a' * 1001}), content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_corpo_nao_json_retorna_400(self):
        response = self.client.post(
            '/api/chat/', data='isso nao e json', content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    @patch('portfolio.views.ask_chatbot')
    def test_resposta_com_sucesso_grava_log(self, mock_ask_chatbot):
        mock_ask_chatbot.return_value = 'resposta de teste'

        response = self.client.post(
            '/api/chat/', data=json.dumps({'message': 'quais suas habilidades?'}), content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['reply'], 'resposta de teste')
        self.assertTrue(
            ChatLog.objects.filter(message='quais suas habilidades?', reply='resposta de teste').exists()
        )

    @patch('portfolio.views.ask_chatbot')
    def test_rate_limit_bloqueia_apos_limite(self, mock_ask_chatbot):
        mock_ask_chatbot.return_value = 'ok'

        for _ in range(8):
            response = self.client.post(
                '/api/chat/', data=json.dumps({'message': 'oi'}), content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)

        response = self.client.post(
            '/api/chat/', data=json.dumps({'message': 'oi'}), content_type='application/json'
        )
        self.assertEqual(response.status_code, 429)


class AdminLoginThrottleTests(TestCase):
    def setUp(self):
        cache.clear()

    def test_bloqueia_apos_varias_tentativas_erradas(self):
        for _ in range(5):
            response = self.client.post('/admin/login/', {'username': 'errado', 'password': 'errado'})
            self.assertEqual(response.status_code, 200)

        response = self.client.post('/admin/login/', {'username': 'errado', 'password': 'errado'})
        self.assertEqual(response.status_code, 429)


class ChatLogModelTests(TestCase):
    def test_str_contem_a_mensagem(self):
        log = ChatLog.objects.create(message='pergunta de teste', reply='resposta')
        self.assertIn('pergunta de teste', str(log))
