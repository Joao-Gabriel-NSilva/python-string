from ExtratorArgumentosUrl import ExtratorArgumentodUrl

url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"
url2 = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=150"

argumento = ExtratorArgumentodUrl(url)
argumento2 = ExtratorArgumentodUrl(url2)

print(argumento.url == argumento2.url)

moedaOrigem, moedaDestino = argumento.extraiArgumentos()
valor = argumento.extraiValor()

print(moedaOrigem, moedaDestino, valor, end='\n\n')
print(argumento)

