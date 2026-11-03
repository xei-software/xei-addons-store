---
title: XEI Rate Updater para SAP Business One – Instalación, primer inicio, licencia y actualización programada
description: Cómo instalar XEI Rate Updater para SAP Business One, conectarlo a SAP Business One, activar la licencia y programar la actualización diaria de los tipos de cambio.
lang: es
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater para SAP Business One – Instalación, primer inicio, licencia y actualización programada

## Requisitos

| | |
|---|---|
| SAP Business One | 10.0 o superior, con el Service Layer |
| Base de datos | Microsoft SQL Server o SAP HANA (en SAP HANA se recomienda una prueba durante la instalación) |
| Sistema | Windows 10 y 11, Windows Server 2016 y posteriores, de 64 bits; Microsoft Edge WebView2 Runtime |
| Red | acceso a internet hacia la fuente de los tipos elegida |
| Idiomas del programa | italiano, inglés, alemán, francés, español, turco |

## Instalación

1. Descargue el zip del programa desde la página de descargas.
2. Extraiga la carpeta del zip en el PC, por ejemplo en `C:\XEI\RateUpdater`.
3. Inicie **XEI.RateUpdater.exe**. El programa ya contiene .NET. Se necesita **Microsoft Edge WebView2 Runtime**, que
   normalmente ya está presente: si falta, el programa lo indica y propone descargarlo.

El programa no tiene instalación. La configuración y el historial están en la carpeta de datos de Windows común a todos
los usuarios del PC. Para actualizar el programa se sustituye la carpeta por la nueva: la configuración y el historial
se conservan.

## Primer inicio

En la primera apertura se abre la página **Primer inicio**, con el código del primer inicio ya escrito.

1. **Conexión a SAP**: *Dirección del Service Layer* y *Sociedades SAP*; después **Probar la conexión**.
2. **Acceso y primer administrador**:
   - *Acceso de los operadores*: **Usuario SAP de cada uno** o **Usuarios propios y usuario SAP técnico**;
   - *Usuario SAP del primer administrador* (por ejemplo `manager`);
   - *Usuario SAP técnico* y contraseña: sirven para la actualización automática. Mejor un usuario dedicado, con el
     único permiso de escribir los tipos de cambio.
3. **Guardar y reiniciar**.

Después, la misma configuración está en **Configuración › SAP**. La fuente de los tipos y la actualización automática
están en **Configuración › Tipos de cambio**.

## Licencia

El programa funciona con un **código de licencia** emitido por XEI.

| Ámbito | Válido para |
|---|---|
| Por sociedad | una base de datos SAP |
| Por servidor | todas las empresas de la instancia SQL Server o SAP HANA |
| Libre | no está ligada a una base de datos |

- **Prueba**: 30 días, libre.
- Menú **Licencia**: estado, vencimiento y ámbito. El código recibido de XEI se pega en **Introduce un código de
  licencia** y es válido al instante, sin reiniciar.
- Para una licencia por empresa o por servidor, el programa debe estar conectado, en solo lectura, a la base de datos
  de la licencia (*Configuración › Licencia*, **Probar la conexión**): allí y en la página Licencia aparecen los
  códigos de la empresa y del servidor, que hay que enviar a [license@xeisrl.com](mailto:license@xeisrl.com).

## Actualización programada con Windows

Así los tipos de cambio se actualizan cada día también con el programa cerrado.

1. Configure el **usuario SAP técnico** (Configuración › SAP).
2. En Windows abra el **Programador de tareas** y cree una tarea básica, por ejemplo cada día a las 7:00.
3. Acción **Iniciar un programa**: `XEI.RateUpdater.exe` en la carpeta del programa, con el argumento `aggiorna`.
4. En las propiedades de la tarea elija **Ejecutar tanto si el usuario inició sesión como si no**.

El comando actualiza los tipos de cambio de hoy y se cierra sin ventana; la ejecución aparece en el **Historial**. Con
varias empresas se añade `--societa <base de datos SAP>`, una tarea para cada empresa. Resultado para el Programador
de tareas: **0** correcto, **1** fallido o con una moneda rechazada, **2** argumentos incorrectos.

Como alternativa, con el programa abierto, basta con activar **Actualización automática** en
*Configuración › Tipos de cambio*.

## Asistencia

Para las licencias: [license@xeisrl.com](mailto:license@xeisrl.com). Para la asistencia:
[info@xeisrl.com](mailto:info@xeisrl.com). En la solicitud indique la versión del programa (menú *Información*) y una
descripción del problema.
