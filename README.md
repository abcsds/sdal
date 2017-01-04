# SDAL
## Spanish Dictionary of Affect in Language
Current SDAL version: 1.2 - Sep 24, 2015

SDAL is a dictionary of 2500 words that have been scored on three affective dimentions:

 - Pleasantness (pleasant / neutral / displeasant)
 - Activation (active / neutral / pasive)
 - Imaginability (easy to imagine / neutral / hard to imagine)

The dictionary as well as it's evaluation are described in detail in the next work:

Agustín Gravano & Matías Dell' Amerlina Ríos, “[Spanish DAL: A Spanish Dictionary of Affect in Language](http://digital.bl.fcen.uba.ar/Download/TechnicalReport/TechnicalReport_00001.pdf)”, Reporte Técnico, Departamento de Computación, FCEyN-UBA, Febrero 2014.

## Usage

Every word contains the following fields:

- obj: weather word is noun, verb, or adjective
- pleasure: mean pleasantness
- activation: mean activation
- imagination: mean imagery
- p_sdev: pleasantness standard deviation
- a_sdev: activation standard deviation
- i_sdev: imagery standard deviation

_ATTENTION_:
Contrary to the original study on http://habla.dc.uba.ar/gravano/sdal, all values are in a scale from -1 to 1 for it's use in affective analysis in microblogs.

## License
SDAL is licensed under a
Creative Commons Attribution-ShareAlike 3.0 Unported License.
See LICENSE.

# Español

## Spanish DAL: Diccionario de afecto en el lenguaje

SDAL es un léxico de 2500 palabras, las cuales han sido anotadas manualmente respecto de tres dimensiones afectivas:

 - agrado (agradable / neutra / desagradable)
 - activación (activa / neutra / pasiva)
 - imaginabilidad (fácil de imaginar / neutra / difícil de imaginar)

Tanto el léxico como su evaluación están descriptas en detalle en el siguiente trabajo:

 Agustín Gravano & Matías Dell' Amerlina Ríos, “[Spanish DAL: A Spanish Dictionary of Affect in Language](http://digital.bl.fcen.uba.ar/Download/TechnicalReport/TechnicalReport_00001.pdf)”, Reporte Técnico, Departamento de Computación, FCEyN-UBA, Febrero 2014.

## Uso

Cada palabra en éste diccionario contiene los siguientes campos:

- obj: Nombre, adjetivo, o verbo
- pleasure: media_agrado
- activation: media_activacion
- imagination: media_imaginabilidad
- p_sdev: stdev_agrado
- a_sdev: stdev_activacion
- i_sdev: stdev_imaginabilidad

_ATTENTION_:
Contrario al estudio original http://habla.dc.uba.ar/gravano/sdal, todos los valores aquí se encuentran en una escala de -1 a 1 para su uso en el análisis de sentimientos en microblogs.

## Licencia
SDAL puede descargarse y usarse en forma libre y gratuita, bajo la Creative Commons Attribution 3.0 Unported License.
Vease LICENSE.txt.
