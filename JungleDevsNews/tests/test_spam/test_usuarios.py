from JungleDevsNews.spam.db import Conexao
from JungleDevsNews.spam.modelos import Usuario


def salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome='Login')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def listar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='Login'), Usuario(nome='Login2')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
