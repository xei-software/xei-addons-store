---
title: XEI.ItemGenerator – Configurador de códigos de artículo
description: Cree en SAP Business One artículos con código, descripciones, datos, precio y lista de materiales compuestos según sus propias reglas.
lang: es
prodotto: XEI.ItemGenerator
versione: 1.5.0
stato: approvato
---

# XEI.ItemGenerator

**Configurador de códigos de artículo para SAP Business One.** Elija las
características del producto y el add-on crea el artículo en los datos maestros con
código, descripciones, datos, precio y lista de materiales ya completados.

## Descripción

Quien vende productos en muchas combinaciones (medidas, acabados, colores, accesorios)
pierde tiempo creando a mano un artículo por cada combinación y corre el riesgo de tener
códigos y descripciones distintos para el mismo producto.

Con XEI.ItemGenerator usted define las reglas una sola vez y el add-on compone los
artículos:

- el **código** nace de los valores elegidos nivel a nivel (por ejemplo
  `PE` mueble alto → `MU` de pared → `070` altura 70 cm = `PEMU070`), más un número
  correlativo que distingue las variantes;
- las **variantes** (por ejemplo color o acabado) tienen sus opciones, que pueden
  heredarse de los niveles anteriores;
- **descripciones, grupos, unidades de medida, propiedades, medidas, peso y precio** del
  artículo se obtienen de los valores y opciones elegidos;
- la **lista de materiales** se compone con los componentes de cada valor y opción.

Si una combinación ya existe, el add-on encuentra el artículo existente en lugar de
crear un duplicado.

## Funciones principales

- **Definición de bases, variantes y estructuras** con los datos maestros del add-on en SAP.
- **Generación de artículos** en una ventana redimensionable, con el árbol de códigos y
  el de variantes; SAP sigue utilizable mientras la ventana está abierta.
- **Configurar artículo desde ofertas de ventas y pedidos de cliente**: con el botón
  derecho en la línea del documento se compone el artículo y se inserta en la línea.
- **Generar artículos similares** desde los datos de un artículo ya generado: basta con
  cambiar una opción.
- **Fórmula de descripción** para componer la descripción, la descripción ampliada y el
  nombre extranjero.
- **Verificación de la configuración**, con la lista de errores y la apertura directa del
  dato que hay que corregir.
- **Importación y exportación Excel** de la configuración, también para copiarla a otra
  empresa.
- **Autorizaciones** propias en las Autorizaciones generales de SAP.
- **Miniatura de la imagen** del artículo en los datos maestros de artículos.

## Requisitos

| | |
|---|---|
| SAP Business One | 10.0 o posterior |
| Base de datos | Microsoft SQL Server o SAP HANA (en SAP HANA se recomienda una prueba durante la instalación) |
| Idiomas del programa | italiano, inglés, alemán, francés, español, turco |
| Sistema | Microsoft .NET Framework 4.8 en el PC del cliente SAP |
| Instalación | Extension Manager de SAP Business One |
| Licencia | código de licencia XEI, que se introduce en el menú **Licenza** (Licencia) del add-on (prueba gratuita de 30 días) |

## Versión actual

**1.5.0** – consulte las [notas de la versión](../../manuali/es/itemgenerator/note-rilascio-1.5.0.md).
