import json

nome = input("Digite seu nome: ")
aluno = {
  "nome": nome,
  "matematica": 7.8,
  "portugues": 5.3,
  "soma" : 0
}


matematica = aluno["matematica"]
portugues = aluno["portugues"]


soma_de_valor = matematica + portugues
aluno["soma"] = soma_de_valor

with open("notas.json", 'a') as arquivo:
    json.dump(aluno, arquivo, ensure_ascii=False)

print("Notas carregadas:")
print(f"Matemática: {matematica}")
print(f"Português: {portugues}")
print(f"Soma das notas: {soma_de_valor}")