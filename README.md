# Projeto de Controle de Despesas 💰
Este projeto é uma aplicação web simples desenvolvida com Flask e SQLAlchemy para gerenciar o controle de despesas. O aplicativo permite que o usuário registre, edite, exclua e visualize despesas cadastradas no banco de dados.

### Tecnologias Utilizadas ⚙️
Flask: Framework para desenvolvimento web.
SQLAlchemy: Biblioteca ORM para interação com o banco de dados.
SQLite: Banco de dados leve e embutido para armazenar os dados das despesas.

### Funcionalidades
Cadastrar Despesas: O usuário pode adicionar uma nova despesa, informando a categoria, descrição e valor.
Visualizar Despesas: O usuário pode visualizar uma lista de todas as despesas cadastradas.
Editar Despesas: O usuário pode editar as informações de uma despesa existente.
Excluir Despesas: O usuário pode excluir uma despesa do banco de dados.
### Pré-requisitos
Certifique-se de ter o Python 3 instalado na sua máquina. Para instalar as dependências do projeto, siga os passos abaixo.

## Como Rodar o Projeto 🚀
Clone o repositório

bash
Copiar código
git clone <URL_DO_REPOSITORIO>
cd <DIRETORIO_DO_PROJETO>
Crie e ative um ambiente virtual

Para garantir que o projeto tenha as dependências corretas, crie um ambiente virtual:

No Windows:

bash
Copiar código
python -m venv .venv
.\.venv\Scripts\activate
No macOS/Linux:

bash
Copiar código
python3 -m venv .venv
source .venv/bin/activate
Instale as dependências

Execute o seguinte comando para instalar as bibliotecas necessárias:

bash
Copiar código
pip install -r requirements.txt
Execute o aplicativo

Para rodar o servidor de desenvolvimento do Flask, execute:

bash
Copiar código
python app.py
O aplicativo estará disponível em http://127.0.0.1:5000/.

## Estrutura do Projeto 📁
bash
Copiar código
.
├── app.py               # Código principal do aplicativo Flask
├── despesas.db          # Banco de dados SQLite
├── templates/            # Arquivos HTML
│   ├── index.html       # Tela de listagem de despesas
│   ├── create.html      # Tela para criar novas despesas
│   └── update.html      # Tela para editar despesas
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo

## Como Funciona
Página Inicial (/):

Exibe todas as despesas cadastradas.
Permite acessar a página de criação de nova despesa.
Criar Despesa (/create):

O usuário pode informar a categoria, descrição e valor da despesa e salvar a nova despesa.
Atualizar Despesa (/update/<id>):

O usuário pode editar uma despesa já cadastrada, alterando sua categoria, descrição e valor.
Excluir Despesa (/delete/<id>):

O usuário pode excluir uma despesa específica.


## Como Contribuir 🤝
Fork este repositório.
Crie uma nova branch com sua feature (git checkout -b feature/feature-name).
Comite suas alterações (git commit -am 'Add new feature').
Envie para o branch principal (git push origin feature/feature-name).
Crie um Pull Request.
