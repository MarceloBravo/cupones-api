from flask import Flask, request, jsonify
from app.cupones import calcular_precio_final

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta para calcular el precio final con cupón e impuesto
@app.route('/precio', methods=['POST'])
def calcular():
    data = request.get_json()  # Obtener datos del cuerpo de la petición
    precio = data.get("precio")  # Precio base
    cupon = data.get("cupon")    # Código de cupón
    impuesto = data.get("impuesto", 0.19)  # Impuesto (por defecto 19%)
    final = calcular_precio_final(precio, cupon, impuesto)  # Calcular precio final
    return jsonify({"precio_final": final})  # Responder con el precio final