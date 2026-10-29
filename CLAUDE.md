# xei-addons-store

Repository **pubblico** del sito degli add-on XEI (GitHub Pages, 6 lingue: it, en, fr, de, tr, es). Struttura e comandi
nel [README](README.md).

## Chi fa cosa

| Sessione | Compito |
|---|---|
| **Pubblica Programma XEI** (`session_01MKTKgsVLNM2hFhvmCuXAvQ`) | questo repository: sito, pagina download, Release pubbliche |
| **Coordinatore XEI** (`session_01LFHg4fgFz64GcRjySuMWFy`) | codice degli add-on, versioni, licenze; OK prima di pubblicare un add-on |
| **Coordinatore Documentazione XEI** (`session_01Rwg5Rtz6Mc3CC5Rrq375Rt`) | testi, manuali, traduzioni, loghi (repository `xei-model-docs`) |

Le decisioni importanti le prende Ivan.

**Consenso di Ivan (24/10/2026, confermato e limitato):** vale **solo** per questo repository: questa sessione lavora
in autonomia su codice, testi, commit e push. XEI.ItemGenerator 1.4.0 ha l'OK di Ivan. Ogni nuovo add-on o nuova
versione richiede il pacchetto XEICore definito e il consenso dei due coordinatori **prima del push di
`site/addons.yml`**. Creare repository, toccare altri
repository, impostazioni (es. GitHub Pages) e segreti li decide Ivan caso per caso.

## Regole (repository pubblico)

- **Mai nel repository:** sorgenti, codici di licenza (`licenza.xei`), chiavi, token, credenziali, nomi di clienti,
  percorsi interni, dati personali delle registrazioni. I test (`tests/test_contenuti.py`) ne bloccano una parte, ma non
  tutto: controllare sempre a mano prima del push.
- **Mai nelle Release pubbliche:** il pacchetto `_TEST`, la mappa di offuscamento, pacchetti con un codice di licenza.
  Si pubblica solo il pacchetto principale, identico a quello della Release dell'add-on (niente ricompilazioni).
  Per le app anche niente dati locali: `impostazioni.json`, `appsettings.Development.json`, `users.json`, `*.user`, `*.log`,
  cartelle `logs/`, `chiavi/`, `sessions/` (`copia_release.problemi_pacchetto` li blocca).
- **Quali add-on:** solo quelli con le licenze offline (XEICore 1.1.1 o successiva), con l'OK del Coordinatore XEI.
  Mai gli add-on di prova né quelli fatti per un singolo cliente.
- **App** (XEI App Framework, programmi Windows come XEI.RateUpdater): in `addons.yml` `tipo: app` e `framework` (la
  `XeiFrameworkVersion` di `Directory.Packages.props` alla versione del tag) al posto di `xeicore`; stessi consensi e
  stessi controlli del pacchetto. Nella pagina download una nota spiega che si estrae la cartella e si avvia il
  programma (serve Microsoft Edge WebView2 Runtime). `copia_release voce` con `--tipo app`.
- **Licenza di prova:** lo zip è pubblico e senza codice. Il pulsante «Richiedi la prova gratuita» apre il modulo
  Microsoft Forms (`modulo_registrazione` in `site/config.yml`, link precompilato con `{addon}` e `{lingua}`); la Logic
  App e il servizio `xei-trial-service` inviano in automatico da license@xeisrl.com il codice di prova di 30 giorni.
  Con `modulo_registrazione` vuoto il pulsante apre un'email precompilata.
- I testi delle pagine vengono dal Coordinatore Documentazione (repository `xei-model-docs`, front matter `title`,
  `description`, `lang`, `prodotto`, `versione`, `stato`). Si copiano in `site/content/` solo i file con
  `stato: approvato`; il generatore scarta comunque ogni altro stato (`bozza`, `interno`, nessuno).
  Mai importare `interno/` di xei-model-docs (documentazione interna). Corrispondenze:
  `sito/<lingua>/home.md` → `pagine/home.md`, `sito/<lingua>/<prodotto>.md` → `addons/<id>.md`,
  `manuali/<lingua>/<prodotto>/note-rilascio-<versione>.md` → `note/<id>-<versione>.md`,
  `manuali/<lingua>/<prodotto>/<nome>.md` e `.pdf` → `manuali/<id>/<nome>.md` e `.pdf`,
  `manuali/_img/<prodotto>/` e `manuali/_file/<prodotto>/` → `site/content/_img/<prodotto>/` e `_file/<prodotto>/`
  (i link relativi dei manuali vengono riscritti dal generatore),
  `sito/<lingua>/privacy.md` → `pagine/privacy.md` (l'informativa dice che il sito non usa cookie né contenuti di
  altri siti: un test lo controlla, non aggiungere caratteri, script o statistiche esterni).
  **Immagini e file dei manuali si guardano uno per uno prima di importarli** (i test non leggono le immagini): niente
  nomi di persone o clienti, percorsi interni, codici società/server reali, campi o moduli di altri programmi.
  Logo e icona in `site/static/img/` (da `loghi/` di xei-model-docs; colori: grigio #686A6F, azzurro #009FE3).
  I testi dell'interfaccia (`site/i18n/`) li mantiene questa sessione.
- **Migrazioni da vecchi programmi** (decisione di Ivan, `xei-model-docs/interno/README.md`): sono solo implicite nel
  codice, anche nel pacchetto pubblicato (all'avvio, senza menu, senza messaggi, solo log; nessuna build dedicata). Mai
  in ciò che il cliente legge: sito, manuali, note, guide, email, schermate, testi dell'interfaccia e file a vista del
  pacchetto (menu, `lang`).
- **Lingue standard degli add-on:** it, en, de, fr, es, tr (il turco nel programma arriva con le prossime versioni;
  in `addons.yml` `lingue_programma` indica quelle davvero presenti nella versione pubblicata).
- **Nessun riferimento** a programmi di partenza (es. il vecchio configuratore), a migrazioni da altri programmi o a
  tabelle non XEI (regola di Ivan, come in `xei-model-docs/CLAUDE.md`). I manuali si prendono solo da `xei-model-docs`,
  mai dai repository degli add-on. I termini vietati sono in `tests/termini_vietati.txt` (copia di
  `xei-model-docs/regole/termini-vietati.txt`, da riallineare quando cambia); le eccezioni le approva Ivan.
- I test devono passare prima di ogni push (`python -m pytest -q`).

## Pubblicare una nuova versione di un add-on

1. **Regola di Ivan, prima di ogni rilascio:** il pacchetto XEICore dell'add-on dev'essere definito (`xeicore` in
   `addons.yml`; il workflow lo confronta con il `PackageReference` del progetto alla versione del tag) e servono i
   consensi di **entrambi** i coordinatori, Coordinatore XEI (pacchetto e SHA-256) e Coordinatore Documentazione
   (testi e manuali), con le date in `ok_coordinatore_xei` e `ok_coordinatore_documentazione`. Senza, i test falliscono.
2. `python -m strumenti.copia_release voce --origine xei-software/<repo> --tag v<versione> --file <Pacchetto>.zip
   --id <id> --data <aaaa-mm-gg>` (per un'app anche `--tipo app`): scarica e controlla lo zip, stampa la voce per
   `site/addons.yml`.
3. Aggiornare `site/addons.yml` e, se servono, testi e manuali in `site/content/`.
4. `python -m pytest -q`, commit e push su `main`: il sito si aggiorna da solo.
5. Il push su `main` di `site/addons.yml` avvia il workflow `release.yml`: per ogni voce senza Release pubblica
   scarica il pacchetto, verifica che sia identico a `addons.yml` (SHA-256, dimensione, nessun file vietato) e crea
   la Release `<id>-v<versione>` con il suo tag. Si può rilanciare a mano da Actions ("Run workflow"). Le sessioni
   Claude non possono creare Release né fare push di tag: per questo la Release parte dal push su `main`, che quindi
   richiede l'OK del Coordinatore XEI già al punto 1. Il workflow usa il segreto `XEI_ADDON_READ_TOKEN` (token in sola
   lettura sui repository degli add-on, scadenza da rinnovare).
6. Avvisare il Coordinatore XEI e il Coordinatore Documentazione.
