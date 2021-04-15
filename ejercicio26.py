try:
    colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
    colores['blanco']
except Exception as e:
    print("Error de :",type(e).__name__)

