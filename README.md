# Ticket Reservation System

## Descrizione del Progetto
Ticket Reservation System è un'applicazione web per la prenotazione di biglietti per eventi. Gli utenti possono visualizzare gli eventi disponibili, cercarli per nome o parola chiave della descrizione, e prenotare i biglietti dopo essersi autenticati. Il pagamento dei biglietti viene gestito tramite Stripe.

## Funzionalità Principali
1. **Visualizzazione degli Eventi**: Nella pagina principale, vengono mostrati tutti gli eventi disponibili. Gli utenti possono cercare eventi specifici inserendo il nome dell'evento o parole chiave della descrizione.
2. **Autenticazione Utenti**: Gli utenti devono essere autenticati per poter prenotare biglietti. La registrazione e il login sono necessari.
3. **Prenotazione Biglietti**: Una volta autenticati, gli utenti possono selezionare l'evento desiderato e il numero di posti. Successivamente, verrà richiesto di inserire i dettagli della carta di pagamento.
4. **Gestione Pagamenti con Stripe**: Il pagamento viene elaborato utilizzando Stripe. Sono supportate diverse carte di test per simulare vari scenari di pagamento.
5. **Gestione degli Eventi**: Solo utenti con permessi specifici possono creare e gestire eventi.

## Requisiti
- Python 3.x
- Django 3.x o superiore
- Stripe API keys (sia pubbliche che segrete)

## Installazione
1. Clona il repository:
    ```bash
    git clone https://github.com/tuo-username/ticket-reservation-system.git
    cd ticket-reservation-system
    ```
2. Installa le dipendenze:
    ```bash
    pip install -r requirements.txt
    ```
3. Configura le chiavi API di Stripe nel tuo `settings.py`:
    ```python
    STRIPE_PUBLIC_KEY = 'your-public-key'
    STRIPE_SECRET_KEY = 'your-secret-key'
    ```
4. Applica le migrazioni del database:
    ```bash
    python manage.py migrate
    ```
5. Avvia il server di sviluppo:
    ```bash
    python manage.py runserver
    ```

## Utilizzo
### Navigazione
- **Pagina Principale**: Visualizza tutti gli eventi disponibili. Puoi cercare eventi specifici utilizzando la barra di ricerca.
- **Dettagli Evento**: Clicca su un evento per vedere i dettagli e avviare il processo di prenotazione.

### Prenotazione Biglietti
1. **Autenticazione**: Effettua il login o registrati se non hai ancora un account.
2. **Selezione Posti**: Inserisci il numero di biglietti desiderati e controlla la disponibilità.
3. **Pagamento**: Inserisci i dettagli della carta di pagamento.
   - Numero di carta: Vedi la sezione successiva per i numeri di carta di test.
   - Data di scadenza: Qualsiasi data futura (es. 12/34).
   - CVC: Qualsiasi combinazione di tre cifre (es. 123).
   - CAP: Qualsiasi codice postale valido.
4. **Conferma**: Dopo il pagamento, la prenotazione verrà registrata e riceverai una conferma.

### Carte di Test per Stripe
Puoi utilizzare i seguenti numeri di carta di test per simulare i pagamenti:

1. **Pagamento Riuscito**
   - **Visa**: `4242 4242 4242 4242`
2. **Pagamento Rifiutato (Fondi Insufficienti)**
   - **Visa**: `4000 0000 0000 9995`
3. **Carta Scaduta**
   - **Visa**: `4000 0000 0000 0069`
4. **CVC Errato**
   - **Visa**: `4000 0000 0000 0127`

### Gestione Eventi
Solo utenti con permessi specifici possono creare e gestire eventi.

## Implementazione del Pagamento con Stripe
Il pagamento viene gestito utilizzando Stripe. Quando un utente effettua una prenotazione:
1. Viene creato un `PaymentIntent` tramite l'API di Stripe.
2. L'utente inserisce i dettagli della carta e Stripe elabora il pagamento.
3. Se il pagamento è riuscito, la prenotazione viene confermata e aggiornata nel database.
