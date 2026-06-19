# Biblioteca de contratos semánticos para IA

Lo que se suele decir vs. lo que se debería decir. Organizado por dominio.

---

## 1. Redacción contractual

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Redáctame una cláusula de confidencialidad. | Redacta una cláusula de confidencialidad para un contrato de prestación de servicios entre dos empresas españolas. Duración: 3 años tras la extinción del contrato. Incluye excepciones por mandato legal y por información de dominio público. Tono jurídico formal. No inventes referencias legales: cita solo artículos que existan; si dudas, no cites. Máximo 200 palabras. |
| Hazme un contrato de servicios. | Redacta solo las cláusulas que pueda fundamentar con los datos aportados. Las que requieran datos ausentes (partes, importes, plazos, jurisdicción) se incluyen como plantilla con campos [PENDIENTE], no se rellenan a ciegas. Estructura por cláusulas numeradas. |
| Añade una penalización por retraso. | Redacta una cláusula penal por retraso en la entrega. Importe: el que yo indique como porcentaje diario sobre el precio; si no lo he indicado, déjalo como [PORCENTAJE]. Fija un tope máximo. No inventes la cuantía. |
| Ponme una cláusula de fuerza mayor. | Redacta una cláusula de fuerza mayor con definición, supuestos enunciativos no limitativos, obligación de notificación y efectos sobre los plazos. No incluyas causas que las partes no puedan invocar legalmente. Tono jurídico formal. |
| Que el contrato proteja al proveedor. | Reequilibra el contrato a favor del proveedor en estos puntos concretos: limitación de responsabilidad, condiciones de pago y causas de resolución. Lista cada cambio propuesto con la cláusula afectada y la redacción nueva. No alteres cláusulas fuera de esos tres puntos. |
| Redacta el objeto del contrato. | Redacta la cláusula de objeto usando solo la descripción del servicio que te paso. No amplíes el alcance ni añadas prestaciones no mencionadas. Si la descripción es ambigua, márcalo con [ACLARAR] en lugar de interpretar. |

---

## 2. Revisión y auditoría de documentos

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Revisa este contrato. | Revisa este contrato e identifica: cláusulas abusivas, ausencia de jurisdicción aplicable, plazos sin fecha cierta y obligaciones sin contraprestación clara. Devuelve una tabla con cláusula afectada, riesgo y reformulación propuesta. No reescribas el contrato entero. Marca [INCIERTO] lo que dependa de información que no consta. |
| Mira si hay algo raro. | Audita el documento contra esta lista cerrada de riesgos: indemnizaciones desproporcionadas, renovación automática sin preaviso, cesión sin consentimiento, exclusividad encubierta. Por cada hallazgo: ubicación, cita literal breve y motivo. Lo que no esté en la lista, ignóralo. |
| ¿Está bien este contrato? | No emitas un juicio global. Evalúa punto por punto contra los criterios que te doy y devuelve, por cada uno, conforme / no conforme / no aplica, con justificación de una línea. La validez final corresponde a revisión jurídica humana. |
| Compara estas dos versiones. | Compara las dos versiones y devuelve solo las diferencias materiales: qué cambió, en qué cláusula y a favor de quién. Ignora cambios de formato o redacción que no alteren el sentido. Tabla con cláusula, versión A, versión B, efecto. |
| Detecta los riesgos. | Identifica riesgos solo a partir del texto, sin presuponer cláusulas que no aparecen. Si una protección habitual falta, indícalo como "ausencia detectada", no como afirmación de hecho. Clasifica cada riesgo en alto, medio o bajo con criterio explícito. |
| Dime qué falta. | Compara el documento contra esta checklist de cláusulas mínimas: [lista]. Devuelve solo las que faltan. No propongas cláusulas adicionales fuera de la checklist. |

---

## 3. Contratación pública

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Resume este pliego. | Resume este pliego en máximo 10 puntos. Extrae solo: objeto, presupuesto base de licitación, criterios de adjudicación con su peso, plazo de ejecución y requisitos de solvencia. Si un dato no aparece, escribe "no consta". Cita el apartado del que sale cada punto. No interpretes. |
| Redacta la oferta técnica. | Redacta la oferta técnica ajustándote a los criterios de adjudicación del pliego, sin prometer medios que no consten como disponibles. No infles cifras ni inventes certificaciones. Marca [APORTAR] todo dato que deba rellenar la empresa. |
| Saca los criterios de valoración. | Extrae los criterios de adjudicación tal como figuran en el pliego: denominación exacta, ponderación y fórmula de cálculo si la hay. No reordenes ni reinterpretes. Si una fórmula no se especifica, indícalo. |
| ¿Cumplimos los requisitos? | Contrasta los requisitos de solvencia del pliego con los datos de la empresa que te aporto. Devuelve, por requisito, cumple / no cumple / falta dato. No asumas datos de solvencia que no te haya dado. |
| Mejora nuestra puntuación. | Indica qué apartados de la oferta pueden subir puntuación según los criterios del pliego, citando el criterio concreto y el peso. No propongas acciones que requieran medios o certificaciones que no consten como disponibles. |
| Hazme el resumen ejecutivo de la licitación. | Resumen ejecutivo en máximo 8 líneas: objeto, importe, plazo de presentación, criterios clave y umbral de solvencia. Solo datos del expediente. Lo que falte se marca como "pendiente de verificar en plataforma". |
| Revisa que el pliego sea legal. | No emitas dictamen de legalidad. Señala apartados que podrían entrar en conflicto con la LCSP por motivos concretos (p. ej. criterios desproporcionados, plazos insuficientes) y márcalos para revisión jurídica. No cites artículos que no estés seguro de que existen. |

---

## 4. Aduanas, fiscalidad y contexto Canarias

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Calcula el IGIC. | Aplica el tipo de IGIC que yo indique. No asumas el tipo: si no lo he especificado, pídemelo antes de calcular. Muestra el desglose: base imponible, tipo aplicado e importe resultante. |
| ¿Lleva AIEM esto? | Indica qué información necesitas para determinar la sujeción al AIEM (clasificación arancelaria, origen, naturaleza del producto). No afirmes la sujeción sin esos datos. Si faltan, lístalos en lugar de deducir. |
| Rellena el DUA. | Estructura los campos del DUA con los datos que te aporto. Los campos sin dato quedan como [PENDIENTE], nunca rellenados por defecto. No inventes códigos TARIC ni valores en aduana. |
| Clasifícame este producto en el arancel. | Propón la partida arancelaria más probable con su justificación, pero indícala como propuesta sujeta a confirmación. No la presentes como clasificación definitiva. Señala qué características del producto cambiarían la partida. |
| Explícame el régimen REF. | Explica solo los aspectos del REF relevantes a la operación que describo. No generalices a supuestos que no he planteado. Si un punto depende de normativa que no puedes verificar, márcalo para confirmación. |
| ¿Cuánto pago de impuestos al importar en Canarias? | Lista los conceptos que pueden aplicar (IGIC, AIEM, arancel, tasas) y qué dato necesitas para cuantificar cada uno. No des una cifra total sin esos datos. No confundas el régimen canario con el peninsular. |

---

## 5. Extracción y estructuración de datos

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Saca los datos de este documento. | Extrae solo estos campos: [lista de campos]. Un valor por campo, copiado literal del documento. Los campos no encontrados van como null, nunca inferidos. No añadas campos que no he pedido. |
| Pásame esto a tabla. | Convierte el contenido en una tabla con estas columnas exactas: [columnas]. Una fila por elemento. Celdas sin dato con "—". No resumas ni interpretes el contenido de las celdas. |
| Genérame el JSON. | Devuelve solo JSON válido, sin texto antes ni después y sin bloques de markdown. Esquema: [esquema]. Campos sin dato como null, nunca cadena vacía ni inventados. Valida que el JSON parsea antes de entregarlo. |
| Estructura esta factura. | Extrae: emisor, NIF, fecha, número, base imponible, tipo impositivo, cuota y total. Copia literal. Si un importe no cuadra con el total, no lo corrijas: márcalo como "discrepancia detectada". |
| Normaliza estos datos. | Normaliza solo el formato (fechas a ISO 8601, importes con dos decimales, NIF sin espacios). No alteres valores ni completes huecos. Lista cualquier valor que no se haya podido normalizar. |
| Saca las entidades. | Extrae solo entidades de estos tipos: [personas, empresas, importes, fechas]. Devuelve tipo y valor literal. No clasifiques en tipos nuevos. Lo ambiguo se etiqueta "sin tipo". |

---

## 6. Análisis de datos

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Analiza estos datos. | Responde solo a estas preguntas concretas: [preguntas]. No generes conclusiones de negocio ni recomendaciones. Si una columna está vacía o malformada, indícalo antes de calcular. |
| Saca las conclusiones. | Extrae solo conclusiones que se deriven directamente de las cifras mostradas. No extrapoles tendencias ni proyectes a futuro. Cada conclusión debe poder rastrearse a un dato concreto. |
| ¿Qué tendencia hay? | Describe la variación observada en el periodo de los datos, sin proyectar más allá. No uses la palabra "tendencia" si solo hay dos puntos. Indica el número de observaciones en que se basa cada afirmación. |
| Dame los KPIs. | Calcula solo los KPIs que yo defina con su fórmula explícita. No inventes métricas. Si falta un dato para una fórmula, marca ese KPI como "no calculable" en lugar de estimarlo. |
| ¿Esto es bueno o malo? | No valores. Presenta la cifra junto a su referencia (periodo anterior o umbral que yo defina) y deja la interpretación al lector. Si no hay referencia, indícalo. |
| Predice el próximo trimestre. | No prediga sin método explícito. Si te pido una proyección, indica el método (p. ej. media móvil), sus supuestos y su margen de error. Marca el resultado como estimación, no como dato. |

---

## 7. Código y software

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Dame el código para X. | Código para X en TypeScript. Sin dependencias externas. Tipado estricto, sin `any`. Con manejo de errores. Sin comentarios dentro del código. Si hay que asumir algo no especificado, indícalo fuera del bloque. |
| Explícame qué hace este código. | Explica qué hace en un párrafo. No sugieras mejoras, no reescribas, no comentes el estilo. Si hay un bug evidente, indícalo al final en una línea precedida de "BUG:". |
| Arregla este bug. | Identifica la causa del bug, propón el cambio mínimo que lo corrige y devuelve solo el fragmento modificado. No refactorices el resto. Explica en una línea por qué fallaba. |
| Optimiza esto. | Optimiza solo [rendimiento / legibilidad / memoria], lo que yo indique. No cambies el comportamiento observable. Lista cada cambio con su motivo. Si un cambio implica un trade-off, decláralo. |
| Revisa mi código. | Revisa contra estos criterios: seguridad, manejo de errores y tipado. Por hallazgo: línea, problema y corrección. No comentes preferencias de estilo salvo que afecten a funcionamiento. |
| Hazme los tests. | Escribe tests para los casos que yo enumere más los límites evidentes (vacío, nulo, máximo). No inventes comportamiento esperado: si una expectativa no está definida, márcala como [DEFINIR] en lugar de asumirla. |
| Documéntalo. | Documenta solo la interfaz pública: qué hace cada función, parámetros y retorno. No documentes lógica interna ni añadas ejemplos no verificables. Sin prosa decorativa. |

---

## 8. Comunicación con cliente y email

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Escríbeme un email para el cliente. | Email comunicando [asunto]. Tono directo, sin disculpas excesivas ni justificaciones largas. Máximo 120 palabras. Cierra con una acción o fecha concreta. No prometas nada que no haya autorizado. |
| Comunica el retraso. | Comunica un retraso de [X] días. Sin excusas extensas. Asume el hecho en la primera frase y propón nueva fecha cierta en la segunda. No ofrezcas compensaciones salvo que yo lo indique. Máximo 100 palabras. |
| Responde a esta queja. | Responde reconociendo el problema concreto que plantea el cliente, sin admitir responsabilidades legales ni prometer reembolsos no autorizados. Propón un siguiente paso. Tono sereno, sin tono defensivo. |
| Pídele los datos que faltan. | Solicita solo estos datos: [lista]. Una petición por línea. Sin rodeos ni agradecimientos previos. Indica para qué los necesitas en una frase. |
| Escríbele para cerrar la venta. | Redacta un mensaje de cierre sin presión artificial, sin urgencia inventada y sin descuentos no autorizados. Resume el valor acordado y propón el siguiente paso concreto. |
| Mándale el presupuesto. | Redacta el email de envío de presupuesto. No incluyas cifras que no consten en el documento adjunto. Limítate a presentar, indicar validez si la hay y proponer una llamada. Lo que no sepa, no lo afirme. |

---

## 9. Traducción

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Tradúcelo. | Traduce al [idioma]. Mantén la terminología jurídica sin localizar nombres de leyes españolas (déjalos en español con traducción entre paréntesis la primera vez). No omitas ni resumas ninguna frase. |
| Tradúceme este contrato. | Traducción literal funcional, no libre. Conserva la numeración de cláusulas. Los términos sin equivalente exacto se dejan en origen con nota entre corchetes. No adaptes el contenido legal a otra jurisdicción. |
| Que suene natural en inglés. | Traduce a inglés idiomático manteniendo el significado exacto. No alteres datos, cifras ni nombres. Si una expresión no tiene equivalente natural, prioriza la fidelidad sobre la fluidez y márcalo. |
| Revisa esta traducción. | Compara origen y traducción frase a frase. Señala solo: omisiones, contrasentidos y términos mal traducidos. No reescribas por estilo. Devuelve tabla con frase origen, traducción y corrección. |

---

## 10. Síntesis y resumen

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Hazme un resumen. | Resume en [N] frases. Sin introducción ni cierre. Cada frase contiene un hecho verificable del texto original. No añadas información que no esté en la fuente. |
| Resúmemelo en corto. | Una sola frase con la idea principal, sin matices secundarios. Si el texto tiene varias ideas principales irreductibles, dilo en lugar de elegir una arbitrariamente. |
| Sácame los puntos clave. | Extrae máximo [N] puntos, cada uno una frase, cada uno anclado a una parte concreta del texto. No jerarquices por importancia salvo que lo pida. No añadas conclusiones propias. |
| Hazme un abstract. | Resumen de [N] palabras con esta estructura: contexto, objeto, hallazgo, implicación. Solo contenido presente en el documento. Sin afirmaciones de novedad no respaldadas. |
| Dime de qué va esto. | Describe el tema y el propósito del documento en dos frases. No resumas el contenido completo. No valores la calidad del documento. |

---

## 11. Generación estructurada y formato

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Hazme una tabla. | Tabla con estas columnas exactas: [columnas]. Una fila por elemento. Celdas sin texto narrativo. Las vacías con "—", nunca con suposiciones. |
| Ponlo bonito. | Formato: [markdown / lista / tabla]. Sin emoticonos. Sin negritas decorativas. Encabezados solo donde aporten estructura. Nada de relleno entre secciones. |
| Pásalo a limpio. | Reformatea respetando el contenido íntegro. No corrijas, no resumas, no reordenes. Aplica solo el formato indicado: [formato]. |
| Genérame el esquema. | Devuelve el esquema en [formato]. Solo los campos que pueda fundamentar. Los campos opcionales sin dato no se incluyen, no se rellenan vacíos. Valida la sintaxis antes de entregar. |
| Hazme la plantilla. | Genera una plantilla con campos marcados [ASÍ] para rellenar. No inventes valores de ejemplo dentro de los campos salvo que pida ejemplos, en cuyo caso márcalos como ilustrativos. |

---

## 12. Investigación y fuentes

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Búscame información sobre X. | Busca información sobre X y cita solo fuentes verificables (URL, autor, fecha). No inventes fuentes. Lo que no puedas respaldar con una fuente real, no lo afirmes o márcalo como "sin fuente verificada". |
| Dame las fuentes. | Aporta solo fuentes que existan y que pueda comprobar. Nada de URLs, autores, títulos o fechas fabricados. Si no tienes fuente real para una afirmación, dilo en lugar de rellenar. |
| ¿Esto es verdad? | Indica qué afirmaciones puedes verificar y cuáles no. Por cada una: verificada / no verificable / contradicha, con la fuente. No conviertas ausencia de prueba en confirmación ni en negación. |
| Investiga el mercado. | Recopila datos solo de fuentes citables y distingue dato de estimación. Marca cada cifra con su fuente y su año. Lo que no tenga fuente, no entra. No proyectes tamaños de mercado sin método. |

---

## 13. Contenido, marketing y creatividad

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Sé creativo. | Margen creativo permitido en metáforas y estructura. Prohibido en datos, cifras, nombres propios, citas y referencias. Todo dato concreto procede de la fuente aportada. |
| Dame un titular. | Propón 3 titulares de máximo 10 palabras. Sin clickbait, sin exclamaciones, sin promesas que el cuerpo no cumpla. Cada uno fiel al contenido. |
| Escríbeme un post. | Post de [longitud] sobre [tema], en mi tono habitual. Sin frases motivacionales vacías, sin emoticonos, sin datos inventados. Si necesito un dato que no me has dado, déjalo como [DATO]. |
| Ponme un ejemplo. | Pon un ejemplo realista del sector [X], con cifras plausibles marcadas como ilustrativas. No lo presentes como caso real ni cites empresas existentes sin fuente. |
| Hazlo más atractivo. | Mejora ritmo y claridad sin añadir afirmaciones nuevas, sin superlativos no justificados y sin alterar los datos. Lista qué has cambiado. |
| Adáptalo a mi sector. | Adapta cambiando solo ejemplos y terminología al sector [X]. No alteres la lógica ni las cifras estructurales. Lista los términos sustituidos. |

---

## 14. Clasificación y decisión

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Clasifica esto. | Clasifica cada elemento en una de estas categorías cerradas: [lista]. No crees categorías nuevas. Lo que no encaje, etiquétalo "sin clasificar". Devuelve solo elemento y categoría. |
| ¿Qué opción es mejor? | Compara las opciones contra criterios fijos: [criterios]. No declares ganador. Marca con "n/d" lo que falte. La decisión la toma el lector. |
| Decide por mí. | No decido por ti. Presento las opciones con sus consecuencias y los datos que faltan para decidir. Si quieres una recomendación, dímelo y la doy etiquetada como opinión, separada de los hechos. |
| Dame tu opinión. | Expongo argumentos a favor y en contra con el mismo nivel de detalle. Si pides opinión explícita, la marco como tal y la separo de los hechos. |
| Prioriza estas tareas. | Ordena según el criterio que yo defina (impacto, urgencia, esfuerzo). Si no lo he definido, pídemelo. No mezcles criterios sin avisar. Muestra el criterio aplicado. |

---

## 15. Documentos y presentaciones

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Genérame un informe. | Informe con esta estructura exacta: 1) Objeto, 2) Hallazgos, 3) Riesgos, 4) Acciones. Cada hallazgo remite a la sección de origen. Lo que no fundamentes en el documento, omítelo. |
| Hazme la presentación. | Una idea por diapositiva. Máximo 6 líneas por diapositiva. Nada que no puedas sostener con el material aportado. Marca [DATO?] cualquier cifra que deba confirmar. |
| Escríbelo más corto. | Reduce a la mitad de palabras sin eliminar ningún dato, cifra ni obligación. Recorta solo redundancias y conectores. Mantén la estructura de apartados. |
| Escríbelo más largo. | Amplía desarrollando solo los puntos ya presentes. No añadas hechos, ejemplos ni cifras nuevas. Si un punto no da más de sí, déjalo. |
| Corrige los errores. | Corrige solo ortografía, puntuación y concordancia. No cambies estilo, orden ni vocabulario. Devuelve el texto corregido y una lista al final con cada cambio. |
| Hazme el resumen ejecutivo. | Resumen ejecutivo de [N] líneas: problema, propuesta, coste, riesgo. Solo datos del documento base. Lo que falte, "pendiente de confirmar". Sin lenguaje promocional. |

---

## 16. Control de incertidumbre (transversal)

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Hazlo como el otro. | Replica estructura, tono y formato del documento que adjunto como modelo. Indica explícitamente qué elementos del modelo no aplican a este caso. |
| Ya sabes lo que quiero. | No asumas lo que quiero. Si una instrucción es ambigua, enumera las interpretaciones posibles y pídeme que elija antes de ejecutar. |
| Complétalo tú. | Completa solo con datos presentes en la fuente. Los huecos van como [PENDIENTE]. No rellenes con valores plausibles ni por defecto. |
| Lo necesito ya. | Prioriza exactitud sobre exhaustividad. Entrega la parte verificada y lista aparte lo que queda pendiente de comprobación humana. |
| Que no se note que es de IA. | (Sin objetivo válido.) Ajusta el registro al tono indicado y revisa coherencia. La validez depende de la revisión humana, no de ocultar el origen. |
| Confío en ti. | La confianza no sustituye la verificación. Marco todo lo no fundamentado, separo hecho de inferencia y dejo la decisión final a tu revisión. |

---

## Regla transversal

Todo encargo se cierra con validación humana. La IA no firma, no decide y no es la fuente de verdad: redacta, compara y señala. Lo que no pueda fundamentarse en una fuente aportada se marca como pendiente, no se inventa.