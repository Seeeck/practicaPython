try:
    lista = [1, 2, 3, 4, 5]
    lista[10]
except Exception as e:
    print("Error:",type(e).__name__)