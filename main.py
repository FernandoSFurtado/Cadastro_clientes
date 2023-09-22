from tkinter import *
from tkinter import ttk, Tk

# Criando Janela
janela = Tk()

class Application():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.widgets_frame_cima()
        self.widgets_frame_baixo()
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
        # Criando botão Limpar
        self.bt_limpar = Button(self.frame_cima, text="Limpar",bd=2, bg = "#187db2", fg = "white",
                                font = ("Verdana 8 bold"))
        self.bt_limpar.place(relx=0.2 ,rely=0.1 ,relwidth=0.1 ,relheight=0.15 )
        # Criando botão Buscar
        self.bt_buscar = Button(self.frame_cima, text="Buscar",bd=2, bg = "#187db2", fg = "white",
                                font = ("Verdana 8 bold"))
        self.bt_buscar.place(relx=0.3 ,rely=0.1 ,relwidth=0.1 ,relheight=0.15 )
        # Criando botão Novo
        self.bt_novo = Button(self.frame_cima, text="Novo",bd=2, bg = "#187db2", fg = "white",
                                font = ("Verdana 8 bold"))
        self.bt_novo.place(relx=0.6 ,rely=0.1 ,relwidth=0.1 ,relheight=0.15 )
        # Criando botão Alterar
        self.bt_altera = Button(self.frame_cima, text="Alterar",bd=2, bg = "#187db2", fg = "white",
                                font = ("Verdana 8 bold"))
        self.bt_altera.place(relx=0.7 ,rely=0.1 ,relwidth=0.1 ,relheight=0.15 )
        # Criando botão Apagar
        self.bt_apagar = Button(self.frame_cima, text="Apagar",bd=2, bg = "#187db2", fg = "white",
                                font = ("Verdana 8 bold"))
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

Application()