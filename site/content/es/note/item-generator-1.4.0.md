---
title: XEI.ItemGenerator 1.4.0 – Notas de la versión
lang: es
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator 1.4.0 – Notas de la versión

## Novedades

- **Herencia de variantes como propuesta.** Con *Heredar variantes* se proponen las
  opciones elegidas en un nivel anterior, pero pueden cambiarse en el nivel que las
  hereda. El botón derecho ofrece **Volver a las opciones propuestas**.
- **Forzar herencia.** Nueva opción en los valores de las bases: impone la elección del
  nivel anterior, que no se puede cambiar en el valor.
- **Tabla y campo de usuario en las variantes.** En *Variantes y opciones* se pueden
  indicar una tabla de usuario y un campo usuario artículo: al crear los artículos, las
  opciones elegidas se añaden a la tabla y se copian en el campo.
- **Ventana Generar artículos más clara.** El panel de variantes muestra solo las
  variantes del valor seleccionado en el árbol; una casilla activa la vista completa por
  nivel.
- **Lista de artículos a generar.** Nuevo ajuste *Añadir a la lista vacía antes la lista
  de artículos a generar* (activado de forma predeterminada): la lista contiene solo la
  última selección. Si se desactiva, los artículos se acumulan.
- **Menús numerados.** Las entradas del Configurador de códigos están numeradas del 0 al 7
  en el orden de trabajo: Configuración, Definición de bases, Variantes y opciones,
  Estructuras de variantes, Generar artículos, Control de coherencia, Verificar
  configuración, Importar / exportar Excel.
- **Subnivel con lista de selección.** En *Definición de bases* la columna Subnivel se
  rellena con la lista de selección de las bases y la flecha abre la base vinculada. Un
  código escrito a mano se rechaza si la base no existe.

## Mejoras

- Verificación de la configuración e importación / exportación Excel actualizadas con los
  nuevos campos.
- Cabeceras de las ventanas más compactas, en línea con el estilo de SAP Business One.
- Traducciones actualizadas al inglés, alemán, francés y español.

## Actualización

- Requiere XEICore 1.1.1, incluido en el paquete.
- En el primer inicio el add-on actualiza por sí solo la estructura de datos (versión 3).
- El código de licencia ya introducido sigue siendo válido.
