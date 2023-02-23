# Desarrolle un algortimo de la suma y multiplicacion 
#con dos variales o numeros.

n1=int(input("Ingrese el primer numero:"))
n2=int(input("Ingrese el segundo numero:"))
oper =input("Ingrese operador[+,*]")
if oper=="+":
   print("La suma es:",n1+n2)
elif oper=="*":
    print("La multiplicacion es:",n1*n2)
else:
    print("Operador desconocido")