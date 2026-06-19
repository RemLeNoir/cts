# Guía teórica

## Definición operativa

Llamamos **contrato semántico temporal** a un documento breve y versionable que fija,
para un encargo concreto, el significado operativo de términos sensibles o ambiguos y
las reglas de interpretación que un modelo debe seguir.

## Por qué hace falta

Las instrucciones humanas suelen apoyarse en contexto compartido. Los modelos no
comparten mundo; predicen texto. Por eso, expresiones como “hazlo claro”, “sé neutral”
o “que suene profesional” suelen producir resultados plausibles pero no necesariamente
alineados con la intención de quien encarga la tarea.

## Antecedentes

### Semántica
Se ocupa del significado codificado y relativamente estable de las expresiones.

### Pragmática
Se ocupa del sentido dependiente del contexto, la intención, la situación y la relación
entre interlocutores.

### Actos de habla
Una frase no solo describe; también puede prometer, pedir, advertir, ordenar o excluir.

### Implicatura
Parte de lo comunicado no está en lo dicho literalmente, sino en lo que el contexto
permite inferir.

## Relación con prompt engineering

Un prompt pide algo.
Un contrato semántico temporal define **cómo debe entenderse** lo que se pide.

### Prompt sin contrato
> Hazlo profesional, claro y breve.

### Prompt con contrato
> “Profesional” = sobrio, verificable y no comercial.
> “Claro” = entendible por perfiles no técnicos sin perder precisión.
> “Breve” = máximo 180 palabras.
> Si claridad y brevedad chocan, gana claridad.
> Es error usar clichés o promesas no demostradas.

## Qué añade frente al prompting clásico

- diccionario del encargo;
- jerarquía de prioridades;
- definición de error;
- tratamiento explícito de incertidumbre;
- criterio de salida verificable.

## Límites

- No elimina del todo la variabilidad del modelo.
- No sustituye conocimiento experto del dominio.
- Puede rigidizar en exceso si el contrato es demasiado estrecho.
- Un contrato mal definido puede formalizar un mal criterio.

## Riesgos

### Riesgo de falsa precisión
Definir mucho no equivale a entender mejor.

### Riesgo de sobrecarga
Si el contrato tiene 5 páginas, deja de ser operativo.

### Riesgo político o institucional
Un contrato puede fijar como neutral un marco que no lo es.

### Riesgo en dominios sensibles
En salud, legal, empleo o educación, el contrato debe incluir revisión humana, límites
de uso y manejo explícito de incertidumbre.

## Regla de oro

El contrato tiene que reducir ambigüedad sin matar la tarea.
