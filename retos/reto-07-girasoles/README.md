# Reto 7 · Girasoles

Semana 7 · voluntario · unos 15-20 minutos al día

## Meta en el juego

Los girasoles dan **energía** (Power). Si cosechas el que tiene **más pétalos** y hay al menos 10 girasoles, la energía se multiplica por 8. `measure()` te dice cuántos pétalos tiene el girasol de debajo.

- Planta girasoles y consigue el bonus ×8 **10 veces seguidas**.

## Concepto de Think Python

**Recorrer una lista para encontrar el máximo**, a mano, sin `max()` (Think Python, cap. 9 *Lists*).

## Requisitos

- [ ] Guardas en una lista los pétalos de cada girasol (y su posición).
- [ ] Una función que recorre la lista y devuelve el mayor (o su posición en la lista).
- [ ] Tras cosechar, replantas y actualizas la lista.
- [ ] Los `.py` del juego copiados en `codigo/` (tal cual salen de tu partida).
- [ ] Al menos **3 commits en días distintos** (se ve en el historial: la idea es programar un poco cada día, no todo la última noche).
- [ ] Al menos una captura de tu granja en `capturas/`.
- [ ] La sección **Mi entrega** rellenada.

## Pistas

```python
def indice_del_mayor(numeros):
    mejor = 0
    for i in range(len(numeros)):
        if numeros[i] > numeros[mejor]:
            mejor = i
    return mejor

quick_print(indice_del_mayor([7, 12, 9]))
```

## Mi entrega

![Mi granja](capturas/granja.png)

**¿Dónde uso el concepto?** (archivo y qué hace esa parte):

**¿Qué me costó más y cómo lo resolví?**

**Una cosa que quiero probar la próxima semana:**
