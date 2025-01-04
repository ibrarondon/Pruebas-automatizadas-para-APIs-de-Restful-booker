# Pruebas automatizadas para APIs de Restful-booker
Restful-booker es un sitio para practicar testing de APIs. Se trata en un sitio de reservaciones en el que desarrollé pruebas automatizadas para verificar el funcionamiento de las APIs.

Apidoc: https://restful-booker.herokuapp.com/apidoc/index.html
### Descripción:
- Se crearon pruebas funcionales autónomas para probar el status del servidor, creación de token, creación, modificación búsqueda y eliminación de reservaciones.
- En las pruebas de búsqueda se consideró crear una reservación que coincida con los parámetros de búsqueda para asegurar que existan estos datos al momento de ejecutarse.
- En las pruebas se consideró la optimización por pares de prueba para reducir los casos de estudio, pero también se consideraron elementos críticos individuales a probar.
- En las pruebas se consideraron casos de pruebas positivos y negativos.
- Luego de cada creación de reserva se procedió a eliminar la reservación para evitar acumulación de datos de prueba en la base de datos que interfirieran con las pruebas subsiguientes.

### Requisitos:
- Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
- Para instalar los paquetes usa los comandos pip pytest y pip request.
- Antes de ejecutar las pruebas asegurarse de tener las configuraciones de pytest adecuadas.

### Herramientas utilizadas:
- Pycharm
- Postman
- Jira

### Análisis de resultados y conclusiones

Probé las APIs createToken, GetBookinIDs, GetBooking, CreateBooking, UpdateBooking, PartialUpdateBooking, DeleteBooking y HealthCheck a través de casos de pruebas automatizadas. Al ejecutar las pruebas encontré que se permite crear token, crear reservaciones, eliminarlas y modificarlas perfectamente. También encontré errores relacionados con la búsqueda de reservaciones por fechas, especialmente del checkin, causando que al realizar las búsquedas se muestre una lista equivocada de reservaciones. Se debe corregir la búsqueda de reservaciones por checkin, checkout y las distintas combinaciones posibles con los parámetros name y lastname para lograr un óptimo funcionamiento de las APIs. 

[Reporte de bugs en JIRA para APIs de Restful-books](https://drive.google.com/file/d/1H_bDyn6-bHc7f3rHPYClaTBFOBiXVTD7/view?usp=sharing) 

*Desarrollado por: Ibrahim Rondón - c13 QA Engineer, TripleTen*
