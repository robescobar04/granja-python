# Reto 1 · Primera cosecha

Semana 1 · voluntario · unos 15-20 minutos al día

## Meta en el juego

Que tu dron trabaje solo: recoger heno y madera sin que tú pulses nada.

- Desbloquea **Plant** (arbustos) si aún no lo tienes.
- Junta heno y madera hasta desbloquear **Senses**.

## Concepto de Think Python

**Bucles**: `while` y `for ... in range(...)` (Think Python: el `for` aparece en el cap. 3, apartado *Repetition*; el `while` llega más adelante en el libro, aquí lo usáis antes).

En el juego todavía no hay variables: todo se hace con llamadas a funciones y bucles.

## Requisitos

- [ ] Tu programa usa un `while` **y** un `for ... in range(...)`.
- [ ] El dron recorre toda la granja (no solo una casilla).
- [ ] Los `.py` del juego copiados en `codigo/` (tal cual salen de tu partida).
- [ ] Al menos **3 commits en días distintos** (se ve en el historial: la idea es programar un poco cada día, no todo la última noche).
- [ ] Al menos una captura de tu granja en `capturas/`.
- [ ] La sección **Mi entrega** rellenada.

## Pistas

Recorrer una columna entera:

```python
for i in range(get_world_size()):
    if can_harvest():
        harvest()
    move(North)
```

¿Y si quieres que no pare nunca? Mételo dentro de un `while True:`. ¿Cómo pasas a la siguiente columna?

## Mi entrega

![Mi granja](capturas/granja.png)

**¿Dónde uso el concepto?** (archivo y qué hace esa parte):

**¿Qué me costó más y cómo lo resolví?**

**Una cosa que quiero probar la próxima semana:**
