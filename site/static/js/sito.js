// Pagina download: galleria delle schermate e pulsanti "Scarica gratis" / "Acquista".
// Se la pagina ha le condizioni d'uso, i pulsanti chiedono prima di accettarle (due spunte).
// Senza JavaScript i link funzionano lo stesso: aprono il modulo o l'email, la prima schermata si apre da sola.
(function () {
  "use strict";

  var galleria = document.querySelector("dialog.galleria");
  if (galleria && galleria.showModal) {
    preparaGalleria(galleria);
  }
  preparaPulsanti(document.querySelector("dialog.condizioni"));

  function preparaGalleria(finestra) {
    var immagine = finestra.querySelector("img");
    var conteggio = finestra.querySelector(".galleria-conteggio");
    var precedente = finestra.querySelector(".galleria-precedente");
    var successiva = finestra.querySelector(".galleria-successiva");
    var elenco = [];
    var posizione = 0;

    function mostra(numero) {
      posizione = (numero + elenco.length) % elenco.length;  // dall'ultima si torna alla prima e viceversa
      immagine.src = elenco[posizione];
      conteggio.textContent = (posizione + 1) + " / " + elenco.length;
      precedente.hidden = successiva.hidden = elenco.length < 2;
    }

    document.querySelectorAll("a.anteprima").forEach(function (link) {
      link.addEventListener("click", function (evento) {
        evento.preventDefault();
        elenco = link.getAttribute("data-immagini").split(" ");
        immagine.alt = link.querySelector("img").alt;
        mostra(0);
        finestra.showModal();
      });
    });
    precedente.addEventListener("click", function () { mostra(posizione - 1); });
    successiva.addEventListener("click", function () { mostra(posizione + 1); });
    finestra.querySelector(".galleria-chiudi").addEventListener("click", function () { finestra.close(); });
    finestra.addEventListener("keydown", function (evento) {
      if (evento.key === "ArrowLeft") { mostra(posizione - 1); }
      if (evento.key === "ArrowRight") { mostra(posizione + 1); }
    });
    // un clic fuori dall'immagine (sullo sfondo scuro) chiude la galleria
    finestra.addEventListener("click", function (evento) {
      if (evento.target === finestra) { finestra.close(); }
    });
  }

  // Apre il link del pulsante: le email nella stessa pagina, il modulo in una nuova scheda.
  function apri(indirizzo) {
    if (indirizzo.indexOf("mailto:") === 0) {
      location.href = indirizzo;
    } else {
      window.open(indirizzo, "_blank", "noopener");
    }
  }

  // "Scarica gratis": modulo per il codice di prova e, subito dopo, il pacchetto. "Acquista": modulo o email.
  function esegui(pulsante) {
    apri(pulsante.href);
    var pacchetto = pulsante.getAttribute("data-pacchetto");
    if (pulsante.getAttribute("data-azione") === "prova" && pacchetto) {
      // il pacchetto arriva come allegato: la pagina resta dov'è
      setTimeout(function () { location.href = pacchetto; }, 300);
    }
  }

  function preparaPulsanti(condizioni) {
    var pulsanti = document.querySelectorAll("a[data-azione]");
    if (!condizioni || !condizioni.showModal) {
      pulsanti.forEach(function (pulsante) {
        pulsante.addEventListener("click", function (evento) {
          evento.preventDefault();
          esegui(pulsante);
        });
      });
      return;
    }

    var spunte = condizioni.querySelectorAll('input[type="checkbox"]');
    var continua = condizioni.querySelector('[value="continua"]');
    var scelto = null;

    function aggiorna() {
      continua.disabled = !Array.prototype.every.call(spunte, function (spunta) { return spunta.checked; });
    }

    spunte.forEach(function (spunta) { spunta.addEventListener("change", aggiorna); });
    pulsanti.forEach(function (pulsante) {
      pulsante.addEventListener("click", function (evento) {
        evento.preventDefault();
        scelto = pulsante;
        spunte.forEach(function (spunta) { spunta.checked = false; });  // si accetta ogni volta
        aggiorna();
        condizioni.showModal();
      });
    });
    condizioni.querySelector('[value="annulla"]').addEventListener("click", function () { condizioni.close(); });
    continua.addEventListener("click", function () {
      condizioni.close();
      esegui(scelto);
    });
  }
})();
