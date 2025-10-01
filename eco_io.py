def main():
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))
    
    suma = num1+num2+num3
    media = suma/3
    mayor = max(num1, num2, num3)
    
    print(f"\nLa suma de los 3 números es: {suma}")
    print(f"\nLa media de los 3 números es: {media}")
    print(f"\nEl número mayor es : {mayor}")
    
    
    
    
if __name__ == "__main__":
    main()
    