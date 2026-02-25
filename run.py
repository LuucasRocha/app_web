from app import create_app

"""
Arquivo responsável por iniciar o servidor da aplicação.
"""
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)