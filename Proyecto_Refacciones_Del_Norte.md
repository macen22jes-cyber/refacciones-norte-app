# Propuesta Estratégica de Transformación Digital e Inteligencia Artificial en Refacciones del Norte
![PORTADA](img/Portada_del_proyecto.jpg)

* **Responsable del proyecto:** Jesús Adrián González Macén
* **Correo electrónico:** macen.22jes@gmail.com
* **Correo electrónico del Lab:** macen.22jes-ia@labmx.ai
* **Ubicación:** Heroica Nogales, Sonora
* **Curso:** Fundamentos de IA con Tecnologías Microsoft


---


## 1. Contexto de la Empresa y Planteamiento del Problema

### 1.1 Antecedentes de Refacciones del Norte
Refacciones del Norte es una empresa familiar ubicada en Heroica Nogales, Sonora, con aproximadamente 30 años de trayectoria comercial y una plantilla de 13 colaboradores. La empresa se dedica a la venta y distribución de refacciones y autopartes automotrices en la región.

Tras el fallecimiento del fundador y antiguo director, la dirección fue asumida por Alejandro González Rivera, quien impulsó un plan de modernización tecnológica para optimizar los procesos operativos y mantener la competitividad de la empresa sin perder la cercanía con los clientes.

### 1.2 Evento Crítico: Error de Captura en Pedido
En marzo de 2026, la falta de controles y validaciones automatizadas en el proceso de compras provocó un incidente crítico de captura durante la elaboración de un pedido de reabastecimiento enviado por correo electrónico al proveedor Gates.

Por un error tipográfico en la orden de compra manual, se procesó la solicitud de **100 sensores de oxígeno Bosch Universal** (clave BOS-0258017025), lo que generó una factura por un monto total de **$191,400 MXN**. 

### 1.3 Impacto Operativo y Financiero
* **Inmovilización de Capital:** Se comprometió una cantidad elevada de flujo de efectivo en inventario de baja rotación inmediata.
* **Falta de Validación Preventiva:** El incidente dejó en evidencia la ausencia de un filtro inteligente que detecte anomalías en las cantidades antes del envío final de los pedidos.
* **Necesidad de Solución:** Se determinó la urgencia de implementar un sistema basado en Inteligencia Artificial que actúe como un mecanismo de doble verificación para prevenir errores humanos en las órdenes de compra.

---




## 2. Solución Tecnológica y Prototipo en Azure

Para dar solución al problema de validación de pedidos y evitar errores como el de los sensores de oxígeno, se diseñó e implementó un prototipo funcional utilizando los servicios en la nube de Microsoft Azure.

### 2.1 Arquitectura del Prototipo
* **Plataforma base:** Azure AI Foundry / Azure AI Studio, aprovechando los modelos de lenguaje de Azure OpenAI para procesar las consultas de manera segura y controlada.
* **Base de Conocimiento:** Se integraron los manuales de procedimientos internos, catálogos estandarizados y políticas de compra de Refacciones del Norte mediante modelos de recuperación de información (RAG).
* **Interfaz de Acceso:** Un agente conversacional inteligente configurado para actuar como asistente de validación preventiva en el proceso de compras.

### 2.2 Enlace Web del Prototipo Funcional
Cumpliendo con los requisitos obligatorios de la evaluación, el prototipo cuenta con un entorno web accesible para que cualquier usuario o evaluador pueda interactuar con el asistente tal como lo haría un usuario real

* **Enlace web del prototipo:** https://ai.azure.com/nextgen/agents/bff04f3a-3739-4615-a3af-7aaee11702d7/preview?version=3

---





## 3. Evaluación de los 6 Principios de IA Responsable

La implementación del asistente en Azure AI Foundry para Refacciones del Norte fue diseñada bajo los principios fundamentales de la Inteligencia Artificial Responsable de Microsoft, asegurando una adopción ética, segura y alineada con los objetivos de la empresa.

### 3.1 Equidad (Fairness)
El asistente trata de manera neutral y sin sesgos todas las solicitudes de información y validación de inventario planteadas por el personal operativo, sin importar el turno, el rol o el nivel de experiencia del usuario dentro de la empresa.

### 3.2 Confiabilidad y Seguridad (Reliability and Safety)
El sistema cuenta con reglas y parámetros de seguridad para detectar anomalías operativas (como el ingreso de un volumen inusual de refacciones o montos desproporcionados). En lugar de autorizar órdenes atípicas de forma automática —previniendo incidentes como el error de los 100 sensores de oxígeno—, el asistente genera una alerta inmediata e interrumpe el flujo hasta recibir una confirmación explícita.

### 3.3 Privacidad y Seguridad (Privacy and Security)
Toda la información comercial, catálogos de productos y registros de clientes procesados en Azure AI Foundry se mantienen protegidos dentro del entorno privado en la nube de la empresa. Los accesos están segmentados individualmente mediante cuentas corporativas, prohibiendo el uso de credenciales compartidas.

### 3.4 Inclusión (Inclusiveness)
El prototipo ofrece una interfaz conversacional accesible en lenguaje natural y sencillo, facilitando que colaboradores con diferentes niveles de habilidades digitales o antecedentes técnicos puedan consultar datos y validar pedidos de manera intuitiva.

### 3.5 Transparencia (Transparency)
Los usuarios están plenamente informados de que están interactuando con un asistente virtual impulsado por IA. La herramienta muestra con claridad las razones de sus sugerencias o alertas de validación, permitiendo auditar la lógica detrás de cada recomendación.

### 3.6 Rendición de Cuentas (Accountability)
La regla de oro de la solución: el asistente actúa únicamente como un mecanismo de consulta, asistencia y doble verificación preventiva. La responsabilidad final de la toma de decisiones, emisión y aprobación de órdenes de compra recae exclusivamente en el personal humano autorizado (Dirección General y Gerencia de Compras).

---




## 4. Personajes del Caso y Criterios de Éxito

En una estructura organizacional compacta como la de Refacciones del Norte (13 colaboradores), los roles asumen responsabilidades operativas clave. A continuación, se detallan los actores involucrados, sus principales preocupaciones y las métricas de éxito definidas para el proyecto.

### 4.1 Personajes Clave y sus Preocupaciones

* **Dirección General (Alejandro González Rivera):**
  * *Preocupación principal:* Proteger el flujo de caja y la estabilidad financiera de la empresa, evitando la inmovilización no planificada de capital por compras masivas erróneas (como el incidente de los $191,400 MXN en sensores de oxígeno).
  * *Expectativa:* Contar con un control preventivo automático sin romper la agilidad de atención y venta que distingue a la refaccionaria.

* **Área de Compras y Mostrador (Manuel Ríos / Equipo Comercial):**
  * *Preocupación principal:* Cometer errores manuales de captura durante la elaboración acelerada de órdenes de compra al surtir faltantes en el catálogo.
  * *Expectativa:* Disponer de una herramienta ágil que alerte oportunamente si un pedido excede los promedios históricos o si hay un error tipográfico en las cantidades antes de ser enviado al proveedor.

* **Administración y Almacén:**
  * *Preocupación principal:* Recibir mercancía no solicitada o sobreinventariar repuestos de baja rotación que saturen el espacio de almacenamiento.
  * *Expectativa:* Mantener coherencia estricta entre las órdenes aprobadas, el espacio físico disponible y el registro contable.

### 4.2 Criterios de Éxito del Proyecto

El éxito de la solución implementada en Azure AI Foundry para Refacciones del Norte se evaluará mediante las siguientes métricas:

1. **Eliminación del 100% de errores de captura crítica:** Garantizar cero incidentes de compras atípicas no autorizadas mediante la alerta preventiva del asistente.
2. **Reducción del tiempo de validación:** Disminuir en un 50% el tiempo que le toma al personal verificar la coherencia de las órdenes de compra frente a las políticas del catálogo.
3. **Adopción por el personal:** Lograr que los colaboradores del área operativa adopten el uso de la interfaz web conversacional como paso estándar en la generación de pedidos.

---




## 5. Conclusiones y Plan de Entrega

### 5.1 Conclusiones del Proyecto
La implementación del prototipo de Inteligencia Artificial en Azure AI Foundry para Refacciones del Norte demuestra cómo una pequeña empresa familiar de 13 colaboradores puede adoptar tecnologías de vanguardia para resolver problemas operativos concretos. 

Al establecer un Asistente de Validación y Control de Compras, la empresa logra blindar su flujo de caja contra errores de captura humana (como el incidente de los $191,400 MXN), garantizando un crecimiento tecnológico seguro, ético y supervisado siempre por el talento humano.
