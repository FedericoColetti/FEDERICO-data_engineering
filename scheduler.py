import schedule
import time
import subprocess
from datetime import datetime

def esegui_etl():
    print(f"\n[{datetime.now()}] Esecuzione ETL...")
    subprocess.run(['python', 'etl_script.py'])
    print(f"[{datetime.now()}] ETL completato!\n")

# Schedula l'ETL ogni giorno alle 2:00 AM
schedule.every().day.at("02:00").do(esegui_etl)

# Alternative:
# schedule.every().hour.do(esegui_etl)  # Ogni ora
# schedule.every(12).hours.do(esegui_etl)  # Ogni 12 ore

print("Scheduler avviato! L'ETL girerà ogni giorno alle 2:00 AM")
print("Premi Ctrl+C per fermare\n")

# Mantieni lo scheduler in esecuzione
while True:
    schedule.run_pending()
    time.sleep(60)  # Controlla ogni minuto se c'è un task da eseguire