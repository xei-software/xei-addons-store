---
title: XEI Rate Updater para SAP Business One 1.0.0 – Notas de la versión
lang: es
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater para SAP Business One 1.0.0 – Notas de la versión

## Funciones de esta versión

- **Tipos de cambio de las monedas en SAP Business One** con los tipos del Banco Central Europeo, del Banco de Italia o
  de Open Exchange Rates: para los tipos de cambio de un día valen los tipos publicados el día anterior.
- **Solo las monedas de la empresa**, en el sentido de la empresa (tipo directo o indirecto), truncadas a seis
  decimales.
- **Moneda local distinta del euro**: tipos cruzados respecto a la moneda local.
- **Actualización manual** desde la página Tipos de cambio, con el resultado de cada moneda.
- **Actualización automática** cada día a la hora elegida, o desde el Programador de tareas de Windows con el comando
  `XEI.RateUpdater.exe aggiorna`.
- **Historial** de las ejecuciones de cada empresa, con los tipos y el resultado de cada moneda.
- **Licencia XEI** libre, por servidor o por empresa; prueba gratuita de 30 días.
- **Idiomas del programa**: italiano, inglés, alemán, francés, español y turco.

## Instalación

- Programa para Windows 10 y 11 y Windows Server 2016 y posteriores, de 64 bits: se extrae la carpeta del zip y se
  inicia `XEI.RateUpdater.exe`; .NET ya está incluido.
- Se necesitan Microsoft Edge WebView2 Runtime, normalmente ya presente, y el Service Layer de SAP Business One 10.0 o
  superior.
