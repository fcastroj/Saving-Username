from database import init_db, guardar_nombre, ver_nombres

def main():
    print("=== Registro de Nombres ===")
    nombre = input("Ingresa tu nombre: ").strip()

    if nombre:
        guardar_nombre(nombre)
        print(f"✅ Nombre '{nombre}' guardado correctamente.")
    else:
        print("⚠️ No se ingresó ningún nombre.")

    print("\n📋 Nombres registrados:")
    ver_nombres()

if __name__ == "__main__":
    init_db()
    main()


print("Test de la aplicación de registro de nombres:")
ver_nombres()
print("La base de datos y la tabla se han inicializado correctamente.")
