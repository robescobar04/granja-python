# Reto 4 · Mis funciones

Semana 4 · voluntario · unos 15-20 minutos al día

## Meta en el juego

Ahora tienes **Variables**, **Functions** e **Import**.

- Planta **árboles** en tablero de ajedrez (los árboles crecen más lentos si tienen otro árbol al lado).
- Mantén zanahorias y heno.
- Junta recursos hasta desbloquear **Pumpkins**.

## Concepto de Think Python

**Funciones**: `def`, parámetros y `return` (Think Python, cap. 3 *Functions* y cap. 6 *Return Values*).

## Requisitos

- [ ] Al menos **dos funciones tuyas** con `def`.
- [ ] Una de ellas recibe parámetros y **devuelve** algo con `return` (por ejemplo, qué plantar en la casilla `(x, y)`).
- [ ] Opcional: pon tus funciones en otro archivo y úsalas con `import`.
- [ ] Los `.py` del juego copiados en `codigo/` (tal cual salen de tu partida).
- [ ] Al menos **3 commits en días distintos** (se ve en el historial: la idea es programar un poco cada día, no todo la última noche).
- [ ] Al menos una captura de tu granja en `capturas/`.
- [ ] La sección **Mi entrega** rellenada.

## Pistas

```python
def que_plantar(x, y):
    if x % 3 == 0:
        return Entities.Carrot
    return Entities.Bush

planta = que_plantar(get_pos_x(), get_pos_y())
quick_print(planta)
```

Recuerda: en el juego no hay `int()`, ni operador ternario (`a if c else b`), ni argumentos con nombre.

## Mi entrega

![Mi granja](capturas/granja.png)

**¿Dónde uso el concepto?** (archivo y qué hace esa parte):

**¿Qué me costó más y cómo lo resolví?**

**Una cosa que quiero probar la próxima semana:**
