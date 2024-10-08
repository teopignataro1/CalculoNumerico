# -*- coding: utf-8 -*-
"""CalculoNumerico.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e_5jK98DxV6Sf7hEJRHYkTdYKbFkZNvV
"""

estudiantes = [
    {"nombre" : "Teo", "notas" : [66, 87, "B", 88]},
    {"nombre" : "Lucas", "notas" : [78, 107, 65, 77]},
    {"nombre" : "Manuel", "notas" : [61, -55, 93, 81.2]},
    {"nombre" : "Pedro", "notas" : ["MB", 97, True, 55]},
    {"nombre" : "José", "notas" : ["A", "A", "MB", "B"]}
]


for estudiante in estudiantes:
  nombre = estudiante["nombre"]
  notas = estudiante["notas"]

  count = 0
  total = 0
  notas_validas = []

  for nota in notas:
    if (type(nota) == int or type(nota) == float) and 0 <= nota <= 100:
      notas_validas.append(nota)
      count += 1
      total += nota
    else:
      print(f"Hay un error en la nota de {nombre}: La nota invalida es {nota}")


  if count > 0:
      promedio = total / count
      print(f"{nombre}: Nota final = {promedio: }")
  else:
      print(f"{nombre}: No hay notas validas")