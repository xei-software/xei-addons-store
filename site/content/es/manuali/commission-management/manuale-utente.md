---
title: XEI.CommissionManagement – Manual de uso
description: Comisiones de los agentes de ventas en SAP Business One: configuración, reglas, cálculo, liquidación, ajustes y extractos.
lang: es
prodotto: XEI.CommissionManagement
versione: 1.1.0
stato: approvato
---

# XEI.CommissionManagement – Manual de uso

| | |
|---|---|
| SAP Business One | 10.0 o posteriores |
| Base de datos | Microsoft SQL Server o SAP HANA (en SAP HANA se recomienda una prueba durante la instalación) |
| Idiomas del programa | italiano, inglés, alemán, francés, español, turco |

## 1. Qué hace el add-on

XEI.CommissionManagement calcula y liquida las **comisiones de los agentes de ventas** a partir de los documentos de
SAP Business One. Cada línea de factura (y de factura de anticipo o nota de crédito) lleva consigo hasta cuatro
porcentajes: uno para el **agente** del documento y uno para cada uno de sus superiores, **jefe de zona**, **jefe
de área** y **director**. El add-on:

- **asigna los porcentajes** a las líneas mientras se rellenan los documentos, según reglas por cliente, grupo de
  clientes, artículo, grupo de artículos, lista de precios, período y descuento (o según los porcentajes
  predeterminados del agente);
- **calcula** las comisiones de los documentos de un período y las divide en **partes**: una parte se devenga con la
  factura, el resto con el cobro (plazo por plazo o cuando todo el documento está cobrado);
- **liquida** las partes a medida que SAP registra los cobros, y **revierte** las de plazos que resultan impagados;
- genera para cada agente el **extracto** de lo calculado, de lo que queda por liquidar y de lo que le corresponde
  en el período (liquidado más **ajustes** manuales), exportable en CSV para Excel, imprimible en PDF y enviable por
  correo a cada agente;
- de forma opcional (opciones en Configuración): estima la comisión al guardar un documento, calcula por sí solo las
  facturas recién registradas, protege los porcentajes corregidos a mano, liquida los cobros parciales, cierra los
  períodos ya entregados, calcula los **premios** sobre la facturación anual, prepara los **borradores de las
  facturas** de los agentes y señala las anomalías (**Verificaciones**).

Todo está en SAP: campos de usuario en los empleados del departamento de ventas y en las líneas de los documentos,
tablas de usuario para reglas, comisiones y ajustes, ninguna base de datos externa. Funciona igual en Microsoft SQL Server y SAP HANA; en SAP HANA se recomienda una prueba durante la instalación.

## 2. Los conceptos: beneficiarios, porcentajes, partes, liquidación

### Quién recibe la comisión (beneficiarios)

El **empleado del departamento de ventas** del documento es el agente. En Agentes se le pueden indicar un **jefe
de zona**, un **jefe de área** y un **director**: son los demás beneficiarios de sus documentos. Cada uno tiene su
propio porcentaje en cada línea (las cuatro columnas *Provv. % agente / capo zona / capo area / direttore*
(Com. % agente / jefe de zona / jefe de área / director)).

- Un empleado recibe comisiones solo si tiene un **rol** (Agente, Jefe de zona, Jefe de área, Director). Un empleado
  sin rol no está "gestionado": sus documentos no generan comisiones y, si está indicado como superior de alguien,
  su parte no se calcula.
- El rol "Agente" vale para quien aparece como empleado de ventas en los documentos; "Jefe de zona", "Jefe de área"
  y "Director" son los títulos con los que un empleado puede elegirse como superior. Quien tiene un rol de superior
  puede tener de todos modos documentos propios: en esos es el agente.

### Los porcentajes

Los porcentajes de una línea vienen de las **reglas** (capítulo 7) o, si no se aplica ninguna regla, de los
**porcentajes predeterminados** del agente del documento (capítulo 6). Se asignan solos mientras se rellena el
documento (capítulo 8), se pueden corregir a mano y se pueden controlar y ajustar en bloque antes del cálculo
(capítulo 9).

### Las partes: a la facturación y al cobro

La comisión de un documento no se debe toda de inmediato. Para cada beneficiario el add-on la divide en partes:

- la parte **a la facturación** (plazo 0), igual al "% a la facturación" del empleado, se devenga en la fecha de
  contabilización del documento;
- el resto se devenga **al cobro**: con la liquidación **por plazos**, una parte por cada plazo del documento, en
  proporción al plazo, liquidable cuando ese plazo está cobrado; con la liquidación **sobre el total**, una sola
  parte (plazo -1), liquidable cuando todos los plazos están cobrados.

Ejemplo: factura de 1.350 de base imponible con 5% de comisión = 63,00; agente con 30% a la facturación y liquidación
por plazos, documento en dos plazos al 50%: parte 0 = 18,90 en la contabilización, plazo 1 = 22,05 y plazo 2 = 22,05 en
los respectivos vencimientos.

### La liquidación

Liquidar una parte significa reconocerla al agente con una fecha de liquidación. El add-on propone las partes por
liquidar leyendo los cobros de SAP (pagos, efectos, reconciliaciones, notas de crédito) y propone la **reversión**
de las partes liquidadas cuyos plazos han dejado de estar saldados (impagados). Una parte **consolidada** es
definitiva: no se revierte y la comisión no se vuelve a calcular.

## 3. Instalación y primer inicio

- Paquete para el Extension Manager: `XEI.CommissionManagement.zip`, desde la página de descargas del sitio
  XEI. En SAP Business One se abre el **Extension Manager**, se importa el paquete y se asigna a la empresa.
- En el primer inicio el add-on crea campos, tablas, índices y autorizaciones. La creación de los campos en las líneas de los documentos requiere **algunos
  minutos**: SAP muestra varias veces el mensaje *"La estructura de la base de datos se ha modificado... se cerrarán
  todas las ventanas abiertas. ¿Continuar?"*: responder **Sí**.
- El menú está en **XEI-Addon › Comisiones**:

    Comisiones
      Configuración                     opciones (seis pestañas) y orden de búsqueda de las reglas
      Agentes                           rol, superiores, % predeterminados, % a la facturación, liquidación, proveedor, usuario SAP
      Reglas de porcentaje              % por cliente / grupo / artículo / grupo de artículos / lista de precios
      Tramos y premios                  premios sobre la facturación anual (si están activos en Configuración)
      Control y asignación %            comparación documentos / reglas y corrección en bloque
      Cálculo de comisiones             cálculo sobre facturas, anticipos y notas de crédito
      Comisiones calculadas             consulta, corrección, recálculo, eliminación
      Liquidación                       partes cobradas por liquidar, impagados por revertir
      Ajustes                           importes manuales por agente y mes, borradores de facturas de los agentes
      Extracto de comisiones            calculadas, por liquidar, liquidadas + ajustes; CSV, impresión/PDF, correo
      Verificaciones                    anomalías por revisar
      Informazioni, Traduzioni, Licenza (Información, Traducciones, Licencia: entradas comunes de los add-ons XEI)

> Después de la instalación: rellenar la **Configuración**, luego los **Agentes** (roles, superiores,
> porcentajes) y luego las **Reglas**. Solo a partir de ese momento los documentos reciben los porcentajes. A los
> usuarios que no son superusuarios se les deben asignar las **autorizaciones** (capítulo 17).

### Licencia

El add-on funciona con un **código de licencia** emitido por XEI.

- **Prueba**: tras solicitar la prueba en el sitio se recibe por correo un **código de prueba**, válido durante 30
  días desde el envío en cualquier empresa.
- **Compra**: se envían a XEI los dos códigos de la ventana **Licenza** (Licencia) (código de la empresa y código
  del servidor, con *Copia* (Copiar)) y se recibe el código de licencia, que vale para la empresa o para el servidor
  de esos códigos.
- Sin un código válido el add-on está **bloqueado**: en su menú quedan *Informazioni* (Información) y *Licenza*, y
  al iniciar se abre por sí sola la ventana **Licenza** con el estado y el motivo.
- Un usuario SAP **superusuario** pega el código en *Inserisci un codice di licenza* (Introducir un código de
  licencia) y pulsa *Salva codice* (Guardar código): el add-on se desbloquea al instante, sin reiniciar SAP.

### Idiomas

El add-on usa el idioma del cliente SAP (en SAP: Usuarios - Configuración \> Visualización \> Idioma): italiano,
inglés, alemán, francés, español o turco; con los demás idiomas queda en italiano. Al cambiar de idioma SAP cierra
las ventanas abiertas y el add-on se reinicia solo. Los textos individuales se pueden adaptar desde **Comisiones \>
Traduzioni** (Traducciones). Quedan en italiano en todos los idiomas los textos que SAP guarda una sola vez en la base
de datos: los nombres de las autorizaciones (Autorizaciones generales \> Provvigioni) y los títulos de los campos
añadidos a documentos y empleados (p. ej. "Provv. % manuali", "% agente"); los mensajes los citan con estos nombres,
para encontrarlos en SAP.

## 4. El trabajo de cada mes, en resumen

1.  **Durante el mes** los documentos reciben los porcentajes solos; quien los introduce puede corregirlos.
2.  **Control y asignación %** sobre las facturas del mes: se ven las líneas cuyos porcentajes no corresponden
    a las reglas y se corrigen en bloque (opcional pero recomendado).
3.  **Cálculo de comisiones** del mes: facturas, facturas de anticipo, notas de crédito.
4.  **Comisiones calculadas**: control por muestreo, correcciones de comisiones concretas.
5.  **Liquidación** con fecha límite a fin de mes: confirmación de las partes cobradas y de las posibles reversiones.
6.  **Ajustes** del mes (premios, recuperaciones, rectificaciones manuales) y, si están activos, los **borradores de
    facturas** de los agentes.
7.  **Extracto de comisiones** "liquidadas y ajustes" del mes: es el importe que se debe reconocer a cada agente; CSV
    para Excel, impresión/PDF o correo a cada agente.
8.  Cuando los extractos están entregados, **período cerrado** hasta fin de mes (si se usa la opción).

Las **Verificaciones** (capítulo 16) se pueden lanzar en cualquier momento, antes del cálculo o antes de los
extractos, para encontrar documentos no calculados, agentes cambiados, líneas sin porcentajes, cobros no liquidados.
A fin de año, **Tramos y premios** (capítulo 15) registra los premios sobre la facturación como ajustes de diciembre.

## 5. Configuración

La Configuración tiene seis pestañas. La pestaña **General** contiene las opciones básicas y el orden de las reglas;
las demás (**Documentos**, **Liquidación**, **Agentes**, **Correo**, **Avisos**) contienen las funciones
adicionales, todas **desactivadas** al principio: cada una tiene debajo una explicación y un ejemplo, y se activa con
la marca cuando hace falta. Se necesita la autorización «Configurazione» (Configuración) (capítulo 17).

![Configurazione, scheda Generale](../../_img/commissionmanagement/cfg.png)

*Configuración de comisiones, pestaña General*

### Pestaña General

Asignar los porcentajes a las líneas de los documentos de venta mientras se rellenan  
Activa la asignación automática (capítulo 8). Si se desactiva, los porcentajes se escriben a mano o con el Control.

Descuento de línea de las reglas  
El descuento con el que las reglas comparan su "descuento mínimo": el *% descuento de la línea* o un campo
de usuario porcentual de las líneas (por ejemplo un descuento "efectivo" calculado por otro add-on).

Precios netos  
Para quien vende a precio neto sin indicar el descuento: si la línea no tiene descuento, el add-on calcula el
**descuento efectivo** como diferencia entre el precio de la lista de precios del cliente y el precio de la línea
(lista 100, precio 80 = descuento 20%), lo escribe en la columna *Provv. sconto effettivo* (Com. descuento efectivo)
y lo usa para las reglas.

Porcentajes también en las líneas «solo impuesto»  
Normalmente las líneas "solo impuesto" no tienen comisión (porcentajes a cero).

Comisiones sobre las facturas de anticipo  
Con la opción activa las facturas de anticipo se calculan y su comisión se **deduce** después de la factura final
que las cierra, de modo que la comisión total es la del importe completo.

Liquidación predeterminada al cobro del documento completo  
Vale para los empleados con liquidación "Según configuración": sí = una sola parte cuando todo el documento está
cobrado; no = una parte por plazo.

Notas de crédito liquidadas al vencimiento  
Normalmente la comisión (negativa) de una nota de crédito se liquida en la fecha de contabilización. Con la opción,
en el vencimiento más lejano entre la nota y las facturas a las que se refiere.

Orden de búsqueda de las reglas  
Las 16 combinaciones de campos posibles para una regla, en el orden en que se prueban. Se cambia el número en la
columna *Orden*: el orden 1 se prueba primero. Véase el capítulo 7.

### Pestaña Documentos

![Configurazione, scheda Documenti](../../_img/commissionmanagement/cfg_documenti.png)

*Pestaña Documentos: estimación, líneas manuales, cálculo automático*

Mostrar la comisión estimada al guardar un documento de venta  
Al añadir o actualizar un pedido, una oferta, una entrega o una factura, la barra de estado indica cuánto se
devengará a cada beneficiario con los porcentajes actuales de las líneas. Ejemplo: *"Comisiones estimadas (Pedido de
cliente 1250): Rossi 63,00; Bianchi 9,00 - total 72,00"*. Es solo una información: no se guarda nada (capítulo 8).

Proteger los porcentajes modificados a mano en las líneas de los documentos  
Quien corrige un porcentaje en la línea la vuelve "manual" (columna *Provv. % manuali* (Com. % manuales)): al
cambiar cliente o agente esa línea no se reasigna. Ejemplo: Rossi baja la línea del 5% al 4% por un acuerdo con el
cliente; luego cambia el cliente: las demás líneas se reasignan, esta queda al 4%. Sin la opción la reasignación
sobrescribe todas las líneas. Quitando la marca "manual" la línea vuelve a ser automática.

Calcular las comisiones al registrar una factura, una factura de anticipo o una nota de crédito  
El cálculo se hace al guardar desde el cliente SAP (con la última elección hecha sobre el descuento global en el
Cálculo): así no hace falta abrir Cálculo de comisiones cada mes. Ejemplo: registrada la factura 1001 de Rossi, la
barra de estado dice *"Comisiones calculadas (Factura 1001): Rossi 63,00; Bianchi 9,00"*. Los documentos creados por
importaciones u otros programas (DI API) no pasan por el cliente: para esos quedan Cálculo de comisiones y las
Verificaciones.

### Pestaña Liquidación

![Configurazione, scheda Liquidazione](../../_img/commissionmanagement/cfg_liquidazione.png)

*Pestaña Liquidación: cobros parciales y período cerrado*

Cobros parciales: liquidar la parte de comisión proporcional a lo cobrado en el plazo  
Sin la opción una parte se liquida solo cuando el plazo está cerrado del todo: con pagos a cuenta o descuentos la
comisión queda parada. Ejemplo: plazo de 500 con parte 22,05; el cliente paga 250 → se liquidan 11,03; al saldarlo,
los otros 11,02. Si se cancela un cobro se revierte solo el exceso (capítulo 12).

Período cerrado: bloquear comisiones hasta el (fecha)  
Hasta esa fecha incluida no se pueden recalcular ni eliminar comisiones, modificar partes, liquidar ni guardar
ajustes. Ejemplo: entregados los extractos de marzo, se pone 31/03: las facturas de marzo quedan excluidas del
recálculo (una factura nunca calculada se puede calcular igualmente). Para corregir algo en el período cerrado:
retrasar la fecha (o quitar la marca), corregir y volver a ponerla.

### Pestaña Agentes

Generar desde los ajustes los borradores de facturas de proveedor de los agentes con proveedor vinculado  
En Ajustes el botón **Borradores de facturas** crea para cada agente un borrador de factura de proveedores (nota
de crédito si el importe es negativo) con una línea de servicio: importe = partes liquidadas en el mes + ajustes y
premios del mes. Ejemplo: Rossi (proveedor F0010), abril: 22,05 + 50,00 - 20,00 = 52,05. La **cuenta de la línea**
es obligatoria (la cuenta de gasto de las comisiones, p. ej. 7xxxx Comisiones pagadas); el **código IVA** es el de
las facturas del agente (vacío = el predeterminado del proveedor). Capítulo 13.

Tramos de facturación anual con premio  
Activa el menú **Tramos y premios**: alcanzado el umbral de base imponible anual, el agente recibe un premio (% de la
facturación del año o importe fijo) registrado como ajuste. Ejemplo: tramos 100.000 → 0,5% y 200.000 → 1%;
Rossi factura 150.000 en 2026: premio de 750,00 en el ajuste de diciembre. Capítulo 15.

Retención orientativa en el extracto de liquidadas: % y descripción  
Solo informativa (sin mínimos ni máximos): en la impresión y en el correo del extracto "liquidadas y ajustes"
aparece una línea "retención" y el neto orientativo. Ejemplo: 8,5 y "Enasarco quota agente": liquidado 1.000,00 →
retención orientativa -85,00, neto orientativo 915,00. Vacío o 0 = ninguna línea.

![Configurazione, scheda Agenti](../../_img/commissionmanagement/cfg_agenti.png)

*Pestaña Agentes: borradores de facturas, tramos y retención orientativa (8,5% Enasarco)*

### Pestaña Correo

![Configurazione, scheda Email](../../_img/commissionmanagement/cfg_email.png)

*Pestaña Correo: envío del extracto a los agentes*

Envío del extracto a los agentes por correo  
Activa el botón **Enviar a los agentes** en el Extracto de comisiones: cada agente recibe solo su propio extracto
(adjunto HTML, que se abre e imprime con cualquier navegador) en la dirección de correo del empleado de ventas (o del
proveedor vinculado). Hay que indicar servidor SMTP, puerto, SSL/TLS, usuario y contraseña del buzón y el remitente;
ejemplo: `smtp.office365.com`, puerto 587, SSL sí, remitente `provvigioni@azienda.it`. La
contraseña se guarda cifrada.

Probar envío  
Manda un mensaje de prueba a la dirección indicada usando los valores escritos en la pestaña (aunque no estén
guardados): si algo no funciona, el mensaje de error del servidor aparece de inmediato.

### Pestaña Avisos

![Configurazione, scheda Avvisi](../../_img/commissionmanagement/cfg_avvisi.png)

*Pestaña Avisos*

Parte cobrada y no liquidada: es una anomalía después de (días)  
En las Verificaciones, la búsqueda "Cobros no liquidados" señala las partes cuyo plazo se cobró hace más de
estos días y que nadie ha liquidado. Ejemplo: 30; plazo cobrado el 05/04 y hoy 10/05: la parte aparece entre las
anomalías hasta que se liquide.

Al iniciar el add-on, señalar las anomalías rápidas en la barra de estado  
Controles rápidos en cada inicio: documentos de los últimos 90 días por calcular, documentos cancelados con
comisiones, agente cambiado tras el cálculo. Ejemplo: *"Comisiones: 3 anomalías por revisar (Comisiones \>
Verificaciones)"*. Capítulo 16.

> Al guardar, la Configuración controla que las opciones activas estén completas: fecha del período cerrado,
> cuenta existente e imputable para los borradores, retención entre 0 y 99,99, servidor, puerto y remitente para el correo.

## 6. Agentes

![Agenti](../../_img/commissionmanagement/agenti.png)

*Agentes: todos los empleados del departamento de ventas de SAP, modificables en la cuadrícula*

La cuadrícula muestra todos los empleados del departamento de ventas de SAP. Se rellenan las columnas y se pulsa
**Guardar**: se guardan solo los empleados modificados (los mismos campos se ven también en el formulario estándar de
los empleados, pestaña de campos de usuario).

| Columna                                             | Significado                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rol                                                 | Agente, Jefe de zona, Jefe de área, Director o *(no gestionado)*: ninguna comisión.                                                                                                                                                                                                                                                                                                                           |
| Jefe de zona, Jefe de área, Director                | Los superiores de este empleado: reciben su porcentaje sobre los documentos de este. Las listas desplegables muestran los empleados que tienen ese rol: asignar primero los roles y guardar, luego los superiores. Un superior ya asignado que tiene otro rol, o ninguno, aparece como *«nombre (rol distinto)»*: no recibe comisiones hasta que se le asigne el rol (también lo señalan las Verificaciones). |
| % agente, % jefe de zona, % jefe de área, % director | Porcentajes **predeterminados** de los documentos de este empleado, usados cuando ninguna regla se aplica a la línea.                                                                                                                                                                                                                                                                                         |
| % a la facturación                                  | Parte de la comisión **de este empleado** (como beneficiario) que se devenga con la contabilización del documento; el resto se devenga al cobro. 100 = todo a la facturación, 0 = todo al cobro.                                                                                                                                                                                                              |
| Liquidación                                         | Para la parte al cobro: *Por plazos*, *Sobre el total* o *Según configuración* (sigue la opción de la Configuración).                                                                                                                                                                                                                                                                                         |
| Proveedor                                           | El proveedor (interlocutor comercial) con el que el agente factura las comisiones: titular de los **borradores de facturas** (capítulo 13); su correo se usa para el envío del extracto si el empleado no tiene uno.                                                                                                                                                                                         |
| Usuario SAP                                         | El usuario SAP que corresponde a este empleado. Un usuario sin la autorización «Estratto di tutti gli agenti» (Extracto de todos los agentes) ve en el Extracto de comisiones solo a sí mismo y a los empleados de los que es jefe de zona, jefe de área o director (capítulo 17).                                                                                                                           |
| Correo (empleado de ventas)                         | El correo del empleado del departamento de ventas (datos maestros de SAP, solo lectura): destinatario del extracto por correo.                                                                                                                                                                                                                                                                                |

Controles al guardar: porcentajes entre 0 y 100, proveedor y usuario SAP existentes, un empleado no puede ser
superior de sí mismo. Ejemplo usado en este manual:

| Empleado | Rol              | Jefe de zona | Jefe de área | % ag. | % j.zona | % j.área | % a la fact. | Liquidación         |
|----------|------------------|--------------|--------------|-------|----------|----------|--------------|---------------------|
| Rossi    | Agente           | Bianchi      | Neri         | 2     | 0,5      | 0,2      | 30           | Por plazos          |
| Bianchi  | Jefe de zona     |              |              | 3     |          |          | 0            | Según configuración |
| Neri     | (no gestionado)  |              |              |       |          |          |              |                     |
| Verdi    | Agente           |              |              | 1,5   |          |          | 100          | Según configuración |

En los documentos de Rossi los beneficiarios son Rossi (agente) y Bianchi (jefe de zona); Neri, aunque está indicado
como jefe de área, no recibe nada hasta que tenga un rol.

## 7. Reglas de porcentaje

![Regole percentuali](../../_img/commissionmanagement/regole.png)

*Reglas de porcentaje del ejemplo*

Una regla dice: "para las líneas con *estas características* los porcentajes son estos". Las características
posibles son cliente, grupo de clientes, artículo, grupo de artículos y lista de precios (la lista de precios del
cliente); se rellenan **solo los campos necesarios** y el add-on reconoce por sí solo la **combinación** (columna
Combinación). Las combinaciones admitidas son 16:

| Tipo | Combinación                                       | Tipo | Combinación                                                 |
|------|---------------------------------------------------|------|-------------------------------------------------------------|
| 1    | Cliente / Artículo / Lista de precios             | 9    | Grupo de clientes / Grupo de artículos / Lista de precios   |
| 2    | Cliente / Artículo                                | 10   | Grupo de clientes / Grupo de artículos                      |
| 3    | Cliente / Grupo de artículos / Lista de precios   | 11   | Grupo de clientes / Lista de precios                        |
| 4    | Cliente / Grupo de artículos                      | 12   | Grupo de clientes                                           |
| 5    | Cliente / Lista de precios                        | 13   | Artículo / Lista de precios                                 |
| 6    | Cliente                                           | 14   | Artículo                                                    |
| 7    | Grupo de clientes / Artículo / Lista de precios   | 15   | Grupo de artículos / Lista de precios                       |
| 8    | Grupo de clientes / Artículo                      | 16   | Grupo de artículos                                          |

Cliente y grupo de clientes juntos (o artículo y grupo de artículos juntos) no están admitidos: la regla no se guarda.

Los demás campos de la regla:

- **Agente**: la regla vale solo para los documentos de ese empleado; *(todos)* = para todos;
- **Desde / Hasta**: período de validez comparado con la fecha del documento; también una sola de las dos fechas;
- **Descuento mínimo**: la regla vale si el descuento de la línea es al menos este (0 = siempre). Sirve para dar
  porcentajes más bajos a las ventas con más descuento;
- **Activa**: una regla desactivada queda archivada pero no se aplica.

### Cómo se elige la regla de una línea

1.  Las combinaciones se prueban en el **orden de la Configuración** (predeterminado 1 → 16, de la más específica a
    la más genérica).
2.  Para cada combinación se buscan primero las reglas del **agente del documento** (si tiene al menos una), luego
    las reglas para todos. Gana la primera combinación que encuentra una regla válida: una regla "para todos" más
    específica (p. ej. Cliente / Grupo de artículos) gana sobre una regla del agente más genérica (p. ej. Grupo de
    artículos).
3.  Entre varias reglas de la misma combinación gana la de fecha de inicio más reciente, luego la de vencimiento más
    cercano, luego la de descuento mínimo alcanzado más alto.
4.  Si ninguna regla vale, se usan los porcentajes predeterminados del agente.

Ejemplo con las reglas de la figura (R1 cliente C001 + grupo de artículos GA100 → 6/1; R2 solo Rossi, grupo GA100 →
7/1; R3 artículo A1 → 4/0,5; R4 artículo A1 con descuento mínimo 10 → 3/0,5; R5 grupo de clientes A, año 2026 → 5/1):

| Línea                                             | Porcentajes agente / jefe de zona | Por qué                                                                   |
|---------------------------------------------------|-----------------------------------|---------------------------------------------------------------------------|
| Rossi, cliente C001, artículo A9 (grupo GA100)    | 6 / 1                             | R1: Cliente / Grupo de artículos se prueba antes que la regla de Rossi     |
| Rossi, cliente C002, artículo A9                  | 7 / 1                             | R2: regla del agente                                                      |
| Verdi, cliente C002, artículo A9                  | 1,5 / 0                           | ninguna regla: porcentajes predeterminados de Verdi                       |
| Verdi, cliente C002, artículo A1, descuento 12    | 3 / 0,5                           | R4: descuento mínimo 10 alcanzado (gana sobre R3)                         |
| Verdi, cliente C002, artículo A1, descuento 5     | 4 / 0,5                           | R3                                                                        |
| Verdi, cliente C003 (grupo A), artículo A1        | 5 / 1                             | R5: Grupo de clientes se prueba antes que Artículo                        |
| como arriba pero en 2027                          | 4 / 0,5                           | R5 vencida, queda R3                                                      |

### El formulario

- **Filtros** (agente, cliente, artículo, solo activas) y **Buscar**.
- **Añadir fila**, **Duplicar filas** y **Eliminar filas** sobre las filas seleccionadas (clic en la cabecera
  de fila, a la izquierda); los cambios son definitivos con **Guardar**. Todos los campos se modifican en la
  cuadrícula (las flechas abren cliente y artículo).
- **Exportar CSV** guarda las reglas mostradas en un archivo con separador ";" (se abre en Excel); **Importar CSV**
  añade las filas de un archivo con las mismas columnas (Agente, Cliente, GruppoClienti, Articolo, GruppoArticoli,
  Listino, Dal, Al, ScontoMinimo, PercAgente, PercCapoZona, PercCapoArea, PercDirettore, Attiva): las filas importadas
  se deben revisar y guardar.
- Al cerrar o buscar con cambios sin guardar el add-on pide confirmación.

## 8. Los porcentajes en los documentos de venta

![Ordine cliente](../../_img/commissionmanagement/ordine.png)

*Pedido de cliente: las columnas Provv. con los porcentajes asignados y, con los precios netos, el descuento efectivo*

Con la asignación activa, en ofertas de ventas, pedidos de cliente, entregas, devoluciones, facturas de deudores,
notas de crédito de clientes y facturas de anticipo de clientes:

- cuando se introduce o se cambia el **artículo**, el **descuento** o el **precio** de una línea, el add-on escribe
  los cuatro porcentajes de la línea (y el descuento efectivo, con los precios netos);
- al elegir varios artículos de la lista, se completan también las líneas añadidas;
- al cambiar el **cliente** o el **empleado del departamento de ventas** de un documento en creación, se
  reasignan todas las líneas. Atención: al cambiar el cliente SAP vuelve a poner el empleado predeterminado de ese
  cliente; si es "ninguno", las líneas quedan como estaban hasta que se elige el agente.

Los porcentajes siguen siendo **modificables a mano** y se guardan con el documento; se reescriben solo si se
cambia otra vez el artículo, el precio o el descuento de esa línea. Los documentos copiados (pedido → entrega →
factura) llevan consigo los porcentajes de las líneas.

> Las columnas *Provv. % agente*, *% capo zona*, *% capo area*, *% direttore* y
> *Provv. sconto effettivo* (Com. % agente, % jefe de zona, % jefe de área, % director y Com. descuento efectivo) las
> hace visibles y modificables el add-on al abrir el documento; para tenerlas siempre en la posición preferida se
> pueden colocar una vez en la configuración del formulario (icono arriba a la derecha de la cuadrícula). En los
> documentos sin empleado de ventas, o con un empleado sin rol, no se escribe nada.

La marca "solo impuesto" de una línea no genera un evento en el cliente: los porcentajes se adaptan con el siguiente
cambio de artículo, precio o descuento de la línea (o al cambiar el agente).

### Líneas manuales (opción "proteger los porcentajes modificados a mano")

![Ordine con riga manuale](../../_img/commissionmanagement/ordine_manuale.png)

*Pedido: la línea con el porcentaje corregido a mano está marcada en "Provv. % manuali" y queda excluida de la
reasignación*

Con la opción activa el add-on muestra también la columna *Provv. % manuali* (Com. % manuales). En cuanto se escribe a
mano uno de los cuatro porcentajes de una línea, la línea queda **marcada como manual** y a partir de ese momento no se
reasigna: ni al cambiar artículo, precio o descuento de la línea, ni al cambiar cliente o agente del documento, ni al
elegir otros artículos de la lista. Las demás líneas siguen las reglas. Para volver al modo automático basta con
quitar la marca: con el siguiente cambio la línea vuelve a recibir los porcentajes de las reglas. La marca pasa a los
documentos copiados y se ve en el Control (columna *% manuales*), donde las líneas manuales no se proponen para la
corrección.

### Estimación y cálculo automático al registrar

![Stima in barra di stato](../../_img/commissionmanagement/stima.png)

*Después de añadir el pedido, la barra de estado muestra la comisión estimada para cada beneficiario*

Dos opciones de la pestaña Documentos actúan cuando el documento se **guarda** desde el cliente SAP:

- **Estimación**: para ofertas, pedidos, entregas, devoluciones, facturas, notas de crédito y facturas de anticipo, la
  barra de estado muestra cuánto se devengaría con los porcentajes actuales de las líneas, beneficiario por
  beneficiario, por ejemplo *"Comisiones estimadas (Pedido de cliente 1250): PRV Rossi 6,00; PRV Bianchi 1,00 -
  total 7,00"*. El descuento global se tiene en cuenta o no según la última elección hecha en el Cálculo. No se guarda
  nada.
- **Cálculo automático**: las facturas, las notas de crédito y (si están activas) las facturas de anticipo
  **añadidas** desde el cliente se calculan de inmediato, como si se hubiera lanzado Cálculo de comisiones solo sobre
  ese documento; la barra de estado dice *"Comisiones calculadas (Factura 1001): ..."*. En Comisiones calculadas el
  origen es "Automático al registrar". Si el cálculo no es posible (anticipo ya deducido, período cerrado, agente no
  gestionado) aparece un aviso y el documento queda registrado con normalidad: se calcula después desde Cálculo de
  comisiones, y las Verificaciones lo señalan entre los "Por calcular".

> Los documentos creados por importaciones, desde el Service Layer o desde la DI API no pasan por el cliente SAP:
> para esos vale siempre Cálculo de comisiones (o el cálculo de todo el período, que toma solo los documentos todavía
> no calculados).

## 9. Control y asignación %

![Controllo e assegnazione percentuali](../../_img/commissionmanagement/controllo.png)

*Control: porcentajes del documento ("Doc.") y propuestos por las reglas, líneas distintas resaltadas*

Antes del cálculo conviene verificar que los porcentajes de los documentos del período correspondan a las reglas
(quien introdujo la factura podría haberlos cambiado, o las reglas pueden haberse actualizado después).

1.  Elegir agente (o todos), período y tipos de documento: facturas, facturas de anticipo, notas de crédito **todavía
    no calculadas** y, si se desea, pedidos de cliente abiertos. Pulsar **Verificar**.
2.  Para cada línea la cuadrícula muestra los porcentajes actuales (*Doc.*), los que darían hoy las reglas
    (*Propuesta*) y el *Origen propuesta* (regla para todos, regla del agente, porcentajes predeterminados). Las
    líneas distintas están resaltadas y ya marcadas; con "Solo líneas distintas de lo propuesto" se ven solo esas.
3.  Quitar la marca a las líneas que se deben dejar como estaban (las correcciones deseadas) y pulsar **Aplicar los %
    propuestos**.

Qué ocurre con las líneas marcadas:

- **pedidos de cliente abiertos**: el pedido se actualiza; los porcentajes corregidos pasan a los documentos que se
  copien de él;
- **facturas, facturas de anticipo y notas de crédito**: son documentos registrados y SAP no permite modificarlos
  (tampoco los campos de usuario de las líneas). El add-on guarda los porcentajes corregidos en una tabla propia y el
  cálculo los usa en lugar de los del documento; el documento SAP queda como está. La columna *Ya corregida*
  lo indica y la columna *Doc.* muestra desde ese momento los porcentajes corregidos.

![Controllo con righe manuali](../../_img/commissionmanagement/controllo_manuale.png)

*Control sobre los pedidos abiertos: las líneas manuales distintas de la propuesta no se marcan ("con % manuales: 3")*

Doble clic en una línea abre el documento. Los documentos con comisiones ya calculadas no aparecen: para corregirlos
se usa Comisiones calculadas (capítulo 11). La columna *% manuales* muestra las líneas cuyos porcentajes se han
corregido a mano en el documento: con la opción "proteger los porcentajes modificados a mano" no se marcan (se pueden
marcar expresamente). Con el período cerrado activo, los documentos registrados con fecha en el período no se corrigen.

## 10. Cálculo de comisiones

![Calcolo provvigioni](../../_img/commissionmanagement/calcolo.png)

*Cálculo de comisiones con el resultado por documento*

Elegir el período (fecha del documento), los tipos (facturas, facturas de anticipo si están activas en Configuración,
notas de crédito) y si **considerar el descuento global** (el documento entero con descuento reduce la base imponible
de cada línea). **Calcular** procesa todos los documentos del período **no cancelados**, con un agente gestionado y
**todavía no calculados**: primero las facturas de anticipo, luego facturas y notas de crédito. La cuadrícula muestra
para cada documento cuántos beneficiarios tienen comisión, el total y el resultado; doble clic abre el documento.

Con **Solo el documento** (tipo y número) se calcula o **recalcula** un documento concreto, por ejemplo después de
una corrección de los porcentajes; el recálculo es posible solo si ninguna de sus partes está liquidada o consolidada.

### Cómo se calcula, paso a paso

Para cada beneficiario (agente y superiores con rol):

1.  **Base imponible de línea** = total de la línea en moneda local, reducido por el descuento global si se pide;
    negativo en las notas de crédito. Las líneas a cero (obsequios) no cuentan.
2.  **Comisión de línea** = base imponible × porcentaje de la línea para ese rol. Las líneas con porcentaje 0 no
    cuentan.
3.  **Total** = suma de las comisiones de línea. De las facturas que cierran un anticipo se resta la comisión
    ya calculada sobre el anticipo (en proporción al importe deducido).
4.  **Partes**: la parte a la facturación (plazo 0) en la fecha de contabilización; el resto por plazos (plazo n al
    vencimiento del plazo n, en proporción a su porcentaje; el último plazo recoge los redondeos) o sobre el total
    (plazo -1 al vencimiento del último plazo). Las notas de crédito tienen una sola parte negativa (plazo 0 en la
    contabilización o, con la opción, al vencimiento).

Los importes se redondean a 2 decimales; el total de la comisión es siempre la suma de las partes.

### Ejemplo: factura 1001

Rossi (30% a la facturación, por plazos), cliente C001, **descuento global 10%**, dos plazos al 50% (31/03 y 30/04):

| Línea          | Total línea | Base imponible (−10%) | % agente | Com. agente | % jefe de zona | Com. jefe de zona |
|----------------|-------------|-----------------------|----------|-------------|----------------|-------------------|
| A1             | 1.000,00    | 900,00                | 5        | 45,00       | 1              | 9,00              |
| A2             | 500,00      | 450,00                | 4        | 18,00       | 0              | \-                |
| A3 (obsequio)  | 0,00        | \-                    | 5        | \-          |                |                   |
| Total          |             | 1.350,00              |          | 63,00       |                | 9,00              |

| Beneficiario                                  | Parte                          | Vencimiento              | Importe |
|-----------------------------------------------|--------------------------------|--------------------------|---------|
| Rossi (agente, 30% a la facturación)          | plazo 0 – a la facturación     | 10/03 (contabilización)  | 18,90   |
|                                               | plazo 1 (35%)                  | 31/03                    | 22,05   |
|                                               | plazo 2 (35%)                  | 30/04                    | 22,05   |
| Bianchi (jefe de zona, 0% a la facturación)   | plazo 1 (50%)                  | 31/03                    | 4,50    |
|                                               | plazo 2 (50%)                  | 30/04                    | 4,50    |

Neri (jefe de área) no recibe nada porque no tiene un rol, aunque la línea A1 tenga el 0,5% en su columna.

### Facturas de anticipo

SAP registra una factura de anticipo con las líneas completas del pedido y un descuento global igual al complemento
del anticipo (anticipo del 30% = descuento del 70%): el add-on usa siempre ese descuento, por lo que la base imponible
es la parte de anticipo (10.000 × 30% = 3.000 → 150,00 al 5%). Cuando la factura final deduce el anticipo, de su
comisión (10.000 × 5% = 500,00) se restan los 150,00 ya calculados: quedan 350,00, divididos en las partes como de
costumbre. Mientras la factura final tenga comisiones calculadas, el anticipo no se puede recalcular ni eliminar (hay
que corregir la factura).

### Qué no se recalcula

- documentos con partes **liquidadas o consolidadas** (primero hay que quitar la liquidación, capítulo 11);
- facturas de anticipo ya deducidas de una factura calculada;
- documentos cancelados: no se calculan; si se calcularon antes de la cancelación, su comisión se debe
  eliminar a mano desde Comisiones calculadas (la Liquidación los ignora).

## 11. Comisiones calculadas: consultar y corregir

![Provvigioni calcolate](../../_img/commissionmanagement/provvigioni.png)

*Comisiones calculadas: lista, líneas del documento con el % del beneficiario y partes*

La lista de arriba muestra una fila por documento y beneficiario (filtros por agente, tipo, período, número, solo no
liquidadas): base imponible, comisión, liquidado, por liquidar, fecha de cálculo. Al hacer clic en una fila, debajo
aparecen las **líneas del documento** con el porcentaje de ese beneficiario y las **partes**. Doble clic abre el
documento en SAP.

Recalcular con % modificados  
Se cambia el porcentaje en las líneas de abajo (columna *%*) y se recalcula solo esta comisión. El documento
SAP no se toca: sirve para corregir un caso concreto sin modificar las reglas. Ejemplo: línea A2 del 4% al 6%
→ 63,00 pasa a 72,00 y las partes a 21,60 / 25,20 / 25,20.

Recalcular del documento  
Recalcula con los porcentajes actuales de las líneas del documento (o corregidos por el Control): anula los cambios
hechos con el botón precedente y recoge las correcciones hechas en el documento.

Guardar partes  
Fecha de liquidación, importe liquidado y marca *Consolidada* de las partes se pueden modificar a mano
(liquidaciones fuera del procedimiento, ajustes): Guardar partes los registra y actualiza el liquidado de la cabecera.

Eliminar comisión  
Quita la comisión de este beneficiario en el documento; el documento vuelve a ser calculable desde el Cálculo (solo
el documento o en el período).

El recálculo y la eliminación están bloqueados si una parte ya está liquidada o consolidada ("Comisiones ya liquidadas
o consolidadas: primero quitar la liquidación": en Guardar partes poner a cero el liquidado), si el documento está en
el **período cerrado** (pestaña Liquidación de la Configuración) y, por prudencia, si el empleado ha salido de la
jerarquía del agente del documento (el recálculo lo borraría: usar Eliminar si es lo deseado).

**Trazabilidad**: cada cabecera y cada parte muestran *Origen*, *Usuario* y *Última modificación*: quién escribió
ese dato por última vez y cómo. Orígenes de las cabeceras: *Cálculo* (desde el menú), *Automático al registrar*
(al registrar la factura), *Recálculo desde el documento*, *Recálculo con % modificados*; de las partes:
*Cálculo*, *Liquidación*, *Reversión impagado*, *Manual* (Guardar partes).

## 12. Liquidación

![Liquidazione](../../_img/commissionmanagement/liquidazione.png)

*Liquidación: propuestas de las partes por liquidar al 31/03*

1.  Indicar la **fecha límite** (normalmente fin de mes), si se incluyen las notas de crédito y, si se desea, marcar
    los agentes que se deben procesar (ninguno = todos). **Procesar**.
2.  La cuadrícula propone:
    - **Liquidar** – partes todavía no liquidadas y no consolidadas con vencimiento dentro de la fecha límite:
      - la parte a la facturación (plazo 0) siempre, en su vencimiento (fecha de contabilización del documento);
      - la parte de un plazo cuando ese plazo está **cerrado** en SAP; la parte sobre el total (plazo -1) cuando
        todos los plazos están cerrados;
      - la **fecha de liquidación** propuesta es la más reciente entre el vencimiento del plazo y la fecha de cobro.
        La fecha de cobro tiene en cuenta cobros (fecha del pago o su vencimiento si es posterior), efectos
        depositados con buen fin, reconciliaciones con asientos o notas de crédito, notas de crédito emitidas sobre
        la factura; si no se puede determinar, vale el vencimiento.
    - **Revertir** (filas rojas) – partes ya liquidadas y no consolidadas cuyos plazos han dejado de estar saldados
      (cobro cancelado, impagado): la liquidación se quita y el importe vuelve a estar por liquidar.
3.  Quitar la marca a las filas que no se deben registrar, corregir si hace falta la fecha de liquidación, marcar
    **Consolidar** en las partes que se deben hacer definitivas. Los totales del pie se actualizan con las marcas.
4.  **Confirmar** registra las filas marcadas; el liquidado de los documentos se actualiza y un procesamiento
    posterior no las vuelve a proponer.

![Storno](../../_img/commissionmanagement/liquidazione_storno.png)

*Tras la cancelación de un cobro: propuesta de reversión de las partes liquidadas*

Ejemplo: la factura 1001 tiene el primer plazo (vencimiento 31/03) cobrado el 05/04. Procesando al 30/04 se proponen
la parte del plazo 1 de Rossi (22,05) y de Bianchi (4,50) con fecha de liquidación 05/04. Si se cancela el cobro, el
procesamiento siguiente propone la reversión de las dos partes; si la parte de Rossi estaba consolidada, se propone
solo la reversión de Bianchi.

> Una parte **consolidada** es definitiva: no se revierte y la comisión del documento no se vuelve a
> calcular. Consolidar cuando las comisiones se han pagado al agente.

### Cobros parciales (opción)

![Liquidazione con incasso parziale](../../_img/commissionmanagement/liquidazione_parziale.png)

*Cobro parcial: filas amarillas con la parte liquidable, la parte entera y lo ya liquidado*

Normalmente la parte de un plazo se liquida solo cuando el plazo está **cerrado**: si el cliente paga a cuenta, la
comisión queda parada. Con la opción **Cobros parciales** la parte se liquida en proporción a lo cobrado:
plazo de 816,75 con parte 22,05, el cliente paga 408,38 (la mitad) → se propone la liquidación de **11,03** (fila
amarilla, con las columnas *Parte entera* 22,05 y *Ya liquidado* 0), en la fecha del cobro si es posterior al
vencimiento; al saldarlo se propone el resto, **11,02**. Si se cancela un cobro, la reversión lleva el liquidado
a la parte todavía cobrada (todo, si no queda nada cobrado). Las partes a la facturación (plazo 0) no cambian; para
las partes "sobre el total del documento" la proporción se calcula sobre lo cobrado de todos los plazos.

### Período cerrado (opción)

Cuando los extractos de un mes se han entregado, se puede **cerrar el período** hasta esa fecha (pestaña
Liquidación de la Configuración): a partir de ese momento, para los documentos con fecha en el período no se
recalculan ni se eliminan comisiones, no se modifican partes ni se liquida o revierte con una fecha en el período, no
se guardan ajustes ni premios en los meses cerrados y el Control no corrige los documentos registrados. En todos los
casos el mensaje dice *"Período cerrado hasta el dd/mm/aaaa"*, antes de cualquier pregunta de confirmación (si las
partes ya están liquidadas dice en cambio *"Comisiones ya liquidadas o consolidadas"*). Una factura del período nunca calculada se puede calcular igualmente. Para
corregir algo: retrasar la fecha (o quitar la marca), corregir y volver a ponerla.

## 13. Ajustes

![Conguagli](../../_img/commissionmanagement/conguagli.png)

*Ajustes de un mes*

Importes manuales por agente y mes, positivos o negativos (premios, reembolsos, recuperaciones, rectificaciones), con
un orden y una descripción. Se eligen año y mes (flechas \< y \> para cambiar de mes, **Mostrar**), se añaden o
eliminan filas y se pulsa **Guardar**: las filas del mes se sustituyen por las de la cuadrícula. Los ajustes aparecen
en el extracto "liquidadas y ajustes" del mes. La columna *Tipo* distingue los ajustes *manuales* de los
*premios* registrados por los tramos (capítulo 15), que aquí se ven pero no se modifican. Con el período cerrado
activo los meses cerrados no se guardan.

### Borradores de facturas de los agentes (opción)

![Bozze fatture agenti](../../_img/commissionmanagement/bozze.png)

*Ajustes: abajo los borradores de factura generados para el mes, con el enlace al borrador y al proveedor*

Cuando el agente factura las comisiones a la empresa, el botón **Borradores de facturas** prepara el documento en
su lugar. Para el mes elegido, para cada agente gestionado que tiene un **proveedor** vinculado (capítulo 6):

- importe = partes **liquidadas en el mes** (por fecha de liquidación) + **ajustes y premios** del mes;
- importe positivo → borrador de **factura de proveedores**; negativo → borrador de **nota de crédito de
  proveedores**; cero → nada;
- el borrador tiene una línea de servicio en la cuenta indicada en Configuración, con el código IVA elegido (o el
  predeterminado del proveedor) y el importe como total de la línea.

Ejemplo: Rossi (proveedor V20000), abril: plazo liquidado el 05/04 de 22,05 + ajustes +50,00 y -20,00 = borrador de
factura de proveedores de **52,05**. Al terminar un mensaje resume agente por agente (borrador creado, ningún
proveedor, importe cero, borrador ya existente). Los borradores del mes están en la cuadrícula de abajo con el
**estado** (abierto, cerrado, es decir ya convertido en factura, eliminado), la fecha y el usuario; la flecha amarilla
abre el borrador o el proveedor. Un agente con un borrador todavía existente para ese mes se omite: para regenerarlo,
eliminar el borrador en SAP. El borrador se completa y se registra después desde SAP como cualquier otro borrador
(número y fecha de la factura del agente).

## 14. Extracto de comisiones

![Estratto provvigioni](../../_img/commissionmanagement/estratto.png)

*Extracto "liquidadas y ajustes" de abril, agrupado por agente*

Tres extractos, para un período y para un agente o todos, agrupados por agente (flechas para expandir y contraer),
con el total al pie y **Exportar CSV** (una fila "Total agente" por cada agente, para abrir en Excel):

| Extracto                         | Qué muestra                                                                                         | Período referido a     |
|----------------------------------|-----------------------------------------------------------------------------------------------------|------------------------|
| Comisiones calculadas            | una fila por documento y beneficiario: base imponible, comisión, liquidado                          | fecha del documento    |
| Comisiones por liquidar          | las partes todavía no liquidadas (o liquidadas en parte) y no consolidadas                          | vencimiento de la parte |
| Comisiones liquidadas y ajustes  | las partes liquidadas más los ajustes de los meses del período: **es lo que se reconoce al agente** | fecha de liquidación   |

### Imprimir / PDF

![Estratto stampato](../../_img/commissionmanagement/estratto_stampa.png)

*El extracto abierto en el navegador: un bloque por agente, totales y retención orientativa*

El botón **Imprimir / PDF** abre en el navegador el extracto mostrado, maquetado: encabezado con empresa, tipo de
extracto y período, un bloque por cada agente con sus filas y el total. Desde ahí se imprime o se guarda en PDF
(Imprimir → "Guardar como PDF"). Si en Configuración está indicada la **retención orientativa** (p. ej. 8,5 "Enasarco
quota agente"), el extracto "liquidadas y ajustes" muestra para cada agente también la fila de la retención y el
**neto orientativo**: son informaciones de referencia para el agente, sin mínimos ni máximos.

### Enviar a los agentes (opción)

Con el envío por correo activo (pestaña Correo de la Configuración), el botón **Enviar a los agentes** manda a cada
agente del extracto mostrado un mensaje con **solo su extracto** adjunto en HTML (se abre e imprime con cualquier
navegador). La dirección es la del empleado del departamento de ventas o, si falta, la del proveedor vinculado. Al
final un resumen indica para cada agente si el envío se realizó, si falta la dirección o qué error dio el servidor.
El botón está activo solo para quien tiene la autorización total sobre el extracto de todos los agentes.

### Cada jefe ve a sus agentes

Un usuario SAP vinculado a un empleado (columna *Usuario SAP* en Agentes) que no tiene la autorización «Estratto di
tutti gli agenti» (Extracto de todos los agentes) encuentra en la lista desplegable solo *(mis agentes)* y los nombres
suyo y de sus subordinados (los empleados de los que es jefe de zona, jefe de área o director): un jefe de zona puede
consultar el extracto de sus agentes sin ver a los demás. Quien no está vinculado a ningún empleado, sin la
autorización, no ve nada.

## 15. Tramos y premios

![Scaglioni e premi](../../_img/commissionmanagement/scaglioni.png)

*Tramos y premios: arriba los tramos, abajo los premios calculados para el año*

Con la opción "tramos de facturación anual con premio" (pestaña Agentes de la Configuración) el menú **Tramos y
premios** gestiona los premios de fin de año ligados a la facturación. Un **tramo** tiene: agente (o *todos*), año (o
*cada año*), umbral de base imponible anual, tipo de premio (*% de la facturación anual* o *importe fijo*),
premio, descripción, activo. Se añaden, modifican y eliminan filas en la cuadrícula de arriba y se pulsa **Guardar
tramos**.

| Agente  | Año          | Facturación anual desde | Tipo de premio                  | Premio | Descripción       |
|---------|--------------|-------------------------|---------------------------------|--------|-------------------|
| (todos) | (cada año)   | 1.000                   | % de la facturación anual       | 0,5    | Premio base       |
| (todos) | (cada año)   | 10.000                  | % de la facturación anual       | 1      | Premio 10.000     |
| Rossi   | 2026         | 12.000                  | importe fijo                    | 500,00 | Premio Rossi 2026 |

**Calcular premios** para un año: la facturación de cada agente es la suma de las bases imponibles de sus comisiones
calculadas (facturas y notas de crédito con fecha en el año; no las facturas de anticipo, ya incluidas en las facturas
finales). El tramo alcanzado es el de **umbral más alto** no superior a la facturación; los tramos del agente
prevalecen sobre los tramos para todos y el año específico sobre "cada año". Premio = facturación × % o importe fijo.
Ejemplo con los tramos de arriba: Rossi 13.150 → tramo 12.000 del agente → **500,00**; Bianchi 2.900 →
tramo 1.000 → 0,5% = **14,50**; Verdi 1.488 → **7,44**. La columna *Ya registrado* muestra el premio
del mismo año ya registrado.

**Registrar premios marcados**: las filas marcadas se convierten en ajustes de tipo *Premio por tramo* en el mes
elegido (normalmente diciembre): desde ahí entran en el extracto "liquidadas y ajustes", en los borradores de facturas
y en los totales del mes como los demás ajustes. Al registrar otra vez el mismo año, el premio registrado se sustituye
(no se duplica); un premio a cero lo quita. Con el período cerrado activo los meses cerrados no se registran.

## 16. Verificaciones y avisos al iniciar

![Verifiche](../../_img/commissionmanagement/verifiche.png)

*Verificaciones: anomalías del período, errores en rojo*

El menú **Verificaciones** busca en un período todo lo que puede hacer que una comisión falte o sea incorrecta. Se
indica el período, si se buscan también los cobros no liquidados (es la búsqueda más lenta) y se pulsa **Verificar**:
cada anomalía tiene una gravedad (**Error** en rojo, **Aviso**), la verificación que la encontró, el agente, el
documento y la explicación con lo que hay que hacer. Doble clic abre el documento.

| Verificación            | Qué señala                                                                                                                         | Qué hacer                                       |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Por calcular            | facturas, anticipos y notas de crédito del período con agente gestionado y sin comisiones                                          | Cálculo de comisiones                           |
| Sin agente              | documentos sin empleado de ventas o con un empleado sin rol                                                                        | verificar si es lo deseado; dar el rol en Agentes |
| Líneas sin %            | documentos con agente gestionado cuyas líneas tienen todos los porcentajes a cero                                                  | Control y asignación % o reglas que faltan      |
| Agente cambiado         | documentos calculados cuyo empleado en SAP es distinto del de la comisión                                                          | Recalcular en Comisiones calculadas             |
| Cancelado               | documentos cancelados con comisiones calculadas                                                                                    | Eliminar comisión                               |
| Jerarquía de agentes    | superior sin rol (su parte no se devenga), porcentaje predeterminado de un rol sin el superior, usuario SAP inexistente            | corregir en Agentes                             |
| Reglas superpuestas     | dos reglas activas iguales (mismos campos, descuento y empleado) con períodos que se superponen: vale solo una de las dos           | corregir las reglas                             |
| Cobros no liquidados    | partes cuyo plazo se cobró hace más de los días indicados en Configuración y todavía no liquidadas                                 | Liquidación                                     |

Con la opción **avisos al iniciar**, cada vez que el add-on arranca ejecuta las verificaciones rápidas (documentos de
los últimos 90 días por calcular, agente cambiado y cancelados en el último año) y, si encuentra algo, lo indica en la
barra de estado unos segundos después del inicio, es decir, después de los posibles mensajes de la licencia:
*"Comisiones: 3 anomalías por revisar (Comisiones \> Verificaciones)"*. Sin anomalías no escribe nada.

## 17. Autorizaciones y trazabilidad

El add-on crea en las **Autorizaciones generales** de SAP (Gestión › Inicialización del sistema ›
Autorizaciones) la entrada **Provvigioni** (Comisiones) bajo *Autorización de usuario*, con cinco subentradas. Los
superusuarios siempre tienen todo; a los demás usuarios se les asigna para cada entrada *Sin autorización*, *Solo
lectura* o *Autorización total*:

![Autorizzazioni generali](../../_img/commissionmanagement/autorizzazioni.png)

*Autorizaciones generales: la entrada Provvigioni con las cinco subentradas, para un usuario sin autorizaciones*

| Autorización                                                                         | Solo lectura                                                                     | Total                                                                        |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Configurazione (Configuración)                                                       | –                                                                                | abrir y guardar la Configuración                                             |
| Agenti, regole e scaglioni (Agentes, reglas y tramos)                                | consultar                                                                        | guardar agentes, reglas y tramos                                             |
| Controllo, calcolo e verifiche (Control, cálculo y verificaciones)                   | consultar Control, Cálculo, Comisiones calculadas, Verificaciones                | aplicar los %, calcular, recalcular, guardar partes, eliminar                |
| Liquidazione, conguagli e bozze fatture (Liquidación, ajustes y borradores de facturas) | consultar Liquidación y Ajustes                                                | confirmar liquidaciones, guardar ajustes, registrar premios, generar borradores |
| Estratto di tutti gli agenti (Extracto de todos los agentes)                         | ver el extracto de todos los agentes (sin ella: solo los propios, capítulo 14)   | también el envío por correo                                                  |

Sin autorización la entrada de menú responde en la barra de estado *"Función no permitida: se necesita la
autorización «…» (Autorizaciones generales \> Provvigioni)"*; con solo lectura la ventana se abre pero los
botones que modifican responden *"Operación no permitida: se necesita la autorización completa en «…»"*.

**Trazabilidad**: cabeceras y partes de las comisiones registran origen, usuario y fecha de la última escritura
(capítulo 11); los ajustes, el usuario y la fecha de modificación; los borradores de facturas, quién los generó y
cuándo. El log del add-on (capítulo 19) registra errores y actualizaciones de la estructura.

## 18. Preguntas frecuentes y problemas

Los porcentajes no se escriben en el documento  
Controlar: la opción en Configuración; que el documento tenga un empleado de ventas con un rol; que el
cliente esté rellenado. Después de un cambio de cliente, volver a elegir el agente.

He corregido un porcentaje en la factura pero SAP no me deja guardarlo  
Las facturas registradas no se modifican. Usar Control y asignación % (antes del cálculo) o Comisiones
calculadas → Recalcular con % modificados (después).

"Comisiones ya liquidadas o consolidadas"  
Para recalcular o eliminar, en Comisiones calculadas poner a cero el liquidado de las partes (Guardar partes) y quitar
la consolidación. Si las partes se han pagado realmente al agente, mejor no tocarlas: registrar la diferencia como
ajuste.

"Anticipo ya deducido de una factura con comisiones calculadas"  
Corregir o eliminar primero la comisión de la factura final, luego el anticipo, y después recalcular la factura.

Una parte no se propone en la liquidación  
El plazo no está cerrado en SAP (pago parcial o todavía no registrado), el vencimiento es posterior a la fecha límite,
o la parte ya está liquidada/consolidada. Las partes de los documentos cancelados no se proponen: eliminar la comisión.

En el primer inicio SAP pide cerrar todas las ventanas  
Es normal cuando se crean campos de usuario: responder Sí hasta el final de la creación (algunos minutos). Vale
también cuando una actualización del add-on añade campos; si el cliente se cierra a mitad, la creación continúa al
reiniciar el add-on.

"Período cerrado hasta el..."  
La operación afecta a una fecha dentro del período cerrado (Configuración, pestaña Liquidación). Si la corrección es
realmente necesaria: retrasar la fecha del bloqueo, corregir y volver a ponerla.

"Función no permitida"  
El usuario SAP no tiene la autorización (capítulo 17): asignarla en las Autorizaciones generales, entrada Provvigioni.

La factura se ha registrado pero la barra de estado dice "Comisiones no calculadas"  
El cálculo automático no era posible (anticipo ya deducido, período cerrado, agente no gestionado): el documento
está registrado con normalidad; calcularlo desde Cálculo de comisiones (las Verificaciones lo muestran entre los
"Por calcular").

El envío por correo da error  
Usar "Probar envío" en la pestaña Correo de la Configuración: el mensaje del servidor indica si son incorrectos
servidor, puerto, SSL o credenciales. Los agentes "sin correo" se completan en los datos maestros del empleado del
departamento de ventas o del proveedor vinculado.

Una línea del documento no toma los porcentajes de las reglas  
Con la opción "proteger los porcentajes modificados a mano" la línea está marcada como manual (columna Provv. %
manuali): quitar la marca y cambiar artículo, precio o descuento, o bien corregir a mano.

Mientras el add-on procesa, SAP no responde  
Durante Verificar, Calcular, Procesar y Aplicar, SAP espera al add-on (barra de estado "Espere, por favor..."): no
cerrar la ventana ni terminar el add-on; de lo contrario el cliente queda en espera y hay que reiniciarlo.

## 19. Datos y notas técnicas

| Dónde                                                          | Qué                                                                                                                                                                                                      |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OSLP (empleados del departamento de ventas)                    | campos `U_XEI_PRV_Ruolo`, `_CapoZona`, `_CapoArea`, `_Direttore`, `_PercAg`, `_PercCZ`, `_PercCA`, `_PercDI`, `_Fatturato`, `_Liquida`, `_Fornitore`, `_Utente` (usuario SAP)                            |
| Líneas de los documentos de marketing (RDR1, INV1, RIN1, DPI1...) | `U_XEI_PRV_Ag`, `_CZ`, `_CA`, `_DI` (porcentajes), `_ScEff` (descuento efectivo), `_Man` (línea manual)                                                                                               |
| `@XEI_PRV_REGOLE`                                              | reglas de los porcentajes                                                                                                                                                                                |
| `@XEI_PRV_DOC`, `@XEI_PRV_RIGHE`, `@XEI_PRV_RATE`              | comisiones calculadas: cabecera por documento y beneficiario, líneas, partes (código = tipo-DocEntry-empleado\[-línea/plazo\], p. ej. `13-386-61-2`); cabeceras y partes con origen, usuario y fecha de modificación |
| `@XEI_PRV_PERC`                                                | porcentajes corregidos por el Control para las líneas de documentos registrados                                                                                                                          |
| `@XEI_PRV_CONG`                                                | ajustes (tipo M manual / P premio, año de referencia del premio)                                                                                                                                         |
| `@XEI_PRV_SCAG`, `@XEI_PRV_BOZZE`                              | tramos; borradores de facturas generados (agente, mes, borrador, proveedor, importe)                                                                                                                     |
| `@XEI_SETTINGS` (ámbito XEI.CommissionManagement)              | opciones de la Configuración (contraseña SMTP cifrada) y versión de la estructura de datos                                                                                                               |
| Autorizaciones (OUPT)                                          | `XEI_PRV` y subentradas `XEI_PRV_P_CFG`, `_ANAG`, `_CALC`, `_LIQ`, `_EST`                                                                                                                                |

- Tipos de documento: 13 factura, 203 factura de anticipo, 14 nota de crédito, 17 pedido (solo en el control).
- Todo pasa por la DI API de SAP (ninguna conexión directa a la base de datos).
- Rendimiento: en los documentos las líneas se leen en bloque (una sola llamada) y se escriben solo las celdas que
  cambian; clientes, artículos y listas de precios se leen una vez por ventana. En la liquidación las fechas de cobro
  (la búsqueda más pesada) se calculan solo para las partes efectivamente liquidables.
- Log: `%LOCALAPPDATA%\XEI\logs\XEI.CommissionManagement.log`.
