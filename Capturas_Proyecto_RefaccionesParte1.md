![PORTADA](img/Portada_del_proyecto.jpg)

# Anexo de Evidencias y Pruebas del Agente - Refacciones del Norte

---

### Figura 1: Configuración Inicial del Agente en Azure AI Foundry
![Configuración Inicial](./img/1.png)
* **Resumen:** Estado base del agente `RefaccionesNorte-AI` utilizando el modelo `gpt-5.6-luna` e instrucciones del sistema, previo a la integración de la herramienta de búsqueda documental (*sin RAG*).

---

### Figura 2: Agente Configurado con Herramienta de Búsqueda Vectorial (RAG)
![Agente con RAG](./img/2.png)
* **Resumen:** Vinculación exitosa de la herramienta **Búsqueda de archivos** (*File Search*) con el índice vectorial cargado, habilitando al agente para consultar la base de conocimiento oficial de la empresa.

---

### Figura 3: Confirmación de Documentos en la Base de Conocimiento
![Base de Conocimiento](./img/3.png)
* **Resumen:** Pestaña de gestión de conocimiento mostrando la subida y procesamiento completado (`Completado`) de los archivos institucionales (`PROYECTO_Refacciones_Del_NORTE.docx`).

---

### Figura 4: Prueba de Seguridad — Resistencia a Prompt Injection
![Prueba de Seguridad](./img/4.png)
* **Resumen:** Intento de manipulación mediante presión por urgencia (*"el cliente está esperando en mostrador"*). El agente mantiene los controles de seguridad, bloquea la acción y exige la autorización explícita de Alejandro González Rivera.

---

### Figura 5: Consulta Operativa de Procedimientos de Trabajo
![Consulta Operativa](./img/5.png)
* **Resumen:** Respuesta estructurada sobre el procedimiento interno para recepción física de mercancía y validación de facturas, basada de forma estricta en la documentación cargada.

---

### Figura 6: Validación Favorable de Cotización de Rutina
![Cotización de Rutina](./img/6.png)
* **Resumen:** Atención a una solicitud habitual (bujías y filtro para Nissan Versa). El agente solicita los datos específicos faltantes (año, motor, proveedor) sin inventar precios ni existencias.

---

### Figura 7: Caso Crítico — Alerta Preventiva por Pedido Atípico
![Alerta Preventiva](./img/7.png)
* **Resumen:** Solicitud de orden de compra por 100 sensores de oxígeno Bosch ($191,400 MXN). El agente activa automáticamente la **ALERTA PREVENTIVA**, detiene la transacción y solicita aprobación por escrito de la Dirección General.

---

### Figura 8: Despliegue y Prueba en Aplicación Web Publicada
![Aplicación Web](./img/8.png)
* **Resumen:** Verificación del agente en la interfaz web independiente desplegada desde Azure, confirmando que la lógica de negocio y las alertas preventivas (pedido masivo) se ejecutan correctamente de cara al usuario final.