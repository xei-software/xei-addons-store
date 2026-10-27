---
title: XEI.ItemGenerator – Instalación, licencia, menús y autorizaciones
description: Cómo instalar XEI.ItemGenerator, activar la licencia, encontrar los menús y asignar las autorizaciones.
lang: es
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator – Instalación, licencia, menús y autorizaciones

## Requisitos

| | |
|---|---|
| SAP Business One | 10.0 o superior |
| Base de datos | Microsoft SQL Server o SAP HANA (en SAP HANA se recomienda una prueba durante la instalación) |
| Sistema | Microsoft .NET Framework 4.8 en el PC del cliente SAP |
| Idiomas del programa | italiano, inglés, alemán, francés, español |

## Instalación

1. Descargue el paquete `XEI.ItemGenerator.zip`.
2. En SAP Business One abra el **Extension Manager**, importe el paquete y asígnelo a la
   empresa.
3. En el primer inicio el add-on crea por sí solo tablas, campos, objetos y las entradas de las autorizaciones.
4. Al terminar, **reinicie el cliente SAP una vez**: las ventanas de las bases y de las variantes
   leen los campos del add-on al iniciar SAP.

Cada actualización del add-on se instala del mismo modo, con el mismo reinicio.

## Licencia

El add-on funciona con un **código de licencia** emitido por XEI.

- **Prueba**: tras solicitar la prueba se recibe por email un **código de prueba**, válido durante
  30 días desde el envío en cualquier empresa.
- **Compra**: se envían a XEI los dos códigos de la ventana **Licenza** (Licencia) y se recibe el código de
  licencia.

La ventana **Licenza** (Licencia):

- Sin un código válido el add-on está **bloqueado**: en su menú solo quedan *Informazioni* (Información) y
  *Licenza* (Licencia), y al iniciar se abre automáticamente la ventana **Licenza** con el estado y el motivo.
- La ventana muestra el **código de la empresa** y el **código del servidor**: para comprar la
  licencia, con *Copia* (Copiar) se envían a [license@xeisrl.com](mailto:license@xeisrl.com).
- Un usuario SAP **superusuario** pega el código recibido en *Inserisci un codice di licenza* (Introducir un
  código de licencia) y pulsa *Salva codice* (Guardar código): el add-on se desbloquea al instante, sin reiniciar SAP.
- El código de prueba es válido en cualquier empresa. El código de licencia es válido para la empresa
  (base de datos) o el servidor de los códigos enviados.
- La misma ventana se abre en cualquier momento desde el menú *Licenza*: estado, vencimiento, número y ámbito
  de la licencia.

![La ventana Licenza con el add-on bloqueado](../../_img/itemgenerator/27_licenza.png)

*La ventana Licenza (Licencia) con el add-on bloqueado: motivo, códigos de la empresa y del servidor, campo para el
código.*

## Menús

Las entradas están en **Módulos › Gestión › Add-ons › XEI-Addon › Configurador de códigos** y, iguales,
en **Inventario › Gestión de artículos › Configurador de códigos**.

| Entrada | Función |
|---|---|
| 0. Configuración | opciones del add-on (manual de uso, capítulo 3) |
| 1. Definición de bases | bases y valores: el árbol del código (capítulo 5) |
| 2. Variantes y opciones | variantes con sus opciones (capítulo 4) |
| 3. Estructuras de variantes | grupos de variantes que se piden para un valor (capítulo 4) |
| 4. Generar artículos | composición y creación de los artículos (capítulo 9) |
| 5. Control de coherencia | recálculo de las composiciones de los artículos generados (capítulo 14) |
| 6. Verificar configuración | control de toda la configuración (capítulo 12) |
| 7. Importar / exportar Excel | configuración en un archivo Excel (capítulo 13) |
| Informazioni, Traduzioni, Licenza (Información, Traducciones, Licencia) | entradas comunes a los add-ons XEI, en italiano (solo bajo XEI-Addon); Licenza: estado y código de licencia |

Con el botón derecho también están **Configurar artículo...** en las líneas de ofertas de ventas y pedidos de cliente
(capítulo 10) y **Generar artículos similares...** en los datos maestros de un artículo generado (capítulo 11).

## Autorizaciones

En **Gestión › Inicialización del sistema › Autorizaciones › Autorizaciones generales** el add-on
añade la rama **Configuratore codici XEI**. Para cada entrada se puede asignar *Autorización
total*, *Solo lectura* o *Sin autorización*. Los superusuarios siempre tienen acceso completo.

![La rama del configurador en las autorizaciones generales](../../_img/itemgenerator/23_autorizzazioni.png)

*La rama del configurador en las autorizaciones generales, para un usuario sin autorizaciones.*

| Entrada | Total | Solo lectura |
|---|---|---|
| Definizione basi | modificar las bases | consultar |
| Definizione varianti | modificar las variantes | consultar |
| Strutture varianti | modificar las estructuras | consultar |
| Generazione articoli | crear artículos (también desde ofertas y pedidos) | componer la lista sin crear |
| Configurazione, verifica, import/export | guardar la configuración, importar desde Excel, control de coherencia | ver la configuración, verificar, exportar |

Sin autorización, la entrada de menú muestra en la barra de estado "Función no autorizada".

## Asistencia

Para las licencias: [license@xeisrl.com](mailto:license@xeisrl.com). Para la asistencia:
[info@xeisrl.com](mailto:info@xeisrl.com). En la solicitud indique la versión del add-on (menú
*Informazioni*) y una descripción del problema.
