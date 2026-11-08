---
title: XEI.ContoLavoro – Instalación, licencia y menús
description: Cómo instalar XEI.ContoLavoro, activar la licencia y encontrar los menús.
lang: es
prodotto: XEI.ContoLavoro
versione: 1.2.1
stato: approvato
---

# XEI.ContoLavoro – Instalación, licencia y menús

## Requisitos

| | |
|---|---|
| SAP Business One | 10.0 o superior |
| Base de datos | Microsoft SQL Server o SAP HANA (en SAP HANA se recomienda una prueba durante la instalación) |
| Sistema | Microsoft .NET Framework 4.8 en el PC del cliente SAP |
| Idiomas del programa | italiano, inglés, alemán, francés, español, turco |

## Instalación

1. Descargue el paquete `XEI.ContoLavoro.zip`.
2. En SAP Business One abra el **Extension Manager**, importe el paquete y asígnelo a la empresa.
3. En el primer inicio el add-on crea tablas, campos, el objeto de la orden de subcontratación y la búsqueda formateada
   del proveedor subcontratista en el almacén. SAP muestra el mensaje *"La estructura de la base de datos se ha
   modificado..."*: responda **Sí** y espere a que termine antes de usar el cliente.

Cada actualización del add-on se instala de la misma manera.

Antes de crear las órdenes se define la serie de numeración de la orden de subcontratación, como para los documentos de SAP: *Módulos › Gestión › Inicialización del sistema › Numeración de documentos*, elemento **Commessa terzista** (Orden de subcontratación) al final de la lista. Sin serie, al abrir *Orden de subcontratación* el add-on avisa de que hay que definirla.

Después de la instalación: rellene la **Configuración** y luego, en SAP, vincule cada almacén del subcontratista a su
proveedor (campo *Fornitore terzista* (Proveedor subcontratista) de los datos maestros del almacén) y marque los
artículos en subcontratación (manual de uso, capítulos 3 y 6).

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

Las entradas están en **XEI-Addon › Subcontratación**. El submenú **Subcontratación** aparece también en el módulo de
SAP elegido en la Configuración (*Compras* o *Producción*).

| Entrada | Función |
|---|---|
| Orden de subcontratación | apertura, búsqueda y creación de las órdenes de subcontratación (manual de uso, capítulos 4 y 5) |
| Crear órdenes desde órdenes de fabricación | órdenes de subcontratación a partir de las elaboraciones externas de las órdenes de fabricación (capítulo 6) |
| Recepción del subcontratista | entrada de los productos de un albarán del subcontratista en varias órdenes de subcontratación (entrada de los productos y salida de los componentes) |
| Transferencia masiva de componentes | envío de los componentes para varias órdenes de subcontratación; se desactiva en la Configuración (capítulo 9) |
| Transferencia de componentes entre órdenes | mueve el stock que ya está en el subcontratista de una orden de subcontratación a otra (capítulo 9) |
| Cierre masivo de entradas de productos | cierra las entradas de mercancías de los productos que siguen abiertas (capítulo 9) |
| Precios de elaboración de subcontratistas | precios de las elaboraciones por subcontratista y producto (capítulo 9) |
| Configuración | opciones del add-on (capítulo 3) |
| Informazioni (Información), Traduzioni (Traducciones), Licenza (Licencia) | entradas comunes de los add-ons XEI; Licenza: estado y código de licencia |
