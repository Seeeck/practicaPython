try:
    resultado = 15 + "20"
except TypeError as e:
    print(type(e).__name__)