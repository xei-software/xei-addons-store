---
title: XEI.ItemGenerator – Manual de uso
description: Cómo configurar bases, valores y variantes y generar los artículos con XEI.ItemGenerator.
lang: es
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator – Manual de uso

La instalación, la licencia, los menús y las autorizaciones se describen en el
[manual de instalación](installazione.md).

## 1. Qué hace el add-on

XEI.ItemGenerator crea en los datos maestros de artículos artículos cuyos códigos se **componen** eligiendo, nivel
por nivel, unos valores: tipo de producto, medida, material... El árbol de elecciones se define una sola
vez; después, en lugar de inventar códigos y descripciones a mano, se componen en una ventana:
el add-on calcula código, descripción, precio, peso, medidas, grupo, propiedades y lista de materiales y
crea los artículos copiando un artículo modelo.

- **Códigos coherentes**: el código es "significativo" (p. ej. `PE090` = mueble alto de 90) más un número progresivo
  que distingue las variantes (color, tirador...).
- **Sin duplicados**: la misma composición genera siempre el mismo artículo; si ya existe,
  el add-on lo encuentra.
- **Muchos artículos de una vez**: varias medidas y varias opciones dan todas las combinaciones.
- **Artículos completos**: descripciones (también en idioma extranjero), datos maestros, precio de
  lista y lista de materiales proceden de la configuración.
- **Desde el documento**: en ofertas de ventas y pedidos de cliente se configura el artículo de la línea sin salir
  del documento.

### Aspectos destacados

- Generación en una ventana redimensionable sobre SAP: árbol de códigos y árbol de variantes
  con marcas (también en ramas distintas), búsqueda, lista de artículos con estado, precio y resultado; SAP
  sigue siendo utilizable. Aspecto del cliente SAP, mensajes con el mismo estilo, textos modificables con el
  botón derecho.
- Precio, peso, medidas, grupos, propiedades, nombre extranjero y lista de materiales compuestos a partir de valores y
  opciones.
- Fórmula de descripción con códigos, opciones y partes opcionales.
- Configurar artículo desde ofertas de ventas y pedidos de cliente; generar artículos similares a partir de un artículo generado.
- Verificación de la configuración con apertura de los datos maestros a corregir; importación/exportación con
  Excel; duplicación.
- Autorizaciones SAP por función; textos en cinco idiomas.

## 2. Conceptos: bases, valores, variantes y estructuras

El código de un artículo se compone de **código neutro** + **sufijo**:

- el **código neutro** es la parte significativa: la concatenación de los códigos de los **valores** elegidos nivel por
  nivel. Cada nivel es una **base** (p. ej. *Tipo mobile*, *Larghezza*) con una longitud fija y sus
  valores; cada valor lleva al **subnivel** siguiente o es el último;
- el **sufijo** es un número progresivo de N dígitos (configuración) que distingue los artículos con el
  mismo código neutro y **variantes** distintas; con 0 dígitos el código es el código neutro;
- una **variante** (p. ej. *Colore*) tiene **opciones** (p. ej. Bianco, Rovere). Las variantes que se piden
  para un valor se agrupan en una **estructura de variantes** vinculada al valor.

En todo el manual se usa este ejemplo, contenido en el archivo
[esempio-cucine.xlsx](../../_file/itemgenerator/esempio-cucine.xlsx), que se importa con
*Importar / exportar Excel*:

```
Tipo mobile cucina (CU, 2 caracteres)          estructura CUSC: Colore
├── BA Mobile base     → Larghezza
└── PE Mobile pensile  → Larghezza
Larghezza (CL, 3 caracteres)                   estructura CUSM: Colore anta + Maniglia, hereda variantes
├── 060 Larghezza 60 cm
└── 090 Larghezza 90 cm
Colore (CUCOL)     BI Bianco · RO Rovere
Maniglia (CUMAN)   AL Maniglia alluminio · NE Maniglia nera
```

El mueble alto de 90 con tirador de aluminio tiene el código neutro `PE090`; generando a la vez blanco y roble, con
un sufijo de 3 dígitos, el blanco (BI va antes que RO) se convierte en `PE090001` y el roble en `PE090002`.

La **composición** (valores de cada nivel + opciones elegidas) identifica el artículo: si se genera de
nuevo la misma composición, el add-on encuentra el artículo existente en lugar de crear otro.

## 3. Configuración

![Configuración](../../_img/itemgenerator/02_configurazione.png)

*La ventana de configuración.*

| Opción | Efecto | Predeterminado |
|---|---|---|
| Dígitos del sufijo | número progresivo tras el código neutro (0-10); 0 = código igual al código neutro (un solo artículo por código neutro) | 0 |
| Fórmula de descripción | cómo se compone la descripción (capítulo 8); vacía = descripciones de los niveles en orden | vacía |
| Descripciones en mayúsculas | descripción, descripción ampliada y nombre extranjero en mayúsculas | No |
| Lista de precios | lista de precios en la que se escribe el precio del artículo (suma de los precios de valores y opciones), en la moneda local | ninguna |
| Unidad de longitud | unidad de las medidas (longitud, ancho, altura) de valores y artículos; vacía = medidas no informadas | ninguna |
| Unidad de peso | unidad del peso de valores y opciones; vacía = peso no informado | ninguna |
| Lista de materiales | tipo de lista de materiales creada con los componentes: Ninguna, Producción, Ventas, Montaje, Modelo | Producción |
| Menú tras la creación | menú que se ejecuta para cada artículo creado (integración con otros add-ons, capítulo 14) | vacío |
| Miniatura | imagen del artículo en la cabecera de los datos maestros de artículos (capítulo 14) | No |
| Añadir a la lista vacía antes la lista | en la generación, *Añadir a la lista* sustituye la lista por la última selección; sin la opción los artículos se acumulan y se quitan con *Vaciar lista* (capítulo 9) | Sí |
| Tema de ventanas | colores de las ventanas del add-on (la generación), como los dos temas del cliente SAP: **SAP SQL** (cabecera oscura, botones dorados) o **SAP HANA** (cabecera azul, botones celestes). Se aplica a todos los add-ons XEI de la empresa; las ventanas abiertas cambian al instante | según la base de datos |

Las opciones se aplican a toda la empresa; si la generación ya está abierta, las usa al volver a abrirse.

## 4. Variantes y estructuras de variantes

### Definición de variantes y opciones

Una variante tiene un código, una descripción y sus **opciones** (pestaña *Opciones*). En la cabecera,
como en las bases, se pueden indicar una **tabla de usuario** y un **campo usuario artículo**: al
crear el artículo, la opción elegida se añade a la tabla (si no está) y su código se
escribe en el campo de usuario del artículo (capítulo 6).

![Variante Colore con las opciones](../../_img/itemgenerator/03_varianti.png)

*La variante Colore con las opciones.*

| Columna | Uso |
|---|---|
| Opción, Descripción | código y descripción de la opción; la descripción es el texto de la opción en la descripción del artículo |
| Desc. extranjera | texto de la opción en el nombre extranjero (vacío = el italiano) |
| Alias | texto libre |
| Precio | contribución al precio del artículo |
| Peso | contribución al peso del artículo |
| Propiedades | propiedades de artículo que se activan: números de 1 a 64 separados por comas (p. ej. `2, 12`) |
| Activo | las opciones desactivadas no aparecen en la generación |

En la pestaña *Componentes* se indican los componentes de la lista de materiales que aportan las opciones
(capítulo 7).

![Componentes de las opciones](../../_img/itemgenerator/04_varianti_componenti.png)

*Componentes de las opciones del tirador: dos tiradores del almacén 01.*

### Estructuras de variantes

Una estructura agrupa las variantes que se piden para un valor de base, con la **posición** (orden
en la generación; todas distintas) y la **posición de descripción** (orden de la opción elegida al final
de la descripción; 0 = no se añade al final). La descripción de la línea, si se indica, sustituye a la
de la variante (p. ej. "Colore anta").

![Estructura de variantes](../../_img/itemgenerator/05_strutture.png)

*La estructura CUSM: color de la puerta y tirador.*

No se puede eliminar una variante usada por una estructura, ni una estructura usada por una base.

## 5. Bases y valores

Cabecera de la base: código, descripción, **longitud de códigos** (todos los valores tienen esa
longitud), clasificación, tabla de usuario y campo usuario artículo. En la pestaña *Valores* hay una línea
por valor:

![Base con los valores](../../_img/itemgenerator/06_basi_valori.png)

*La base CU con los valores: descripciones, subnivel, estructura de variantes.*

![Columnas de los valores](../../_img/itemgenerator/06b_basi_valori.png)

*Las columnas siguientes: datos para el artículo (grupo, propiedades, precio, medidas, peso).*

Las columnas son muchas: **maximizando la ventana** la tabla se amplía y se ven todas.

| Columna | Uso |
|---|---|
| Código, Descripción | código del valor (con la longitud exacta indicada en la base) y descripción |
| Desc. artículo | texto del valor en la descripción del artículo |
| Desc. extranjera | texto del valor en el nombre extranjero del artículo (vacío = el italiano) |
| Subnivel | base del nivel siguiente (lista de selección; la flecha abre la base); vacío = último nivel |
| Estructura variantes | variantes que se piden para el valor (la flecha abre la estructura) |
| Heredar variantes | las variantes ya presentes en un nivel anterior parten con las opciones elegidas en ese nivel, **propuestas**: se pueden cambiar en el valor (botón derecho en la generación para volver a las propuestas). Mientras siguen la propuesta, la opción cuenta una sola vez |
| Forzar herencia | con Heredar variantes: se aplica la elección del nivel anterior y no se cambia en el valor (la variante no aparece en su nivel) |
| Activo | los valores desactivados no aparecen en la generación |
| UM inventario / compras / ventas | unidades de medida textuales del artículo |
| Grupo de artículos, Grupo UM | grupo de artículos y grupo de unidades de medida del artículo |
| Propiedades | propiedades de artículo que se activan (1-64) |
| Precio, Peso | contribuciones al precio y al peso del artículo |
| Longitud, Ancho, Altura | medidas del artículo |

Cómo se usan estos datos para el artículo se explica en el capítulo 6. En la pestaña *Componentes* se
indican los componentes de la lista de materiales que aportan los valores:

![Componentes de los valores](../../_img/itemgenerator/07_basi_componenti.png)

*El mueble alto lleva dos escuadras.*

- **Tabla de usuario** (una tabla de usuario sin objeto, por ejemplo una tabla de colores): al
  crear el artículo, el valor elegido se añade a ella (código y descripción), si no está.
- **Campo usuario artículo** (por ejemplo un campo *Colore* de los datos maestros de artículos): al crear
  el artículo se escribe en él el código del valor elegido.
- Las bases de **primer nivel** son las que no son subnivel de ningún valor.

Al guardar, el add-on controla longitudes, códigos repetidos, subnivel distinto de la propia
base, propiedades y componentes; el motivo de un error aparece en la barra de estado y no se
guarda. No se puede eliminar una base usada por artículos generados o que sea subnivel de otra base.

> **Duplicar** (en bases, variantes y estructuras): con un registro abierto prepara un registro nuevo con los
> mismos datos y todas las líneas; se escribe el código nuevo y se pulsa *Crear*. Útil para bases
> similares (p. ej. otra gama de medidas).

## 6. Datos del artículo creado

Cada dato del artículo procede de los valores de la composición y de las opciones elegidas, con dos reglas:

- **se aplica el último nivel que lo indica**: un nivel posterior redefine los niveles anteriores; un
  dato vacío o cero no borra el de un nivel anterior;
- **se suma**: todos los valores y las opciones elegidas contribuyen. Una opción heredada cuenta una
  sola vez, en el nivel en el que se eligió, mientras el nivel que la hereda la siga; una
  elección propia en ese nivel cuenta también allí (aunque sea la misma opción).

| Dato del artículo | Desde | Regla |
|---|---|---|
| Código | códigos de los valores | código neutro + sufijo (máx. 50 caracteres) |
| Descripción, descripción ampliada | desc. artículo de los valores, descripciones de las opciones | fórmula (capítulo 8); la descripción se trunca a 200 caracteres, la ampliada está completa en el campo *Descripción ampliada* |
| Nombre extranjero | desc. extranjera de valores y opciones | misma fórmula; vacío si ninguno tiene desc. extranjera |
| Comentarios | composición | árbol con los valores y las opciones elegidas |
| Grupo de artículos | valores | último nivel; ninguno = el del modelo |
| Grupo UM | valores | último nivel; con un grupo no se usan las UM textuales |
| UM inventario / compras / ventas | valores | último nivel, cada una por separado |
| Propiedades | valores y opciones | se suman: se activan todas |
| Longitud, ancho, altura | valores | último nivel, cada una por separado; en compras y ventas |
| Peso | valores y opciones | se suma; en compras y ventas |
| Precio | precio de valores y opciones | se suma; en la lista de precios de la configuración |
| Lista de materiales | componentes de valores y opciones | se suman (capítulo 7) |

Ejemplo: mueble alto de 90 en roble con tirador de aluminio (el color se elige en el nivel 1 y
lo hereda el 090).

| Nivel | Elección | Precio | Peso | Medidas | Grupo | Propiedades |
|---|---|---|---|---|---|---|
| 1 Tipo | PE Pensile | 100 | 10 | ancho 350, altura 720 | 101 | 1, 3 |
| 1 Colore | RO Rovere | 30 | 1,5 | | | 2 |
| 2 Larghezza | 090 L90 | 40 | 3 | longitud 900 | | 5 |
| 2 Maniglia | AL Alluminio | 5 | 0,2 | | | |
| **Artículo PE090002** | | **175** | **14,7** | **900 × 350 × 720** | **101** | **1, 2, 3, 5** |

Todo lo demás (cuentas, datos de planificación, proveedor, almacenes...) procede del **artículo
modelo** elegido en la generación: los nuevos artículos copian sus datos, sin stock, precios,
códigos de barras, lista de materiales, últimos precios ni nombre extranjero.

![El artículo creado](../../_img/itemgenerator/12_articolo.png)

*El artículo creado: descripción, nombre extranjero, grupo, precio en la lista de precios.*

![Propiedades](../../_img/itemgenerator/13_articolo_proprieta.png)

*Propiedades activadas por valores y opciones.*

![Medidas y peso](../../_img/itemgenerator/14_articolo_misure.png)

*Medidas y peso en los datos de ventas.*

## 7. Lista de materiales

Cada valor de base y cada opción de variante puede tener **componentes** (pestaña *Componentes*
de los dos datos maestros): el artículo componente, la **cantidad por una unidad** del artículo generado
y, opcional, el **almacén** de salida (vacío = el predeterminado del componente). Al
crear el artículo, el add-on crea su lista de materiales con los componentes de toda la composición:

1. para cada nivel, del primero al último, los componentes del valor elegido y después los de las opciones
   elegidas;
2. las opciones **heredadas** no vuelven a aportar sus componentes;
3. el **mismo artículo con el mismo almacén** se convierte en una sola línea con las cantidades sumadas;
4. la lista de materiales tiene cantidad 1 y el **tipo** de la configuración (producción, ventas, montaje,
   modelo); con *Ninguna*, o si la composición no tiene componentes, no se crea la lista de materiales;
5. el artículo y la lista de materiales se guardan juntos: si la lista de materiales no se puede crear, tampoco se conserva
   el artículo y el motivo está en la columna *Resultado* de la generación.

> SAP acepta cada tipo de lista de materiales solo en artículos adecuados (por ejemplo la lista de producción
> en un artículo de inventario, las de ventas y de montaje en un artículo de venta que no es de
> inventario): el artículo modelo debe tener las características adecuadas para el tipo elegido en la
> configuración.

En el ejemplo, el mueble alto lleva 2 escuadras, la opción roble 1 puerta y el tirador de aluminio 2
tiradores del almacén 01. El mueble alto de 90 en roble con tirador de aluminio tiene esta lista de materiales:

![Lista de materiales](../../_img/itemgenerator/15_distinta.png)

*La lista de materiales creada con el artículo.*

En la generación, la columna *Componentes* de la lista muestra cuántas líneas tendrá la lista de materiales; tras la
creación el resultado dice "Con lista de materiales (n componentes)". La verificación de la configuración señala
componentes inexistentes, con cantidad cero o con almacenes inexistentes.

## 8. Fórmula de descripción

La fórmula (configuración) decide cómo se componen la descripción, la descripción ampliada y el nombre
extranjero.

| Marcador | Se convierte en |
|---|---|
| `{1}`, `{2}`... | la *desc. artículo* del valor elegido en el nivel 1, 2... |
| `{C:1}`, `{N:1}` | el código y la descripción del valor elegido en el nivel 1 |
| `{V:CUCOL}` | la descripción de la opción elegida para la variante `CUCOL` |
| `{VC:CUCOL}` | el código de la opción elegida para la variante `CUCOL` |
| `{NEUTRO}` | el código neutro |
| `[ ... ]` | parte opcional: aparece solo si todos los marcadores que contiene tienen un valor |

- **Fórmula vacía**: las desc. artículo de los niveles en orden.
- **Al final** se añaden las descripciones de las opciones con posición de descripción mayor que cero, en
  ese orden, si la fórmula no cita ya su variante con `{V:...}` o `{VC:...}`.
- Un marcador sin valor queda vacío; dentro de `[ ]` elimina toda la parte, separadores incluidos.
- Los espacios dobles se eliminan; con *Descripciones en mayúsculas* todo va en mayúsculas; en los marcadores
  no importa si se escriben en mayúsculas o minúsculas.
- **Nombre extranjero**: la misma fórmula con las desc. extranjeras (las italianas donde faltan); vacío
  si ningún valor y ninguna opción tiene desc. extranjera.
- Un marcador desconocido se queda en el texto, para que se vea; la verificación de la configuración lo
  señala, igual que los corchetes sin cerrar o anidados.

Ejemplos con el mueble alto de 60 en roble con tirador de aluminio:

| Fórmula | Descripción |
|---|---|
| *(vacía)* | `Pensile L60 Rovere Maniglia alluminio` |
| `{1} {V:CUCOL} {2}` | `Pensile Rovere L60 Maniglia alluminio` |
| `{N:1} {C:2} - {NEUTRO}` | `Mobile pensile 060 - PE060 Rovere Maniglia alluminio` |
| `{1} {2}[ con {V:CUMAN}]` | `Pensile L60 con Maniglia alluminio Rovere`; sin tirador: `Pensile L60 Rovere` |
| *(vacía)*, mayúsculas | `PENSILE L60 ROVERE MANIGLIA ALLUMINIO` |
| *(vacía)*, nombre extranjero | `Wall unit L60 Oak Maniglia alluminio` |

## 9. Generación de los artículos

La generación es una **ventana independiente, sobre SAP**: se maximiza, se minimiza y se
redimensiona como cualquier ventana de Windows (los paneles se adaptan; los separadores entre paneles se
arrastran). La posición, el tamaño, los separadores y el ancho de las columnas se recuerdan por usuario; la
primera vez se abre a pantalla completa. Mientras está abierta, SAP sigue siendo utilizable, también durante la
creación de los artículos. Los colores siguen el **Tema de ventanas** de la configuración (capítulo 3):
en la cabecera está el formato del código y, debajo, un panel que indica desde dónde se ha abierto la
generación (línea de un documento, artículo similar) o qué no funciona.

Las operaciones largas (abrir muchos niveles, buscar, marcar una rama entera, añadir o crear
muchos artículos) **muestran lo que están haciendo** en la parte inferior de la ventana (mensaje con
el avance, barra) y se detienen con *Interrumpir*; mientras tanto los comandos están bloqueados y la ventana
sigue activa. Los resultados se leen en la parte inferior, con un icono (verde, naranja, rojo). Un error
imprevisto se muestra en un mensaje y la ventana sigue siendo utilizable.

![Generación con variantes](../../_img/itemgenerator/09_genera_varianti.png)

*Anchos 060 y 090 del mueble bajo y del mueble alto marcados (en dos ramas), color blanco y roble,
tirador de aluminio y negro: 16 artículos a componer.*

1. **Artículo modelo** (arriba, opcional, se recuerda de una sesión a otra): los nuevos
   artículos copian sus datos (capítulo 6). El botón *...* (o F2) busca el artículo por código o
   descripción; junto al código se ve la descripción, o *Artículo no encontrado en los datos maestros de artículos*.
   Sin modelo, los artículos se crean solo con los datos de la configuración.
2. **Árbol de códigos** (a la izquierda): las bases del primer nivel con sus valores; el signo **+**
   abre el subnivel de un valor. En azul, los valores con variantes; al pasar el ratón sobre un
   valor se ven la descripción del artículo, las variantes y el subnivel. Se **marcan los valores
   del último nivel** (los únicos con casilla), también más de uno e **incluso en ramas distintas**:
   junto a las ramas se ve cuántos valores están marcados debajo (*✓ 2*) y, bajo el árbol, sus códigos
   neutros.
   - **Buscar**: un código neutro completo (p. ej. `PE090`) lleva directamente a su valor; si no,
     lleva al valor siguiente que contiene el texto en el código o en la descripción (Intro para el
     siguiente, Ctrl+F para volver a la búsqueda). La búsqueda incluye también los niveles aún no
     abiertos.
   - **Expandir todo**, **Contraer**, **Desmarcar todo**; **Código neutro** muestra el código neutro junto a
     cada valor.
   - Botón derecho en una rama: *Marcar los valores del último nivel debajo*, *Desmarcar
     debajo*, *Expandir debajo*. Doble clic o barra espaciadora en un valor del último nivel:
     marca o desmarca.
3. **Variantes y opciones** (a la derecha): la **estructura del valor seleccionado** en el árbol (clic o
   flechas), con sus variantes en el orden de la estructura, las opciones que se marcan y su
   contribución al precio; el título indica de qué valor se trata. Una variante heredada lo indica
   junto al nombre: *propuesta por el nivel 1, Tipo: modificable* (sigue la elección hecha arriba),
   *elección propia, distinta del nivel 1* (con el botón derecho *Volver a las opciones propuestas*),
   *como el nivel 1: herencia forzada* (capítulo 5). La misma variante en el mismo nivel se
   elige **una sola vez** para todos los valores marcados. La casilla *Todas las variantes de los valores
   marcados, por nivel* muestra en cambio todas las variantes de los valores marcados agrupadas por
   nivel, con *solo para 060* si una variante afecta solo a algunos valores. Varias opciones de la misma
   variante dan varios artículos; una variante sin opciones marcadas no entra en la composición.
   Botón derecho: *Marcar todas las opciones* / *Desmarcar todas las opciones*. Debajo se ve cuántos artículos
   se compondrán.
4. **Añadir a la lista**: compone todas las combinaciones en la lista inferior, con código,
   descripción, precio, número de componentes de la lista de materiales y estado. De forma predeterminada (opción *Añadir
   a la lista vacía antes la lista*, capítulo 3) la lista se vacía y contiene solo la última
   selección; con la opción desactivada los artículos se acumulan y los que ya están en la lista no se
   repiten. Las marcas de valores y opciones se mantienen (se quitan con *Desmarcar todo*): se cambia
   una opción o un valor y se vuelve a añadir.
5. **Generar artículos (n)**: crea los artículos marcados de la lista (n en el botón), uno a uno,
   con el resultado línea por línea y la barra de avance. *Interrumpir* detiene la creación después del
   artículo en curso. Al final, en la parte inferior de la ventana, aparece el resumen: *Artículos creados: n.*,
   y después, solo si los hay, los que mientras tanto ya había creado otro usuario y los que tienen
   errores; la lista se sitúa en el primer artículo creado.

![Lista de los artículos compuestos](../../_img/itemgenerator/08_genera.png)

*Los 16 artículos compuestos (el final de la lista): 15 ya en los datos maestros de artículos (en amarillo) y uno por crear,
PE060004, con precio y número de componentes.*

| Estado | Significado |
|---|---|
| A crear | código = código neutro + primer sufijo libre (ni en los datos maestros de artículos ni ya en la lista) |
| Ya existente | la misma composición ya está en los datos maestros de artículos: el código es el del artículo existente (amarillo) |
| Creado | artículo creado (verde); el resultado indica si tiene lista de materiales |
| Error | el motivo está en la columna *Resultado* (rojo): código ya usado, sufijos agotados, código demasiado largo, error de SAP. Se puede corregir y generar de nuevo |

![Resultado de la generación](../../_img/itemgenerator/11_genera_esito.png)

*Resultado de la generación: los muebles bajos de 60 y de 90 en blanco creados (en verde) y el resumen en la parte inferior;
sin componentes no tienen lista de materiales (con los componentes el resultado dice "Con lista de materiales").*

En la lista, la casilla (solo en los artículos a crear o con error) decide qué artículos se crean.
**Doble clic** (o Intro) en un artículo creado o ya existente lo abre en los datos maestros de artículos de SAP (la
generación se minimiza y se vuelve a abrir desde la barra de tareas). Un artículo aún por
crear no abre nada: en la parte inferior de la ventana se lee *El artículo ... aún no está en los datos maestros de artículos*;
lo mismo si mientras tanto el artículo se ha eliminado en SAP. Botón derecho: *Abrir en datos maestros de artículos*,
*Copiar código*, *Quitar de la lista*, *Marcar todo*, *Desmarcar todo*; Supr quita las líneas
seleccionadas, Ctrl+C copia sus códigos. *Vaciar lista* empieza de cero. Si en la lista hay
artículos aún no creados, al cerrar o vaciar se pide confirmación.

### Mensajes y textos de la ventana

Las preguntas y los mensajes de la generación (por ejemplo *¿Crear 2 artículos en los datos maestros de artículos?*) tienen el mismo
aspecto que la ventana: Intro elige el botón resaltado, Esc responde No. Quien tiene
la autorización **Modifica testi add-on XEI** (modificar textos add-on XEI) puede cambiar los textos de la ventana como en las
ventanas de SAP: botón derecho en una etiqueta, un botón, el título de un panel, la cabecera
de una columna o el texto de un mensaje y, después, **Modifica testo...** (Modificar texto); **Testi di questa finestra...** (Textos de esta ventana)
(también al final de los menús de los árboles y de la lista) los muestra todos. El texto personalizado se aplica a
todos los usuarios en el idioma en uso y se ve al instante.

![Pregunta antes de la creación](../../_img/itemgenerator/25_messaggio.png)

*La pregunta antes de la creación, con el estilo de la ventana.*

![Modifica testo](../../_img/itemgenerator/26_modifica_testo.png)

*Modifica testo (Modificar texto) desde el botón derecho en el botón Buscar: texto original y texto personalizado.*

Antes de crear cada artículo, el add-on vuelve a comprobar que mientras tanto nadie haya creado la misma
composición o usado el código. Cada artículo se crea en una única operación (artículo, lista de materiales,
tablas de usuario, composición): un error no deja datos a medias.

## 10. Artículos desde ofertas de ventas y pedidos de cliente

En las **ofertas de ventas** y en los **pedidos de cliente**, botón derecho en una línea › **Configurar
artículo...**:

![Configurar artículo desde la línea](../../_img/itemgenerator/17_ordine_menu.png)

*Configurar artículo desde la línea del pedido.*

La generación se abre para esa línea (lo indican el título de la ventana y el panel superior).
Se compone y se crea el artículo como siempre; después **Usar en la línea** pone en la línea del documento
el artículo seleccionado en la lista (creado o ya existente; si la lista tiene solo uno no hace falta
seleccionarlo), cierra la generación y vuelve a mostrar el documento en primer plano. SAP rellena la línea como
si el código se hubiera escrito a mano: descripción, precio de la lista de precios del cliente, almacén.

![Generación abierta desde la línea](../../_img/itemgenerator/18_genera_documento.png)

*Generación abierta desde la línea 2 del pedido: el artículo recién creado seleccionado y "Usar en la
línea".*

![Artículo en la línea](../../_img/itemgenerator/19_ordine_riga.png)

*El artículo en la línea del pedido.*

- Si la línea ya tiene un artículo generado por el configurador, la generación parte de su
  configuración: basta con cambiar una opción para obtener la variante correcta.
- Si la generación ya está abierta, pasa a la nueva línea; la lista se mantiene, de modo que se puede reutilizar un
  artículo compuesto antes.
- El documento debe permanecer abierto; un documento cerrado o no modificable no cambia (el motivo
  aparece en la parte inferior de la ventana).

## 11. Artículos similares

En los datos maestros de un artículo creado por el configurador, botón derecho › **Generar artículos
similares...**: la generación se abre con la configuración del artículo ya establecida (su valor
final marcado en el árbol, ya abierto hasta él, y las opciones elegidas) y con el propio artículo
como modelo. Se cambian valores y opciones y se añaden los artículos a la lista. Si la
generación ya está abierta (aunque esté minimizada) vuelve al primer plano con la configuración
del artículo; la lista se mantiene.

![Botón derecho en un artículo generado](../../_img/itemgenerator/16_simili_menu.png)

*El botón derecho en un artículo generado.*

![Generación de artículos similares](../../_img/itemgenerator/20_simili.png)

*Generación desde la configuración de PE090002 (tema SAP HANA): mueble alto de 90, roble y tirador de
aluminio ya marcados; como modelo, el propio artículo.*

Si mientras tanto la configuración ha cambiado (valores quitados o desactivados, subniveles distintos), la
generación parte de cero, con un aviso; las opciones que ya no existen se ignoran.

## 12. Verificación de la configuración

Controla toda la configuración (también los valores y las opciones desactivados) y muestra los problemas, primero
los errores y después los avisos. **Doble clic** en una línea abre los datos maestros a corregir en el registro;
*Verificar de nuevo* repite el control tras las correcciones. Al ampliar la ventana (incluso a pantalla
completa) la lista de problemas se adapta a ella.

![Verificación de la configuración](../../_img/itemgenerator/21_verifica.png)

*Verificación: una estructura de variantes que no existe y un valor que hereda sin variantes que
heredar.*

| Tipo | Control |
|---|---|
| Error | base sin longitud; código con longitud distinta de la de la base; código repetido |
| Error | subnivel, estructura de variantes, grupo de artículos, grupo UM inexistentes; propiedades no válidas |
| Error | variante inexistente en una estructura; opción repetida |
| Error | componente sin artículo, con artículo o almacén inexistentes, con cantidad cero, para un valor o una opción que no existe |
| Error | base subnivel de sí misma (ciclo, con la ruta); ninguna base de primer nivel |
| Aviso | base sin valores activos; estructura sin variantes; variante sin opciones activas |
| Aviso | base que no se alcanza desde el primer nivel (subnivel solo de valores desactivados) |
| Aviso | ruta que da códigos de más de 50 caracteres, sufijo incluido |
| Aviso | valor que hereda las variantes sin variantes iguales en los niveles anteriores; Forzar herencia sin Heredar variantes |
| Aviso | fórmula con marcadores desconocidos o corchetes incorrectos |

## 13. Importación y exportación con Excel

![Importación desde Excel](../../_img/itemgenerator/22_excel.png)

*Importación del archivo de ejemplo realizada correctamente.*

**Exportar...** pregunta dónde guardar y escribe toda la configuración en un archivo .xlsx, una hoja por
tipo de datos maestros, con la cabecera en negrita e inmovilizada. **Importar** lee el archivo indicado
(*Examinar...*). Al ampliar la ventana, el nombre del archivo y la lista del resultado se amplían.

| Hoja | Una línea por | Columnas |
|---|---|---|
| Basi | valor (los datos de la base se repiten) | Base, Descrizione base, Lunghezza, Classificazione, Tabella utente, Campo utente, Codice, Descrizione, Desc. articolo, Desc. straniera, Sotto livello, Struttura varianti, Eredita varianti, Forza ereditarietà, Attivo, UM magazzino, UM acquisti, UM vendite, Valore, Dim. 1, Dim. 2, Dim. 3, Peso, Gruppo articoli, Gruppo UM, Proprietà, Note |
| Componenti basi | componente | Base, Valore, Componente, Descrizione, Quantità, Magazzino, Note |
| Varianti | opción | Variante, Descrizione variante, Tabella utente, Campo utente, Opzione, Descrizione, Desc. straniera, Alias, Valore, Peso, Proprietà, Note, Attivo |
| Componenti varianti | componente | Variante, Opzione, Componente, Descrizione, Quantità, Magazzino, Note |
| Strutture | variante | Struttura, Descrizione struttura, Variante, Descrizione variante, Posizione, Pos. descrizione |

- Las columnas se reconocen por el **título**: el orden no importa y las desconocidas se ignoran. El
  archivo puede tener también solo algunas hojas.
- Números en formato italiano (`1.234,5`) o inglés (`1234.5`); sí/no con Y, S, Sì, X, 1, Vero.
- Los códigos con ceros iniciales (`060`) deben escribirse como texto (en Excel con el apóstrofo: `'060`);
  de lo contrario, Excel los convierte en números.
- La importación **primero controla todo** el archivo: si hay un error no escribe nada y la lista
  muestra hoja, línea y motivo de cada error.
- Después escribe todo a la vez: cada base, variante o estructura del archivo se añade o se actualiza y
  sus líneas **sustituyen** a las existentes; los componentes cambian solo para las bases y variantes
  presentes en las hojas de los componentes; lo que no está en el archivo se queda como está.

Usos típicos: exportar, modificar en Excel (nuevos valores, precios actualizados) y volver a importar; copiar
la configuración a otra empresa; partir de un ejemplo como
[esempio-cucine.xlsx](../../_file/itemgenerator/esempio-cucine.xlsx).

## 14. Datos maestros de artículos, control de coherencia, otros add-ons

### Miniatura de la imagen

Con la opción *Miniatura*, los datos maestros de artículos muestran la imagen del artículo (campo Imagen,
en la carpeta de imágenes de SAP) en el espacio libre de la cabecera, a la izquierda de las casillas Artículo
de inventario/de venta/de compra. El recuadro toma las proporciones de la imagen y se oculta si
el artículo no tiene imagen. Los datos maestros de artículos no se ralentizan.

![Miniatura en los datos maestros de artículos](../../_img/itemgenerator/24_miniatura.png)

*La miniatura en los datos maestros de artículos.*

### Control de coherencia

Recalcula la composición de todos los artículos generados. Sirve si los datos de la configuración se
han modificado fuera del add-on; también elimina las composiciones de los artículos eliminados en SAP.

### Integración con otros add-ons

Con un *Menú tras la creación* en la configuración, para cada artículo creado el add-on ejecuta ese menú
después de registrar su código en la tabla XEI `@XEI_IG_EVENTS`: otro add-on que esté a la escucha de
ese menú puede completar el artículo.
