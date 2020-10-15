import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def fibonacci():
    proximo = 1
    anterior = 0
    limite = 100
    found = 0
    resposta = "<h1>Fibonacci</h1>0,"
    pular_linha = 10
    while found < limite:
        tmp = proximo
        proximo = proximo + anterior
        anterior = tmp
        found += 1
        resposta += str(proximo) + ","
        pular_linha -= 1
        if(pular_linha == 0):
            pular_linha = 10
            resposta += "<br>"
    return resposta


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
