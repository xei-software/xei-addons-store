# XEI Add-on per SAP Business One

Sito pubblico degli add-on XEI: descrizioni, manuali e download, in italiano, inglese, francese, tedesco, turco e
spagnolo.

**Sito:** https://xei-software.github.io/xei-addons-store/

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
| `site/content/<lingua>/manuali/<id>.md` | manuale di ogni add-on |
| `site/content/<lingua>/pagine/privacy.md` | informativa sulla privacy |
| `site/templates/`, `site/static/` | modelli delle pagine e stile |
| `build.py` | genera il sito statico |
| `strumenti/copia_release.py` | controlla il pacchetto di un add-on e prepara la Release pubblica (`.github/workflows/release.yml`) |
| `tests/` | controlli automatici |

Se un testo manca in una lingua, la pagina mostra l'italiano con un avviso.

## Comandi

```
pip install -r requirements.txt
python -m pytest -q                                   # controlli
python build.py --out anteprima --url-base ""         # anteprima locale
python -m http.server -d anteprima                    # poi http://localhost:8000
```

A ogni push su `main` GitHub Actions esegue i test, genera il sito e lo pubblica su GitHub Pages
(`.github/workflows/pages.yml`).
