print("Hello")

nome = 'Luiz'
profissao = "Programador"
print(nome, profissao)

#email = input('Digite seu email:')
#senha = input('Digite sua senha:')

#print("email:", email)
#print("senha:", senha)


from iqoptionapi.stable_api import IQ_Option
import os 
from dotenv import load_dotenv


def load_env():
    load_dotenv(".env")
    return os.getenv("EMAIL_IQOPTION"), os.getenv("SENHA_IQOPTION")

email, senha = load_env()
#email = os.environ.get("EMAIL_IQOPTION")
#senha = os.getenv("SENHA_IQOPTION")
print(email, senha)


API = IQ_Option(email, senha)