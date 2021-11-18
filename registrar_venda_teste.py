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

Builder.load_string(open("gui2.kv", encoding="utf-8").read(), rulesonly=True)

class EfetuarVendaScreen(Screen):
    txt_id = ObjectProperty(None)
    txt_prod = ObjectProperty(None)
    txt_quant = ObjectProperty(None)
    data = ObjectProperty(None)
    devolucao = ObjectProperty(None)
    data_compra = ObjectProperty(None)
    data_devolucao = ObjectProperty(None)
    lbl_resposta = ObjectProperty(None)

sm = ScreenManager()
sm.add_widget(EfetuarVendaScreen(name='venda'))
sm.current = 'venda'

class CrudKivy(App):


    def criar_tabela(self):
        self.conexao = sqlite3.connect('control.db')
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
        self.conexao = sqlite3.connect('control.db')
        self.cursor = self.conexao.cursor()
        sql = """CREATE TABLE IF NOT EXISTS pendencias (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    produtor_id INTEGER,
                    produto TEXT NOT NULL,
                    quantidade INTEGER NOT NULL,
                    data TEXT NOT NULL,
                    devolucao TEXT NOT NULL,
                    data_compra TEXT NOT NULL,
                    data_devolucao TEXT NOT NULL"""
        self.cursor.execute(sql)

    def tabela_produtos(self):
        self.conexao = sqlite3.connect('control.db')
        self.cursor = self.conexao.cursor()
        sql = """CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_produto TEXT NOT NULL,
                    gtin TEXT NOT NULL
                    )"""
        self.cursor.execute(sql)


    def registrar_venda(self, txt_prod, txt_quant, txt_proid, data, devolucao, data_compra, data_devolucao):
        edt = sm.get_screen('venda')
        self.cursor.execute("""INSERT INTO pendencias
                                (produto, quantidade, produtor_id,
                                data, devolucao, data_compra, data_devolucao) VALUES
                                (?, ?, ?, ?, ?,?,?)""",
                           (txt_prod, txt_quant, txt_proid, data, devolucao, data_compra, data_devolucao))
        self.conexao.commit()
        edt.lbl_resposta.text = 'Venda Efetuada Com Sucesso!'


    def build(self):
        App.title = "ALRA"
        Window.size = (320, 480)
        self.criar_tabela()
        self.tabela_produtos()
        self.tabela_pendencias()
        return sm
CrudKivy().run()
