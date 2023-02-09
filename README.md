# Tarea 1 física estadística
## Juan Daniel Castrellón Botero - 201729285

Este programa simula un caminante aleatorio en una dimensión. La longitud de cada paso corresponde a 1mm. El programa permite correr varias veces el caminante aleatorio con el fin de obtener una gráfica. Para correr el programa, es necesario descargar las dependencias del mismo, para ello se corre el comando

```
pip install -r requirements.txt
```
Una vex se instalan las dependencias, se puede correr el programa con el comando

```
python3 main.py
```

Una vez adentro, se encuentra un menú con las siguientes opciones

1. Run random walk with N steps
2. Run many times random walk
3. Run many times the random walk with many N
4. Exit

Para poder seleccionar una opción, poner el número que se desea. 

1) Corre un único caminante aleatorio con N pasos, el parámetro N se introduce por el usuario. Al final, se obtiene la posición final del caminante
2) Corre muchas veces un caminante aleatorio, los parámetros de N, y el número de veces que se corre son introducidas por el usuario. El resultado final es una imagen en la carpeta *histograms*, el nombre también será un input del usuario. Asimismo, se imprime en consola las medias obtenidas y esperadas, con sus varianzas.
3) Corre, para varios N, num_run veces el caminante aleatorio. Esta función recibe el mínimo N, el máximo N, el tamaño del paso de N, y el número de veces que se corre cada vez. El resultado es una carpeta dentro de *histograms*, el nombre será introducido por el usuario, donde se hará un histograma por cada N que se pruebe. Asimismo, se imprime en consola una tabla con los valores esperados de varianza y media, y los valores obtenidos de ambas magnitudes por cada número de pasos.
