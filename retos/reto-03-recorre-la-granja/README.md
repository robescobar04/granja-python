# Reto 3 · Recorre la granja

Semana 3 · voluntario · unos 15-20 minutos al día

## Meta en el juego

Las zanahorias necesitan tierra arada (`till()`).

- Reparte la granja por **columnas**: unas de zanahorias, otras de arbustos y otras de hierba.
- Consigue zanahorias, madera y heno hasta desbloquear **Trees**.

## Concepto de Think Python

**Bucles anidados**: un `for` dentro de otro `for` para recorrer una cuadrícula, y `%` para repartirla (Think Python, caps. 3 y 5).

## Requisitos

- [ ] Tu programa tiene un `for` dentro de otro `for`.
- [ ] Usa `%` con `get_pos_x()` (o `get_pos_y()`) para repartir la granja.
- [ ] Ara solo las casillas de zanahorias (¡`till()` otra vez las vuelve a dejar en hierba!).
- [ ] Los `.py` del juego copiados en `codigo/` (tal cual salen de tu partida).
- [ ] Al menos **3 commits en días distintos** (se ve en el historial: la idea es programar un poco cada día, no todo la última noche).
- [ ] Al menos una captura de tu granja en `capturas/`.
- [ ] La sección **Mi entrega** rellenada.

## Pistas

Esqueleto para recorrer toda la granja:

```python
for i in range(get_world_size()):
    for j in range(get_world_size()):
        if get_pos_x() % 3 == 0:
            quick_print("columna de zanahorias")
        move(North)
    move(East)
```

## Mi entrega

![Mi granja](capturas/granja.png)

**¿Dónde uso el concepto?** (archivo y qué hace esa parte):

**¿Qué me costó más y cómo lo resolví?**

**Una cosa que quiero probar la próxima semana:**
