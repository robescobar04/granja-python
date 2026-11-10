# Reto 2 · El dron ve

Semana 2 · voluntario · unos 15-20 minutos al día

## Meta en el juego

Con **Senses** el dron ya sabe dónde está (`get_pos_x()`, `get_pos_y()`) y qué hay debajo (`get_entity_type()`).

- Haz una granja en **tablero de ajedrez**: arbustos en unas casillas y hierba en las otras.
- Junta lo necesario para desbloquear **Operators** y luego **Carrots**.

## Concepto de Think Python

**Condicionales**: `if / elif / else`, expresiones booleanas (`and`, `or`, `not`, `==`) y el operador módulo `%` (Think Python, cap. 5 *Conditionals and Recursion*).

## Requisitos

- [ ] Tu programa usa `if` con `elif` o `else`.
- [ ] Usa `%` para decidir qué va en cada casilla.
- [ ] En la captura se ve el tablero de ajedrez.
- [ ] Los `.py` del juego copiados en `codigo/` (tal cual salen de tu partida).
- [ ] Al menos **3 commits en días distintos** (se ve en el historial: la idea es programar un poco cada día, no todo la última noche).
- [ ] Al menos una captura de tu granja en `capturas/`.
- [ ] La sección **Mi entrega** rellenada.

## Pistas

Una casilla es "negra" del tablero si `x + y` es par:

```python
if (get_pos_x() + get_pos_y()) % 2 == 0:
    plant(Entities.Bush)
```

¿Qué pasa si plantas encima de algo que aún no ha crecido? Pruébalo y mira qué devuelve `plant(...)` con `quick_print`.

## Mi entrega

![Mi granja](capturas/granja.png)

**¿Dónde uso el concepto?** (archivo y qué hace esa parte):

**¿Qué me costó más y cómo lo resolví?**

**Una cosa que quiero probar la próxima semana:**
