from flask import Flask, redirect, url_for
from routes.auth import auth_bp
from routes.user import user_bp
import secrets

app = Flask(__name__)
# Chave secreta para manter o login ativo
app.secret_key = secrets.token_hex(16)

# Registra os módulos de Login e Usuário
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/user')

@app.route('/')
def home():
    # Quando abrir o site, vai direto para /auth/ (seu index.html)
    return redirect(url_for('auth.index'))

if __name__ == '__main__':
    print("Servidor rodando em http://127.0.0.1:5000/auth")
    app.run(debug=True)