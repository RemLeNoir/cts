# Guía de contribución

Gracias por contribuir.

## Qué esperamos

Este repositorio acepta contribuciones en cinco frentes:

- mejora teórica y bibliográfica;
- mejora de plantillas;
- nuevos casos de uso;
- mejora de tests y scripts;
- materiales formativos.

## Reglas básicas

1. Todo cambio práctico debe hacer explícito su contrato semántico.
2. Todo ejemplo nuevo debe incluir:
   - `README.md` con prompt y salida esperada;
   - `test_case.json`;
   - términos ambiguos definidos;
   - errores prohibidos;
   - tratamiento de incertidumbre.
3. No se aceptan ejemplos que normalicen invenciones o “relleno”.
4. En salud y legal, el ejemplo debe exigir revisión humana.
5. Si añades bibliografía, prioriza:
   - fuentes primarias;
   - textos en español;
   - documentación oficial.

## Estilo de redacción

- Español claro.
- Frases concretas.
- Evita jerga inflada.
- Si una palabra como “profesional”, “claro” o “neutral” es importante, defínela.

## Flujo mínimo de PR

1. Crea tu rama.
2. Realiza cambios.
3. Ejecuta:
   ```bash
   python scripts/run_example_tests.py
   pytest
   ```
4. Abre PR usando la plantilla.
5. Explica:
   - qué cambias;
   - qué contrato añades o alteras;
   - qué riesgo semántico reduces.

## Convenciones

### Nombres de carpetas
- minúsculas;
- guiones para separar palabras.

### Archivos JSON/YAML
- claves descriptivas;
- valores explícitos;
- nada de campos vacíos si pueden evitarse.

## Checklist antes de enviar

- [ ] El cambio es trazable.
- [ ] El contrato es explícito.
- [ ] Los tests pasan.
- [ ] No introduces términos vagos sin definir.
- [ ] La documentación acompaña al cambio.

## Preguntas frecuentes

### ¿Puedo proponer una variante del concepto?
Sí. Siempre que expliques qué problema resuelve mejor y cómo se evaluaría.

### ¿Puedo subir ejemplos empresariales reales?
Sí, si están anonimizados y no exponen datos sensibles.

### ¿Puedo añadir un caso polémico?
Sí, pero debe explicitar sus límites, riesgos y criterios de revisión humana.
