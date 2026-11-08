---
title: XEI.ContoLavoro – Manual de uso
description: Cómo gestionar con XEI.ContoLavoro las órdenes de subcontratación, los envíos de componentes, las recepciones de productos y la subcontratación desde órdenes de fabricación.
lang: es
prodotto: XEI.ContoLavoro
versione: 1.2.1
stato: approvato
---

# XEI.ContoLavoro – Manual de uso

La instalación, la licencia y los menús también se describen en la
[guía de instalación](installazione.md).

## 1. Qué hace el add-on

XEI.ContoLavoro gestiona las elaboraciones encargadas a **subcontratistas** (proveedores externos) que reciben
componentes de la empresa, los elaboran y devuelven un producto terminado o semielaborado. Para cada elaboración se
abre una **orden de subcontratación** que reúne:

- los **productos** que se deben obtener, con su lista de materiales (componentes que se envían y elaboraciones que se
  pagan);
- el **pedido de compra** al subcontratista, alineado automáticamente con la orden de subcontratación;
- los **envíos de componentes** al almacén del subcontratista, las **devoluciones** y los **desechos**;
- la **recepción** de los productos: entrada de mercancías de productos y elaboraciones, salida de los componentes
  consumidos, recibo de producción para los productos que proceden de una orden de fabricación (capítulo 6);
- la situación en tiempo real: cuánto se ha enviado y usado, qué queda en el subcontratista y qué falta.

La orden de subcontratación se cierra sola cuando todos los productos se han recibido y en el subcontratista no quedan
componentes.

### Lo más destacado

- Cabecera como una transferencia de stock, con propagación de los almacenes a las líneas y almacén del subcontratista
  protegido después de los movimientos.
- Lotes y números de serie elegidos en el add-on: propuesta a partir de los lotes de la orden en el subcontratista
  (trazabilidad) y FEFO, modificable a mano; lote del producto entrante mediante un script SQL configurable;
  recepción de productos en una única transacción.
- Carpeta Documentos con todos los documentos vinculados, agrupados y fáciles de abrir.
- Costes de los productos recalculados en cada grabación; pedido de compra alineado automáticamente.
- Órdenes de subcontratación desde órdenes de fabricación, transferencia masiva y entre órdenes, cierre masivo de las
  entradas de mercancías.
- Mismo funcionamiento en SQL Server y SAP HANA; textos traducibles.

## 2. Instalación y menús

### Instalación

- El paquete `XEI.ContoLavoro.zip` se importa en el Extension Manager de SAP Business One.
- En el primer arranque el add-on crea tablas, campos, el objeto (UDO) `XEI_CL_COMMESSA` y la búsqueda formateada del
  proveedor subcontratista en el almacén. SAP pide confirmar que *"la estructura de la base de datos se ha
  modificado"*: responder y esperar a que termine antes de usar el cliente.
- Antes de crear las órdenes se define la **serie de numeración** de la orden de subcontratación, como para los documentos de SAP: **Módulos › Gestión › Inicialización del sistema › Numeración de documentos**, elemento *Commessa terzista* (Orden de subcontratación) al final de la lista. Sin serie, al abrir *Orden de subcontratación* el add-on avisa de que hay que definirla.

### Menús

**Módulos › Gestión › Add-ons › XEI-Addon › Subcontratación**:

| Entrada | Función |
|---|---|
| Orden de subcontratación | apertura, búsqueda y creación de las órdenes de subcontratación |
| Crear órdenes desde órdenes de fabricación | órdenes a partir de las elaboraciones externas de las órdenes de fabricación (capítulo 6) |
| Recepción del subcontratista | un albarán del subcontratista con productos de varias órdenes: se elige el proveedor, se indican las cantidades recibidas en los productos abiertos de sus órdenes (*Proponer* = pendiente) y *Registrar* realiza la recepción orden por orden, con entrada de los productos y salida de los componentes |
| Transferencia masiva de componentes | envío de componentes para varias órdenes (se desactiva en la Configuración, capítulo 3) |
| Transferencia de componentes entre órdenes | traslada el stock que ya está en el subcontratista de una orden a otra |
| Cierre masivo de entradas de productos | cierra las entradas de mercancías de los productos que siguen abiertas |
| Precios de elaboración de subcontratistas | precios de las elaboraciones por proveedor y producto |
| Configuración | opciones del add-on |
| Informazioni (Información), Traduzioni (Traducciones), Licenza (Licencia) | entradas comunes a los add-ons XEI; Licenza: estado y código de licencia |

Las mismas entradas, salvo *Configuración*, *Informazioni*, *Traduzioni* y *Licenza*, están también en el módulo SAP
elegido en la configuración (capítulo 3), en la posición elegida: **Módulos › Compras ›
Subcontratación** (predeterminado) o **Módulos › Producción › Subcontratación**.

### Licencia

El add-on funciona con un **código de licencia** emitido por XEI. Después de solicitar la prueba se recibe por email
un **código de prueba**, válido 30 días desde el envío en cualquier empresa; para la compra se envían a XEI los dos
códigos de la ventana **Licenza** (Licencia) y se recibe el código de licencia.

- Sin un código válido el add-on está **bloqueado**: en su menú solo quedan *Informazioni* (Información) y *Licenza*
  (Licencia), y al arrancar se abre sola la ventana **Licenza** con el estado y el motivo.
- La ventana muestra el **código de la empresa** y el **código del servidor**: para comprar la licencia, con *Copia*
  (Copiar) se envían a [license@xeisrl.com](mailto:license@xeisrl.com).
- Un usuario SAP **superusuario** pega el código recibido en *Inserisci un codice di licenza* (Introduzca un código de
  licencia) y pulsa *Salva codice* (Guardar código): el add-on se desbloquea en seguida, sin reiniciar SAP.
- El código de licencia vale para la empresa (base de datos) o para el servidor de los códigos enviados.
- La misma ventana se abre en cualquier momento desde el menú *Licenza*: estado, vencimiento, número y ámbito de la
  licencia.

## 3. Configuración

Las opciones se definen en un formulario con carpetas (la carpeta *Lotes* se describe en el capítulo 7). Las opciones
valen para toda la empresa; los formularios ya abiertos las usan al volver a abrirse.

![General](../../_img/contolavoro/10_config_generale.png)

*General*

![Precios](../../_img/contolavoro/11_config_prezzi.png)

*Precios*

![Inventario](../../_img/contolavoro/12_config_magazzino.png)

*Inventario*

![Series y motivos](../../_img/contolavoro/13_config_documenti.png)

*Series y motivos*

| Opción | Efecto | Predet. |
|---|---|---|
| **General** | | |
| Pedido de compra de origen | campo para vincular la orden al pedido de compra del que nace | No |
| Pedido de cliente de origen | columna pedido de cliente en las líneas de producto | No |
| Productos sin lista de materiales | permite productos sin lista de materiales: se compone a mano | No |
| Cerrar la entrada de mercancías del producto | tras la recepción, la entrada del producto se cierra (no se factura) | No |
| Recalcular el precio de la entrada del producto | si cambia el precio de la elaboración, actualiza la entrada del producto | No |
| Ofertas de proveedor desde OF | al crear desde OF vincula las ofertas de proveedor | No |
| Transferencia masiva | permite la transferencia masiva de los componentes; con No la entrada de menú avisa de que la función está desactivada | Sí |
| Lista subcontratista | muestra la columna "Lista subcontratista" en la lista de materiales | Sí |
| Contratos de proveedor | precios de elaboración desde los contratos (solo SQL Server) | No |
| Lista de precios predefinida de las órdenes | lista de costes propuesta en las nuevas órdenes; sirve para crear las órdenes desde órdenes de fabricación (capítulo 6) | – |
| Menú también en el módulo SAP | módulo con el submenú *Subcontratación*: Compras o Producción | Compras |
| Posición en el menú del módulo | al final, al principio o después de una entrada del módulo | al final |
| **Precios** | | |
| Precio de elaboración / componentes modificable | precios modificables en la lista de materiales de la orden | No |
| Precio de elaboración / componente de la lista de materiales | como primera opción el precio de la lista de materiales (componente: solo OF) | No |
| Repartir el coste de elaboración | reparte el coste total entre los productos (solo desde OF) | No |
| No bloquear con precios a cero | la recepción se permite también con precios a cero | No |
| Revalorizar componentes | revalorización de los componentes en la salida de producción (inventario permanente) | No |
| **Inventario** | | |
| Almacén predeterminado del artículo | las líneas de componente parten del almacén predeterminado del artículo | Sí |
| Stock como enviado | para los componentes indicados, el stock en el subcontratista cuenta como enviado | No |
| Componentes por línea | componentes separados por producto | No |
| Necesidad variable | reparte lo enviado entre los productos | No |
| Solicitudes de transferencia | envío de componentes con una solicitud de traslado en lugar de la transferencia de stock | No |
| Lista de picking | crea también la lista de picking (activa las solicitudes) | No |
| **Series y motivos** | | |
| Series | pedido de compra, entradas de mercancías de productos y elaboraciones, transferencias | predeterminada de SAP |
| Motivos de transporte | para transferencias, pedido, entrada de mercancías, salidas, entradas (si la empresa usa los motivos de transporte) | – |
| **Lotes** | | |
| Script del lote entrante | SQL con {ItemCode}, {WhsCode}, {DocEntry} que devuelve el lote del producto recibido (véase el capítulo 7) | orden-número correlativo |

## 4. La orden de subcontratación

### Cabecera

La cabecera está organizada como la de la transferencia de stock: a la izquierda proveedor, referencia del
proveedor, proyecto y pedidos vinculados; a la derecha numeración, estado, fechas, lista de costes y los dos
almacenes.

![Orden de subcontratación: cabecera y pestaña Productos](../../_img/contolavoro/01_prodotti.png)

*Orden de subcontratación: cabecera y pestaña Productos*

- **Proveedor**: al elegirlo propone el almacén del usuario y el **almacén del subcontratista** vinculado al proveedor
  (campo *Fornitore terzista* (Proveedor subcontratista) de los datos maestros del almacén) o el marcado como
  predeterminado.
- **Del almacén**: almacén de la empresa; de aquí salen los componentes, aquí vuelven los productos y en este almacén
  nacen las líneas del pedido de compra.
- **Alm. subcontr.**: solo se puede cambiar mientras la orden no tenga movimientos de componentes; después el campo se
  desactiva y la grabación rechaza el cambio de todos modos.
- Al cambiar un almacén de la cabecera se propone, como en la transferencia de stock, trasladarlo a las líneas de la
  lista de materiales **todavía sin movimientos**.

![Cambio de un almacén de la cabecera con productos ya introducidos](../../_img/contolavoro/09_propaga_magazzino.png)

*Cambio de un almacén de la cabecera con productos ya introducidos*

### Productos

Se elige el artículo (también varios artículos a la vez desde la lista) y la cantidad a producir: la lista de
materiales se copia de SAP y se refiere a una pieza (teniendo en cuenta la cantidad base de la lista). Las columnas
muestran la cantidad a producir, recibida, pendiente, el coste de los componentes y de las elaboraciones.

### Lista de materiales

![Lista de materiales por producto: componentes con almacenes, precios, necesidad, usado](../../_img/contolavoro/02_distinta.png)

*Lista de materiales por producto: componentes con almacenes, precios, necesidad, usado*

Para cada producto: componentes (artículos de inventario que se envían) y elaboraciones (servicios que se pagan al
subcontratista). Con **Modificar lista de materiales** se cambian almacenes y precios de las líneas todavía sin
movimientos; con *Añadir línea* / *Borrar línea* de SAP se añaden componentes y elaboraciones o se quitan los que no
tienen movimientos. Desde el menú contextual de la línea de producto: **Reprocesar** (el producto vuelve al
subcontratista como componente con las nuevas elaboraciones) y **Recomponer lista de materiales** (sustituye la lista
por los componentes elegidos).

### Componentes

![Situación de los componentes: necesidad, enviado, stocks y pendiente de envío](../../_img/contolavoro/03_componenti.png)

*Situación de los componentes: necesidad, enviado, stocks y pendiente de envío*

Los componentes de todos los productos agrupados por artículo y almacenes: necesidad, usado, disponible en la empresa,
stock en el almacén del subcontratista, solicitudes y listas de picking, enviado, pendiente de envío, stock de la
orden en el subcontratista, devoluciones y desechos. Los movimientos se hacen con los botones al pie de la orden:
**Enviar componentes** y **Devoluciones y desechos** (*Devolución de componentes del subcontratista*, *Transferir
desechos*, *Salida de desechos en el subcontratista*). Cada uno abre una ventana con las cantidades que se deben mover
en las celdas amarillas: *Proponer* las rellena, *Poner a cero* las vacía, y se pueden cambiar a mano.

### Documentos

![Documentos vinculados a la orden, uno por línea, con las líneas del documento elegido](../../_img/contolavoro/04_documenti.png)

*Documentos vinculados a la orden, uno por línea, con las líneas del documento elegido*

Todos los documentos SAP vinculados a la orden, uno por línea en orden cronológico, con el enlace para abrirlos;
*Mostrar* filtra por tipo de documento. Debajo, en *Líneas del documento*, las líneas del documento elegido con lotes,
números de serie y ubicaciones.

## 5. Flujo de trabajo

1. **Orden de subcontratación**: proveedor, almacenes, productos y cantidades; *Añadir*.
2. **Pedido al subcontratista**: la ventana *Pedido al subcontratista* crea el pedido de compra, con una línea por
   producto y una por cada elaboración; si el pedido ya existe, el botón lo abre. Los cambios posteriores de la orden
   (productos nuevos o eliminados, cantidades, precios, fechas) se trasladan al pedido al grabar; las líneas ya
   recibidas solo cambian de cantidad.

   ![Creación del pedido de compra](../../_img/contolavoro/05_oda.png)

   *Creación del pedido de compra*

3. **Enviar componentes**: en la ventana *Transferencia de componentes* la columna *A enviar* propone el pendiente de
   envío (se cambia a mano); *OK* crea la transferencia de stock al almacén del subcontratista. Con la opción
   correspondiente se crea una solicitud de traslado con lista de picking.

   ![Transferencia de componentes](../../_img/contolavoro/06_trasferimento.png)

   *Transferencia de componentes*

4. **Recibir productos**: en la ventana *Recepción de productos* la columna *A recibir* propone el pendiente (se
   cambia a mano) y *Tipo de movimiento* elige entre *Entrada de productos y salida de componentes*, *Solo entrada de
   productos* y *Solo salida de componentes*; después *OK*. Se crean: la entrada de mercancías de las elaboraciones y
   de los productos desde el pedido de compra, la salida de mercancías de los componentes del almacén del
   subcontratista y los recibos de producción para los productos que proceden de OF (capítulo 6).

   ![Recepción de productos](../../_img/contolavoro/07_versamento.png)

   *Recepción de productos*

> El producto entra al coste completo (componentes + elaboración); con la opción "Cerrar la entrada de mercancías del
> producto" la entrada se cierra y no se factura: se facturan las elaboraciones.

Si un componente que se debe dar de salida supera el stock de la orden en el subcontratista, se pregunta si dar
salida al stock restante (Sí / No / Sí a todo).

## 6. Subcontratación desde órdenes de fabricación

Cuando algunas fases de una **orden de fabricación (OF)** se realizan en subcontratistas, el add-on crea las órdenes
de subcontratación a partir de las líneas de la OF. En cada recepción emite para la OF los componentes consumidos por
el subcontratista y, cuando han vuelto todas las elaboraciones externas, registra el recibo de producción del
producto terminado.

### Configuración en SAP

> La elaboración externa es un **artículo no inventariable** con el campo **Conto lavoro** (Subcontratación) = Sí, no
> un recurso de SAP: una elaboración definida como recurso no aparece en la lista de las OF.

| Dónde | Qué configura | En el ejemplo |
|---|---|---|
| Datos maestros del artículo de la elaboración | artículo no inventariable, campo de usuario **Conto lavoro** (Subcontratación) = Sí; el **proveedor preferido** es el subcontratista propuesto en la lista | `LAV-SALD` Soldadura del bastidor, proveedor `F-TER01`; `LAV-MONT` Montaje del eje, proveedor `F-TER02` |
| Lista de materiales del producto terminado | una línea por cada elaboración externa, con la cantidad por pieza; en las líneas de los componentes que se envían al subcontratista, el campo **Lavorazione terzista** (Elaboración subcontratista) con el código de la elaboración y el método de emisión **Manual** | `CMP-01`, `CMP-02` → `LAV-SALD`; `CMP-03`, `CMP-04` → `LAV-MONT` |
| Lista de materiales del producto terminado | **Lista subcontratista** = Sí si el producto terminado está completo cuando vuelven todas las elaboraciones externas: el add-on registra el recibo de producción. Con No, el recibo de producción lo registra usted en SAP | `PF-100` = Sí |
| Datos maestros del almacén del subcontratista | campo **Fornitore terzista** (Proveedor subcontratista) (capítulo 4) | `T-TER01` → `F-TER01`; `T-TER02` → `F-TER02` |
| *Precios de elaboración de subcontratistas* | precio por subcontratista, producto terminado y elaboración (orden de búsqueda del precio en el capítulo 9) | `F-TER01` / `PF-100` / `LAV-SALD` 12,00; `F-TER02` / `PF-100` / `LAV-MONT` 3,50 |
| Configuración, pestaña *General* (capítulo 3) | **Lista de precios predefinida de las órdenes**: la lista de costes de las órdenes creadas desde las OF. Sin ella, *Crear órdenes* pide indicarla y no crea las órdenes | Lista de precios base |

Los componentes con notificación posterior vinculados a la elaboración no se envían al subcontratista: los emite el
recibo de producción desde el almacén de la línea de la OF. La columna **Motivo / avisos** de la lista lo indica. Los
demás componentes de la lista de materiales, que no tienen elaboración, quedan como en cualquier OF.

> **Control al grabar la lista de materiales.** Cuando graba una lista de materiales que tiene el campo
> **Lavorazione terzista** (Elaboración subcontratista) relleno, el add-on controla los códigos indicados. Si algo no
> está bien aparece el aviso *"Lista de materiales PF-100, campo "Lavorazione terzista":"* con un punto para cada
> caso; la lista de materiales queda grabada.
>
> - Recurso: *"LAV-SALD es un recurso: la elaboración externa debe crearse como artículo no inventariable con "Conto
>   lavoro" = Sí, y los componentes deben vincularse a ese código."*
> - Código que no es un artículo: *"LAV-SALD no es un artículo."*
> - Artículo sin Conto lavoro: *"El artículo LAV-SALD no tiene "Conto lavoro" = Sí en los datos maestros."*
> - Elaboración que no es línea de la lista: *"LAV-SALD no es una línea de la lista de materiales: la OF no tendrá la
>   línea de la elaboración y no se podrá crear la orden de subcontratación."*
> - Componentes con notificación posterior: *"Componentes con notificación posterior con la elaboración LAV-SALD: no
>   se envían al subcontratista (necesitan el método de emisión manual)."*

### Ejemplo paso a paso

El producto terminado `PF-100` Carro tiene dos elaboraciones externas: la soldadura del bastidor en `F-TER01`
«Subcontratista Ejemplo 1» y el montaje de los ejes en `F-TER02` «Subcontratista Ejemplo 2». Cada carro tiene un
bastidor y dos ejes. La OF n.º 500 está liberada para 100 carros en el almacén `01`:

| Línea | Artículo | Cantidad | Emisión | Lavorazione terzista | Precio |
|---|---|---|---|---|---|
| 1 | `LAV-SALD` Soldadura del bastidor (elaboración) | 100 | | | 12,00 |
| 2 | `CMP-01` Tubo (m) | 250 | Manual | `LAV-SALD` | 4,00 |
| 3 | `CMP-02` Placa | 400 | Manual | `LAV-SALD` | 1,50 |
| 4 | `LAV-MONT` Montaje del eje (elaboración) | 200 | | | 3,50 |
| 5 | `CMP-03` Rueda | 400 | Manual | `LAV-MONT` | 5,00 |
| 6 | `CMP-04` Perno | 200 | Manual | `LAV-MONT` | 2,00 |
| 7 | `CMP-05` Tornillo | 1.600 | notificación posterior | | |

| Paso | Documento SAP creado | Efecto en la OF |
|---|---|---|
| 1. **Subcontratación › Crear órdenes desde órdenes de fabricación**: selecciona las dos líneas de la OF 500 y pulsa *Crear órdenes* | ningún documento SAP: orden de subcontratación 1001 (`F-TER02`, de `01` a `T-TER02`, producto `LAV-MONT` 200, lista `CMP-03` 2 y `CMP-04` 1 por pieza) y orden 1002 (`F-TER01`, de `01` a `T-TER01`, producto `LAV-SALD` 100, lista `CMP-01` 2,5 y `CMP-02` 4 por pieza), en el orden de las líneas de la lista | ninguno |
| 2. En cada orden pulse *Pedido al subcontratista* y confirme la ventana *Pedido al subcontratista* | pedido de compra a `F-TER01`: `LAV-SALD` 100 × 12,00; pedido de compra a `F-TER02`: `LAV-MONT` 200 × 3,50 | ninguno |
| 3. En cada orden pulse *Enviar componentes* y, con las cantidades propuestas, *OK* | transferencia de stock de `01` a `T-TER01`: `CMP-01` 250, `CMP-02` 400; de `01` a `T-TER02`: `CMP-03` 400, `CMP-04` 200 | ninguno |
| 4. Vuelven 60 bastidores: en la orden 1002 pulse *Recibir productos*, en la ventana *Recepción de productos* escriba 60 en *A recibir* y pulse *OK* | entrada de mercancías desde el pedido: `LAV-SALD` 60 × 12,00; emisión para producción desde `T-TER01`: `CMP-01` 150, `CMP-02` 240 | emitidos los componentes de las líneas 2 y 3; ningún recibo: faltan los ejes, y un mensaje lo indica (*"OF 500: el producto terminado entrará en el almacén cuando vuelva también la elaboración LAV-MONT."*) |
| 5. Vuelven 100 ejes: orden 1001, *Recibir productos*, 100 en *A recibir*, *OK* | entrada de mercancías `LAV-MONT` 100 × 3,50; emisión para producción desde `T-TER02`: `CMP-03` 200, `CMP-04` 100; recibo de producción `PF-100` **50** | 60 bastidores y 100 ejes bastan para 50 carros: 50 terminados; SAP emite por notificación posterior `CMP-05` 800 |
| 6. Vuelven otros 100 ejes: orden 1001, *Recibir productos*, 100 en *A recibir*, *OK* | entrada de mercancías `LAV-MONT` 100; emisión para producción `CMP-03` 200, `CMP-04` 100; recibo de producción `PF-100` **10** | 60 terminados, los demás esperan los bastidores (*"OF 500: entradas 10 piezas del producto terminado; las demás entrarán cuando vuelva también la elaboración LAV-SALD."*); la orden 1001 se cierra sola |
| 7. Vuelven los últimos 40 bastidores: orden 1002, *Recibir productos*, 40 en *A recibir*, *OK* | entrada de mercancías `LAV-SALD` 40; emisión para producción `CMP-01` 100, `CMP-02` 160; recibo de producción `PF-100` **40** | 100 terminados; la orden 1002 se cierra sola. La OF la cierra usted en SAP |

> El recibo de producción vale el coste de las elaboraciones externas por pieza: para cada elaboración, componentes y
> precio de la elaboración, por la cantidad por pieza. En el ejemplo un carro vale
> (2,5 × 4,00 + 4 × 1,50 + 12,00) + 2 × (2 × 5,00 + 1 × 2,00 + 3,50) = 28,00 + 31,00 = **59,00**.

### Casos particulares

- **Varias OF**: las líneas con el mismo proveedor y el mismo almacén de devolución (columna *Alm. devolución*) van en
  la misma orden, un producto por línea; con almacenes de devolución distintos se crean órdenes distintas.
- **Servicios del subcontratista**: un componente no inventariable con **Lavorazione terzista** (Elaboración
  subcontratista) (por ejemplo una prueba) se convierte en una elaboración de la orden, con una línea más en el pedido
  al subcontratista.
- **Lista subcontratista = No**: el add-on registra la entrada de mercancías de la elaboración y la salida de los
  componentes; el recibo de producción lo registra usted en SAP, por ejemplo después de un montaje interno.
- **Recibos de producción registrados en SAP** en la misma OF: el add-on los resta, el producto terminado no entra dos
  veces.
- **Orden interrumpida**: si interrumpe una orden, la elaboración vuelve a la lista y puede crear otra.
- **Componentes con notificación posterior**: los componentes con notificación posterior vinculados a la elaboración
  no se envían al subcontratista; la columna **Motivo / avisos** lo indica.
- **Lista de materiales de la orden**: en los productos que proceden de OF no se modifica; usted cambia el precio de
  la elaboración (columna *Coste elab.*), que se traslada al pedido al subcontratista al grabar. Con la opción
  *Repartir el coste de elaboración* el *Coste elab. total* de la cabecera se divide entre los productos en proporción
  a la cantidad.
- La opción *Cerrar la entrada de mercancías del producto* no vale para las órdenes que proceden de OF: la entrada de
  mercancías de la elaboración queda abierta, para facturar.
- **Ofertas de proveedor**: con la opción *Ofertas de proveedor desde OF*, *Oferta proveedor* vincula a la línea una
  línea de oferta, con su proveedor, precio y fecha de entrega; las líneas de oferta no elegidas se cierran.

### Por qué una OF no aparece en la lista

La lista muestra las elaboraciones listas para convertirse en orden. Active **Mostrar también las líneas no
preparadas**: aparecen también las demás, con el motivo y qué hacer en la columna **Motivo / avisos**. Las líneas no
preparadas no se pueden seleccionar; si hace clic en su casilla de selección, el motivo aparece también en la barra de
estado.

| Motivo (ejemplo en pantalla) | Qué hacer |
|---|---|
| Ya en la orden de subcontratación n.º 1001. | nada: abra la orden desde la columna *Orden* |
| LAV-SALD es un recurso: la elaboración externa debe crearse como artículo no inventariable con "Conto lavoro" = Sí, y los componentes deben vincularse a ese código. | cree el artículo de la elaboración y escriba su código en **Lavorazione terzista** (Elaboración subcontratista) en los componentes |
| Los componentes indican la elaboración LAV-SALD, que no es un artículo. | corrija **Lavorazione terzista** en los componentes o cree el artículo |
| El artículo LAV-SALD no tiene "Conto lavoro" = Sí en los datos maestros. | configure **Conto lavoro** (Subcontratación) = Sí en los datos maestros del artículo |
| La OF no tiene la línea de la elaboración LAV-SALD: añadirla a la OF (o a la lista de materiales del producto). | añada la línea a la OF, o a la lista de materiales para las próximas OF |
| Ningún componente para enviar: en las líneas de los componentes indicar "Lavorazione terzista" = LAV-SALD y el método de emisión manual. | rellene los componentes que se envían, con el método de emisión Manual |
| OF no liberada: liberarla en SAP. | libere la OF |

Una elaboración definida como recurso de SAP es una causa frecuente: la elaboración externa debe crearse como
artículo no inventariable con **Conto lavoro** (Subcontratación) = Sí.

En las líneas preparadas la misma columna da los avisos que no impiden la selección:

| Aviso | Qué hacer |
|---|---|
| Componentes con notificación posterior con esta elaboración: no se envían al subcontratista (necesitan el método de emisión manual). | si se deben enviar, ponga el método de emisión Manual |
| Indicar el proveedor. | elija el proveedor en la columna *Proveedor* |
| El proveedor F-TER01 no tiene ningún almacén de subcontratista vinculado. | vincule el almacén del subcontratista al proveedor (campo **Fornitore terzista** (Proveedor subcontratista)): sin él, la orden no se crea |

## 7. Lotes, números de serie y ubicaciones

Para transferencias, devoluciones, desechos y salida de los componentes en la recepción, los lotes y los números de
serie se eligen en una ventana del add-on, **antes** de crear los documentos. Después todos los documentos se crean en
una única operación.

![Recepción: se propone el lote LA de la orden, no el lote LE, que caduca antes pero no es de la orden](../../_img/contolavoro/23_selezione_lotti.png)

*Recepción: se propone el lote LA de la orden, no el lote LE, que caduca antes pero no es de la orden*

- **Propuesta automática**: desde el almacén del subcontratista (salida de componentes, devolución, desechos) primero
  los lotes **enviados a esa orden** (columna "De la orden", obtenida del registro de transacciones de lotes de SAP),
  después por fecha de caducidad (FEFO); desde el almacén de la empresa por fecha de caducidad (FEFO).
- **Elección manual**: la columna "A usar" es modificable; la cantidad se limita al stock del lote (descontadas otras
  líneas del mismo lote) y a 1 para los números de serie. *Proponer* rehace la propuesta, *Poner a cero* lo vacía
  todo. La confirmación solo es posible cuando cada línea tiene exactamente la cantidad solicitada.
- Solo se proponen lotes y números de serie **liberados** (ni bloqueados ni no accesibles).
- Las solicitudes de traslado no mueven lotes: para ellas no se abre ninguna selección.

### Lote del producto entrante

El lote del producto recibido se calcula con un **script SQL** configurable (Configuración › Lotes), con tres parámetros
fijos: `{ItemCode}` artículo, `{WhsCode}` almacén de entrada, `{DocEntry}` orden de subcontratación. El script
predefinido devuelve número de orden + número correlativo (p. ej. `20160256-1`); *Verificar* lo ejecuta con datos de
prueba. El lote creado aparece en el mensaje de fin de recepción. El mismo script da el lote del producto terminado de
la orden de fabricación (capítulo 6) en el recibo de producción. Si el producto terminado se gestiona por números de
serie, o el script no devuelve un lote, la recepción no se registra y un mensaje explica qué hacer. Para los números de
serie: **Lista subcontratista** = No en la lista de materiales del producto terminado y recibo de producción registrado
en SAP.

![Script del lote entrante](../../_img/contolavoro/19_config_lotti.png)

*Script del lote entrante*

### Documentos en borrador

El documento se crea como borrador, que se completa en el formulario de SAP, con almacenes con **ubicaciones**,
productos entrantes con **números de serie**, script del lote vacío o sin resultado y en la transferencia masiva. Se
completa el documento y se pulsa *Añadir*: el add-on elimina el borrador y continúa. En las líneas con lotes o números
de serie que elegir, en el borrador también la ubicación se indica en SAP junto con los lotes.

![Documento en borrador: "Completar el documento (lotes, números de serie, ubicaciones) y pulsar Añadir para continuar"](../../_img/contolavoro/20_bozza_trasferimento.png)

*Documento en borrador: "Completar el documento (lotes, números de serie, ubicaciones) y pulsar Añadir para continuar"*

## 8. Devoluciones y desechos

- **Devoluciones y desechos › Devolución de componentes del subcontratista**: cantidad en *A devolver* (*Proponer* =
  stock de la orden en el subcontratista), después *OK*: transferencia desde el almacén del subcontratista al almacén
  de la empresa.
- **Devoluciones y desechos › Transferir desechos**: cantidad en *A desechar*; traslada los desechos del
  subcontratista a un almacén a elección.
- **Devoluciones y desechos › Salida de desechos en el subcontratista**: en la ventana *Salida de desechos*, salida de
  mercancías de los desechos directamente desde el almacén del subcontratista.

  ![Salida de desechos](../../_img/contolavoro/08_scarti.png)

  *Salida de desechos*

Los componentes desechados vuelven al pendiente de envío.

## 9. Funciones de servicio

### Órdenes desde órdenes de fabricación

Muestra las elaboraciones externas de las OF liberadas, listas para convertirse en orden, y crea **una orden por
proveedor y almacén de devolución**. Con *Mostrar también las líneas no preparadas* explica por qué una elaboración no
está lista. Configuración, ejemplo completo y casos particulares en el capítulo 6.

![Las dos elaboraciones externas de la OF del ejemplo (capítulo 6), una por subcontratista](../../_img/contolavoro/15_da_odp.png)

*Las dos elaboraciones externas de la OF del ejemplo (capítulo 6), una por subcontratista*

### Transferencia masiva de componentes

Analiza las órdenes abiertas (filtros por fechas, proveedor, componente) y propone los componentes con pendiente de
envío, respetando la disponibilidad compartida entre las órdenes si la empresa bloquea el stock negativo. Crea una
transferencia por proveedor (en borrador si se necesitan lotes o ubicaciones). Las líneas con el almacén del
subcontratista ausente o igual al de partida se excluyen y se indican.

![Componentes con pendiente de envío, agrupados por proveedor y orden](../../_img/contolavoro/18_trasf_massivo.png)

*Componentes con pendiente de envío, agrupados por proveedor y orden*

### Transferencia de componentes entre órdenes

Traslada el stock que ya está en el subcontratista de una orden a otra sin movimientos de inventario (solo registro).
Por eso solo es posible entre órdenes **abiertas** con el **mismo almacén del subcontratista**: la lista propone solo
esas; con almacenes distintos la operación se bloquea y la mercancía debe devolverse y enviarse de nuevo. El stock se
vuelve a leer en el momento de la confirmación.

![Transferencia entre órdenes](../../_img/contolavoro/14_trasf_commesse.png)

*Transferencia entre órdenes*

### Cierre masivo de entradas de productos y precios de elaboración

*Cierre masivo de entradas de productos* muestra las entradas de mercancías de los productos todavía abiertas y cierra
las elegidas. *Precios de elaboración de subcontratistas* es la tabla de los precios de las elaboraciones por
subcontratista y producto.

Orden de búsqueda del precio de una elaboración: contratos de proveedor (opción, solo SQL Server), precios por
subcontratista, lista de materiales (opción), precio del proveedor de SAP, lista de precios de la orden.

![Entradas de mercancías de los productos todavía abiertas](../../_img/contolavoro/16_chiusura_emp.png)

*Entradas de mercancías de los productos todavía abiertas*

![Precios de las elaboraciones por subcontratista y producto](../../_img/contolavoro/17_prezzi_lav.png)

*Precios de las elaboraciones por subcontratista y producto*

## 10. Datos, campos y tipos de movimiento

| Tabla | Contenido |
|---|---|
| `@XEI_CL_OCNT` | cabecera de la orden (UDO `XEI_CL_COMMESSA`, con series) |
| `@XEI_CL_CNT1` | productos |
| `@XEI_CL_CNT2` | lista de materiales (componentes y elaboraciones) |
| `@XEI_CL_PRZLAV` | precios de elaboración por subcontratista y producto |
| `@XEI_CL_TRCOMM` | transferencias entre órdenes |

Campos en las tablas de SAP (prefijo `XEI_CL_`):

| Campo | Tablas | Contenido |
|---|---|---|
| `U_XEI_CL_ENTRY` | líneas de los documentos | orden de subcontratación (DocEntry) |
| `U_XEI_CL_LINENUM` | líneas de los documentos | línea de producto o de lista de materiales |
| `U_XEI_CL_TYPE` | líneas de los documentos | tipo de movimiento (tabla siguiente) |
| `U_XEI_CL_TXT`, `U_XEI_CL_OPIT`, `U_XEI_CL_ITEM`, `U_XEI_CL_WKEY`, `U_XEI_CL_ENBL` | líneas de los documentos | texto, artículo y OF de referencia, ofertas utilizables |
| `U_XEI_CL_ICNT` | artículos | artículo en subcontratación |
| `U_XEI_CL_TERZF`, `U_XEI_CL_DFTR` | almacenes | proveedor subcontratista del almacén, almacén del subcontratista predeterminado |
| `U_XEI_CL_DISTTERZ` | listas de materiales | lista subcontratista (recibo de producción desde OF) |
| `U_XEI_CL_ILAV` | líneas de lista de materiales y de OF | elaboración a la que pertenece el componente |

Si la empresa los usa, el add-on rellena también el código comercial, el motivo de transporte, el porte y el
transportista de los documentos.

| Tipo | Documento | Significado |
|---|---|---|
| EMP | pedido de compra, entrada de mercancías | producto |
| OAL | pedido de compra, entrada de mercancías | elaboración |
| UMC | salida de mercancías (emisión para producción si procede de OF) | componentes consumidos |
| TSO | transferencia de stock o solicitud | componentes enviados al subcontratista |
| TSI | transferencia de stock | devolución de componentes |
| TSS | transferencia de stock | transferencia de desechos |
| UMR | salida de mercancías | desechos en el subcontratista |
| EPR | recibo de producción | producto terminado de la OF (capítulo 6) |

En los cálculos se excluyen los documentos cancelados y las devoluciones se restan línea por línea.

## 11. Idiomas

El add-on sigue el idioma del cliente SAP. Están disponibles **italiano** (idioma base), **inglés**, **alemán**,
**francés**, **español** y **turco**: menús, formularios, columnas, botones, mensajes y comentarios de los documentos
creados. Con un idioma no previsto se usa el italiano.

| Idioma SAP | Textos del add-on | Commessa terzista | Terzista |
|---|---|---|---|
| Italian (Italy) | italiano | Commessa terzista | terzista |
| English (United States / United Kingdom) | inglés | Subcontracting Job | subcontractor |
| German | alemán | Lohnfertigungsauftrag | Lohnfertiger |
| French | francés | Ordre de sous-traitance | sous-traitant |
| Spanish (Spain / Latin America) | español | Orden de subcontratación | subcontratista |
| Turkish | turco | Fason iş emri | fasoncu |

Los términos siguen los de SAP Business One en el mismo idioma (por ejemplo *Vendor*, *Posting Date*, *Inventory
Transfer*, *Bill of Materials*, *Batch* en inglés; *Tedarikçi*, *Kayıt tarihi*, *Stok nakli*, *Ürün ağacı*, *Parti*
en turco).

### Cambiar el idioma

1. **Gestión › Configuración › General › Usuarios**, pestaña *Visualización*, campo *Idioma*, después *Actualizar*.
2. SAP avisa de que se cerrarán todas las ventanas abiertas: responder *Sí*.
3. El add-on vuelve a cargar solo los textos y crea de nuevo los menús en el nuevo idioma: no es necesario reiniciarlo.

![Orden de subcontratación con el cliente en inglés](../../_img/contolavoro/24_commessa_en.png)

*Orden de subcontratación con el cliente en inglés*

![Pestaña Documentos con el cliente en turco](../../_img/contolavoro/25_commessa_tr.png)

*Pestaña Documentos con el cliente en turco*

### Personalizar los textos

Cada texto se puede cambiar para el cliente concreto desde el menú **Traduzioni** (Traducciones) del add-on o con el
botón derecho en los formularios (*Modifica testo…* (Modificar texto…), *Testi di questa form…* (Textos de este
formulario…)). Se necesita la autorización `XEI_TEXTS` (los superusuarios la tienen siempre). Las personalizaciones se
mantienen en las actualizaciones del add-on.

Quedan en italiano los textos que SAP guarda en la base de datos, por ejemplo las descripciones de los campos de
usuario y el título de la tabla *Prezzi lavorazioni terzisti* (Precios de elaboración de subcontratistas). Las
entradas *Informazioni*, *Traduzioni* y *Licenza* del framework, con sus ventanas, están en italiano en todos los
idiomas.
