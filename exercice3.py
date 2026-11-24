import sqlite3

# Connexion à la base (crée le fichier si inexistant)
conn = sqlite3.connect("clients.db")
cursor = conn.cursor()

print("\n1. Tous les clients")
cursor.execute("SELECT * FROM clients")
for ligne in cursor.fetchall():
    print(ligne)

print("\n2. Clients de Lyon")
cursor.execute("SELECT nom, email FROM clients WHERE ville = ?", ("Lyon",))
for ligne in cursor.fetchall():
    print(ligne)

print("\n3. Clients triés par nom")
cursor.execute("SELECT nom, ville FROM clients ORDER BY nom ASC")
for ligne in cursor.fetchall():
    print(ligne)

print("\n4. Nombre de clients par ville")
cursor.execute("SELECT ville, COUNT(*) FROM clients GROUP BY ville")
for ligne in cursor.fetchall():
    print(ligne)

print("\n5. Modifier une ligne")
cursor.execute("UPDATE clients SET ville = ? WHERE nom = ?", ("Nantes", "Tom Laurent"))
conn.commit()
cursor.execute("SELECT * FROM clients WHERE nom = ?", ("Tom Laurent",))
print(cursor.fetchone())

conn.close()