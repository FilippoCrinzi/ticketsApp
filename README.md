Descrizione del Progetto

Ticket Reservation System è un'applicazione web per la prenotazione di biglietti per eventi. Gli utenti possono visualizzare gli eventi disponibili, cercarli per nome o parola chiave della descrizione, e prenotare i biglietti dopo essersi autenticati. Il pagamento dei biglietti viene gestito tramite Stripe, una delle principali piattaforme di pagamento online.

Funzionalità Principali

Visualizzazione degli Eventi: Nella pagina principale, vengono mostrati tutti gli eventi disponibili. Gli utenti possono cercare eventi specifici inserendo il nome dell'evento o parole chiave della descrizione.
Autenticazione Utenti: Gli utenti devono essere autenticati per poter prenotare biglietti. La registrazione e il login sono necessari.
Prenotazione Biglietti: Una volta autenticati, gli utenti possono selezionare l'evento desiderato e il numero di posti. Successivamente, verrà richiesto di inserire i dettagli della carta di pagamento.
Gestione Pagamenti con Stripe: Il pagamento viene elaborato utilizzando Stripe. Sono supportate diverse carte di test per simulare vari scenari di pagamento.
Gestione degli Eventi: Solo utenti con permessi specifici possono creare e gestire eventi.
Utilizzo

Navigazione
Pagina Principale: Visualizza tutti gli eventi disponibili. Puoi cercare eventi specifici utilizzando la barra di ricerca.
Dettagli Evento: Clicca su un evento per vedere i dettagli e avviare il processo di prenotazione.
Prenotazione Biglietti
Autenticazione: Effettua il login o registrati se non hai ancora un account.
Selezione Posti: Inserisci il numero di biglietti desiderati e controlla la disponibilità.
Pagamento: Inserisci i dettagli della carta di pagamento.
Numero di carta: Vedi la sezione successiva per i numeri di carta di test.
Data di scadenza: Qualsiasi data futura (es. 12/34).
CVC: Qualsiasi combinazione di tre cifre (es. 123).
CAP: Qualsiasi codice postale valido.
Conferma: Dopo il pagamento, la prenotazione verrà registrata e riceverai una conferma.
Carte di Test per Stripe
Puoi utilizzare i seguenti numeri di carta di test per simulare i pagamenti:

Pagamento Riuscito
Visa: 4242 4242 4242 4242
Pagamento Rifiutato (Fondi Insufficienti)
Visa: 4000 0000 0000 9995
Carta Scaduta
Visa: 4000 0000 0000 0069
CVC Errato
Visa: 4000 0000 0000 0127
Gestione Eventi
Solo utenti con permessi specifici possono creare e gestire eventi.

Implementazione del Pagamento con Stripe

Il pagamento viene gestito utilizzando Stripe. Quando un utente effettua una prenotazione:

Viene creato un PaymentIntent tramite l'API di Stripe.
L'utente inserisce i dettagli della carta e Stripe elabora il pagamento.
Se il pagamento è riuscito, la prenotazione viene confermata e aggiornata nel database.

