print ("*****Suma******")

try:
    n1= int (input("\nIngrese un numero:"))
    n2= int (input("Ingrese otro numero:"))
except:
    print("Ocurrio un error")

print(f"el resultado es {n1+n2}")