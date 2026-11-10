# Reto 5 · Calabazas gigantes

Semana 5 · voluntario · unos 15-20 minutos al día

## Meta en el juego

Las calabazas que crecen juntas en un cuadrado se unen en una **calabaza gigante**, que da mucho más. Pero algunas mueren (`Entities.Dead_Pumpkin`) y hay que replantarlas.

- Llena toda tu granja de calabazas y consigue que se una en **una sola calabaza gigante** antes de cosechar.

## Concepto de Think Python

**`while` con condición**: repetir *hasta que* algo se cumpla, usando una variable contador que se actualiza en cada vuelta (los bucles `while` de Think Python).

## Requisitos

- [ ] Un `while` cuya condición **no** es `True` (por ejemplo `while pendientes > 0:`).
- [ ] Una variable que cuenta cuántas calabazas faltan.
- [ ] La captura muestra la calabaza gigante entera.
- [ ] Los `.py` del juego copiados en `codigo/` (tal cual salen de tu partida).
- [ ] Al menos **3 commits en días distintos** (se ve en el historial: la idea es programar un poco cada día, no todo la última noche).
- [ ] Al menos una captura de tu granja en `capturas/`.
- [ ] La sección **Mi entrega** rellenada.

## Pistas

Una función que recorre la granja, replanta las muertas y cuenta las que faltan:

```python
def contar_pendientes():
    pendientes = 0
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_entity_type() == Entities.Dead_Pumpkin:
                plant(Entities.Pumpkin)
                pendientes += 1
            move(North)
        move(East)
    return pendientes
```

Falta algo: ¿y las que siguen vivas pero aún no han crecido? (`can_harvest()`).

## Mi entrega

![Mi granja](capturas/granja.png)

**¿Dónde uso el concepto?** (archivo y qué hace esa parte):

**¿Qué me costó más y cómo lo resolví?**

**Una cosa que quiero probar la próxima semana:**
