// Pagina «Richiedi la prova»: la apre il pulsante «Richiedi una prova» del menu Licenza dell'add-on con
// ?prodotto=<nome dell'add-on>&codice=<codice della società>. Porta al modulo di prova già compilato.
// Nessun cookie, nessun dato salvato: i parametri passano solo dall'indirizzo al modulo.

// Codice della società come lo mostra il menu Licenza: 3 gruppi da 4 caratteri Base32 di Crockford
// (0-9 e A-Z senza I, L, O, U), maiuscoli, separati da trattini; null se non è valido.
function codiceSocieta(testo) {
  var codice = (testo || "").replace(/\s+/g, "").toUpperCase();
  var gruppo = "[0-9A-HJKMNP-TV-Z]{4}";
  return new RegExp("^" + gruppo + "-" + gruppo + "-" + gruppo + "$").test(codice) ? codice : null;
}

// Indirizzo del modulo con prodotto e codice, oppure null se mancano o non sono validi.
function indirizzoModulo(modello, ricerca, prodottiAmmessi) {
  var parametri = new URLSearchParams(ricerca);
  var prodotto = (parametri.get("prodotto") || "").trim();
  var codice = codiceSocieta(parametri.get("codice"));
  if (!modello || prodottiAmmessi.indexOf(prodotto) < 0 || codice === null) {
    return null;
  }
  return modello.split("{addon}").join(encodeURIComponent(prodotto))
                .split("{codice}").join(encodeURIComponent(codice));
}

// Con il modulo del sito: la pagina dell'applicazione con il codice della società da mettere nel modulo, oppure null.
function paginaModulo(pagine, ricerca) {
  var parametri = new URLSearchParams(ricerca);
  var pagina = pagine[(parametri.get("prodotto") || "").trim()];
  var codice = codiceSocieta(parametri.get("codice"));
  return pagina && codice ? pagina + "?codice=" + encodeURIComponent(codice) + "#prova" : null;
}

if (typeof module !== "undefined") {
  module.exports = { indirizzoModulo: indirizzoModulo, codiceSocieta: codiceSocieta, paginaModulo: paginaModulo };
}

if (typeof document !== "undefined") {
  document.addEventListener("DOMContentLoaded", function () {
    var pagina = document.getElementById("richiedi-prova");
    if (!pagina) {
      return;
    }
    // il cambio di lingua tiene prodotto e codice
    document.querySelectorAll("a[hreflang]").forEach(function (link) {
      link.href = link.href.split("?")[0] + location.search;
    });
    var pagine = JSON.parse(pagina.dataset.pagine || "{}");
    if (Object.keys(pagine).length > 0) {
      // modulo del sito: si va al modulo dell'applicazione, con il codice già scritto
      var destinazione = paginaModulo(pagine, location.search);
      if (destinazione) {
        location.replace(destinazione);
      } else {
        document.getElementById("prova-senza-dati").hidden = false;
      }
      return;
    }
    var indirizzo = indirizzoModulo(pagina.dataset.modello, location.search, JSON.parse(pagina.dataset.prodotti));
    if (!indirizzo) {
      document.getElementById("prova-senza-dati").hidden = false;
      return;
    }
    var parametri = new URLSearchParams(location.search);
    document.getElementById("prova-prodotto").textContent = parametri.get("prodotto").trim();
    document.getElementById("prova-codice").textContent = codiceSocieta(parametri.get("codice"));
    document.getElementById("prova-vai").href = indirizzo;
    document.getElementById("prova-dati").hidden = false;
  });
}

// Pagina dell'applicazione: il codice della società arrivato da «Richiedi una prova» va nel modulo.
if (typeof document !== "undefined") {
  document.addEventListener("DOMContentLoaded", function () {
    var campo = document.getElementById("codiceSocieta");
    var codice = codiceSocieta(new URLSearchParams(location.search).get("codice"));
    if (campo && codice && !campo.value) {
      campo.value = codice;
    }
  });
}
