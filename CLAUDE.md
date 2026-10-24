# xei-addons-store

Repository **pubblico** del sito degli add-on XEI (GitHub Pages, 6 lingue: it, en, fr, de, tr, es). Struttura e comandi
nel [README](README.md).

## Chi fa cosa

| Sessione | Compito |
|---|---|
| **Pubblica Programma XEI** (`session_01MKTKgsVLNM2hFhvmCuXAvQ`) | questo repository: sito, pagina download, Release pubbliche |
| **Coordinatore XEI** (`session_01RmGx3qkcdk2mSAcaNtW6Zd`) | codice degli add-on, versioni, licenze; OK prima di pubblicare un add-on |
| **Coordinatore Documentazione XEI** (`session_01Rwg5Rtz6Mc3CC5Rrq375Rt`) | testi, manuali, traduzioni, loghi (repository `xei-model-docs`) |

Le decisioni importanti le prende Ivan.

**Consenso di Ivan (24/10/2026):** questa sessione lavora in autonomia sul repository (push, tag, Release) e può
pubblicare XEI.ItemGenerator 1.4.0. Per ogni nuovo add-on o nuova versione resta l'OK del Coordinatore XEI.

## Regole (repository pubblico)

- **Mai nel repository:** sorgenti, codici di licenza (`licenza.xei`), chiavi, token, credenziali, nomi di clienti,
  percorsi interni, dati personali delle registrazioni. I test (`tests/test_contenuti.py`) ne bloccano una parte, ma non
  tutto: controllare sempre a mano prima del push.
- **Mai nelle Release pubbliche:** il pacchetto `_TEST`, la mappa di offuscamento, pacchetti con un codice di licenza.
  Si pubblica solo il pacchetto principale, identico a quello della Release dell'add-on (niente ricompilazioni).
- **Quali add-on:** solo quelli con le licenze offline (XEICore 1.1.1 o successiva), con l'OK del Coordinatore XEI.
  Mai gli add-on di prova né quelli fatti per un singolo cliente.
- **Licenza di prova (fase A):** lo zip è pubblico e senza codice. Il cliente si registra con il modulo Microsoft Forms
  (`modulo_registrazione` in `site/config.yml`). Il codice di prova di 30 giorni lo crea Ivan con il generatore di
  XEICore e lo invia da license@xeisrl.com. La fase B (codice automatico) è rimandata.
- I testi delle pagine vengono dal Coordinatore Documentazione (repository `xei-model-docs`, front matter `title`,
  `description`, `lang`, `prodotto`, `versione`, `stato`). Si copiano in `site/content/` solo i file con
  `stato: approvato`; il generatore scarta comunque quelli in `bozza`. Corrispondenze:
  `sito/<lingua>/home.md` → `pagine/home.md`, `sito/<lingua>/<prodotto>.md` → `addons/<id>.md`,
  `manuali/<lingua>/<prodotto>/note-rilascio-<versione>.md` → `note/<id>-<versione>.md`, manuale → `manuali/<id>.md`,
  `legale/<lingua>/privacy-registrazione.md` → `pagine/privacy.md`.
  Logo e icona in `site/static/img/` (da `loghi/` di xei-model-docs; colori: grigio #686A6F, azzurro #009FE3).
  I testi dell'interfaccia (`site/i18n/`) li mantiene questa sessione.
- I test devono passare prima di ogni push (`python -m pytest -q`).

## Pubblicare una nuova versione di un add-on

1. OK del Coordinatore XEI per add-on e versione.
2. `python -m strumenti.copia_release voce --origine xei-software/<repo> --tag v<versione> --file <Pacchetto>.zip
   --id <id> --data <aaaa-mm-gg>`: scarica e controlla lo zip, stampa la voce per `site/addons.yml`.
3. Aggiornare `site/addons.yml` e, se servono, testi e manuali in `site/content/`.
4. `python -m pytest -q`, commit e push su `main`: il sito si aggiorna da solo.
5. `git tag <id>-v<versione> && git push origin <id>-v<versione>`: il workflow `release.yml` scarica il pacchetto,
   verifica che sia identico a `addons.yml` (SHA-256, dimensione, nessun file vietato) e crea la Release pubblica.
   Le sessioni Claude non possono creare Release direttamente: si passa sempre dal tag. Il workflow usa il segreto
   `XEI_ADDON_READ_TOKEN` (token in sola lettura sui repository degli add-on).
6. Avvisare il Coordinatore XEI e il Coordinatore Documentazione.
