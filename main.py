
import os
from sqlalchemy import create_engine , Column, String, Integer
from sqlalchemy.orm  import sessionmaker, declarative_base 

# Criando banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")



# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando Tabela
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id" ,Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email",String)
    senha = Column("senha", String)
                     

    # Definindo Atributos da Classe.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando Tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

# Salvar no Banco de dados.
os.system("cls || clear")

print("Solicitando dados para o usuário")
inserir_nome = input("Dgite seu nome")
inserir_email = input("Dgite seu email")
inserir_senha = input("Dgite sua senha")
        


usuario = Usuario(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(usuario)
session.commit()




# Listando todos os usuraios do banco de dados.
print("\nExibindo todos os usuraios do banco de dados.")
lista_usuarios = session.query(Usuario).all()

# Read
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

#fechando conexão
session.close()