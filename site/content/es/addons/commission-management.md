---
title: XEI.CommissionManagement – Comisiones de agentes
description: Calcula y liquida en SAP Business One las comisiones de agentes, jefes de zona, jefes de área y directores, desde las reglas hasta el extracto de cada agente.
lang: es
prodotto: XEI.CommissionManagement
versione: 1.1.0
stato: approvato
---

# XEI.CommissionManagement

**Comisiones de los agentes de ventas en SAP Business One.** Los porcentajes llegan solos a las líneas de los
documentos, el add-on calcula las comisiones, las liquida a medida que los clientes pagan y prepara el extracto de cada
agente.

## Descripción

Calcular las comisiones a mano o en hojas de cálculo obliga a revisar cada mes facturas, cobros y acuerdos con los
agentes, con el riesgo de errores y de extractos distintos de lo que dice el ERP.

Con XEI.CommissionManagement todo se queda en SAP Business One:

- cada línea de factura lleva hasta **cuatro porcentajes**: agente, jefe de zona, jefe de área y director;
- los porcentajes vienen de las **reglas** por cliente, grupo de clientes, artículo, grupo de artículos, lista de
  precios, período y descuento, o de los porcentajes predeterminados del agente, y se pueden corregir a mano;
- la comisión se divide en una parte **al facturar** y partes **al cobrar**, plazo por plazo o sobre el total del
  documento;
- la **liquidación** propone las partes cobradas y anula las de los plazos que vuelven a estar impagados;
- el **extracto** de cada agente se exporta a CSV, se imprime en PDF o se envía por correo electrónico.

## Funciones principales

- **Agentes y jerarquía**: rol, jefe de zona, jefe de área, director, porcentajes predeterminados, parte al facturar y
  tipo de liquidación de cada empleado de ventas.
- **Reglas de porcentajes** con orden de búsqueda configurable, descuento mínimo y período de validez, exportables e
  importables en CSV.
- **Porcentajes en los documentos de ventas** mientras se rellenan, con estimación de la comisión al guardar y
  protección de las líneas corregidas a mano.
- **Control y asignación de %**: compara los porcentajes de los documentos con las reglas y los corrige en bloque.
- **Cálculo** sobre facturas de deudores, facturas de anticipo y notas de crédito, también automático al registrar la
  factura.
- **Liquidación** de las partes cobradas, también en proporción a los cobros parciales, con período cerrado.
- **Ajustes**, **tramos y premios** sobre la facturación anual y **borradores de facturas** de los agentes.
- **Verificaciones** de anomalías y **autorizaciones** propias en las Autorizaciones generales de SAP.

## Requisitos

| | |
|---|---|
| SAP Business One | 10.0 o posterior |
| Base de datos | Microsoft SQL Server o SAP HANA (en SAP HANA se recomienda una prueba durante la instalación) |
| Idiomas del programa | italiano, inglés, alemán, francés, español, turco |
| Sistema | Microsoft .NET Framework 4.8 en el PC del cliente SAP |
| Correo | servidor de correo SMTP accesible, solo para enviar los extractos a los agentes por correo electrónico (Configuración › Correo) |
| Instalación | Extension Manager de SAP Business One |
| Licencia | código de licencia XEI, que se introduce en el menú **Licenza** (Licencia) del add-on (prueba gratuita de 30 días) |

## Versión actual

**1.1.0** – consulte las [notas de la versión](../../manuali/es/commissionmanagement/note-rilascio-1.1.0.md) y el
[manual de uso](../../manuali/es/commissionmanagement/manuale-utente.md).
