
# DETERMINAR EL PROMEDIO SEMANAL DEL CLIMA
print("Temperaturas diarias")
temperaturas = {}
for i in range(7):
    temperatura = float(input(f"Ingrese temperatura del día {i+1}: "))
    temperaturas[f"Día {i+1}"] = temperatura

# Calcular promedio
promedio = sum(temperaturas.values()) / len(temperaturas)

print("Temperaturas semanales:")
for dia, temperatura in temperaturas.items():
    print(f"{dia}: {temperatura}°C")
print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")


