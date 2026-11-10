# Reto 8 · Diccionarios

Semana 8 · voluntario · unos 15-20 minutos al día

## Meta en el juego

Con **Dictionaries** puedes guardar *posición → pétalos* directamente.

- Rehaz el reto 7 con un diccionario en vez de una lista.
- Reto libre final: automatiza tu granja entera (calabazas, girasoles, árboles...) con todo lo aprendido.

## Concepto de Think Python

**Diccionarios**: crear `{}`, `d[clave] = valor`, recorrer las claves con `for`, `in` (Think Python, cap. 10 *Dictionaries*).

## Requisitos

- [ ] Un diccionario cuyas claves son posiciones `(x, y)`.
- [ ] Lo actualizas después de cada cosecha.
- [ ] En **Mi entrega**: ¿qué te ha resultado más cómodo, la lista del reto 7 o el diccionario? ¿Por qué?
- [ ] Los `.py` del juego copiados en `codigo/` (tal cual salen de tu partida).
- [ ] Al menos **3 commits en días distintos** (se ve en el historial: la idea es programar un poco cada día, no todo la última noche).
- [ ] Al menos una captura de tu granja en `capturas/`.
- [ ] La sección **Mi entrega** rellenada.

## Pistas

```python
petalos = {}
petalos[(get_pos_x(), get_pos_y())] = measure()
for pos in petalos:
    quick_print(pos, petalos[pos])
```

## Mi entrega

![Mi granja](capturas/granja.png)

**¿Dónde uso el concepto?** (archivo y qué hace esa parte):

**¿Qué me costó más y cómo lo resolví?**

**Una cosa que quiero probar la próxima semana:**
