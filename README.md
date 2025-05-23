# Reto-04
## Ejercicio en Clase:
Se utilizan clases para representar herencia, composición, encapsulamiento y polimorfismo, las respectivas clases tienen sus setters, getters y debida implementación.

## Explicación de cada parte del código: 
### `Point`
Clase base que representa un punto en el plano cartesiano con coordenadas `x` y `y`. Contiene métodos para:
- Obtener y modificar coordenadas.
- Calcular distancia entre dos puntos.

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

### `Tipos de Triangulos`

### `Isoceles`
Hereda de `Triangle`. 
- Implementa su propia fórmula para calcular el área a partir del lado repetido y la base.

### `Equilateral`
Hereda de `Triangle`. 
- Ángulos fijos en 60°.
- Cálculo del área a través de su altura: `altura = (√3 / 2) * lado`.

### `Scalene`
Hereda de `Triangle`. 
- Usa la fórmula de Herón para el cálculo del área.

### `TriRectangle`
Hereda de `Triangle`.
- Cálculo del área: `(cateto1 × cateto2) / 2`.
- Nos da la hipotenusa automáticamente.

Nota: se valida si los valores asignados para los lados y los ángulos de las figuras tienen valores con sentido (No se permite el ingreso de lados o ángulos negativos)

### Fuentes:
Área del triángulo isóceles: 
- https://www.youtube.com/watch?v=ZdP8TQVI7OQ
  
Deducción de la fórmula de Heron:
- https://www.youtube.com/watch?v=6c_VZQhIwCk
  
Área del triángulo equilátero con base a la altura del mismo: 
- https://www.universoformulas.com/matematicas/geometria/area-triangulo-equilatero/#:~:text=%C2%BFC%C3%B3mo%20se%20obtiene%3F,base%20por%20la%20altura%3F).


## Modificación de Restaurante:
