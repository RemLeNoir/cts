# Biblioteca de contratos semánticos para IA

Lo que se suele decir vs. lo que se debería decir.

---

## 0. Las seis cláusulas de todo contrato semántico

| Cláusula | Qué fija |
|---|---|
| Rol y tono | Quién habla y en qué registro. |
| Alcance | Qué entra y, sobre todo, qué no entra. |
| Criterios de calidad | Qué hace que la salida sea válida. |
| Límites y prohibiciones | Qué no se puede hacer ni inventar. |
| Formato de salida | Estructura exacta esperada. |
| Verificación | Cómo se autocomprueba antes de entregar. |

Cada fila de esta biblioteca instancia una o varias de estas cláusulas.

---

## 1. Redacción contractual

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Redáctame una cláusula de confidencialidad. | Cláusula de confidencialidad para contrato de servicios entre dos empresas españolas. Duración: 3 años tras la extinción. Excepciones por mandato legal y dominio público. Tono jurídico formal. No inventes referencias legales: cita solo artículos que existan; si dudas, no cites. Máximo 200 palabras. |
| Hazme un contrato de servicios. | Redacta solo las cláusulas que pueda fundamentar con los datos aportados. Las que requieran datos ausentes (partes, importes, plazos, jurisdicción) van como plantilla con campos [PENDIENTE]. Cláusulas numeradas. |
| Añade una penalización por retraso. | Cláusula penal por retraso en la entrega. Importe como porcentaje diario sobre el precio; si no lo he indicado, déjalo como [PORCENTAJE]. Fija un tope máximo. No inventes la cuantía. |
| Ponme fuerza mayor. | Cláusula de fuerza mayor con definición, supuestos enunciativos no limitativos, obligación de notificación y efectos sobre plazos. No incluyas causas no invocables legalmente. Tono formal. |
| Que el contrato proteja al proveedor. | Reequilibra a favor del proveedor en tres puntos: limitación de responsabilidad, condiciones de pago y causas de resolución. Lista cada cambio con la cláusula afectada y la redacción nueva. No toques nada fuera de esos tres puntos. |
| Redacta el objeto. | Redacta la cláusula de objeto usando solo la descripción del servicio que te paso. No amplíes el alcance ni añadas prestaciones no mencionadas. Si es ambigua, márcala con [ACLARAR]. |
| Ponme una cláusula de pago. | Cláusula de condiciones de pago: importe, plazo, forma e intereses de demora. Los datos que no consten van como campo a rellenar. No fijes un plazo por defecto ni inventes el tipo de interés. |
| Redacta la resolución del contrato. | Cláusula de resolución con causas tasadas, preaviso y efectos. Distingue resolución por incumplimiento de desistimiento. No incluyas causas que no me hayas confirmado. |
| Hazme una cláusula de propiedad intelectual. | Cláusula de cesión/licencia de PI. Especifica qué se cede, en exclusiva o no, ámbito territorial y temporal. Lo no definido queda como [PENDIENTE]. No presumas cesión total salvo que lo indique. |
| Pon protección de datos. | Cláusula de tratamiento de datos conforme a la relación responsable-encargado que yo indique. No determines roles tú: si no consta quién es responsable y quién encargado, pídelo. No cites artículos del RGPD que no estés seguro de que existen. |
| Redacta el anexo de niveles de servicio. | Anexo de SLA con métricas, umbrales y penalizaciones que yo aporte. Tabla métrica/umbral/medición/penalización. Campos sin dato como [DEFINIR]. No inventes umbrales estándar. |
| Hazme la cláusula de no competencia. | Cláusula de no competencia con objeto, ámbito territorial, duración y, si aplica, compensación. Señala que su validez depende de proporcionalidad y revisión jurídica. No fijes duración por defecto. |

---

## 2. Revisión y auditoría de documentos

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Revisa este contrato. | Identifica: cláusulas abusivas, ausencia de jurisdicción, plazos sin fecha cierta y obligaciones sin contraprestación. Tabla con cláusula afectada, riesgo y reformulación. No reescribas el contrato entero. Marca [INCIERTO] lo que no conste. |
| Mira si hay algo raro. | Audita contra esta lista cerrada: indemnizaciones desproporcionadas, renovación automática sin preaviso, cesión sin consentimiento, exclusividad encubierta. Por hallazgo: ubicación, cita breve y motivo. Lo que no esté en la lista, ignóralo. |
| ¿Está bien este contrato? | No emitas juicio global. Evalúa punto por punto contra los criterios dados: conforme / no conforme / no aplica, con justificación de una línea. La validez final corresponde a revisión jurídica humana. |
| Compara estas dos versiones. | Devuelve solo diferencias materiales: qué cambió, en qué cláusula y a favor de quién. Ignora cambios de formato o redacción que no alteren el sentido. Tabla cláusula/versión A/versión B/efecto. |
| Detecta los riesgos. | Identifica riesgos solo a partir del texto, sin presuponer cláusulas ausentes. Si falta una protección habitual, indícalo como "ausencia detectada". Clasifica alto/medio/bajo con criterio explícito. |
| Dime qué falta. | Compara contra esta checklist de cláusulas mínimas: [lista]. Devuelve solo las que faltan. No propongas cláusulas fuera de la checklist. |
| ¿Es vinculante esto? | No dictamines la validez. Señala qué elementos podrían afectar al carácter vinculante (firma, capacidad, objeto, consentimiento) y márcalos para revisión jurídica. |
| Revisa el anexo técnico. | Contrasta el anexo técnico con el cuerpo del contrato y señala solo contradicciones, duplicidades y referencias cruzadas rotas. No valores la calidad técnica del contenido. |

---

## 3. Contratación pública

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Resume este pliego. | Máximo 10 puntos: objeto, presupuesto base de licitación, criterios de adjudicación con su peso, plazo de ejecución y requisitos de solvencia. Si un dato no aparece, "no consta". Cita el apartado de origen. No interpretes. |
| Redacta la oferta técnica. | Ajústate a los criterios de adjudicación del pliego, sin prometer medios que no consten como disponibles. No infles cifras ni inventes certificaciones. Marca [APORTAR] todo dato que deba rellenar la empresa. |
| Saca los criterios de valoración. | Extrae los criterios tal como figuran: denominación exacta, ponderación y fórmula si la hay. No reordenes ni reinterpretes. Si una fórmula no se especifica, indícalo. |
| ¿Cumplimos los requisitos? | Contrasta los requisitos de solvencia del pliego con los datos de la empresa que aporto: cumple / no cumple / falta dato. No asumas datos de solvencia no facilitados. |
| Mejora nuestra puntuación. | Indica qué apartados pueden subir puntuación según los criterios del pliego, citando criterio y peso. No propongas acciones que requieran medios o certificaciones no disponibles. |
| Redacta el sobre administrativo. | Lista la documentación administrativa exigida por el pliego y su estado con mis datos: aportada / pendiente / no aplica. No declares cumplida documentación que no me conste. |
| Hazme la declaración responsable. | Estructura la declaración responsable según el modelo del pliego. Campos de identificación como [PENDIENTE]. No afirmes el cumplimiento de requisitos sin que yo lo confirme. |
| Calcula la oferta económica óptima. | Aplica la fórmula de valoración económica del pliego con los parámetros que figuran en él. Muestra el cálculo. Si la fórmula no está completa en el texto, no la inventes: indícalo. |
| Redacta una subsanación. | Escrito de subsanación que responda solo al defecto concreto requerido por la mesa, aportando o aclarando lo solicitado. No introduzcas documentación no pedida ni argumentos de fondo nuevos. |
| Prepara la justificación de baja temeraria. | Estructura la justificación de la oferta presuntamente anormal según los conceptos que el órgano requiera. Marca [APORTAR] cada justificante de coste. No inventes cifras de costes. |
| Analiza si recurrir la adjudicación. | Identifica posibles motivos de recurso a partir del expediente (defectos de valoración, criterios mal aplicados, plazos) y márcalos para revisión jurídica. No afirmes la viabilidad del recurso ni cites plazos sin confirmarlos. |
| Revisa que el pliego sea legal. | No dictamines legalidad. Señala apartados potencialmente conflictivos con la LCSP (criterios desproporcionados, plazos insuficientes, solvencia restrictiva) para revisión jurídica. No cites artículos no verificados. |
| Hazme el resumen ejecutivo de la licitación. | Máximo 8 líneas: objeto, importe, plazo de presentación, criterios clave, umbral de solvencia. Solo datos del expediente. Lo que falte, "pendiente de verificar en plataforma". |
| Prepara la documentación de la UTE. | Lista la documentación específica de UTE exigida por el pliego (compromiso, porcentajes, representante). Campos de las empresas como [PENDIENTE]. No fijes porcentajes de participación por defecto. |

---

## 4. Aduanas, fiscalidad y contexto Canarias

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Calcula el IGIC. | Aplica el tipo de IGIC que yo indique. Si no lo he especificado, pídemelo antes de calcular. Desglose: base imponible, tipo aplicado, importe. No asumas el tipo general. |
| ¿Lleva AIEM esto? | Indica qué información necesitas para determinar la sujeción al AIEM (clasificación, origen, naturaleza). No afirmes la sujeción sin esos datos. Si faltan, lístalos. |
| Rellena el DUA. | Estructura los campos del DUA con los datos aportados. Los sin dato quedan [PENDIENTE]. No inventes códigos TARIC ni valor en aduana. |
| Clasifícame este producto en el arancel. | Propón la partida más probable con justificación, marcada como propuesta sujeta a confirmación. Señala qué características cambiarían la partida. No la presentes como definitiva. |
| Explícame el REF. | Explica solo los aspectos del REF relevantes a la operación que describo. No generalices a supuestos no planteados. Lo que dependa de normativa no verificable, márcalo. |
| ¿Cuánto pago al importar en Canarias? | Lista los conceptos que pueden aplicar (IGIC importación, AIEM, arancel, tasas) y qué dato necesitas para cuantificar cada uno. No des total sin esos datos. No confundas régimen canario con peninsular. |
| Calcula el valor en aduana. | Aplica el método de valoración que corresponda con los datos que aporto (precio, transporte, seguro, ajustes). Muestra cada componente. Lo que falte, [PENDIENTE]. No estimes importes de transporte. |
| ¿Aplica origen preferencial? | Indica qué prueba de origen y qué requisitos exigiría el acuerdo aplicable. No afirmes el origen preferencial sin documentación. Marca para verificación qué acuerdo concreto rige. |
| Diferencia IGIC importación de IGIC interior. | Explica solo la diferencia en el caso que describo: hecho imponible, momento de devengo y sujeto pasivo en cada caso. No entres en supuestos que no he planteado. |
| Prepara el despacho de importación. | Lista la documentación del despacho según la operación (factura, packing list, transporte, certificados) y su estado. Campos sin dato como pendientes. No des por presentado lo que no conste. |
| Explícame el régimen de depósito aduanero. | Describe solo las obligaciones del régimen aplicables a mi caso: entrada, permanencia, contabilidad de existencias y ultimación. Lo que dependa de la autorización concreta, márcalo para verificación. |

---

## 5. Redacción administrativa española

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Hazme un recurso. | Estructura el recurso [reposición/alzada] contra el acto que describo: identificación del acto, motivos y petición. Marca [VERIFICAR PLAZO] sin afirmar el plazo. No cites artículos que no estés seguro de que existen. |
| Responde a este requerimiento. | Responde solo a lo requerido por la Administración, aportando o aclarando lo solicitado. No introduzcas información no pedida. Marca [APORTAR] cada documento que deba adjuntar. |
| Redacta unas alegaciones. | Alegaciones frente a la propuesta que adjunto, rebatiendo punto por punto solo los hechos o fundamentos del expediente. No inventes hechos ni jurisprudencia. Lo no acreditable, márcalo. |
| Escribe una solicitud a la Administración. | Solicitud con: identificación del interesado, exposición, petición concreta y órgano destinatario. Datos personales como campos a rellenar. Sin fórmulas de cortesía excesivas. |
| Redacta un escrito de subsanación administrativa. | Responde al defecto concreto señalado en el requerimiento, aportando lo solicitado. No amplíes a otros aspectos del expediente. |
| Hazme un certificado. | Estructura el certificado con los hechos que yo declare como ciertos. No certifiques hechos que no me consten ni añadas afirmaciones no respaldadas. Campos de identificación como [PENDIENTE]. |

---

## 6. Extracción y estructuración de datos

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Saca los datos de este documento. | Extrae solo estos campos: [lista]. Un valor por campo, copiado literal. Los no encontrados como null, nunca inferidos. No añadas campos no pedidos. |
| Pásame esto a tabla. | Tabla con estas columnas exactas: [columnas]. Una fila por elemento. Celdas sin dato con "—". No resumas ni interpretes el contenido de las celdas. |
| Genérame el JSON. | Solo JSON válido, sin texto ni markdown alrededor. Esquema: [esquema]. Campos sin dato como null, nunca vacíos ni inventados. Verifica que parsea antes de entregar. |
| Estructura esta factura. | Extrae: emisor, NIF, fecha, número, base, tipo, cuota, total. Literal. Si un importe no cuadra con el total, no lo corrijas: marca "discrepancia detectada". |
| Normaliza estos datos. | Normaliza solo el formato (fechas ISO 8601, importes con dos decimales, NIF sin espacios). No alteres valores ni completes huecos. Lista lo no normalizable. |
| Saca las entidades. | Extrae solo estos tipos: [personas, empresas, importes, fechas]. Tipo y valor literal. No crees tipos nuevos. Lo ambiguo, "sin tipo". |
| Cruza estos dos ficheros. | Cruza por la clave [campo]. Devuelve coincidencias, solo-en-A y solo-en-B en tres bloques. No fusiones registros con clave dudosa: márcalos como conflicto. |
| Deduplica esta lista. | Marca duplicados por [criterio exacto]. No fusiones registros con datos divergentes; lístalos como posibles duplicados para revisión. No elimines nada por tu cuenta. |

---

## 7. Análisis de datos

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Analiza estos datos. | Responde solo a estas preguntas: [preguntas]. Sin conclusiones de negocio ni recomendaciones. Si una columna está vacía o malformada, indícalo antes de calcular. |
| Saca las conclusiones. | Solo conclusiones derivadas directamente de las cifras mostradas. No extrapoles ni proyectes. Cada conclusión rastreable a un dato concreto. |
| ¿Qué tendencia hay? | Describe la variación observada en el periodo de los datos, sin proyectar. No uses "tendencia" con solo dos puntos. Indica el número de observaciones de cada afirmación. |
| Dame los KPIs. | Calcula solo los KPIs que defina con su fórmula explícita. No inventes métricas. Si falta un dato, marca ese KPI "no calculable" en lugar de estimarlo. |
| ¿Esto es bueno o malo? | No valores. Presenta la cifra junto a su referencia (periodo anterior o umbral que yo defina). Si no hay referencia, indícalo. La interpretación es del lector. |
| Predice el próximo trimestre. | No proyectes sin método explícito. Indica método (p. ej. media móvil), supuestos y margen de error. Marca el resultado como estimación, no dato. |
| Encuentra correlaciones. | Reporta solo asociaciones presentes en los datos, con su medida. No afirmes causalidad. Señala el tamaño de muestra y los casos atípicos que la condicionan. |
| Detecta anomalías. | Define qué cuenta como anomalía con un criterio explícito (umbral o desviación). Lista solo lo que cumpla ese criterio. No marques puntos por intuición. |

---

## 8. Código y software

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Dame el código para X. | Código para X en TypeScript. Sin dependencias externas. Tipado estricto, sin `any`. Con manejo de errores. Sin comentarios dentro. Si hay que asumir algo, indícalo fuera del bloque. |
| Explícame qué hace este código. | Explica qué hace en un párrafo. No sugieras mejoras, no reescribas, no comentes el estilo. Si hay bug evidente, una línea al final con "BUG:". |
| Arregla este bug. | Identifica la causa, propón el cambio mínimo que lo corrige y devuelve solo el fragmento modificado. No refactorices el resto. Explica en una línea por qué fallaba. |
| Optimiza esto. | Optimiza solo [rendimiento/legibilidad/memoria], lo que indique. No cambies el comportamiento observable. Lista cada cambio con su motivo. Declara cualquier trade-off. |
| Revisa mi código. | Revisa contra: seguridad, manejo de errores y tipado. Por hallazgo: línea, problema, corrección. No comentes estilo salvo que afecte al funcionamiento. |
| Hazme los tests. | Tests para los casos que enumere más los límites evidentes (vacío, nulo, máximo). No inventes comportamiento esperado: lo no definido va como [DEFINIR]. |
| Documéntalo. | Documenta solo la interfaz pública: qué hace cada función, parámetros y retorno. No documentes lógica interna ni añadas ejemplos no verificables. Sin prosa decorativa. |
| Refactoriza este módulo. | Refactoriza preservando el comportamiento observable y la API pública. Cambios estructurales solo. Sin cambios funcionales. Si detectas un bug, no lo arregles: anótalo aparte. |
| Migra esto a [tecnología]. | Migra preservando el comportamiento. Marca con [REVISAR] toda equivalencia que no sea exacta entre origen y destino. No introduzcas mejoras aprovechando la migración. |
| Genérame datos de prueba. | Genera datos sintéticos con el esquema [esquema] y marca el conjunto como ficticio. Sin datos personales reales, sin NIF/IBAN válidos reales. Casos límite incluidos. |
| Escríbeme el prompt para el agente. | Define para el agente: objetivo, herramientas permitidas, herramientas prohibidas, formato de salida y condición de parada. Incluye qué hacer ante datos faltantes (preguntar, no inventar). |
| Diséñame el esquema de base de datos. | Esquema con las entidades y relaciones que describo. Tipos y restricciones explícitos. Lo no especificado como [DEFINIR], sin claves ni índices por defecto sin justificar. No asumas cardinalidades. |

---

## 9. Specs y diseño de producto

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Hazme una spec. | Define el producto completo y 100% operativo de una vez. Sin fases, sin MVP, sin roadmap, sin "iterar después". Si falta información para definir algo por completo, márcalo como [DEFINIR], no lo difieras a una fase. |
| Empecemos por un MVP. | No plantees MVP. Especifica el alcance completo. Si el alcance es demasiado grande para una entrega, dilo explícitamente en lugar de recortarlo a un mínimo viable. |
| Hazme el roadmap. | No produzcas roadmap por fases. Entrega el conjunto completo de requisitos como una sola definición operativa. La priorización temporal la decido yo aparte, no la asumas. |
| Define los requisitos. | Lista requisitos funcionales y no funcionales completos. Cada uno verificable. Lo ambiguo como [ACLARAR]. No inventes requisitos no mencionados ni los marques como "opcionales" para diferirlos. |
| Diséñame la arquitectura. | Arquitectura completa para el alcance definido sobre el stack que uso (TypeScript, Next.js, Prisma, PostgreSQL, VPS+PM2+Nginx). No propongas Vercel ni servicios que no haya mencionado. Justifica cada componente. |
| Estima el esfuerzo. | No estimes plazos sin método. Descompón en tareas concretas. Si pido estimación, marca cada cifra como aproximada con sus supuestos. No conviertas la estimación en compromiso. |

---

## 10. Comunicación con cliente y email

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Escríbeme un email para el cliente. | Email sobre [asunto]. Tono directo, sin disculpas excesivas ni justificaciones largas. Máximo 120 palabras. Cierra con acción o fecha concreta. No prometas nada no autorizado. |
| Comunica el retraso. | Comunica un retraso de [X] días. Sin excusas extensas. Asume el hecho en la primera frase y propón nueva fecha cierta en la segunda. Sin compensaciones salvo que lo indique. Máximo 100 palabras. |
| Responde a esta queja. | Reconoce el problema concreto sin admitir responsabilidades legales ni prometer reembolsos no autorizados. Propón un siguiente paso. Tono sereno, sin defensividad. |
| Pídele los datos que faltan. | Solicita solo estos datos: [lista]. Una petición por línea. Sin rodeos ni agradecimientos previos. Indica para qué los necesitas en una frase. |
| Escríbele para cerrar la venta. | Mensaje de cierre sin presión artificial, sin urgencia inventada y sin descuentos no autorizados. Resume el valor acordado y propón el siguiente paso. |
| Mándale el presupuesto. | Email de envío de presupuesto. No incluyas cifras que no consten en el adjunto. Presenta, indica validez si la hay y propón llamada. Lo que no sepa, no lo afirme. |
| Negocia el precio. | Redacta la respuesta a la negociación manteniendo las condiciones que yo fije como innegociables. No concedas descuentos no autorizados. Marca [DECIDIR] cualquier contrapartida. |
| Escribe el seguimiento. | Seguimiento breve de [asunto] sin reproches por la falta de respuesta. Recuerda el punto pendiente y propón fecha. Máximo 80 palabras. |

---

## 11. Traducción

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Tradúcelo. | Traduce al [idioma]. Mantén la terminología jurídica sin localizar nombres de leyes españolas (déjalos en origen con traducción entre paréntesis la primera vez). No omitas ni resumas ninguna frase. |
| Tradúceme este contrato. | Traducción literal funcional, no libre. Conserva la numeración de cláusulas. Términos sin equivalente exacto en origen con nota entre corchetes. No adaptes el contenido legal a otra jurisdicción. |
| Que suene natural. | Traduce a [idioma] idiomático manteniendo el significado exacto. No alteres datos, cifras ni nombres. Si una expresión no tiene equivalente natural, prioriza fidelidad sobre fluidez y márcalo. |
| Revisa esta traducción. | Compara origen y traducción frase a frase. Señala solo omisiones, contrasentidos y términos mal traducidos. No reescribas por estilo. Tabla frase origen/traducción/corrección. |
| Localiza este texto. | Adapta solo formatos locales (fechas, moneda, unidades) al mercado [X]. No cambies el contenido sustantivo. Lista cada adaptación. |

---

## 12. Síntesis y resumen

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Hazme un resumen. | Resume en [N] frases. Sin introducción ni cierre. Cada frase un hecho verificable del original. No añadas información ausente en la fuente. |
| Resúmemelo en corto. | Una sola frase con la idea principal, sin matices secundarios. Si hay varias ideas principales irreductibles, dilo en lugar de elegir una. |
| Sácame los puntos clave. | Máximo [N] puntos, cada uno una frase anclada a una parte concreta del texto. No jerarquices salvo que lo pida. Sin conclusiones propias. |
| Hazme un abstract. | Resumen de [N] palabras: contexto, objeto, hallazgo, implicación. Solo contenido del documento. Sin afirmaciones de novedad no respaldadas. |
| Dime de qué va esto. | Tema y propósito del documento en dos frases. No resumas el contenido completo ni valores la calidad. |
| Resume esta reunión. | Extrae solo: decisiones tomadas, tareas asignadas con responsable y puntos abiertos. No inventes acuerdos no explícitos. Lo dudoso como "a confirmar". |

---

## 13. Generación estructurada y formato

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Hazme una tabla. | Tabla con estas columnas exactas: [columnas]. Una fila por elemento. Sin texto narrativo en celdas. Vacías con "—", nunca con suposiciones. |
| Ponlo bonito. | Formato: [markdown/lista/tabla]. Sin emoticonos. Sin negritas decorativas. Encabezados solo donde aporten estructura. Sin relleno entre secciones. |
| Pásalo a limpio. | Reformatea respetando el contenido íntegro. No corrijas, no resumas, no reordenes. Aplica solo el formato indicado: [formato]. |
| Genérame el esquema. | Esquema en [formato]. Solo campos fundamentables. Los opcionales sin dato no se incluyen. Valida la sintaxis antes de entregar. |
| Hazme la plantilla. | Plantilla con campos marcados [ASÍ]. No metas valores de ejemplo dentro de los campos salvo que pida ejemplos, en cuyo caso márcalos como ilustrativos. |
| Conviértelo a CSV. | CSV con separador [coma/punto y coma] y cabecera. Escapa los campos con el separador. No alteres valores. Indica la codificación. |

---

## 14. Investigación y verificación

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Búscame información sobre X. | Busca sobre X y cita solo fuentes verificables (URL, autor, fecha). No inventes fuentes. Lo no respaldable con fuente real, no lo afirmes o márcalo "sin fuente verificada". |
| Dame las fuentes. | Solo fuentes que existan y pueda comprobar. Nada de URLs, autores, títulos o fechas fabricados. Si no tienes fuente real, dilo en lugar de rellenar. |
| ¿Esto es verdad? | Indica qué afirmaciones puedes verificar y cuáles no: verificada / no verificable / contradicha, con fuente. No conviertas ausencia de prueba en confirmación ni en negación. |
| Investiga el mercado. | Solo fuentes citables. Distingue dato de estimación. Cada cifra con su fuente y año. Lo sin fuente, fuera. No proyectes tamaños de mercado sin método. |
| Verifica esta afirmación. | Busca evidencia a favor y en contra con el mismo esfuerzo. Reporta ambas. No selecciones solo lo que confirma. Concluye solo lo que las fuentes sostengan. |
| Hazme un perfil de esta empresa. | Solo datos de fuentes públicas citables. No infieras facturación, plantilla ni propiedad sin fuente. Lo no encontrado, "no consta". Sin juicios reputacionales. |

---

## 15. Contenido, marketing y creatividad

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Sé creativo. | Margen creativo en metáforas y estructura. Prohibido en datos, cifras, nombres propios, citas y referencias. Todo dato concreto procede de la fuente aportada. |
| Dame un titular. | 3 titulares de máximo 10 palabras. Sin clickbait, sin exclamaciones, sin promesas que el cuerpo no cumpla. Cada uno fiel al contenido. |
| Escríbeme un post. | Post de [longitud] sobre [tema], en mi tono habitual. Sin frases motivacionales vacías, sin emoticonos, sin datos inventados. Lo que no me hayas dado, como [DATO]. |
| Ponme un ejemplo. | Ejemplo realista del sector [X], con cifras plausibles marcadas como ilustrativas. No lo presentes como caso real ni cites empresas existentes sin fuente. |
| Hazlo más atractivo. | Mejora ritmo y claridad sin añadir afirmaciones nuevas, sin superlativos no justificados y sin alterar datos. Lista qué has cambiado. |
| Adáptalo a mi sector. | Adapta cambiando solo ejemplos y terminología al sector [X]. No alteres la lógica ni las cifras estructurales. Lista los términos sustituidos. |
| Escríbeme la descripción del producto. | Describe solo características que me consten como ciertas. Sin superlativos no demostrables ("el mejor", "líder") salvo que aporte la prueba. Lo no confirmado, [VERIFICAR]. |

---

## 16. Formación y material didáctico

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Hazme el temario. | Temario completo del curso sobre [tema] para [perfil], con objetivos de aprendizaje por bloque. No marques bloques como opcionales para diferirlos. Lo que dependa de duración, como [AJUSTAR]. |
| Explícalo fácil. | Explica al nivel de [perfil] sin perder exactitud. Si simplificar introduce un error, no simplifiques: marca el matiz. No uses analogías que distorsionen el concepto. |
| Hazme ejercicios. | Ejercicios sobre [tema] con su solución. Cada uno con un único objetivo de aprendizaje. No inventes datos que parezcan reales. Marca el nivel de dificultad. |
| Prepara la evaluación. | Preguntas alineadas una a una con los objetivos de aprendizaje. Cada pregunta con respuesta correcta justificada. Sin preguntas ambiguas ni con dos respuestas válidas. |
| Hazme las diapositivas del curso. | Una idea por diapositiva, máximo 6 líneas. Solo contenido del temario aportado. Marca [EJEMPLO] donde haga falta un caso que deba aportar yo. |

---

## 17. Control de incertidumbre (transversal)

| Lo que se suele decir | Lo que se debería decir |
|---|---|
| Hazlo como el otro. | Replica estructura, tono y formato del documento que adjunto como modelo. Indica qué elementos del modelo no aplican a este caso. |
| Ya sabes lo que quiero. | No asumas lo que quiero. Si una instrucción es ambigua, enumera las interpretaciones posibles y pídeme que elija antes de ejecutar. |
| Complétalo tú. | Completa solo con datos presentes en la fuente. Los huecos van como [PENDIENTE]. No rellenes con valores plausibles ni por defecto. |
| Lo necesito ya. | Prioriza exactitud sobre exhaustividad. Entrega la parte verificada y lista aparte lo pendiente de comprobación humana. |
| Confío en ti. | La confianza no sustituye la verificación. Marco todo lo no fundamentado, separo hecho de inferencia y dejo la decisión final a tu revisión. |
| Tú decide. | Presento las opciones con sus consecuencias y los datos que faltan. Si quieres recomendación explícita, la doy etiquetada como opinión, separada de los hechos. |

---

## 18. Antipatrones sin versión válida

Instrucciones cuyo objetivo en sí es inválido. No tienen columna "buena": se rechazan o se reconducen.

| Lo que se suele decir | Por qué no tiene versión válida |
|---|---|
| Que no se note que es de IA. | El objetivo es ocultar el origen, no mejorar la salida. Se reconduce a tono y calidad; el origen no se disimula. |
| Invéntate los datos que falten. | Pide fabricación explícita. Se sustituye por marcar huecos como pendientes. |
| Cita algo que suene oficial. | Pide apariencia de autoridad sin fundamento. Se sustituye por citar solo fuentes reales o no citar. |
| Dame una cifra aunque sea aproximada, lo que sea. | Pide un número sin base. Se sustituye por indicar qué dato falta para calcularlo. |
| Asegúrame que esto es legal. | Pide una garantía que la IA no puede dar. Se reconduce a señalar puntos para revisión jurídica. |
| Convénceme de que tengo razón. | Pide confirmación sesgada. Se sustituye por exponer argumentos a favor y en contra por igual. |

---

## Regla transversal

Todo encargo se cierra con validación humana. La IA no firma, no decide y no es la fuente de verdad: redacta, compara y señala. Lo que no pueda fundamentarse en una fuente aportada se marca como pendiente, no se inventa.