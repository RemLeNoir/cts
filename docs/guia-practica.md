# Guía práctica

## Cómo redactar un contrato semántico temporal

## Paso 1: delimitar la tarea
Responde a tres preguntas:
- qué salida necesitas;
- para quién;
- para qué decisión o uso real.

## Paso 2: escribir el diccionario del encargo
Define solo los términos que, si se dejan abiertos, harán que el modelo improvise.

Ejemplo:
- “claro” = entendible por un lector no especialista;
- “riguroso” = separa hecho, inferencia y opinión;
- “accionable” = cada apartado termina con una decisión o siguiente paso.

## Paso 3: ordenar prioridades
Nunca dejes que todas las exigencias pesen igual.

Ejemplo:
1. precisión;
2. utilidad;
3. tono;
4. estética.

## Paso 4: declarar errores
No digas solo lo que quieres.
Declara también lo que sería una mala salida.

Ejemplo:
- inventar datos;
- ocultar incertidumbre;
- usar lenguaje inflado;
- responder con frases genéricas.

## Paso 5: tratar la incertidumbre
Define qué debe hacer el modelo cuando falte información.

Opciones frecuentes:
- marcar pendiente;
- emitir hipótesis etiquetada;
- pedir validación humana;
- detenerse si el riesgo es alto.

## Paso 6: definir la salida
Especifica:
- formato;
- secciones;
- longitud;
- elementos obligatorios;
- elementos prohibidos.

## Plantilla mínima

```markdown
### Objetivo
...

### Audiencia
...

### Términos definidos
- “...”
- “...”

### Prioridades
1. ...
2. ...

### Errores
- ...
- ...

### Incertidumbre
- ...

### Criterios de salida
- ...
```

## Checklist rápido

- [ ] La tarea está acotada.
- [ ] Los términos vagos están definidos.
- [ ] Las prioridades están ordenadas.
- [ ] Los errores están explicitados.
- [ ] La incertidumbre tiene política.
- [ ] La salida se puede comprobar.
- [ ] Hay al menos un test.

## Qué no hacer

- usar palabras comodín sin definir;
- mezclar tono, formato y criterio de verdad;
- pedir “completo” y “brevísimo” sin jerarquizar;
- pedir naturalidad y luego exigir salida totalmente rígida sin negociar ese conflicto;
- creer que JSON resuelve por sí solo el sentido.
