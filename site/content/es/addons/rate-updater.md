---
title: XEI Rate Updater para SAP Business One – Tipos de cambio de las monedas
description: Actualiza cada día los tipos de cambio de las monedas en SAP Business One con los tipos oficiales del BCE, del Banco de Italia o de Open Exchange Rates.
lang: es
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater para SAP Business One

**Los tipos de cambio de las monedas en SAP Business One, actualizados por sí solos.** Cada día el programa toma los
tipos de una fuente oficial y los escribe en SAP Business One, en el sentido y con los decimales que usa SAP.

## Descripción

Actualizar los tipos de cambio a mano significa copiar cada mañana los tipos de un sitio web en la tabla de tipos de
cambio de SAP, moneda por moneda, con el riesgo de olvidar un día o de invertir un tipo.

XEI Rate Updater para SAP Business One lo hace por usted:

- toma los tipos del **Banco Central Europeo**, del **Banco de Italia** o de **Open Exchange Rates**;
- para los tipos de cambio de un día usa los tipos publicados **el día anterior**; en fines de semana y festivos usa
  el último día publicado;
- escribe en SAP solo las **monedas gestionadas por la empresa**, en el sentido que usa la empresa (tipo directo o
  indirecto), truncadas a seis decimales;
- con una **moneda local distinta del euro** calcula los tipos cruzados respecto a ella;
- se usa **a mano**, eligiendo la fecha, o **cada día de forma automática**;
- guarda el **historial** de cada actualización: quién la hizo, la fuente, los tipos y el resultado de cada moneda.

## Funciones principales

- **Tipos de cambio**: fecha de los tipos de cambio, fuente y botón *Actualizar los tipos en SAP*; el resultado muestra
  para cada moneda el tipo directo, el tipo indirecto y si se ha escrito en SAP.
- **Historial**: las ejecuciones de la empresa, de la más reciente a la más antigua; cada fila se abre sobre las
  monedas.
- **Actualización automática**: cada día a la hora elegida, o desde el Programador de tareas de Windows.
- **Errores bajo control**: un error en una moneda no detiene las demás; cada ejecución indica qué ha fallado.
- **Inicio de sesión con el usuario SAP** de cada persona, con sus autorizaciones sobre los tipos de cambio; el
  administrador asigna a cada usuario las funciones *Actualización de tipos de cambio* e *Historial*.

## Requisitos

| | |
|---|---|
| SAP Business One | 10.0 o superior, con el Service Layer |
| Base de datos | Microsoft SQL Server o SAP HANA (en SAP HANA se recomienda una prueba durante la instalación) |
| Sistema | Windows 10 y 11, Windows Server 2016 y posteriores, de 64 bits; Microsoft Edge WebView2 Runtime |
| Red | acceso a internet hacia la fuente de los tipos elegida (BCE, Banco de Italia u Open Exchange Rates con su clave API) |
| Idiomas del programa | italiano, inglés, alemán, francés, español, turco |
| Instalación | se extrae la carpeta del programa, sin instalación; .NET ya está incluido |
| Licencia | código de licencia XEI, libre, por servidor o por empresa (prueba gratuita de 30 días) |

## Versión actual

**1.0.0** – consulte las [notas de la versión](../../manuali/es/rateupdater/note-rilascio-1.0.0.md) y el
[manual de uso](../../manuali/es/rateupdater/manuale-utente.md).
