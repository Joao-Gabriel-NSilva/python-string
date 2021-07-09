import re  #biblioteca de expressões regulares (padrões)

padrao = "[0-9]{4,5}-?[0-9]{4}"
teste = "[a-z].[a-z]"


texto1 = "Meus números são 95362-6782, 85902467, 902341457, 2567-0846"

retorno = re.findall(padrao, texto1)
print(retorno)
