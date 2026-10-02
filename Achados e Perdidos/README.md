# 🔎 Achados & Perdidos

Mini aplicação web desenvolvida com Python, Flask e SQLite para gerenciamento de objetos perdidos e encontrados.

## Funcionalidades

- Cadastro de item perdido ou encontrado
- Nome, descrição, local e contato
- Visualização dos itens
- Filtro por Perdidos e Encontrados
- Busca por palavra-chave
- Marcação de item como Resolvido
- Mensagens de feedback
- Interface visual com HTML, CSS e JavaScript

## Tecnologias

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript

## Como executar

1. Instale o Python.
2. Abra o terminal na pasta do projeto.
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute:

```bash
python app.py
```

5. Acesse:

```text
http://127.0.0.1:5000
```

O banco `database.db` será criado automaticamente na primeira execução.

## Estrutura

```text
achados-perdidos/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   ├── index.html
│   └── cadastrar.html
└── static/
    ├── style.css
    └── script.js
```

## Autor

Projeto desenvolvido para atividade escolar.
