from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "chave-secreta"
DATABASE = "database.db"

def conectar():
    conexao = sqlite3.connect(DATABASE)
    conexao.row_factory = sqlite3.Row
    return conexao

def criar_banco():
    conexao = conectar()
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS itens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            local TEXT NOT NULL,
            contato TEXT NOT NULL,
            tipo TEXT NOT NULL,
            status TEXT DEFAULT 'Pendente'
        )
    """)
    conexao.commit()
    conexao.close()

@app.route("/")
def index():
    filtro = request.args.get("filtro", "Todos")
    busca = request.args.get("busca", "")
    conexao = conectar()

    query = "SELECT * FROM itens WHERE 1=1"
    parametros = []

    if filtro in ["Perdidos", "Encontrados"]:
        query += " AND tipo = ?"
        parametros.append(filtro[:-1])

    if busca:
        query += """ AND (nome LIKE ? OR descricao LIKE ? OR local LIKE ?)"""
        termo = f"%{busca}%"
        parametros.extend([termo, termo, termo])

    query += " ORDER BY id DESC"
    itens = conexao.execute(query, parametros).fetchall()
    conexao.close()

    return render_template("index.html", itens=itens, filtro=filtro, busca=busca)

@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        dados = (
            request.form["nome"],
            request.form["descricao"],
            request.form["local"],
            request.form["contato"],
            request.form["tipo"]
        )
        conexao = conectar()
        conexao.execute("""
            INSERT INTO itens (nome, descricao, local, contato, tipo)
            VALUES (?, ?, ?, ?, ?)
        """, dados)
        conexao.commit()
        conexao.close()
        flash("Item cadastrado com sucesso!", "sucesso")
        return redirect(url_for("index"))

    return render_template("cadastrar.html")

@app.route("/resolver/<int:id>")
def resolver(id):
    conexao = conectar()
    conexao.execute("UPDATE itens SET status = 'Resolvido' WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()
    flash("Item marcado como resolvido!", "sucesso")
    return redirect(url_for("index"))

if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)
