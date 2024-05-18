def validate_name(name):
    if not name:
        raise ValueError("El nombre del producto no puede estar vacío")
    if type(name) is not str:
        raise ValueError("El nombre del producto debe ser una cadena de texto")

def validate_price(price):
    if price <= 0:
        raise ValueError("El precio del producto debe ser positivo")
    if type(price) not in [int, float]:
        raise ValueError("El precio del producto debe ser un número")

def validate_stock(stock):
    if stock < 0:
        raise ValueError("El stock del producto no puede ser negativo")
    if type(stock) is not int:
        raise ValueError("El stock del producto debe ser un entero")

def validate_product(product):
    validate_name(product.name)
    validate_price(product.price)
    validate_stock(product.stock)
