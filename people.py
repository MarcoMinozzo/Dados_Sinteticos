import csv
from faker import Faker

# Gerar dados aleatórios
fake = Faker()
data = [(i + 1, fake.first_name(), fake.last_name()) for i in range(1000000)]

# Criar e escrever no arquivo CSV
csv_filename = "people.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["PersonId", "FirstName", "LastName"])  # Cabeçalho
    writer.writerows(data)

print(f"Arquivo CSV '{csv_filename}' criado com 1.000.000 registros!")
