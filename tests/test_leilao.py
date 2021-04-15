from unittest import TestCase

from src.leilao.dominio import Leilao, Lance, Usuario


class TestLeilao(TestCase):


    def setUp(self):
        self.gui = Usuario('Gui')
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_passados_de_forma_crescente(self):
        self.Alex = Usuario('Alex')
        self.lance_do_alex = Lance(self.Alex, 100.0)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_alex)



        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_passados_de_forma_decrescente(self):
        self.Alex = Usuario('Alex')
        self.lance_do_alex = Lance(self.Alex, 100.0)

        self.leilao.propoe(self.lance_do_alex)
        self.leilao.propoe(self.lance_do_gui)



        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_quando_houver_apenas_um_lance(self):

        self.leilao.propoe(self.lance_do_gui)


        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_passados_tres_lances(self):
        Alex = Usuario('Alex')
        lance_do_alex = Lance(Alex, 100.0)
        mateus = Usuario('Mateus')
        lance_do_mateus = Lance(mateus, 200.0)


        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_alex)
        self.leilao.propoe(lance_do_mateus)



        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_lance_quando_leilao_nao_tiver_lance(self):
        self.leilao.propoe(self.lance_do_gui)
        quantidade_de_lances = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances)

    def test_deve_permitir_propor_lance_caso_o_usuario_anterior_seja_diferente(self):
        yuri = Usuario('yuri')
        lance_do_yuri = Lance(yuri, 200.0)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances)


    def test_nao_deve_permitir_lance_caso_usuario_seja_o_mesmo(self):
        lance_do_gui = Lance(self.gui, 200.0)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui)
            
