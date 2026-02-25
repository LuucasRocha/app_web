from flask import Flask

"""
Função fábrica que cria e configura a aplicação Flask.
Retorna:
    app (Flask): instância configurada da aplicação.
"""
def create_app():
    app = Flask(__name__)

    from .routes import register_routes
    # Registro das rotas da aplicação
    register_routes(app)

    return app