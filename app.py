from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///despesas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o SQLAlchemy com o app
db = SQLAlchemy(app)

# Definindo o modelo (tabela) para o banco de dados
class Despesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    valor = db.Column(db.Float, nullable=False)

# Criando o banco de dados dentro do contexto da aplicação
with app.app_context():
    db.create_all()

# Rota principal - Exibe todas as despesas
@app.route('/')
def index():
    despesas = Despesa.query.all()
    return render_template('index.html', despesas=despesas)

# Rota para criar uma nova despesa
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        categoria = request.form['categoria']
        descricao = request.form['descricao']
        valor = float(request.form['valor'])

        nova_despesa = Despesa(categoria=categoria, descricao=descricao, valor=valor)
        db.session.add(nova_despesa)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

# Rota para atualizar uma despesa existente
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    despesa = Despesa.query.get_or_404(id)
    if request.method == 'POST':
        despesa.categoria = request.form['categoria']
        despesa.descricao = request.form['descricao']
        despesa.valor = float(request.form['valor'])
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', despesa=despesa)

# Rota para excluir uma despesa
@app.route('/delete/<int:id>')
def delete(id):
    despesa = Despesa.query.get_or_404(id)
    db.session.delete(despesa)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
