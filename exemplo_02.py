
constante_bonus = 1000
nome_usuario = input("Digite  o seu nome: " )

salario_usuario = float(input("Digite  o valor do seu salário: " ))

bonus_usuario = float(input("Digite  o valor do bonus recebido: " ))

valor_do_bonus = 1000 +salario_usuario * bonus_usuario

print(f"O usuário {nome_usuario}, possui o bonus de {valor_do_bonus}")
