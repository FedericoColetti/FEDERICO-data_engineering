import psycopg2

# Connessione a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="347589"  
)

cursor = conn.cursor()

# Esegui una query
cursor.execute("SELECT * FROM public.clienti;")
clienti = cursor.fetchall()

# Mostra i risultati
print("CLIENTI NEL DATABASE:")
for cliente in clienti:
    print(cliente)

cursor.close()
conn.close()

import psycopg2

print("Step 1: Inizio script")

try:
    # Connessione a PostgreSQL
    print("Step 2: Connessione al database...")
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="347589"  # La tua password
    )
    print("Step 3: Connessione riuscita!")

    cursor = conn.cursor()
    print("Step 4: Cursor creato")

    # Esegui una query
    cursor.execute("SELECT * FROM public.clienti;")
    clienti = cursor.fetchall()
    print("Step 5: Query eseguita")

    # Mostra i risultati
    print("CLIENTI NEL DATABASE:")
    for cliente in clienti:
        print(cliente)

    cursor.close()
    conn.close()
    print("Step 6: Connessione chiusa - Fine!")

except Exception as e:
    print(f"ERRORE: {e}")


