# Leia uma cidade
# Dizer se a cidade digitado começa ou nao com a palavra SANTO


city = input("Digite o nome de uma cidade: ").strip()

splitando = city.split()
santo = "santo" in splitando[0].lower()
print(f"o nome da cidade começa com Santo: {santo}")

#////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////


print("=" * 60)
print("ALTERNATIVA 1")

# city = input("Digite o nome de uma cidade: ").strip()

santo1 = splitando[0].lower().find("santo")
print(f"O nome da cidade começa com Santo: {santo1}")


#////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////


print("=" * 60)
print("ALTERNATIVA 2")

# city = input("Digite o nome de uma cidade: ").strip()

print(f"O cidade começa com Santo: {city[:5].lower() == "santo"}")
