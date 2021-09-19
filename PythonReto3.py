from math import ceil
  
def bancoAmigo(nuip: int, depositos: list) -> tuple:
  
    interesAhorro = 0
    ahorroTotal = 0
    for item in depositos:

      ahorroTotal += item
      interes = 0

      if item >= 300000:
        interes = (interesAhorro + ahorroTotal) * 5 / 100

      interesAhorro += interes

    if ahorroTotal >= 3600000:
      interesAdicional = ahorroTotal * 12 / 100
    else:
      interesAdicional = ahorroTotal * 7 / 100
      
    interesGenerado = interesAdicional + interesAhorro
    montoFinal = interesGenerado + ahorroTotal
    
    return nuip, ahorroTotal, ceil(interesGenerado), ceil(montoFinal)

print(bancoAmigo(10254852, [124274,0,0,2478545,0,124578,0,0,0,0,0,2154657]))
print ( bancoAmigo (2148542 ,[300000 ,450000 ,0 ,0 ,0 ,0 ,260000 ,0 ,500000 ,0 ,420000 ,0]))