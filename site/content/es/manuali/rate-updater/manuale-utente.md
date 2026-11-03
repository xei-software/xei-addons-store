---
title: XEI Rate Updater para SAP Business One – Manual de uso
description: "Tipos de cambio de las monedas en SAP Business One: instalación, primer inicio, actualización manual y automática, historial y licencia."
lang: es
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater para SAP Business One – Manual de uso

| | |
|---|---|
| SAP Business One | 10.0 o superior, con el Service Layer |
| Base de datos | Microsoft SQL Server o SAP HANA (en SAP HANA se recomienda una prueba durante la instalación) |
| Sistema | Windows 10 y 11, Windows Server 2016 y posteriores, de 64 bits; Microsoft Edge WebView2 Runtime |
| Idiomas del programa | italiano, inglés, alemán, francés, español, turco |

## 1. Qué hace

XEI Rate Updater para SAP Business One actualiza los **tipos de cambio de las monedas** en SAP Business One con los
tipos publicados por una fuente oficial:

1. toma los tipos de la **fuente** elegida para la fecha solicitada;
2. lee de la empresa SAP la **moneda local** y el **sentido** de los tipos de cambio: tipo directo (moneda local por
   una unidad de moneda extranjera) o tipo indirecto (moneda extranjera por una unidad de moneda local);
3. si la moneda local no es el euro, calcula los **tipos cruzados** respecto a ella;
4. para cada **moneda gestionada por la empresa** escribe en SAP el tipo de cambio en la fecha, en el sentido de la
   empresa, truncado a seis decimales;
5. guarda la ejecución en el **historial**.

Un error en una moneda no detiene las demás.

### La fecha de los tipos

Los tipos de un día se publican al final de la jornada. Por eso, para los tipos de cambio de un día en SAP se usan los
tipos publicados **el día anterior**. En los días sin publicación (fines de semana, festivos) vale el último día
publicado antes.

*Ejemplo*: los tipos de cambio del lunes 24 de febrero de 2025 son los tipos del viernes 21 de febrero. La fecha de los
tipos de cambio no puede ser futura.

### Las fuentes de los tipos

| Fuente | Notas |
|---|---|
| Banco Central Europeo (BCE) | predeterminada, gratuita, sin clave |
| Banco de Italia | tipos de cambio oficiales italianos, muchas monedas |
| Open Exchange Rates | requiere una clave API de Open Exchange Rates (Configuración › Tipos de cambio) |

Todas las fuentes publican los tipos respecto al euro. Con una moneda local distinta del euro, la fuente debe cotizarla.

### Las monedas

El programa reconoce las monedas por el **código ISO** (por ejemplo `USD`, `CHF`). En SAP las monedas extranjeras
deben tener como código el código ISO. Para la moneda local, si en SAP tiene otro código (por ejemplo «Eu» o «€» para
el euro), se indica el código ISO en *Configuración › Tipos de cambio*.

## 2. Instalación

1. Extraiga la carpeta del zip en el PC, por ejemplo en `C:\XEI\RateUpdater`.
2. Inicie **XEI.RateUpdater.exe**. El programa ya contiene .NET. Se necesita **Microsoft Edge WebView2 Runtime**, que
   normalmente ya está presente: si falta, el programa lo indica y propone descargarlo.

El programa no tiene instalación. La configuración y el historial están en la carpeta de datos de Windows de todos los
usuarios del PC, por lo que valen para cualquiera que use el programa en ese PC y para la actualización programada.

## 3. Primer inicio

En la primera apertura el programa muestra la página **Primer inicio**: todavía no está conectado a SAP. El código del
primer inicio ya está escrito.

1. **Conexión a SAP**:
   - *Dirección del Service Layer*;
   - *Sociedades SAP*: las bases de datos que se pueden elegir al iniciar sesión;
   - **Probar la conexión**.
2. **Acceso y primer administrador**:
   - *Acceso de los operadores*: **Usuario SAP de cada uno** (cada persona entra con su propio usuario SAP) o
     **Usuarios propios y usuario SAP técnico**;
   - *Usuario SAP del primer administrador* (por ejemplo `manager`);
   - *Usuario SAP técnico* y su contraseña: sirven para la **actualización automática**. Mejor un usuario dedicado, con
     el único permiso de escribir los tipos de cambio.
3. **Guardar y reiniciar**: el programa se vuelve a abrir en la página de inicio de sesión.

La misma configuración se cambia después en **Configuración › SAP**.

![Primer inicio](../../_img/rateupdater/00b-primo-avvio.png)

*Primer inicio: conexión a SAP, ámbito de la licencia y primer administrador.*

![Configuración › SAP](../../_img/rateupdater/05-impostazioni-sap.png)

*Configuración › SAP: dirección del Service Layer, empresas y acceso de los operadores.*

## 4. Inicio de sesión

Se entra con el **usuario de SAP Business One** y su contraseña. Arriba a la derecha se ven el usuario y la empresa.

![Inicio de sesión](../../_img/rateupdater/00-accesso.png)

*Inicio de sesión con el usuario de SAP Business One.*

Con *Usuario SAP de cada uno* el programa escribe los tipos de cambio con el usuario de quien trabaja: valen sus
autorizaciones de SAP sobre los tipos de cambio.

### Funciones de los usuarios

Un administrador asigna a cada usuario las funciones desde la página **Usuarios** del menú, igual para los usuarios
SAP y para los usuarios propios:

| Función | Qué permite |
|---|---|
| Actualización de tipos de cambio | actualizar los tipos de cambio en SAP desde la página Tipos de cambio |
| Historial | ver las ejecuciones de la actualización, manuales y automáticas |

El administrador tiene todas las funciones. El primer administrador es el usuario SAP indicado en el Primer inicio.

## 5. Tipos de cambio

Menú **Tipos de cambio**.

1. **Fecha de los tipos de cambio en SAP**: de entrada es hoy y no puede ser futura. Debajo se indica qué tipos se usan
   y la fuente configurada.
2. Pulse **Actualizar los tipos en SAP**.
3. El **resultado** indica la fecha, la fuente, el día de los tipos, cuántas monedas se han escrito y la moneda local.
   La tabla muestra para cada moneda de la fuente:

| Columna | Qué muestra |
|---|---|
| Moneda | código ISO |
| Tipo directo | moneda local por una unidad de moneda extranjera |
| Tipo indirecto | moneda extranjera por una unidad de moneda local |
| Resultado | **escrita en SAP**, **no gestionada** (la empresa no usa esta moneda) o rechazada, con el error de SAP |

Debajo se ve el estado de la **actualización automática**, con la última ejecución.

![Tipos de cambio](../../_img/rateupdater/01-cambi.png)

*Tipos de cambio: fecha, fuente y estado de la actualización automática.*

![Resultado de la actualización](../../_img/rateupdater/02-cambi-esito.png)

*Resultado: tipos de la fuente, monedas escritas en SAP y monedas que la empresa no gestiona.*

## 6. Historial

Menú **Historial**: las ejecuciones de la empresa, de la más reciente a la más antigua.

| Columna | Qué muestra |
|---|---|
| Iniciada | fecha y hora de la ejecución |
| Por | el usuario, o *automática* |
| Tipos al | la fecha de los tipos de cambio en SAP |
| Fuente | la fuente de los tipos |
| Tipos publicados el | el día de los tipos usados |
| Monedas escritas | cuántas monedas se han escrito en SAP |
| Resultado | **correcta** o **fallida** |

Una fila se abre sobre las monedas, con los tipos y el resultado de cada una. El historial guarda las últimas
ejecuciones (100 de entrada, en *Configuración › Tipos de cambio*).

![Historial](../../_img/rateupdater/03-storico.png)

*Historial: actualizaciones manuales y automáticas de la empresa.*

![Historial con las monedas](../../_img/rateupdater/03b-storico-valute.png)

*Una fila abierta: tipos y resultado de cada moneda.*

## 7. Configuración › Tipos de cambio

Solo para los administradores. Tras los cambios pulse **Guardar configuración**.

| Opción | Qué hace |
|---|---|
| Fuente de los tipos | Banco Central Europeo (predeterminada), Banco de Italia u Open Exchange Rates |
| Código ISO de la moneda local | solo si en SAP la moneda local tiene un código distinto del ISO; vacío = se toma de SAP |
| Clave API de Open Exchange Rates | solo con la fuente Open Exchange Rates; se guarda cifrada |
| Actualización automática | cada día el programa actualiza por sí solo los tipos de hoy de cada empresa, con el usuario SAP técnico |
| Hora de la actualización automática | en formato HH:mm (predeterminada 07:00) |
| Ejecuciones en el historial | cuántas ejecuciones conservar para cada empresa, de 10 a 1000 (predeterminado 100) |

![Configuración › Tipos de cambio](../../_img/rateupdater/04-impostazioni-cambi.png)

*Configuración › Tipos de cambio: fuente, moneda local, actualización automática e historial.*

## 8. Actualización automática

Los tipos de cambio de hoy se actualizan cada día de dos maneras.

### Con el programa abierto

Con **Actualización automática** activada, pasada la hora configurada el programa actualiza los tipos de cambio de hoy
de cada empresa con el usuario SAP técnico y guarda la ejecución en el historial (*Por*: automática). Si el programa
estaba cerrado a la hora fijada, actualiza en cuanto se vuelve a abrir. Si la fuente o SAP no responden, lo vuelve a
intentar poco después.

### Con el Programador de tareas de Windows

Así los tipos de cambio se actualizan también sin abrir el programa.

1. Haga el primer inicio y configure el **usuario SAP técnico** (Configuración › SAP).

   ![Usuario SAP técnico](../../_img/rateupdater/05b-impostazioni-sap-tecnico.png)

   *El usuario SAP técnico en Configuración › SAP.*

2. En Windows abra el **Programador de tareas** y cree una tarea básica, por ejemplo cada día a las 7:00.
3. Como acción elija **Iniciar un programa**:
   - programa: `XEI.RateUpdater.exe` en la carpeta del programa;
   - argumentos: `aggiorna`.
4. En las propiedades de la tarea elija **Ejecutar tanto si el usuario inició sesión como si no**, con un usuario de
   Windows del PC.

El comando actualiza los tipos de cambio de hoy con el usuario SAP técnico y se cierra, sin ventana. Usa la misma
configuración y el mismo historial que el programa. Argumentos opcionales:

| Argumento | Significado |
|---|---|
| `--societa <base de datos SAP>` | la empresa que se actualiza; con una sola empresa configurada no hace falta |
| `--data aaaa-mm-gg` | la fecha de los tipos de cambio, si no es hoy |

El Programador de tareas recibe el resultado: **0** correcto, **1** fallido o con una moneda rechazada, **2**
argumentos incorrectos. El detalle está en el historial. Si el comando ya ha actualizado los tipos de cambio de hoy, el
programa abierto no los vuelve a actualizar.

## 9. Licencia

El programa funciona con un **código de licencia** emitido por XEI, en tres ámbitos:

| Ámbito | Válido para |
|---|---|
| Por sociedad | una base de datos SAP |
| Por servidor | todas las empresas de la instancia SQL Server o SAP HANA |
| Libre | no está ligada a una base de datos |

La **prueba gratuita** dura 30 días y es libre.

![Licencia](../../_img/rateupdater/06-licenza.png)

*La página Licencia: estado, vencimiento, ámbito y campo para el código.*

![Configuración › Licencia](../../_img/rateupdater/06b-impostazioni-licenza.png)

*Configuración › Licencia: los tres ámbitos de la licencia.*

Menú **Licencia**: estado, vencimiento y ámbito de la licencia. El código recibido de XEI se pega en **Introduce un
código de licencia** y es válido al instante, sin reiniciar. Para una licencia por empresa o por servidor, el programa
debe estar conectado, en solo lectura, a la base de datos de la licencia (*Configuración › Licencia*, **Probar la
conexión**): los códigos de la empresa y del servidor que hay que enviar a XEI aparecen allí y en la página Licencia.

Para las licencias: [license@xeisrl.com](mailto:license@xeisrl.com).

## 10. Preguntas frecuentes y problemas

| Qué ve | Por qué | Qué hacer |
|---|---|---|
| Una moneda está *no gestionada* | La empresa SAP no usa esa moneda | Nada: solo se escriben las monedas de la empresa |
| Una moneda de la empresa no se actualiza | En SAP la moneda no tiene el código ISO como código | Use en SAP el código ISO (por ejemplo `USD`) |
| La ejecución se detiene enseguida con un error sobre la moneda local | La fuente no cotiza la moneda local, o en SAP tiene un código que no es ISO | Indique el código ISO en *Configuración › Tipos de cambio* o elija otra fuente |
| El resultado de una moneda es un error de SAP | SAP ha rechazado el tipo de cambio (por ejemplo, por las autorizaciones del usuario) | Lea el error; compruebe las autorizaciones de SAP del usuario sobre los tipos de cambio |
| La actualización automática no se inicia | Está desactivada, o falta el usuario SAP técnico | Actívela en *Configuración › Tipos de cambio* y configure el usuario técnico en *Configuración › SAP* |
| El programa pide instalar WebView2 | Falta Microsoft Edge WebView2 Runtime | Acepte la descarga propuesta, o instálelo desde el sitio de Microsoft |

## 11. Asistencia

Para las licencias: [license@xeisrl.com](mailto:license@xeisrl.com). Para la asistencia:
[info@xeisrl.com](mailto:info@xeisrl.com). En la solicitud indique la versión del programa (menú *Información*) y una
descripción del problema.
