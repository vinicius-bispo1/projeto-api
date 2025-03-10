# Primeiro criamos o ambiente virtual com o VENV

# O Venv é um ambiente virtual usado para criar uma instalação isolada do Python para um projeto,
# Permitindo que cada projeto tenha suas próprias dependências e versões de pacotes, sem interferir em outros projetos

# - Evita confitos entre pacotes de diferentes projetos
# - Mantém dependências organizadas e especificas para cada projeto
# - Evita alterar pacotes do sistema operacional.

# Criando ambiente Virtual

# No Windows -> python -m venv venv
# Ativando o ambiente virtual -> source venv/Scripts/activate
# Para desativar -> deactivate

# No Mac/Linux -> python3 -m venv venv
# Ativando o ambiente virtual -> source venv/bin/activate
# Para desativar -> deactivate

# O que é o Pip? É o gerenciador de pacotes do Python. Ele permite instalar, atualizar e remover bibliotecas e frameworks diretamente do Python Package Index (PyPi), o repositório oficial de pacotes do Python.

# Para verificar se o pip está instalado utilize o comando: pip --version

# Após isso, iremos instalar o Flask com o Pip
# pip install flask

# Antes da parte prática iremos criar um arquivo requirements.txt, para listar todos os módulos para a execução do projeto

# Criando um requirements, coloque o seguinte comando no terminal: pip freeze > requirements.txt

# --------------------------------- 1º PARTE DA AULA -------------------------------------

# Aqui estamos importando a classe Flask dos pacotes baixados que são necessários para criar a aplicação web.
# Uma classe é um modelo que usamos para criar funcionalidades específicas. Ela ajuda a organizar e estruturar melhor o código, permitindo reutilização e fácil manutenção.

# from flask import Flask

# Aqui o app recebe a classe Flask assim estamos dizendo que o app poderá utilizar todas as suas funcionalidades, e colocamos o (__name__) para que dessa forma o flask identifique automaticamente em qual arquivo o projeto está rodando, no caso no app.py ele também entra como uma questão de boas práticas de código.
# app = Flask(__name__)

# Esse @ se chama decorator e utilizamos ele para ligar a rota a função, ou seja quando chamamos @app.route("/") na rota home será associada a função homepage(), basicamente um atalho para conectar funções a rotas no flask
# @app.route('/')
# def homepage():
#     return "<h3>Minha página usando Flask</h3>"

# print(__name__)

# Esse código também entra no escopo de boas práticas, ele garante que o Flask não inicie automaticamente ao importamos um arquivo diferente, somente quando realmente rodarmos o servidor, o app.run(debug=True) ativa o modo de debug que permite que o servidor recarregue automaticamente quando o código muda, e mostra as mensagens de erro detalhadas no navegador.
# if __name__ == "__main__":
#     app.run(debug=True)

# ---------------------------------- 2º PARTE DA AULA -------------------------------------------------------

# Agora que já temos uma rota configurada, precisamos de um banco de dados para guardar os nossos livros, para isso iremos usar o banco de dados que já vem embutido no Python o SQLite3

# SQLite -> É um banco de dados relacional leve e embutido no próprio Python, e que não precisa de servidor rodando, é executado localmente, ideal para aplicações pequenas e médias, como APIs simples e apps locais.

# Porque utilizaremos SQLite ao invés do MYSQL?

# - Leve e rápido
# - Utiliza SQL padrão (INSERT, DELETE, UPDATE, SELECT)
# - Embutido no Python
# - Não há necessidade de configurar servidor

# Por ele já ser integrado ao python não precisamos baixar, apenas importar

from flask import Flask
import sqlite3


app = Flask(__name__)

# Função que irá iniciar o banco de dados


def init_db():
    # Nessa linha estamos abrindo a conexão com o banco de dados sqlite3, se o arquivo do banco de dados não existir ele será criado automaticamente, isso acontece graças ao comando IF NOT EXISTS, o uso do with garante que a conexão seja fechada automaticamente depois que as operações forem concluídas (boa prática para evitar vazamento de memória)
    with sqlite3.connect('database.db') as conn:
        # Traduzindo a linha acima: "Na conexão do sqlite3 conecte o arquivo database.db como conn(connection), o conn será necessário para podermos manipular o banco de dados SQL (inserir, atualizar ou buscar dados)"

        # Agora o conn que está conectado com o arquivo database.db poderá interagir com o banco de dados, nesse comando abaixo estamos criando nossa tabela, precisamos colocar em """ aspas, isso em python é chamado de string multilinha, dessa forma fica melhor de se visualizar do que colocar todas as colunas em uma única linha.
        conn.execute("""CREATE TABLE IF NOT EXISTS livros(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     titulo TEXT NOT NULL,
                     categoria TEXT NOT NULL,
                     autor TEXT NOT NULL,
                     imagem_url TEXT NOT NULL
                     )""")
        # Os tipos de dados INTEGER é equivalente ao INT do MySQl e pode armazenar até 9 quintilhões de números
        # O tipo de dado TEXT é equivalente ao varchar, porém a quantidade de texto que pode armazenar depende da memória ram disponível, se tivermos 2GB de ram disponível poderemos armazenar 2.147.483.647 (Dois bilhões, cento e quarenta e sete milhões, quatrocentos e oitenta e três mil, seiscentos e quarenta e sete caracteres)

        # Se quisermos confirmar que o banco foi criado com sucesso podemos utilizar esse print
        print("Banco de dados inicializado com sucesso! ✅")


init_db()


@app.route('/')
def homepage():
    return "<h3>Minha página usando Flask</h3>"


if __name__ == "__main__":
    app.run(debug=True)
