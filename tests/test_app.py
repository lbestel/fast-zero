from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Organizando as informações

    response = client.get('/')  # Ação (executar a aplicação)

    assert response.status_code == HTTPStatus.OK  # Garantir que foi testado
    assert response.json() == {'message': 'Olá Mundo!'}
