import kivy
kivy.require('2.0.0')
import sqlite3
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

Builder.load_string(open("gui.kv", encoding="utf-8").read(), rulesonly=True)

class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior, RecycleGridLayout):
    pass

class SelectableButton(RecycleDataViewBehavior, Button):
    pass

# funcionando
class MenuScreen(Screen):
    lbl_resposta = ObjectProperty(None)

# funcionando
class rv(Screen):
    col1 = ListProperty()
    col2 = ListProperty()
    conexao = sqlite3.connect("controle.db")

    def pegar_produtos(self):
        self.col1 = []
        self.col2 = []
        with self.conexao:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT id, nome_produto FROM produtos ORDER BY id ASC")
            self.conexao.commit()
            rows = cursor.fetchall()
            for row in rows:
                self.col1.append(row[0])
                self.col2.append(row[1])

# funcionando <bambiarra alert!>
class prd(Screen):
    col1 = ListProperty('')
    col2 = ListProperty('')
    conexao = sqlite3.connect('controle.db')

    def pegar_produtores(self):
        self.col1 = []
        self.col2 = []
        with self.conexao:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT id, nome FROM produtores ORDER BY id ASC")
            self.conexao.commit()
            rows = cursor.fetchall()
            for row in rows:
                self.col1.append(row[0])
                self.col2.append(row[1])

# funcionando <bambiarra alert!>
class vsr(Screen):
    col1 = ListProperty('')
    col2 = ListProperty('')
    conexao = sqlite3.connect('controle.db')

    def visualizar_produtores(self):
        self.col1 = []
        self.col2 = []
        with self.conexao:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT id, nome FROM produtores ORDER BY id ASC")
            self.conexao.commit()
            rows = cursor.fetchall()
            for row in rows:
                self.col1.append(row[0])
                self.col2.append(row[1])


# funcionando
class CadastroCompletoProdutor(Screen):
    id = ObjectProperty(None)
    nome = ObjectProperty(None)
    end = ObjectProperty(None)
    cpf = ObjectProperty(None)
    insc = ObjectProperty(None)
    coord = ObjectProperty(None)

    def atualizar_form(self, t1, t2, t3, t4, t5):
        self.ids.nome.text = 'Produtor: ' + t1
        self.ids.end.text = 'endereço: ' + t2
        self.ids.cpf.text = 'CPF ou CNPJ: ' + t3
        self.ids.insc.text = 'Inscrição Estadual: ' + t4
        self.ids.coord.text = 'Coordenadas Geográficas: ' + t5

class VisualizarCadastroCompleto(Screen):
    id = ObjectProperty(None)
    nome = ObjectProperty(None)
    end = ObjectProperty(None)
    cpf = ObjectProperty(None)
    insc = ObjectProperty(None)
    coord = ObjectProperty(None)

    def atualizar_form(self, t1, t2, t3, t4, t5):
        self.ids.nome.text = 'Produtor: ' + t1
        self.ids.end.text = 'endereço: ' + t2
        self.ids.cpf.text = 'CPF ou CNPJ: ' + t3
        self.ids.insc.text = 'Inscrição Estadual: ' + t4
        self.ids.coord.text = 'Coordenadas Geográficas: ' + t5


# funcionando
class ProdutorLoginScreen(Screen):
    txt_id = ObjectProperty(None)
    txt_log = ObjectProperty(None)
    txt_sen = ObjectProperty(None)
    lbl_resposta = ObjectProperty(None)

# isso aqui será implementado para efetivação de login
    def atualizar_form(self, t1,  t2, t3, t4, t5):
        self.ids.nome.text = 'Logado Como: ' + t1
        self.ids.end.text = 'endereço: ' + t2
        self.ids.cpf.text = 'CPF ou CNPJ: ' + t3
        self.ids.insc.text = 'Inscrição Estadual: ' + t4
        self.ids.coord.text = 'Coordenadas Geográficas: ' + t5

# fase de implementação
class ProdutorScreen(Screen):
    id = ObjectProperty(None)
    nome = ObjectProperty(None)
    end = ObjectProperty(None)
    cpf = ObjectProperty(None)
    insc = ObjectProperty(None)
    coord = ObjectProperty(None)
    lbl_resposta = ObjectProperty(None)

# fase de implementação
    def atualizar_form(self, t1, t2, t3, t4, t5):
        self.ids.nome.text = 'Produtor: ' + t1
        self.ids.end.text = 'endereço: ' + t2
        self.ids.cpf.text = 'CPF ou CNPJ: ' + t3
        self.ids.insc.text = 'Inscrição Estadual: ' + t4
        self.ids.coord.text = 'Coordenadas Geográficas: ' + t5

# funcionando
class RevendaLoginScreen(Screen):
    txt_nome = ObjectProperty(None)
    txt_sen = ObjectProperty(None)
    lbl_resposta = ObjectProperty(None)

# funcionando
class RevendaScreen(Screen):
    lbl_resposta = ObjectProperty(None)

# fase de implementação
class EfetuarVendaScreen(Screen):
    txt_id = ObjectProperty(None)
    txt_prod = ObjectProperty(None)
    txt_quant = ObjectProperty(None)
    data = ObjectProperty(None)
    devolucao = ObjectProperty(None)
    data_compra = ObjectProperty(None)
    data_devolucao = ObjectProperty(None)
    lbl_resposta = ObjectProperty(None)

# funcionando
class FiscalizacaoLoginScreen(Screen):
    txt_nome = ObjectProperty(None)
    txt_sen = ObjectProperty(None)
    lbl_resposta = ObjectProperty(None)

# funcionando
class FiscalizacaoScreen(Screen):
    lbl_resposta = ObjectProperty(None)

# funcionando
class create_sc(Screen):
    txt_nome = ObjectProperty(None)
    txt_end = ObjectProperty(None)
    txt_cpf = ObjectProperty(None)
    txt_insc = ObjectProperty(None)
    txt_coord = ObjectProperty(None)
    txt_log = ObjectProperty(None)
    txt_sen = ObjectProperty(None)
    lbl_resposta = ObjectProperty(None)

# funcionando
class create_sc2(Screen):
    txt_nome = ObjectProperty(None)
    txt_end = ObjectProperty(None)
    txt_cpf = ObjectProperty(None)
    txt_insc = ObjectProperty(None)
    txt_coord = ObjectProperty(None)
    txt_log = ObjectProperty(None)
    txt_sen = ObjectProperty(None)
    lbl_resposta = ObjectProperty(None)

# funcionando
class CadastrarProdutoScreen(Screen):
    txt_nmpd = ObjectProperty(None)
    txt_gtin = ObjectProperty(None)

sm = ScreenManager()
sm.add_widget(create_sc(name='create'))
sm.add_widget(create_sc2(name='create2'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProdutorLoginScreen(name='produtorlogin'))
sm.add_widget(ProdutorScreen(name='produtor'))
sm.add_widget(RevendaLoginScreen(name='revendalogin'))
sm.add_widget(RevendaScreen(name='revenda'))
sm.add_widget(EfetuarVendaScreen(name='venda'))
sm.add_widget(rv(name='rv'))
sm.add_widget(prd(name='prd'))
sm.add_widget(vsr(name='vsr'))
sm.add_widget(CadastroCompletoProdutor(name='cadastrocompletoprodutor'))
sm.add_widget(VisualizarCadastroCompleto(name='visualizarcadastro'))
sm.add_widget(CadastrarProdutoScreen(name='cadastrarproduto'))
sm.add_widget(FiscalizacaoLoginScreen(name='fiscalizacaologin'))
sm.add_widget(FiscalizacaoScreen(name='fiscalizacao'))
sm.current = 'menu'

class CrudKivy(App):

    def selecionar_todos_produtos(self):
        rv = sm.get_screen('rv')
        rv.pegar_produtos()
        sm.current = 'rv'

    def selecionar_todos_produtores(self):
        prd = sm.get_screen('prd')
        prd.pegar_produtores()
        sm.current = 'prd'

    def visualizar_todos_produtores(self):
        vsr = sm.get_screen('vsr')
        vsr.visualizar_produtores()
        sm.current = 'vsr'

    def criar_tabela(self):
        self.conexao = sqlite3.connect('controle.db')
        self.cursor = self.conexao.cursor()
        sql = """ CREATE TABLE IF NOT EXISTS produtores(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT (50) NOT NULL,
                    endereco TEXT (50),
                    cpf TEXT (50),
                    inscricao TEXT (50),
                    coordenadas TEXT (50),
                    login TEXT (50),
                    senha TEXT (50))"""
        self.cursor.execute(sql)

    def tabela_pendencias(self):
        self.conexao = sqlite3.connect('controle.db')
        self.cursor = self.conexao.cursor()
        sql = """CREATE TABLE IF NOT EXISTS pendencias (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    produtor_id INTEGER,
                    produto TEXT NOT NULL,
                    quantidade INTEGER NOT NULL,
                    data CURRENT_TIMESTAMP,
                    devolucao CURRENT_TIMESTAMP,
                    data_compra CURRENT_TIMESTAMP,
                    data_devolucao CURRENT_TIMESTAMP,
                    FOREIGN KEY(produtor_id) REFERENCES produtores(id))"""
        self.cursor.execute(sql)

    def tabela_produtos(self):
        self.conexao = sqlite3.connect('controle.db')
        self.cursor = self.conexao.cursor()
        sql = """CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_produto TEXT NOT NULL,
                    gtin TEXT NOT NULL
                    )"""
        self.cursor.execute(sql)

    def inserir_dados(self, txt_nome, txt_end, txt_cpf, txt_insc, txt_coord, txt_log, txt_sen):
        edt = sm.get_screen('create')
        self.cursor.execute("""INSERT INTO produtores
                                (nome, endereco, cpf, inscricao, coordenadas, login, senha) VALUES
                                (?, ?, ?, ?, ?, ?, ?)""",
                            (txt_nome, txt_end, txt_cpf, txt_insc, txt_coord, txt_log, txt_sen))
        self.conexao.commit()
        edt.lbl_resposta.text = "Produtor Cadastrado com Sucesso!"

    def cadastrar_produto(self, txt_nmpd, txt_gtin):
        edt = sm.get_screen('cadastrarproduto')
        self.cursor.execute("""INSERT INTO produtos (nome_produto, gtin) VALUES (?, ?)""", (txt_nmpd, txt_gtin))
        self.conexao.commit()
        edt.lbl_resposta.text = 'Produto Cadastrado Com Sucesso!'

    def registrar_venda(self, txt_prod, txt_quant, txt_proid, data, devolucao, data_compra, data_devolucao):
        edt = sm.get_screen('venda')
        self.cursor.execute("""INSERT INTO pendencias
                                (produto, quantidade, produtor_id,
                                data, devolucao, data_compra, data_devolucao) VALUES
                                (?, ?, ?, ?, ?,?,?)""",
                           (txt_prod, txt_quant, txt_proid, data, devolucao, data_compra, data_devolucao))
        self.conexao.commit()
        edt.lbl_resposta.text = 'Venda Efetuada Com Sucesso!'

    def dados_produtor(self, id, slc):
        self.cursor.execute("SELECT * FROM produtores WHERE id = ?", (id))
        self.conexao.commit()
        records = self.cursor.fetchall()
        slc = sm.get_screen('cadastrocompletoprodutor')
        for row in records:
            slc.atualizar_form(str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]))

    def dados_cadastro(self, id, slc):
        self.cursor.execute("SELECT * FROM produtores WHERE id = ?", (id))
        self.conexao.commit()
        records = self.cursor.fetchall()
        slc = sm.get_screen('visualizarcadastro')
        for row in records:
            slc.atualizar_form(str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]))



    def build(self):
        App.title = "ALRA"
        Window.size = (320, 480)
        self.criar_tabela()
        self.tabela_produtos()
        self.tabela_pendencias()
        return sm
CrudKivy().run()
