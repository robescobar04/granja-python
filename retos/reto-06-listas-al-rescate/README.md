# Reto 6 · Listas al rescate

Semana 6 · voluntario · unos 15-20 minutos al día

## Meta en el juego

En el reto 5 el dron recorre **toda** la granja una y otra vez, aunque solo falten 2 calabazas. Con **Lists** puedes apuntar dónde están las que faltan y volver solo a esas.

- La misma calabaza gigante, pero más rápido.
- Desbloquea **Sunflowers**.

## Concepto de Think Python

**Listas**: crear una lista vacía, `append`, recorrerla con `for`, `len` (Think Python, cap. 9 *Lists*).

## Requisitos

- [ ] Guardas en una lista las posiciones `(x, y)` de las calabazas que faltan.
- [ ] Recorres esa lista en vez de toda la granja.
- [ ] Una función `ir_a(x, y)` que lleve el dron a una posición.
- [ ] En **Mi entrega**: ¿cuánto más rápido va que tu reto 5?
- [ ] Los `.py` del juego copiados en `codigo/` (tal cual salen de tu partida).
- [ ] Al menos **3 commits en días distintos** (se ve en el historial: la idea es programar un poco cada día, no todo la última noche).
- [ ] Al menos una captura de tu granja en `capturas/`.
- [ ] La sección **Mi entrega** rellenada.

## Pistas

```python
faltan = []
faltan.append((get_pos_x(), get_pos_y()))
for pos in faltan:
    quick_print(pos[0], pos[1])
quick_print(len(faltan))
```

Ojo: en el juego las listas solo tienen `append`, `insert`, `remove` y `pop` (nada de `sort`, `index`...).

## Mi entrega

![Mi granja](capturas/granja.png)

**¿Dónde uso el concepto?** (archivo y qué hace esa parte):

**¿Qué me costó más y cómo lo resolví?**

**Una cosa que quiero probar la próxima semana:**
