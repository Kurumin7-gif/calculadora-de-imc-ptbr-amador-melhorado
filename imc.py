
## Addons

from operator import truediv
import colorama
from colorama import Fore, Style, Back

## INICIO ##
restart = True

## Digite seus dados

print ("Calcule seu IMC agora mesmo!")
Altura = float(input("Digite sua Altura: "))
Massa = float(input("Digite sua Massa: "))

# Calculo do IMC
IMC = Massa/Altura**2

## Resultado
print ("Seu IMC é: ""{:.2f}".format(IMC))

## Condição
if IMC < 18.5 :
  print (Fore.YELLOW + "Você está abaixo do peso!")
elif IMC < 25 :
  print (Fore.GREEN + "Peso Normal, continue assim! =)")
elif IMC < 30 :
    print (Fore.YELLOW + "Você está Acima do peso!")
elif IMC < 35 :
    print (Fore.RED + "Obesidade Grau 1!")
elif IMC < 40 :
    print (Fore.RED + "Obesidade Grau 2!!")
else:
    print (Fore.RED + "Obesidade Grau 3 ou Mórbida!!!!")
restart = input("Deseja refazer o teste? sim/não --> ")
if restart == "sim" or restart == "s":
   restart
elif restart == "n" or restart == "não":
    print ("Obrigado por usar! Volte sempre.")
else:
   print ("não entendi, volte depois")
   exit ()

## Fim

## feature can be add: yes and no option restart



