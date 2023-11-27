import random                                                                                                                                                                                                                                                                       

dinero = float(input("Cual es el valor de dinero que gastaste "))

if dinero < 100:
    print("Descuento no aplicado")
else:
    bolauno = random.randint(1, 2)
    bolados = random.randint(3, 4)
    bolatres = random.randint(bolauno, bolados)
    bolacuatro = random.randint(bolatres, 5)
    if bolacuatro == 1:
        print("Descuento no aplicado")
    elif bolacuatro == 2:
        print("Deacuento de 10%")
        print(f"{dinero * 0.9} por favor")
    elif bolacuatro == 3:
        print("descuento de 20%")
        print(f"{dinero * 0.8} por favor")
    elif bolacuatro == 4:
        print("descuento de 30%")
        print(f"{dinero * 0.7} por favor")     
    elif bolacuatro == 5:
        print("descuento de 40%")
        print(f"{dinero * 0.6} por favor")
