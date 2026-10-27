---
title: XEI.CommissionManagement – Instalación, licencia, menús y autorizaciones
description: Cómo instalar XEI.CommissionManagement, activar la licencia, encontrar los menús y asignar las autorizaciones.
lang: es
prodotto: XEI.CommissionManagement
versione: 1.1.0
stato: approvato
---

# XEI.CommissionManagement – Instalación, licencia, menús y autorizaciones

## Requisitos

| | |
|---|---|
| SAP Business One | 10.0 o superior |
| Base de datos | Microsoft SQL Server o SAP HANA (en SAP HANA se recomienda una prueba durante la instalación) |
| Sistema | Microsoft .NET Framework 4.8 en el PC del cliente SAP |
| Idiomas del programa | italiano, inglés, alemán, francés, español, turco |
| Correo | servidor de correo SMTP accesible, solo para enviar los extractos a los agentes por correo electrónico (Configuración › Correo) |

## Instalación

1. Descargue el paquete `XEI.CommissionManagement.zip`.
2. En SAP Business One abra el **Extension Manager**, importe el paquete y asígnelo a la empresa.
3. En el primer inicio el add-on crea campos, tablas, índices y autorizaciones. La creación de los campos en las
   líneas de los documentos requiere **algunos minutos**: SAP muestra varias veces el mensaje *"La estructura de la
   base de datos se ha modificado... se cerrarán todas las ventanas abiertas. ¿Continuar?"*: responda **Sí**.

Cada actualización del add-on se instala de la misma manera.

Después de la instalación: rellene la **Configuración**, luego los **Agentes** (roles, superiores, porcentajes) y
luego las **Reglas**. Solo a partir de ese momento los documentos reciben los porcentajes. A los usuarios que no son
superusuarios se les deben asignar las **autorizaciones** (más abajo).

## Licencia

El add-on funciona con un **código de licencia** emitido por XEI.

- **Prueba**: tras solicitar la prueba se recibe por email un **código de prueba**, válido durante 30 días desde el
  envío en cualquier empresa.
- **Compra**: se envían a XEI los dos códigos de la ventana **Licenza** (Licencia) y se recibe el código de licencia.

La ventana **Licenza** (Licencia):

- Sin un código válido el add-on está **bloqueado**: en su menú solo quedan *Informazioni* (Información) y *Licenza*
  (Licencia), y al iniciar se abre automáticamente la ventana **Licenza** con el estado y el motivo.
- La ventana muestra el **código de la empresa** y el **código del servidor**: para comprar la licencia, con *Copia*
  (Copiar) se envían a [license@xeisrl.com](mailto:license@xeisrl.com).
- Un usuario SAP **superusuario** pega el código recibido en *Inserisci un codice di licenza* (Introducir un código de
  licencia) y pulsa *Salva codice* (Guardar código): el add-on se desbloquea al instante, sin reiniciar SAP.
- El código de prueba es válido en cualquier empresa. El código de licencia es válido para la empresa (base de datos)
  o el servidor de los códigos enviados.
- La misma ventana se abre en cualquier momento desde el menú *Licenza*: estado, vencimiento, número y ámbito de la
  licencia.

## Menús

Las entradas están en **XEI-Addon › Comisiones**.

| Entrada | Función |
|---|---|
| Configuración | opciones (seis pestañas) y orden de búsqueda de las reglas (manual de uso, capítulo 5) |
| Agentes | rol, superiores, % predeterminados, % a la facturación, liquidación, proveedor, usuario SAP (capítulo 6) |
| Reglas de porcentaje | % por cliente, grupo de clientes, artículo, grupo de artículos, lista de precios (capítulo 7) |
| Tramos y premios | premios sobre la facturación anual, si están activos en Configuración (capítulo 15) |
| Control y asignación % | comparación de los documentos con las reglas y corrección en bloque (capítulo 9) |
| Cálculo de comisiones | cálculo sobre facturas, facturas de anticipo y notas de crédito (capítulo 10) |
| Comisiones calculadas | consulta, corrección, recálculo, eliminación (capítulo 11) |
| Liquidación | partes cobradas por liquidar, impagados por revertir (capítulo 12) |
| Ajustes | importes manuales por agente y mes, borradores de facturas de los agentes (capítulo 13) |
| Extracto de comisiones | calculadas, por liquidar, liquidadas y ajustes; CSV, impresión/PDF, correo (capítulo 14) |
| Verificaciones | anomalías por revisar (capítulo 16) |
| Informazioni (Información), Traduzioni (Traducciones), Licenza (Licencia) | entradas comunes de los add-ons XEI; Licenza: estado y código de licencia |

## Autorizaciones

En las **Autorizaciones generales** de SAP (Gestión › Inicialización del sistema › Autorizaciones) el add-on crea la
entrada **Provvigioni** (Comisiones) bajo *Autorización de usuario*, con cinco subentradas. Los superusuarios siempre
tienen todo; a los demás usuarios se les asigna para cada entrada *Sin autorización*, *Solo lectura* o *Autorización
total*.

![Autorizaciones generales](../../_img/commissionmanagement/autorizzazioni.png)

*Autorizaciones generales: la entrada Provvigioni con las cinco subentradas, para un usuario sin autorizaciones.*

| Autorización | Solo lectura | Total |
|---|---|---|
| Configurazione (Configuración) | – | abrir y guardar la Configuración |
| Agenti, regole e scaglioni (Agentes, reglas y tramos) | consultar | guardar agentes, reglas y tramos |
| Controllo, calcolo e verifiche (Control, cálculo y verificaciones) | consultar Control, Cálculo, Comisiones calculadas, Verificaciones | aplicar los %, calcular, recalcular, guardar partes, eliminar |
| Liquidazione, conguagli e bozze fatture (Liquidación, ajustes y borradores de facturas) | consultar Liquidación y Ajustes | confirmar liquidaciones, guardar ajustes, registrar premios, generar borradores |
| Estratto di tutti gli agenti (Extracto de todos los agentes) | ver el extracto de todos los agentes (sin ella: solo los propios) | también el envío por correo |

Sin autorización la entrada de menú responde en la barra de estado *"Función no permitida: se necesita la
autorización «…» (Autorizaciones generales > Provvigioni)"*; con solo lectura la ventana se abre, pero los botones
que modifican responden *"Operación no permitida: se necesita la autorización completa en «…»"*.

## Asistencia

Para las licencias: [license@xeisrl.com](mailto:license@xeisrl.com). Para la asistencia:
[info@xeisrl.com](mailto:info@xeisrl.com). En la solicitud indique la versión del add-on (menú *Informazioni*) y una
descripción del problema.
