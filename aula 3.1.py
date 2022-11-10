#Funções

preco= 1999.90
imposto=preco*0.5
print (imposto)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto
  
preco= 299
imposto= calcular_imposto(preco)
print(imposto)
valores = [1.99, 24.50, 78.27, 1515.5]
for valor in valores:
print(f"O imposto de {valores} é {calcular_imposto(valores[i])}")
