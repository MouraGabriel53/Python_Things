senhas = {
  "gmail": "123",
  "github": "123",
  "netflix": "123",
}

site = input("Digite o nome do site: ").lower()

if site in senhas:
  print(f"A senha para o site {site} é: {senhas[site]}")
else:
  print(f"Senha não encontrada para o site {site}.")