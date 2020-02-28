# API universidad

## Objetivo

Esta aplicación web permite mediante la URL acceder a la información almacenda en un archivo CSV.

Los datos son mostrados en formato JSON

## Acciones

* get - Obtiene todos los registros
* # http://localhost:8080/alumnos?action=get&token=1234
* put - Inserta un nuevo registro
* # http://localhost:8080/alumnos?action=insert&token=1234&matricula=171502&nombre=Emma&primer_apellido=romero&segundo_apellido=Sosa&carrera=TIC
* delele - Borra un registro
* search - Busca un registro
* # http://localhost:8080/alumnos?action=buscar&token=1234&matricula=1715013
* update - Actualiza un registro
* # http://localhost:8080/alumnos?action=actualizar&token=1234&matricula=17101&nombre=Fatima&primer_apellido=Perez&segundo_apellido=Cruz&carrera=TIC