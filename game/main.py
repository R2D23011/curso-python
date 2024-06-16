import random

options = ('piedra', 'papel', 'tijera')
user_score = 0
computer_score = 0
rounds = 1

print('Hola, bienvenido')
print('Vamos a jugar piedra, papel o tijera')
user_name = input('Ingresa tu nombre => ')
print('Hola ', user_name, '!')
print('*'*18)
print('ROUND ', rounds)
print('*'*18)
print('Elige una opcion a continuacion')


user_option = input('piedra, papel o tijera => ')
user_option=user_option.lower()
computer_option = random.choice(options)

while True:
  if not user_option in options:
    print('Elige una opcion valida')
    user_option = input('Elije nuevamente: piedra, papel o tijera => ').lower()
  else:
    break

print('Tu eleccion fue => ', user_option)
print('El CPU eligio =>' , computer_option)


if user_option == computer_option:
  print('*' * 18)
  print('Empate!')
  print('*' * 18)
  computer_score += 0
  user_score += 0

elif user_option == 'piedra':
  if computer_option == 'tijera':
    print('piedra gana a tijera')
    print('*' * 18)
    print(user_name, ' ganó!')
    print('*' * 18)
    user_score += 1
  else:
    print('papel gana a piedra')
    print('*' * 18)
    print(user_name, ' perdió!')
    print('*' * 18)
    computer_score += 1

elif user_option == 'papel':
  if computer_option == 'piedra':
    print('papel gana a piedra')
    print('*' * 18)
    print(user_name, 'ganó!!')
    print('*' * 18)
    user_score += 1
  else:
    print('tijera gana a papel')
    print('*' * 18)
    print(user_name, 'perdió!')
    print('*' * 18)
    computer_score +=1

elif user_option == 'tijera':
  if computer_option == 'papel':
    print('*' * 18)
    print('tijera gana a papel')
    print(user_name, 'ganó!!')
    print('*' * 18)
    user_score +=1
  else:
    print('piedra gana a tijera')
    print('*' * 18)
    print(user_name, 'perdió!')
    print('*' * 18)
    computer_score +=1

print('Puntuación final:', user_name, '=>', user_score, 'CPU =>', computer_score)
print('*' * 18)

rounds += 1

seguir_jugando = "si"

while seguir_jugando.lower() == "si":
  print("¿Quieres seguir jugando?")
  seguir_jugando = input("Ingresa \"si\" o \"no\": ")
  if seguir_jugando.lower() == "si":
    print('*'*18)
    print('ROUND ', rounds)
    print('*'*18)
    user_option = input('piedra, papel o tijera => ')
    user_option=user_option.lower()
    computer_option = random.choice(options) 

    while True:
      if not user_option in options:
        print('Elige una opcion valida')
        user_option = input('Elije nuevamente: piedra, papel o tijera => ').lower()
      else:
        break

    print('Tu eleccion fue => ', user_option)
    print('El CPU eligio =>' , computer_option)

    if user_option == computer_option:
      print('*' * 18)
      print('Empate!')
      print('*' * 18)
      user_score += 0
      computer_score += 0

    elif user_option == 'piedra':
      if computer_option == 'tijera':
        print('piedra gana a tijera')
        print('*' * 18)
        print(user_name, ' ganó!')
        print('*' * 18)
        user_score += 1
      else:
        print('papel gana a piedra')
        print('*' * 18)
        print(user_name, ' perdió!')
        print('*' * 18)
        computer_score +=1

    elif user_option == 'papel':
      if computer_option == 'piedra':
        print('papel gana a piedra')
        print('*' * 18)
        print(user_name, 'ganó!!')
        print('*' * 18)
        user_score += 1
      else:
        print('tijera gana a papel')
        print('*' * 18)
        print(user_name, 'perdió!')
        print('*' * 18)
        computer_score +=1

    elif user_option == 'tijera':
      if computer_option == 'papel':
        print('tijera gana a papel')
        print('*' * 18)
        print(user_name, 'ganó!!')
        print('*' * 18)
        user_score += 1
      else:
        print('piedra gana a tijera')
        print('*' * 18)
        print(user_name, 'perdió!')
        print('*' * 18)
        computer_score +=1
        
    print('Puntuación final:', user_name, '=>', user_score, 'CPU =>', computer_score)
    rounds += 1
    
    if computer_score == 5:
      print('CPU WINS')
      break
  
    elif user_score == 5:
      print('YOU WIN')
      break