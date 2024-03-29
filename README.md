# 
# Exemplo de API Python Restful
Flask, SQLAlchemy e Alembic

## Development server

Navigate to `http://localhost:5000/cinema`. The app will automatically reload if you change any of the source files.

## API REQUESTS: 

ROTA                           |     HTTP(Verbo)   |        Request        |    Return   |    Description                 |
------------------------------ | ----------------- | --------------------- | ----------- | ------------------------------ |
/cinema/                       |       GET         |          -            |     HTML    | API index                      |
/cinema/filmes                 |       GET         |          -            |     JSON    | List filmes                    |
/cinema/filmes                 |       POST        |       JSON            |     JSON    | Create filme                   |
/cinema/filmes/{title}         |       GET         |     string(title)     |     JSON    | Get filme and atores by title  |
/cinema/filmes/{param}         |       PUT         |     JSON, param       |     JSON    | Update filme by param          |
/cinema/filmes/{title}         |       DELETE      |  JSON, string(title)  |    boolean  | Delete filme by title          |
/cinema/atores                 |       GET         |          -            |     JSON    | List atores                    |
/cinema/atores                 |       POST        |        JSON           |     JSON    | Create ator                    |
/cinema/atores/{id}            |       GET         |       int(id)         |     JSON    | Get ator by id                 |
/cinema/atores/{id}            |       PUT         |    JSON, int(id)      |     JSON    | Update ator by id              |
/cinema/atores/{id}            |       DELETE      |    JSON, int(id)      |    boolean  | Delete ator by id              |