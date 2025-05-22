# Reto-04
Se utilizan clases para representar herencia, composición, encapsulamiento y polimorfismo, las respectivas clases tienen sus setters, getters y debida implementación.

## Explicación de cada parte del código: 
### `Point`
Clase base que representa un punto en el plano cartesiano con coordenadas `x` y `y`. Contiene métodos para:
Obtener y modificar coordenadas.
Calcular distancia entre dos puntos.

### `Line`
Representa un segmento de línea entre dos puntos. Calcula y almacena su longitud automáticamente. Métodos:
- Obtener y modificar los puntos de inicio y fin.
- Obtener la longitud del segmento.

### `Shape`
Clase que representa una figura geométrica en general. Guarda:
- Si la figura es regular o no.
- Lista de vértices (`Point`), lados (`Line`) y ángulos internos.

En ella se puede: 
- Calcular perímetro.
- Calcular suma de ángulos internos (puede ser sobrescrito).

## Figuras Derivadas de `Shape`

### `Rectangle`
Hereda de `Shape`, representa un rectángulo. Calcula:
- Área (`base × altura`)
- Perímetro (`2(base + altura)`)
- Longitud de la diagonal.

### `Square`
Hereda de `Rectangle`. Representa un cuadrado, donde todos los lados son iguales.
- Calcula área (`lado²`), perímetro (`4 × lado`) y conserva los métodos del rectángulo.

### `Triangle`
Clase base para todos los tipos de triángulos. Almacena:
- Lados (3)
- Ángulos internos (3)

Implementa:
- Cálculo de área usando la fórmula de Herón.
- Perímetro y suma de ángulos.
- Clasificación del triángulo según sus ángulos: agudo, obtuso o rectángulo.

###
