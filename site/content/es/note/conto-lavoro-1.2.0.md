---
title: XEI.ContoLavoro 1.2.0 – Notas de la versión
description: Funciones y correcciones de XEI.ContoLavoro 1.2.0 para SAP Business One.
lang: es
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro 1.2.0 – Notas de la versión

## Funciones de esta versión

- En la lista «Crear órdenes desde órdenes de fabricación», con la casilla «Mostrar también las líneas no preparadas», aparecen también las elaboraciones que no pueden convertirse en orden de
  subcontratación, con el motivo y lo que hay que hacer en la columna «Motivo / avisos».
- Al guardar una lista de materiales, un aviso señala los códigos que hay que corregir en el campo «Lavorazione
  terzista» (Elaboración del subcontratista): recursos, códigos que no son artículos, artículos sin «Conto lavoro»
  (Subcontratación), elaboraciones que no son líneas de la lista de materiales, componentes con notificación
  retroactiva.
- Licencia XEI con la ventana **Licenza** (Licencia) en el menú del add-on: estado, códigos de la empresa y del
  servidor, introducción del código; prueba gratuita de 30 días.

## Correcciones de esta versión

- Una orden de subcontratación interrumpida no impide crear otra orden de subcontratación desde la misma línea de la
  orden de fabricación.
- Los componentes con notificación retroactiva vinculados a una elaboración externa no se envían al subcontratista y
  la orden de fabricación los toma una sola vez.
- Sin la serie de numeración de la orden de subcontratación, al abrir *Orden de subcontratación* el add-on indica dónde definirla.
- La transferencia masiva de componentes está activa en la configuración predeterminada; con la opción desactivada, la entrada de menú avisa de que la función está desactivada.
- Las órdenes de subcontratación creadas desde órdenes de fabricación usan la lista de precios predefinida de las órdenes (Configuración › General): sin ella, «Crear órdenes» pide indicarla.
- En la lista «Crear órdenes desde órdenes de fabricación» las líneas se seleccionan y el proveedor se cambia.
