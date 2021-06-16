# **Progra Aplicada Parcial**

crear un website y un restapi

## **el website debe tener (5 pts)**
- la pagina home con links a register y login
- la pagina register
    1. recaptcha v2 checkbox
    2. debe encriptar la password
    3. en la bd se debe guardar password y salt
    4. verificar que el usuario sea unico
- la pagina login
    1. sin recaptcha, no recaptcha
    2. debe usar la user,password y salt para verificar que sean correctos
    3. pasar a la pagina dashboard
- la pagina dashboard debe tener la funcionalidad web para enviar los datos
de la restapi, en forma de formularios

## **el restapi (4 pts)**
- debe tener un endpoint segun la tabla
- debe tener los metodos:
    1. get - obtener un registro de la tabla por id
    2. post - obtener todos los registros de la tabla
    3. put - insert
    4. patch - update
    5. delete - delete
- la restapi debe tener `app.run(debug=True, port=23512)`: esto para que tenga
un puerto distinto al del website y que puedan tener los dos levantados al mismo
tiempo.

    |aplicacion                               |url                      |
    |:---------------------------------------:|:-----------------------:|
    |website: app.run(debug=True)             |`http://127.0.0.1:5000/` |
    |restapi: app.run(debug=True, port=23512) |`http://localhost:23512/`|


# **instrucciones para las bases de datos (1 pts)**

## sakila
---
- en `workbench` ir a `administration`
- luego ir a `data import/restore`
- click en la opcion `import from self-contained file`
- colocar la ruta del archivo `sakila-schema.sql`
- click en el boton `start import`
- hacer lo mismo para el archivo `sakila-data.sql`

## world
---
- en `workbench` ir a `administration`
- luego ir a `data import/restore`
- click en la opcion `import from self-contained file`
- colocar la ruta del archivo `world.sql`
- click en el boton `start import`

## tabla user
---
- sakila o world schemas deben estar como `default`(osea en negrita)
- click en boton de `crear un nuevo archivo sql (create new sql file)`
- colocar alli este codigo:
```sql
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) NOT NULL,
  `user_email` varchar(50) NOT NULL,
  `password` varchar(60) NOT NULL,
  `salt` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
);
```