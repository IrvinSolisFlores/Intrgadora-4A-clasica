from db import conectar
from ventas import terminal_venta
from decimal import Decimal
from datetime import datetime

if __name__ == "__main__":
    try:
        con = conectar()
        if con.is_connected():
            print(" Conectado correctamente a MySQL")
        con.close()
        input("Presione Enter para iniciar la terminal de venta...")
        terminal_venta()
    except Exception as err:
        print(f" Error al conectar a MySQL: {err}")
