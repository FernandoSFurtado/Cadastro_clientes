from tkinter import *
from tkinter import ttk, Tk
import sqlite3

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image

import webbrowser

from PIL import ImageTk, Image

# Criando Janela
janela = Tk()

class Relatorios():
    def printCliente(self):
        webbrowser.open("cliente.pdf")
    def gerarRelatorioCliente(self):
        self.c = canvas.Canvas("cliente.pdf")

        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.cidadeRel = self.cidade_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200,790, 'Ficha do Cliente')

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50,700, 'Codigo: ')
        self.c.drawString(50,670, 'Nome: ')
        self.c.drawString(50,640, 'Telefone: ')
        self.c.drawString(50,610, 'Cidade: ')

        self.c.setFont("Helvetica", 18)
        self.c.drawString(150,700, self.codigoRel)
        self.c.drawString(150,670, self.nomeRel)
        self.c.drawString(150,640, self.telefoneRel)
        self.c.drawString(150,610, self.cidadeRel)

        self.c.rect(20, 720, 550, 200, fill=False, stroke=False)

        self.c.showPage()
        self.c.save()
        self.printCliente()

class Funcoes():
    def limpar_tela(self):
        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.telefone_entry.delete(0,END)
        self.cidade_entry.delete(0,END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor(); print("Conectando ao Banco de Dados")
    def desconectar_bd(self):
        self.conn.close(); print("Desconectado do Banco de Dados")
    def criar_bd(self):
        self.conecta_bd()
        # Criando Tabelas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconectar_bd()
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade) VALUES (?,?,?)""",
                            (self.nome, self.telefone, self.cidade))
        self.conn.commit()
        self.desconectar_bd()
        self.select_lista()
        self.limpar_tela()
    def select_lista(self):
        self.lista_cli.delete(*self.lista_cli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC;  """)
        for i in lista:
            self.lista_cli.insert("",END,values=i)
        self.desconectar_bd()
    def ondoubleclick(self, event):
        self.limpar_tela()
        self.lista_cli.selection()

        for i in self.lista_cli.selection():
            col1,col2,col3,col4 = self.lista_cli.item(i,'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" DELETE FROM clientes WHERE cod = ? """,(self.codigo))
        self.conn.commit()

        self.desconectar_bd()
        self.limpar_tela()
        self.select_lista()
    def alterar(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
                            WHERE cod = ? """,(self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()

        self.desconectar_bd()
        self.select_lista()
        self.limpar_tela()
    def busca_cliente(self):
        self.conecta_bd()
        self.lista_cli.delete(*self.lista_cli.get_children())

        self.nome_entry.insert(END,'%')
        nome = self.nome_entry.get()
        self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes 
        WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC """ % nome)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.lista_cli.insert("",END, values=i)
        self.limpar_tela()
        self.desconectar_bd()

class Application(Funcoes,Relatorios):
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.widgets_frame_cima()
        self.widgets_frame_baixo()
        self.criar_bd()
        self.select_lista()
        self.menus()
        janela.mainloop()
    def tela(self):
        self.janela.title("Cadastro de clientes")
        self.janela.configure(background='#1e3743')
        self.janela.geometry('700x500')
        self.janela.resizable(True,True)
        self.janela.maxsize(width=900,height=700)
        self.janela.minsize(width=500, height=400)
    def frames_da_tela(self):
        self.frame_cima = Frame(self.janela, bd = 4, bg="#dfe3ee", highlightbackground='#759fe6',
                                highlightthickness=3)
        self.frame_cima.place(relx=0.02 ,rely=0.02 ,relwidth=0.96 ,relheight=0.46 )

        self.frame_baixo = Frame(self.janela, bd = 4, bg="#dfe3ee", highlightbackground='#759fe6',
                                highlightthickness=3)
        self.frame_baixo.place(relx=0.02 ,rely=0.5 ,relwidth=0.96 ,relheight=0.46 )
    def widgets_frame_cima(self):
        self.canvas_bt_esquerda = Canvas(self.frame_cima, bd=0, bg='#1e3743', highlightbackground='gray',
                                highlightthickness=5)
        self.canvas_bt_esquerda.place(relx=0.19 ,rely=0.08, relwidth=0.22, relheight=0.19 )

        self.canvas_bt_direita = Canvas(self.frame_cima, bd=0, bg='#1e3743', highlightbackground='gray',
                                highlightthickness=5)
        self.canvas_bt_direita.place(relx=0.59 ,rely=0.08, relwidth=0.32, relheight=0.19 )

        # Criando botão Limpar
        '''
        self.imgLimpar = PhotoImage(file='img/limpar.png')
        self.imgLimpar = self.imgLimpar.subsample(3,3)

        self.style = ttk.Style()
        self.style.configure("BW.TButton", relwidth=0.2, relheight=0.8, foreground= "gray",
                             borderwidth=0, bordercolor='gray', background='#dfe3ee', image=self.imgLimpar)
        '''
        self.bt_limpar = Button(self.frame_cima, text="Limpar",bd=2, bg = "#187db2", fg = "white",
                                font = ("Verdana 8 bold"),activebackground='#108ecb'
                                ,activeforeground='white',command=self.limpar_tela)
        self.bt_limpar.place(relx=0.2 ,rely=0.1 ,relwidth=0.1 ,relheight=0.15 )
        # Criando botão Buscar
        '''
        self.imgBuscar = PhotoImage(file='img/buscar.png')
        self.imgBuscar = self.imgBuscar.subsample(3,3)

        self.style = ttk.Style()
        self.style.configure("BW.TButton", relwidth=0.2, relheight=0.8, foreground= "gray",
                             borderwidth=0, bordercolor='gray', background='#dfe3ee', image=self.imgBuscar)
        '''
        self.bt_buscar = Button(self.frame_cima, text="Buscar",bd=2, bg = "#187db2", fg = "white",
                                font = ("Verdana 8 bold"),activebackground='#108ecb'
                                ,activeforeground='white',command=self.busca_cliente)
        self.bt_buscar.place(relx=0.3 ,rely=0.1 ,relwidth=0.1 ,relheight=0.15 )
        # Criando botão Novo
        '''
        self.imgNovo = PhotoImage(file='img/add.png')
        self.imgNovo = self.imgNovo.subsample(3,3)

        self.style = ttk.Style()
        self.style.configure("BW.TButton", relwidth=0.2, relheight=0.8, foreground= "gray",
                             borderwidth=0, bordercolor='gray', background='#dfe3ee', image=self.imgNovo)
        '''
        self.bt_novo = Button(self.frame_cima, text="Novo",bd=2, bg = "#187db2", fg = "white",
                                font = ("Verdana 8 bold"),activebackground='#108ecb'
                                ,activeforeground='white',command=self.add_cliente)
        self.bt_novo.place(relx=0.6 ,rely=0.1 ,relwidth=0.1 ,relheight=0.15 )
        # Criando botão Alterar
        '''
        self.imgAlterar = PhotoImage(file='img/alterar.png')
        self.imgAlterar = self.imgAlterar.subsample(3,3)

        self.style = ttk.Style()
        self.style.configure("BW.TButton", relwidth=0.2, relheight=0.8, foreground= "gray",
                             borderwidth=0, bordercolor='gray', background='#dfe3ee', image=self.imgAlterar)
        '''
        self.bt_altera = Button(self.frame_cima, text="Alterar",bd=2, bg = "#187db2", fg = "white",
                                font = ("Verdana 8 bold"),activebackground='#108ecb'
                                ,activeforeground='white',command=self.alterar)
        self.bt_altera.place(relx=0.7 ,rely=0.1 ,relwidth=0.1 ,relheight=0.15 )
        # Criando botão Apagar
        '''
        self.imgApagar = PhotoImage(file='img/delete.png')
        self.imgApagar = self.imgApagar.subsample(3,3)

        self.style = ttk.Style()
        self.style.configure("BW.TButton", relwidth=0.2, relheight=0.8, foreground= "gray",
                             borderwidth=0, bordercolor='gray', background='#dfe3ee', image=self.imgApagar)
        '''
        self.bt_apagar = Button(self.frame_cima, text="Apagar",bd=2, bg = "#187db2", fg = "white",
                                font = ("Verdana 8 bold"),activebackground='#108ecb'
                                ,activeforeground='white',command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8 ,rely=0.1 ,relwidth=0.1 ,relheight=0.15 )

        # Criando Label e Entry do código
        self.lb_codigo = Label(self.frame_cima, text="Código",bg="#dfe3ee", fg="#187db2")
        self.lb_codigo.place(relx=0.05 ,rely=0.05)

        self.codigo_entry = Entry(self.frame_cima)
        self.codigo_entry.place(relx=0.05 ,rely=0.15 ,relwidth=0.08)

        # Criando Label e Entry do nome
        self.lb_nome = Label(self.frame_cima, text="Nome",bg="#dfe3ee", fg="#187db2")
        self.lb_nome.place(relx=0.05 ,rely=0.35)

        self.nome_entry = Entry(self.frame_cima)
        self.nome_entry.place(relx=0.05 ,rely=0.45 ,relwidth=0.85)

        # Criando Label e Entry do telefone
        self.lb_telefone = Label(self.frame_cima, text="Telefone",bg="#dfe3ee", fg="#187db2")
        self.lb_telefone.place(relx=0.05 ,rely=0.6)

        self.telefone_entry = Entry(self.frame_cima)
        self.telefone_entry.place(relx=0.05 ,rely=0.7 ,relwidth=0.4)

        # Criando Label e Entry do cidade
        self.lb_cidade = Label(self.frame_cima, text="Cidade",bg="#dfe3ee", fg="#187db2")
        self.lb_cidade.place(relx=0.5 ,rely=0.6)

        self.cidade_entry = Entry(self.frame_cima)
        self.cidade_entry.place(relx=0.5 ,rely=0.7 ,relwidth=0.4)
    def widgets_frame_baixo(self):
        self.lista_cli = ttk.Treeview(self.frame_baixo, height = 3, column=("col1","col2","col3","col4"))
        self.lista_cli.heading("#0", text="")
        self.lista_cli.heading("#1", text="Código")
        self.lista_cli.heading("#2", text="Nome")
        self.lista_cli.heading("#3", text="Telefone")
        self.lista_cli.heading("#4", text="Cidade")

        self.lista_cli.column("#0",width=1)
        self.lista_cli.column("#1",width=50)
        self.lista_cli.column("#2",width=200)
        self.lista_cli.column("#3",width=125)
        self.lista_cli.column("#4",width=125)

        self.lista_cli.place(relx=0.01 ,rely=0.03 ,relwidth=0.95 ,relheight=0.95)

        self.scrooolLista = Scrollbar(self.frame_baixo, orient='vertical')
        self.lista_cli.configure(yscroll=self.scrooolLista.set)
        self.scrooolLista.place(relx=0.96, rely=0.035, relwidth=0.03, relheight=0.95)
        self.lista_cli.bind("<Double-1>",self.ondoubleclick)
    def menus(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu2 = Menu(menubar, tearoff=0)

        def Quit(): self.janela.destroy()

        menubar.add_cascade(label="Opções",menu=filemenu)
        menubar.add_cascade(label="Relatorios",menu=filemenu2)

        filemenu.add_command(label="Sair",command=Quit)
        filemenu.add_command(label="Limpa Cliente", command=self.limpar_tela)

        filemenu2.add_command(label="Ficha do Cliente", command=self.gerarRelatorioCliente)



Application()