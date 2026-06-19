from __future__ import annotations

from typing import Any

DOMAIN_SECTIONS = {
    "corporativo": {
        "Decisión": "Propongo un piloto acotado de 6 semanas con dos equipos y criterio de éxito documentado.",
        "Beneficio": "Reduce correcciones por ambigüedad y deja trazables prioridades, errores y límites.",
        "Riesgo": "Si el contrato se vuelve demasiado largo, perderá operatividad y adopción.",
        "Siguiente paso": "Validar una plantilla común y medir rondas de revisión antes y después."
    },
    "ux-producto": {
        "Usuario": "Persona que entra por primera vez, no conoce la función y necesita orientación inmediata.",
        "Fricción": "No entiende qué puede hacer ni por qué la pantalla está vacía.",
        "Copy final": "Todavía no hay resultados. Ajusta los filtros o crea tu primer elemento.",
        "Criterio de éxito": "La pantalla se entiende en menos de 5 segundos y orienta la acción."
    },
    "periodismo": {
        "Titular": "La redacción adopta contratos semánticos para reducir ambigüedad en usos de IA.",
        "Entradilla": "El cambio busca fijar criterios de claridad, atribución y manejo de incertidumbre.",
        "Contexto": "La medida aparece tras detectar diferencias entre respuestas plausibles y respuestas verificables.",
        "Límites": "El sistema no sustituye contraste de fuentes ni edición humana."
    },
    "investigacion-academica": {
        "Pregunta": "Cómo mejorar la reproducibilidad de instrucciones dadas a modelos de lenguaje.",
        "Hallazgos": "La explicitación de criterios y tests mejora comparabilidad y revisión.",
        "Lagunas": "Faltan métricas estables para medir calidad semántica en tareas abiertas.",
        "Siguiente paso": "Crear corpus anotado de contratos y salidas evaluadas por expertos."
    },
    "salud": {
        "Información general": "El texto debe informar sin diagnosticar ni sustituir valoración clínica.",
        "Señales de alerta": "Si hay empeoramiento, dolor intenso o síntomas persistentes, consulta a un profesional.",
        "Límite": "Esta salida es orientativa y requiere revisión humana antes de uso asistencial.",
        "Siguiente paso": "Adaptar la redacción a comprensión lectora de pacientes."
    },
    "legal": {
        "Supuesto": "Se solicita un resumen inicial de cláusulas y dudas interpretativas.",
        "Norma aplicable": "Debe indicarse la base normativa o contractual relevante si está disponible.",
        "Riesgo": "Presentar la salida como consejo definitivo sería incorrecto.",
        "Revisión humana": "La salida requiere validación por profesional jurídico antes de uso externo."
    }
}

def generate_output(test_case: dict[str, Any]) -> str:
    domain = test_case["dominio"]
    expected = test_case["expected_output"]
    order = expected.get("priority_order", [])
    sections = DOMAIN_SECTIONS[domain]

    lines: list[str] = []
    for section_name in order:
        title = section_name.capitalize() if section_name.capitalize() in sections else section_name
        content = sections.get(title, f"Contenido para {title}.")
        lines.append(f"## {title}\n{content}\n")

    if not lines:
        for title, content in sections.items():
            lines.append(f"## {title}\n{content}\n")

    output = "\n".join(lines).strip()
    max_words = expected.get("max_words", 9999)

    words = output.split()
    if len(words) > max_words:
        output = " ".join(words[:max_words])

    return output

if __name__ == "__main__":
    import json
    import sys
    from pathlib import Path

    path = Path(sys.argv[1])
    test_case = json.loads(path.read_text(encoding="utf-8"))
    print(generate_output(test_case))
