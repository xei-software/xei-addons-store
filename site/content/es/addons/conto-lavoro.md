---
title: XEI.ContoLavoro – Subcontratación
description: Gestiona en SAP Business One los trabajos confiados a los subcontratistas, desde el pedido y el envío de los componentes hasta el retorno del producto terminado.
lang: es
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro

**La subcontratación en SAP Business One.** Una orden de subcontratación para cada trabajo reúne el pedido al
subcontratista, los componentes enviados, los retornos y la entrada del producto terminado, con la situación siempre
actualizada.

## Descripción

Seguir la subcontratación a mano significa mantener alineados pedidos de compra, transferencias y entradas, y saber en
todo momento qué hay en cada subcontratista. Con XEI.ContoLavoro lo hace SAP Business One:

- para cada trabajo se abre una **orden de subcontratación** con los productos que se deben obtener y su lista de
  materiales: componentes que enviar y elaboraciones que pagar;
- el **pedido de compra al subcontratista** se genera a partir de la orden de subcontratación y queda alineado con cada
  modificación;
- los **componentes** se envían al almacén del subcontratista, con retornos y desechos;
- la **entrada de producción** registra en una sola operación la entrada del producto y de las elaboraciones y la
  salida de los componentes consumidos;
- la orden de subcontratación muestra en todo momento qué se ha enviado, qué se ha utilizado, qué queda en el
  subcontratista y qué falta, y se cierra sola cuando está terminada.

## Funciones principales

- **Orden de subcontratación** con las pestañas Productos, Lista de materiales, Componentes y Documentos: todos los
  documentos SAP vinculados, agrupados y listos para abrir.
- **Subcontratación desde órdenes de fabricación**: las fases externas de una orden de fabricación se convierten en
  órdenes de subcontratación, los componentes se toman en cada retorno y el producto terminado entra en el almacén
  cuando han vuelto todas las elaboraciones.
- **Lotes y números de serie** propuestos a partir de los lotes de la orden de subcontratación en el subcontratista y
  por fecha de vencimiento, modificables a mano; lote del producto entrante calculado por un script configurable.
- **Costes** de los productos recalculados en cada guardado, con los **precios de elaboración** por subcontratista y
  producto.
- **Transferencia masiva** de componentes, **transferencia entre órdenes de subcontratación** en el mismo
  subcontratista y **cierre masivo** de las entradas de mercancías.

## Requisitos

| | |
|---|---|
| SAP Business One | 10.0 o posterior |
| Base de datos | Microsoft SQL Server o SAP HANA (en SAP HANA se recomienda una prueba durante la instalación) |
| Idiomas del programa | italiano, inglés, alemán, francés, español, turco |
| Sistema | Microsoft .NET Framework 4.8 en el PC del cliente SAP |
| Instalación | Extension Manager de SAP Business One |
| Licencia | código de licencia XEI, que se introduce en el menú **Licenza** (Licencia) (prueba gratuita de 30 días) |

## Versión actual

**1.2.0** – consulte las [notas de la versión](../../manuali/es/contolavoro/note-rilascio-1.2.0.md) y el manual de uso.
