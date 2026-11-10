# Granja Python

Retos semanales para practicar Python en casa con el juego **[The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/)**: programas un dron que cultiva una granja, y cada cosa que consigues desbloquea nuevas partes del lenguaje.

La idea no es pasarse el juego: es **programar un poco casi todos los días**. Son 8 retos, uno por semana, voluntarios. Cada uno sigue el juego y además practica un concepto de *Think Python*.

¿No tienes el juego? Hay un camino alternativo **gratuito** con la misma tarea: [gdscript-python](https://github.com/maximofernandezriera/gdscript-python) (*Learn GDScript From Zero*, en el navegador). Elige uno de los dos.

## Cómo empezar

1. Pulsa **Use this template → Create a new repository** (arriba a la derecha). Ponle de nombre `granja-python` y déjalo **público** para que tu profesor pueda verlo.
2. Clónalo en tu ordenador (o trabaja desde la web de GitHub, como prefieras).
3. Pásale a tu profesor el enlace de tu repo.

## Cada semana

1. Abre el `README.md` del reto de la semana en [`retos/`](retos/).
2. Juega y programa **un rato varios días** (15-20 minutos basta).
3. Copia tus programas del juego a la carpeta `codigo/` del reto. Haz un commit **cada día que avances**: cada reto pide al menos 3 commits en días distintos.
4. Haz una captura de tu granja (en Windows: `Win + Shift + S`; en macOS: `Cmd + Shift + 4`; en Steam también `F12`), guárdala en `capturas/` y rellena la sección **Mi entrega** del README del reto.
5. Marca el reto como hecho en la tabla de abajo.

## Dónde están tus programas

El juego guarda cada ventana de código como un archivo `.py` dentro de la carpeta de tu partida. En Windows suele estar en:

```
%USERPROFILE%\AppData\LocalLow\TheFarmerWasReplaced\TheFarmerWasReplaced\Saves\
```

Si no la encuentras, usa el buscador de archivos con el nombre de uno de tus programas (por ejemplo `main.py`). Copia los `.py` **tal cual**; no hace falta subir los otros archivos de la partida.

## Python del juego ≠ Python normal

El juego usa un lenguaje casi igual a Python, pero con diferencias. Si algo de clase no te funciona en el juego, mira aquí:

| En Python normal | En el juego |
|---|---|
| `print("hola")` sale en la consola | `print` sale como humo encima del dron; usa `quick_print(...)` para ver el texto en la salida |
| `int(3.7)` | No existe; todos los números son decimales. Usa `3.7 // 1` |
| `[x for x in ...]` (comprensiones) | No existen: usa un `for` con `append` |
| `a if c else b` | No existe: usa un `if` normal |
| `f(x, sep="-")` (argumentos con nombre) | No existen |
| `lambda`, `class`, `*args`, `**kwargs` | No existen |
| `lista.sort()`, `lista.index(...)` | Las listas solo tienen `append`, `insert`, `remove` y `pop` |
| Todo disponible desde el principio | Variables, funciones, listas, diccionarios... se **desbloquean** jugando |

Puedes escribir el código en un editor externo (VS Code, etc.): el juego lee los mismos `.py`.

## Si usas Linux

El juego es para Windows y macOS, pero funciona bien con Steam y Proton: en Steam, botón derecho sobre el juego → **Propiedades → Compatibilidad** → marca *Forzar el uso de una herramienta de compatibilidad de Steam Play* y elige la última versión de Proton.

## Mi progreso

| Semana | Reto | Concepto | Hecho |
|---|---|---|---|
| 1 | [Primera cosecha](retos/reto-01-primera-cosecha/) | `while` y `for` | [ ] |
| 2 | [El dron ve](retos/reto-02-el-dron-ve/) | `if / elif / else`, `%` | [ ] |
| 3 | [Recorre la granja](retos/reto-03-recorre-la-granja/) | bucles anidados | [ ] |
| 4 | [Mis funciones](retos/reto-04-mis-funciones/) | `def`, parámetros, `return` | [ ] |
| 5 | [Calabazas gigantes](retos/reto-05-calabazas-gigantes/) | `while` con condición | [ ] |
| 6 | [Listas al rescate](retos/reto-06-listas-al-rescate/) | listas | [ ] |
| 7 | [Girasoles](retos/reto-07-girasoles/) | buscar el máximo en una lista | [ ] |
| 8 | [Diccionarios](retos/reto-08-diccionarios/) | diccionarios | [ ] |

Si te atascas en el juego más de 20 minutos, para, apunta qué intentabas en **Mi entrega** y pregúntalo en clase. Atascarse también cuenta como práctica.
