# Latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input('Masukkan suhu dalam celcius : '))
print("suhu adalah ",celcius, "Celcius")

# Reamur
# (4/5) C
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur, "Reamur")


# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ",kelvin, "Kelvin")

# Fahrenheit ke Kelvin
print("\nKONVERSI FAHRENHEIT TO KELVIN\n")

fahrenheit = float(input('Masukkan suhu dalam fahrenheit : '))
print("suhu adalah ",fahrenheit, "Fahrenheit")

celcius = (5/9) * (fahrenheit - 32)
kelvin = celcius + 273
print("suhu dalam kelvin adalah ",kelvin, "Kelvin")

# Kelvin to Fahrenheit
print("\nKONVERSI KELVIN TO FAHRENHEIT\n")

kelvin = float(input('Masukkan suhu dalam kelvin : '))
print("suhu adalah ",kelvin, "Kelvin")

celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit")

