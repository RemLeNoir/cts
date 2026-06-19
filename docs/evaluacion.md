# Evaluación

## Qué se evalúa

Un contrato semántico temporal no se evalúa solo por “si suena bien”.
Se evalúa por cumplimiento observable.

## Capas de evaluación

### Estructural
- ¿el contrato tiene todos los campos?
- ¿el JSON/YAML valida contra esquema?

### Semántica
- ¿los términos críticos están definidos?
- ¿las prioridades resuelven conflictos reales?
- ¿los errores cubren fallos frecuentes?

### Comportamiento
- ¿la salida respeta orden, límites y prohibiciones?
- ¿gestiona incertidumbre como se pidió?

### Utilidad
- ¿sirve para la decisión real?
- ¿reduce rondas de corrección?

## Métricas sugeridas

| Métrica | Definición | Escala |
|---|---|---|
| Cobertura de términos | términos ambiguos definidos / términos ambiguos detectados | 0-1 |
| Cumplimiento de prioridades | reglas priorizadas respetadas / reglas priorizadas totales | 0-1 |
| Tasa de errores prohibidos | errores detectados / respuestas evaluadas | 0-1 |
| Manejo de incertidumbre | incertidumbres bien marcadas / incertidumbres detectadas | 0-1 |
| Cumplimiento de formato | validaciones de salida superadas / validaciones totales | 0-1 |
| Utilidad práctica | valoración humana de uso real | 1-5 |

## Protocolo mínimo

1. redactar contrato;
2. crear 3-10 casos de prueba;
3. fijar salida esperada;
4. ejecutar tests;
5. revisar fallos;
6. iterar.

## Qué mirar en una auditoría

- términos vagos sin definir;
- conflicto entre prioridades;
- ausencia de política de incertidumbre;
- sobrecontratación semántica;
- contradicciones entre plantilla y test.
