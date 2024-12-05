import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from openpyxl import Workbook
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

# Configuração do Banco de Dados
conn = sqlite3.connect('estoque.db')
c = conn.cursor()

# Criação das tabelas
c.execute('''CREATE TABLE IF NOT EXISTS produto (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                preco REAL NOT NULL,
                rua TEXT NOT NULL,
                prateleira TEXT NOT NULL,
                coluna TEXT NOT NULL)''')

c.execute('''CREATE TABLE IF NOT EXISTS movimentacao (
                id INTEGER PRIMARY KEY,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL,
                tipo TEXT NOT NULL,
                data TEXT NOT NULL,
                FOREIGN KEY (produto_id) REFERENCES produto (id))''')

conn.commit()

# Inserir produtos de teste no banco de dados
produtos_teste = [
    ("Camiseta", "Roupas", 50, 39.99, "Rua A", "Prateleira 1", "Coluna 1"),
    ("Caneca", "Utensílios", 200, 19.99, "Rua B", "Prateleira 2", "Coluna 1"),
    ("Celular", "Eletrônicos", 30, 1999.99, "Rua C", "Prateleira 3", "Coluna 2"),
    ("Notebook", "Eletrônicos", 20, 5999.99, "Rua D", "Prateleira 4", "Coluna 3"),
    ("Caderno", "Papelaria", 100, 9.99, "Rua E", "Prateleira 5", "Coluna 4")
]

# Verificar se já existem produtos para não duplicar
c.execute("SELECT COUNT(*) FROM produto")
if c.fetchone()[0] == 0:
    c.executemany('''INSERT INTO produto (nome, categoria, quantidade, preco, rua, prateleira, coluna) 
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', produtos_teste)
    conn.commit()

# Classe Estoque
class Estoque:
    def __init__(self):
        self.conn = sqlite3.connect('estoque.db')
        self.c = self.conn.cursor()

    def cadastrar_produto(self, nome, categoria, quantidade, preco, rua, prateleira, coluna):
        try:
            self.c.execute('''INSERT INTO produto 
                              (nome, categoria, quantidade, preco, rua, prateleira, coluna) 
                              VALUES (?, ?, ?, ?, ?, ?, ?)''',
                           (nome, categoria, quantidade, preco, rua, prateleira, coluna))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar produto: {e}")

    def gerar_relatorio_estoque(self):
        self.c.execute("SELECT nome, categoria, quantidade, preco FROM produto")
        return self.c.fetchall()

    def exportar_relatorio_excel(self, file_name):
        try:
            produtos = self.gerar_relatorio_estoque()
            if not produtos:
                messagebox.showinfo("Exportação", "Nenhum produto para exportar.")
                return

            # Criação do arquivo Excel
            wb = Workbook()
            ws = wb.active
            ws.title = "Relatório de Estoque"

            # Cabeçalhos
            ws.append(["Nome", "Categoria", "Quantidade", "Preço"])

            # Dados
            for produto in produtos:
                ws.append(produto)

            wb.save(file_name)
            messagebox.showinfo("Exportação", f"Relatório salvo em {file_name}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar relatório: {e}")

    def buscar_produtos(self, nome, categoria):
        self.c.execute("SELECT * FROM produto WHERE nome LIKE ? AND categoria LIKE ?", (f"%{nome}%", f"%{categoria}%"))
        return self.c.fetchall()

    def registrar_movimentacao(self, produto_id, quantidade, tipo):
        try:
            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.c.execute('''INSERT INTO movimentacao (produto_id, quantidade, tipo, data) 
                              VALUES (?, ?, ?, ?)''', (produto_id, quantidade, tipo, data))
            self.conn.commit()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao registrar movimentação: {e}")

# Tela de Login
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Login", font=("Arial", 24), foreground="darkblue")
        label.pack(pady=20)

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self._create_input("Usuário", self.username_var)
        self._create_input("Senha", self.password_var)

        ttk.Button(self, text="Entrar", command=self.login).pack(pady=10)

    def _create_input(self, label_text, variable):
        ttk.Label(self, text=label_text).pack(pady=5)
        ttk.Entry(self, textvariable=variable, show="*" if "Senha" in label_text else "").pack(pady=5)

    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()

        # Validação simples
        if username == "admin" and password == "admin":
            self.controller.show_frame("MainPage")
        else:
            messagebox.showerror("Erro", "Credenciais inválidas.")

# Tela Principal
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Sistema de Gerenciamento de Estoque", font=("Arial", 24), foreground="darkblue")
        label.pack(pady=20)

        ttk.Button(self, text="Cadastrar Produto", command=lambda: controller.show_frame("CadastroPage")).pack(pady=10)
        ttk.Button(self, text="Relatório de Estoque", command=lambda: controller.show_frame("RelatorioPage")).pack(pady=10)
        ttk.Button(self, text="Buscar Produto", command=lambda: controller.show_frame("BuscaPage")).pack(pady=10)
        ttk.Button(self, text="Movimentação de Estoque", command=lambda: controller.show_frame("MovimentacaoPage")).pack(pady=10)

# Página de Cadastro de Produto
class CadastroPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Cadastro de Produto", font=("Arial", 24), foreground="darkblue")
        label.pack(pady=10)

        # Variáveis de entrada
        self.nome_var = tk.StringVar()
        self.categoria_var = tk.StringVar()
        self.quantidade_var = tk.IntVar()
        self.preco_var = tk.DoubleVar()
        self.rua_var = tk.StringVar()
        self.prateleira_var = tk.StringVar()
        self.coluna_var = tk.StringVar()

        # Campos
        self._create_input("Nome", self.nome_var)
        self._create_input("Categoria", self.categoria_var)
        self._create_input("Quantidade", self.quantidade_var)
        self._create_input("Preço", self.preco_var)
        self._create_input("Rua", self.rua_var)
        self._create_input("Prateleira", self.prateleira_var)
        self._create_input("Coluna", self.coluna_var)

        ttk.Button(self, text="Cadastrar", command=self.cadastrar_produto).pack(pady=10)
        ttk.Button(self, text="Voltar", command=lambda: controller.show_frame("MainPage")).pack(pady=10)

    def _create_input(self, label_text, variable):
        ttk.Label(self, text=label_text).pack(pady=5)
        ttk.Entry(self, textvariable=variable).pack(pady=5)

    def cadastrar_produto(self):
        self.controller.estoque.cadastrar_produto(
            self.nome_var.get(),
            self.categoria_var.get(),
            self.quantidade_var.get(),
            self.preco_var.get(),
            self.rua_var.get(),
            self.prateleira_var.get(),
            self.coluna_var.get()
        )

# Página de Relatório de Estoque
class RelatorioPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Relatório de Estoque", font=("Arial", 24), foreground="darkblue")
        label.pack(pady=10)

        self.canvas = None
        ttk.Button(self, text="Gerar Relatório Gráfico", command=self.gerar_grafico).pack(pady=10)
        ttk.Button(self, text="Exportar para Excel", command=self.exportar_excel).pack(pady=10)
        ttk.Button(self, text="Voltar", command=lambda: controller.show_frame("MainPage")).pack(pady=10)

    def gerar_grafico(self):
        dados = self.controller.estoque.gerar_relatorio_estoque()
        if not dados:
            messagebox.showinfo("Relatório", "Nenhum dado para gerar gráfico.")
            return
        
        categorias = [item[1] for item in dados]
        quantidades = [item[2] for item in dados]

        fig, ax = plt.subplots()
        ax.bar(categorias, quantidades)
        ax.set_xlabel('Categoria')
        ax.set_ylabel('Quantidade')
        ax.set_title('Relatório de Estoque')

        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(fig, self)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def exportar_excel(self):
        self.controller.estoque.exportar_relatorio_excel("relatorio_estoque.xlsx")

# Página de Busca de Produto
class BuscaPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Buscar Produto", font=("Arial", 24), foreground="darkblue")
        label.pack(pady=10)

        # Variáveis de busca
        self.nome_var = tk.StringVar()
        self.categoria_var = tk.StringVar()

        self._create_input("Nome", self.nome_var)
        self._create_input("Categoria", self.categoria_var)

        ttk.Button(self, text="Buscar", command=self.buscar_produtos).pack(pady=10)
        ttk.Button(self, text="Voltar", command=lambda: controller.show_frame("MainPage")).pack(pady=10)

    def _create_input(self, label_text, variable):
        ttk.Label(self, text=label_text).pack(pady=5)
        ttk.Entry(self, textvariable=variable).pack(pady=5)

    def buscar_produtos(self):
        nome = self.nome_var.get()
        categoria = self.categoria_var.get()
        produtos = self.controller.estoque.buscar_produtos(nome, categoria)
        if produtos:
            messagebox.showinfo("Produtos Encontrados", f"Produtos encontrados: {produtos}")
        else:
            messagebox.showinfo("Busca", "Nenhum produto encontrado.")

# Página de Movimentação de Estoque
class MovimentacaoPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Movimentação de Estoque", font=("Arial", 24), foreground="darkblue")
        label.pack(pady=20)

        self.produto_var = tk.StringVar()
        self.quantidade_var = tk.IntVar()
        self.tipo_var = tk.StringVar()

        self._create_input("Produto", self.produto_var)
        self._create_input("Quantidade", self.quantidade_var)
        self._create_input("Tipo de Movimentação (Entrada/Saída)", self.tipo_var)

        ttk.Button(self, text="Registrar Movimentação", command=self.registrar_movimentacao).pack(pady=10)
        ttk.Button(self, text="Voltar", command=lambda: controller.show_frame("MainPage")).pack(pady=10)

    def _create_input(self, label_text, variable):
        ttk.Label(self, text=label_text).pack(pady=5)
        ttk.Entry(self, textvariable=variable).pack(pady=5)

    def registrar_movimentacao(self):
        produto_nome = self.produto_var.get()
        quantidade = self.quantidade_var.get()
        tipo = self.tipo_var.get()

        if tipo not in ['Entrada', 'Saída']:
            messagebox.showerror("Erro", "Tipo de movimentação deve ser 'Entrada' ou 'Saída'.")
            return

        self.controller.estoque.c.execute("SELECT id, quantidade FROM produto WHERE nome = ?", (produto_nome,))
        produto = self.controller.estoque.c.fetchone()

        if produto is None:
            messagebox.showerror("Erro", f"Produto '{produto_nome}' não encontrado.")
            return

        produto_id, estoque_atual = produto

        if tipo == "Entrada":
            nova_quantidade = estoque_atual + quantidade
        else:
            if estoque_atual < quantidade:
                messagebox.showerror("Erro", "Quantidade insuficiente em estoque.")
                return
            nova_quantidade = estoque_atual - quantidade

        self.controller.estoque.c.execute("UPDATE produto SET quantidade = ? WHERE id = ?", (nova_quantidade, produto_id))
        self.controller.estoque.conn.commit()

        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.controller.estoque.c.execute('''INSERT INTO movimentacao (produto_id, quantidade, tipo, data) 
                                            VALUES (?, ?, ?, ?)''',
                                         (produto_id, quantidade, tipo, data))
        self.controller.estoque.conn.commit()

        messagebox.showinfo("Sucesso", "Movimentação registrada com sucesso!")

# Classe Principal da Aplicação
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gerenciamento de Estoque")
        self.geometry("900x700")
        self.estoque = Estoque()

        self.frames = {}
        for F in (LoginPage, MainPage, CadastroPage, RelatorioPage, MovimentacaoPage, BuscaPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
