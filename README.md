# XEI Add-on per SAP Business One

Sito pubblico degli add-on XEI: descrizioni, manuali e download, in italiano, inglese, francese, tedesco, turco e
spagnolo.

**Sito:** https://store.xeisrl.com/

Ogni add-on si prova gratuitamente per 30 giorni: si richiede la prova dal sito e il codice arriva per email da
license@xeisrl.com. Senza un codice di licenza valido l'add-on non si avvia. Per acquistare una licenza scrivere a
license@xeisrl.com.

## Come è fatto

| Cartella | Contenuto |
|---|---|
| `site/config.yml` | lingue, email delle licenze, indirizzo del modulo di registrazione |
| `site/addons.yml` | add-on pubblicati: versione, pacchetto, SHA-256, Release pubblica |
| `site/i18n/<lingua>.yml` | testi dell'interfaccia (menu, pulsanti), uno per lingua |
| `site/content/<lingua>/addons/<id>.md` | descrizione di ogni add-on |
| `site/content/<lingua>/manuali/<id>/<nome>.md` e `.pdf` | manuali di ogni add-on (immagini e file di esempio in `site/content/_img`, `_file`) |
| `site/content/<lingua>/pagine/home.md`, `pagine/privacy.md` | testo della home e informativa sulla privacy |
| `site/content/<lingua>/note/<id>-<versione>.md` | note di rilascio |
| `site/templates/`, `site/static/` | modelli delle pagine e stile |
| `build.py` | genera il sito statico |
| `strumenti/copia_release.py` | controlla il pacchetto di un add-on e prepara la Release pubblica (`.github/workflows/release.yml`) |
| `tests/` | controlli automatici |

Se un testo manca in una lingua, la pagina mostra l'italiano con un avviso.

Il sito pubblica anche `/prodotti-prova.json`, l'elenco dei prodotti con la prova (nome, versione pubblicata, XEICore)
ricavato da `site/addons.yml`: il servizio delle prove (`xei-trial-service`) lo legge da qui. Per aggiungere un prodotto
alle prove basta pubblicarne la voce in `addons.yml`; `prova: false` in una voce la toglie dall'elenco.

Manutenzione: con `manutenzione: {fino_al: aaaa-mm-gg}` in `site/config.yml` tutto lo store diventa una sola pagina
«Torna a trovarci il …» (6 lingue, stile del sito, link a xeisrl.com); ogni altro indirizzo mostra lo stesso messaggio
(404). Resta `/prodotti-prova.json` per il servizio delle prove. Togliendo le righe il sito torna com'era.

Disponibilità di un programma, in `site/addons.yml`:

- `attivo: false`: il programma sparisce da tutto il sito (pagine, link, manuali e loro immagini, elenco delle prove);
  togliendo la riga torna com'era. La Release pubblica già creata resta su GitHub, ma il sito non la mostra.
- `su_richiesta: true`: nessun pacchetto (niente `versione`, `file`, `sha256`, `tag_pubblico`, `xeicore`); al posto di
  «Scarica gratis» e «Acquista» un solo pulsante «Richiedi informazioni», email già compilata a `email_informazioni`
  (info@xeisrl.com, in `site/config.yml`). Niente prova automatica né Release. Servono comunque i due consensi.

## Comandi

```
pip install -r requirements.txt
python -m pytest -q                                   # controlli
python build.py --out anteprima                        # anteprima locale
python -m http.server -d anteprima                    # poi http://localhost:8000
```

A ogni push su `main` GitHub Actions esegue i test, genera il sito e lo pubblica su GitHub Pages
(`.github/workflows/pages.yml`).
