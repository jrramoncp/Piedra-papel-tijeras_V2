# Piedra, Papel o Tijeras

## Descripción

Este es un simple juego de "Piedra, Papel o Tijeras" implementado en Python. El juego enfrenta al jugador contra el ordenador en una serie de rondas. El objetivo es ganar la mayoría de las 5 rondas. 

El programa sigue las reglas clásicas:
- Piedra gana a Tijeras
- Tijeras ganan a Papel
- Papel gana a Piedra

## Cómo Funciona

1. **Inicio del Juego**: El juego comienza con un mensaje de bienvenida que indica que el mejor de 5 rondas ganará.
2. **Rondas**: En cada ronda, el jugador elige entre Piedra, Papel o Tijeras introduciendo un número (1 para Piedra, 2 para Papel, 3 para Tijeras).
3. **Elección del Ordenador**: El ordenador elige aleatoriamente entre Piedra, Papel o Tijeras.
4. **Determinación del Ganador**: Se compara la elección del jugador con la del ordenador para determinar el ganador de la ronda.
5. **Marcador**: El juego lleva un marcador que muestra las victorias del jugador y del ordenador.
6. **Fin del Juego**: El juego termina después de 5 rondas. Se muestra un mensaje final indicando si el jugador ganó o perdió.

## Cómo Ejecutar

Para ejecutar el juego, sigue estos pasos:

1. Asegúrate de tener Python 3 instalado en tu sistema.
2. Guarda el código en un archivo llamado `piedra_papel_tijeras.py`.
3. Abre una terminal o línea de comandos.
4. Navega hasta el directorio donde guardaste el archivo.
5. Ejecuta el archivo con el siguiente comando:

   ```bash
   python piedra_papel_tijeras.py

# Ejemplo de uso

Jugemos a Piedra, papel o tijeras. El mejor de 5 gana!
Escribe: 1.Piedra | 2.Papel | 3.Tijeras
1
Ordenador: Tijeras
El jugador gana la ronda
MARCADOR
Jugador 1
Ordenador 0
Escribe: 1.Piedra | 2.Papel | 3.Tijeras
2
Ordenador: Piedra
El ordenador gana la ronda
MARCADOR
Jugador 1
Ordenador 1
...
¡Enhorabuena! Has ganado la partida

# Contribuir

Si deseas contribuir al proyecto, siéntete libre de enviar un pull request con mejoras o correciones