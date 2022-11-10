#Funções

preco= 1999.90
imposto=preco*0.5
print (imposto)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto
  
preco= 299
imposto= calcular_imposto(preco)
print(imposto)