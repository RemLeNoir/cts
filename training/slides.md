---
marp: true
paginate: true
theme: default
---

# Contratos semánticos temporales
Semántica aplicada para trabajar con IA

---

## Problema

Las personas hablan con contexto compartido.
Los modelos responden con probabilidad.
Entre ambas cosas aparece la ambigüedad operativa.

---

## Idea central

Un contrato semántico temporal define:
- significado operativo;
- prioridades;
- errores;
- incertidumbre;
- criterio de salida.

---

## No es

- una ontología universal;
- una receta mágica de prompts;
- una capa decorativa.

---

## Sí es

- una especificación pequeña;
- versionable;
- enseñable;
- evaluable.

---

## Cinco bloques

1. Diccionario del encargo
2. Jerarquía de prioridades
3. Definición de error
4. Tratamiento de incertidumbre
5. Criterios de salida

---

## Ejemplo

“Hazlo profesional”

mejor que:

“Usa tono sobrio, directo y verificable; evita lenguaje promocional.”

---

## Flujo

encargo → contrato → test → salida → evaluación → iteración

---

## Dominios sensibles

En salud y legal:
- no diagnóstico;
- no consejo definitivo;
- revisión humana obligatoria.

---

## Qué medimos

- cobertura de términos;
- cumplimiento de prioridades;
- errores prohibidos;
- manejo de incertidumbre;
- utilidad real.

---

## Cierre

Si tú no defines el significado operativo,
lo definirá el modelo por promedio.
