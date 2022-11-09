nome = input("Escreva seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"Boa noite, seu nome é {nome} ")
print("Sua idade é {}".format(idade))
dobro= idade*2
print ("O dobro da sua idade é: {}".format(dobro))
if idade >=18 and genero == "M":
  print ("Você é maior de idade, agora pode dirigir! E precisa fazer o servicio militar")
else: 
  print("Você é joven, não pode dirigir!")

genero= input("Informe o gênero, M=Masculino, F=Feminino, O=Outros)
              