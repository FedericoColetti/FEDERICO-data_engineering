import pandas as pd
import psycopg2
from datetime import datetime

print("=== INIZIO ETL ===")

# EXTRACT: Leggi il CSV
print("Step 1: Leggendo CSV...")
df = pd.read_csv('ordini_sporchi.csv', sep=',', skipinitialspace=True)
print(f"Trovate {len(df)} righe")

# TRANSFORM: Pulisci i dati
print("\nStep 2: Pulizia dati...")

# Rimuovi righe con cliente_id vuoto
df = df.dropna(subset=['cliente_id'])
print(f"Dopo rimozione cliente_id vuoto: {len(df)} righe")

# Valida le date
def valida_data(data_str):
    try:
        datetime.strptime(str(data_str), '%Y-%m-%d')
        return True
    except:
        return False

df = df[df['data_ordine'].apply(valida_data)]
print(f"Dopo validazione date: {len(df)} righe")

# Rimuovi clienti che non esistono (solo id 1,2,3,4)
clienti_validi = [1, 2, 3, 4]
df = df[df['cliente_id'].isin(clienti_validi)]
print(f"Dopo validazione clienti: {len(df)} righe")

print(f"\nDati puliti: {len(df)} righe")

# LOAD: Carica nel database
print("\nStep 3: Caricamento nel database...")
try:
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="347589"
    )
    cursor = conn.cursor()
    
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO public.ordini (cliente_id, prodotto, prezzo, data_ordine) VALUES (%s, %s, %s, %s)",
            (int(row['cliente_id']), row['prodotto'], row['prezzo'], row['data_ordine'])
        )
    
    conn.commit()
    print(f"Caricate {len(df)} righe nel database!")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"ERRORE nel caricamento: {e}")

print("\n=== FINE ETL ===")