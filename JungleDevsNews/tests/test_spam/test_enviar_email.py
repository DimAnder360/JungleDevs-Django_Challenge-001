import pytest

from JungleDevsNews.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['andersonbernardo@jungledevs.com', 'jungledevs@jungledevs.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'jungledevs@jungledevs.com',
        'Jungle Devs News - Notícias pra você!',
        'Confira as notícias do mundo da tecnologia e dos negócios'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'jungledevs']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'jungledevs@jungledevs.com',
            'Jungle Devs News - Notícias pra você!',
            'Confira as notícias do mundo da tecnologia e dos negócios'
        )
