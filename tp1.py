import math

# Métodos de resolución de ecuaciones no lineales
def biseccion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("El intervalo proporcionado no encierra una raíz.")
    
    iteraciones = 0
    c = a
    while (b - a) / 2 > tol and iteraciones < max_iter:
        c = (a + b) / 2
        if abs(f(c)) < tol:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteraciones += 1
    return c, iteraciones

def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("El intervalo proporcionado no encierra una raíz.")
    
    iteraciones = 0
    c = a
    while abs(f(c)) > tol and iteraciones < max_iter:
        c = b - (f(b) * (a - b)) / (f(a) - f(b))
        if abs(f(c)) < tol:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteraciones += 1
    return c, iteraciones

def punto_fijo(g, x0, tol=1e-6, max_iter=100):
    iteraciones = 0
    x1 = g(x0)
    while abs(x1 - x0) > tol and iteraciones < max_iter:
        x0 = x1
        x1 = g(x0)
        iteraciones += 1
    return x1, iteraciones

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    iteraciones = 0
    x1 = x0 - f(x0) / df(x0)
    while abs(x1 - x0) > tol and iteraciones < max_iter:
        x0 = x1
        x1 = x0 - f(x0) / df(x0)
        iteraciones += 1
    return x1, iteraciones

def secante(f, x0, x1, tol=1e-6, max_iter=100):
    iteraciones = 0
    while abs(x1 - x0) > tol and iteraciones < max_iter:
        x_temp = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_temp
        iteraciones += 1
    return x1, iteraciones

if __name__ == "__main__":
    # 1️⃣ Preguntar qué método(s) quiere usar
    print("\nSeleccione los métodos que desea utilizar:")
    print("1. Bisección")
    print("2. Regula Falsi")
    print("3. Punto Fijo")
    print("4. Newton-Raphson")
    print("5. Secante")
    seleccion = input("\nIngrese los números de los métodos separados por coma (ej. 1,2,3): ")
    seleccion = [int(x.strip()) for x in seleccion.split(',')]

    # 2️⃣ Ingresar la función si al menos un método es elegido
    if seleccion:
        funcion_str = input("\nIngrese la función en términos de x (ejemplo: x**3 - 4*x - 9): ")

        def safe_eval(funcion_str):
            try:
                return lambda x: eval(funcion_str, {"x": x, "math": math, "exp": math.exp, "cos": math.cos})
            except Exception as e:
                print(f"Error al evaluar la función: {e}")
                return None

        f = safe_eval(funcion_str)
        if not f:
            exit()  # Salir si la función no se evalúa correctamente

    # 3️⃣ Pedir datos según el método seleccionado
    if 1 in seleccion or 2 in seleccion:  # Bisección y Regula Falsi necesitan intervalo
        a = float(input("\nIngrese el límite inferior del intervalo: "))
        b = float(input("Ingrese el límite superior del intervalo: "))

    tol = float(input("\nIngrese la tolerancia para el error relativo porcentual: "))
    max_iter = int(input("Ingrese el número máximo de iteraciones: "))

    if 3 in seleccion:  # Punto Fijo necesita x0
     x0_punto_fijo = float(input("\nIngrese un valor inicial para Punto Fijo: "))

     def g(x):
        argumento = -x**2 / 10
        if argumento < -1:
            argumento = -1
        elif argumento > 1:
            argumento = 1
        return math.acos(argumento)

    if 4 in seleccion:  # Newton-Raphson necesita x0 y derivada
        x0_newton = float(input("\nIngrese un valor inicial para Newton-Raphson: "))
        df = lambda x: (f(x + 1e-5) - f(x)) / 1e-5  # Aproximación numérica

    if 5 in seleccion:  # Secante necesita x0 y x1
        x0_secante = float(input("\nIngrese un primer valor inicial para Secante: "))
        x1_secante = float(input("Ingrese un segundo valor inicial para Secante: "))

    # 4️⃣ Ejecutar los métodos seleccionados
    if 3 in seleccion:  # Punto Fijo
        try:
            raiz_punto_fijo, iter_punto_fijo = punto_fijo(g, x0_punto_fijo, tol, max_iter)
            if math.isnan(raiz_punto_fijo):
                print("⚠️ Error en Punto Fijo: Valor fuera del dominio de arccos.")
            else:
                print(f"\n🔹 Punto Fijo: raíz = {raiz_punto_fijo}, iteraciones = {iter_punto_fijo}")
        except Exception as e:
            print(f"⚠️ Error en Punto Fijo: {e}")

    if 4 in seleccion:  # Newton-Raphson
        try:
            raiz_newton, iter_newton = newton_raphson(f, df, x0_newton, tol, max_iter)
            print(f"\n🔹 Newton-Raphson: raíz = {raiz_newton}, iteraciones = {iter_newton}")
        except Exception as e:
            print(f"⚠️ Error en Newton-Raphson: {e}")

    if 5 in seleccion:  # Secante
        try:
            raiz_secante, iter_secante = secante(f, x0_secante, x1_secante, tol, max_iter)
            print(f"\n🔹 Secante: raíz = {raiz_secante}, iteraciones = {iter_secante}")
        except Exception as e:
            print(f"⚠️ Error en Secante: {e}")
