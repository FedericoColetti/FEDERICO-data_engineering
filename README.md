# Data Engineering ETL Pipeline & Scheduler

## 📋 Descrizione

Un **pipeline ETL completo** che estrae dati sporchi da CSV, li pulisce e li carica automaticamente in un database PostgreSQL ogni notte.

Questo progetto dimostra competenze fondamentali di **Data Engineering**: data validation, ETL processing, database design, e automazione dei processi.

---

## 🎯 Cosa fa

1. **Estrazione (E)**: Legge dati da file CSV sporchi
2. **Trasformazione (T)**: Pulisce e valida i dati
   - Rimuove righe con ID cliente mancante
   - Valida il formato delle date
   - Valida gli ID cliente
3. **Caricamento (L)**: Inserisce i dati nel database PostgreSQL
4. **Automazione**: Lo scheduler esegue il processo ogni notte automaticamente alle 2:00 AM

---

## 📁 Struttura del Progetto
---

## 🛠️ Tecnologie Usate

- **Python 3.x** - Linguaggio principale
- **PostgreSQL** - Database
- **psycopg2** - Connettore Python-PostgreSQL
- **Pandas** - Data manipulation
- **Schedule** - Job scheduler
- **GitHub** - Version control

---

## 🚀 Come Usarlo

### Prerequisiti
```bash
pip install psycopg2 pandas schedule
```

### Configurazione Database
```python
# Credenziali di connessione in etl_script.py
host = "localhost"
database = "postgres"
user = "postgres"
password = "347589"
```

### Esegui l'ETL manualmente
```bash
python etl_script.py
```

### Avvia lo scheduler automatico
```bash
python scheduler.py
```
Lo scheduler girerà in background e eseguirà l'ETL ogni giorno alle 2:00 AM.

---

## 📊 Risultati

- ✅ **4 clienti** nel database
- ✅ **5+ ordini** caricati automaticamente
- ✅ **100% data validation** - Nessun dato sporco nel database
- ✅ **Automazione 24/7** - Zero intervento manuale

---

## 📈 Cosa Ho Imparato

✅ SQL avanzato (SELECT, WHERE, ORDER BY, JOIN, GROUP BY)
✅ Python per data processing
✅ Progettazione database relazionali
✅ ETL pipeline da zero
✅ Automazione di processi
✅ Git e GitHub

---

## 🔄 Prossimi Passi

- ☁️ Migrare su AWS/Google Cloud
- 🔥 Scalare con Apache Spark per Big Data
- 📊 Aggiungere monitoring e logging
- 🚨 Implementare error handling avanzato

---

## 👤 Autore

**Federico** - Data Engineer in Learning
- GitHub: [@FedericoColetti](https://github.com/FedericoColetti)

---

*Creato il 21 Giugno 2026 - Primo progetto Data Engineering!* 🎉
