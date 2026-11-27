# Anteprima interna dello store

Specchio privato di quello che andrà su store.xeisrl.com: serve a controllare le modifiche prima di pubblicarle e
per uso interno. È su **Azure Static Web Apps, piano Free** (nessun costo, nessun account nuovo: si usa la
sottoscrizione Azure di XEI). Si entra solo con il login **GitHub** e solo gli utenti **invitati con il ruolo
`interno`** vedono le pagine; chiunque altro viene mandato al login e poi riceve «accesso negato».

## Come funziona

- Le modifiche al sito si fanno sul ramo **`anteprima`**. Ogni push su `anteprima` avvia il workflow
  `.github/workflows/anteprima.yml`: test, poi `python build.py --anteprima`, poi la pubblicazione su Azure.
- L'anteprima è il sito com'è, **anche durante la manutenzione** (si vede quello che andrà online alla riapertura), con
  una fascia gialla «Anteprima interna XEI» in alto, fuori dai motori di ricerca, senza il dominio dello store.
- Dopo il controllo si unisce `anteprima` su `main`: il sito pubblico si aggiorna come sempre.
- Le regole di accesso sono in `staticwebapp.config.json`, scritto da `build.py` (`REGOLE_ANTEPRIMA`): tutte le pagine
  solo per il ruolo `interno`, login solo con GitHub.

## Da fare una volta (Ivan o Enrico, circa 15 minuti)

Le sessioni Claude non creano risorse Azure né segreti: questi passi li fa chi ha accesso al portale Azure e alle
impostazioni del repository.

1. **Creare la Static Web App.** Portale Azure → «Crea una risorsa» → **Static Web App** → Crea.
   - Sottoscrizione: quella di XEI; gruppo di risorse: `xei-licenze` (o uno nuovo, es. `xei-store`).
   - Nome: `xei-store-anteprima`.
   - Tipo di piano: **Free**.
   - Origine della distribuzione: **Altro** (non «GitHub»: la pubblicazione la fa già il nostro workflow; con «GitHub»
     Azure aggiungerebbe un suo workflow al repository).
   - Area per le API: Europa occidentale. → Rivedi e crea → Crea.
2. **Copiare il token di distribuzione.** Nella risorsa creata: Panoramica → **Gestisci token di distribuzione** →
   copia.
3. **Salvarlo come segreto del repository.** GitHub → xei-software/xei-addons-store → Settings → Secrets and variables →
   Actions → **New repository secret**: nome `AZURE_ANTEPRIMA_TOKEN`, valore il token copiato.
4. **Prima pubblicazione.** GitHub → Actions → «Anteprima interna (Azure Static Web Apps)» → **Run workflow** sul ramo
   `anteprima`. Alla fine l'indirizzo è in Azure, Panoramica → URL (`https://<nome>.azurestaticapps.net`).
5. **Invitare le persone** (una alla volta). Nella risorsa: Impostazioni → **Gestione ruoli** → **Invita**:
   - Provider di autenticazione: **GitHub**;
   - Dettagli invitato: il **nome utente GitHub** della persona (es. quello con cui è nell'organizzazione xei-software);
   - Dominio: l'indirizzo dell'anteprima;
   - Ruolo: **`interno`** (esattamente così, minuscolo);
   - Scadenza dell'invito: il massimo proposto (di solito 168 ore).
   → **Genera** e manda il link alla persona: lo apre, entra con GitHub e accetta. Da quel momento vede l'anteprima.
   Per togliere l'accesso: Gestione ruoli → la persona → Elimina.

Da verificare nel portale (non ho potuto leggere la documentazione Microsoft da qui): il piano Free comprende la
gestione dei ruoli con gli inviti, con un numero limitato di utenti invitati (circa 25) e circa 250 MB di sito; oggi
l'anteprima pesa circa 30 MB.

## Limiti

- L'accesso è per **utente invitato**, non automatico per tutta l'organizzazione GitHub: chi entra nell'organizzazione
  va invitato anche qui, chi esce va tolto. L'accesso automatico ai membri dell'organizzazione con GitHub Pages
  richiede GitHub Enterprise Cloud (a pagamento).
- Il modulo della prova nell'anteprima manda le richieste al servizio vero, che accetta solo i moduli inviati da
  store.xeisrl.com: dall'anteprima risponde «non autorizzato». Le prove del modulo si fanno come sempre dal sito
  pubblico o con il comando di prova del servizio.
