import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()


# Criando tabela.

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    # Definindo campos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    idade = Column("idade", String)
    cpf = Column("cpf", String)
    setor = Column("setor", String)
    funcao = Column("função", String)
    salario = Column("salario", String)
    telefone = Column("telefone", String)


    # Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str, idade: str, cpf: str, setor: str, funcao: str, salario: str, telefone: str):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone


# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

# Salvar no banco de dados.
os.system("cls || clear")

# Create
print("Solicitando dados para adicionar funcionario")
inserir_nome = input("Digite seu nome: ")
inserir_email = input("Digite seu e-mail: ")
inserir_senha = input("Digite seu senha: ")
inserir_idade = input("Digite sua idade: ")
inserir_cpf = input("Digite sua idade: ")
inserir_setor = input("Digite seu setor: ")
inserir_funcao = input("Digite sua função: ")
inserir_salario = input("Digite seu salario: ")
inserir_telefone = input("Digite seu telefone")


usuario = Usuario(nome=inserir_nome, email=inserir_email, senha=inserir_senha, idade=inserir_idade, cpf=inserir_cpf, setor=inserir_setor, funcao=inserir_funcao, salario=inserir_salario, telefone=inserir_telefone)
session.add(usuario)
session.commit()

# Listando todos os usuários do banco de dados.
# Read
print("\nExibindo todos os usuários do bando de dados.")
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha} - {usuario.idade} - {usuario.cpf} - {usuario.setor} - {usuario.funcao} - {usuario.salario} - {usuario.telefone} ")

# Delete
print("\nExcluindo um usuário.")
email_usuario = input("Informe o email do usuário para ser excluido: ")

usuario = session.query(Usuario).filter_by(email = email_usuario).first()
session.delete(usuario)
session.commit()
print(f"{usuario.nome} excluido com sucesso.")

# Listando todos os usuários do banco de dados.
# Read
print("\nExibindo todos os usuários do bando de dados.")
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha} - {usuario.idade} - {usuario.cpf} - {usuario.setor} - {usuario.funcao} - {usuario.salario} - {usuario.telefone}")

# Update
print("\nAtualizando dados do usuário.")
email_usuario = input("Informe o email do usuário que será atualizado: ")

usuario = session.query(Usuario).filter_by(email = email_usuario).first()

usuario.nome = input("Digite seu nome: ")
usuario.email = input("Digite seu e-mail: ")
usuario.senha = input("Digite seu senha: ")

session.commit()

# Listando todos os usuários do banco de dados.
# Read
print("\nExibindo todos os usuários do bando de dados.")
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha} - {usuario.idade} - {usuario.cpf} - {usuario.setor} - {usuario.funcao} - {usuario.salario} - {usuario.telefone}")

# Fechando conexão.
session.close()