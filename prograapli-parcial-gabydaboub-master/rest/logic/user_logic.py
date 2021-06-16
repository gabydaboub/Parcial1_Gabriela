from core.pyba_logic import PybaLogic


class UserLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getUserById(self, id):
        database = self.createDatabaseObj()
        sql = f"select * from User where id={id};"
        result = database.executeQuery(sql)
        return result

    def insertUser(self, User):
        database = self.createDatabaseObj()
        sql = (
            f"INSERT INTO `sakila`.`User`"
            + f"(`id`,`nombre`,`contacto_email`,`ingresos`,`egresos`) "
            + f"VALUES(0, '{User['nombre']}', '{User['contactoEmail']}', "
            + f"{User['ingresos']}, {User['egresos']});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateUser(self, id, User):
        database = self.createDatabaseObj()
        sql = (
            f"UPDATE `sakila`.`User` "
            + f"SET `nombre` = '{User['nombre']}', `contacto_email` = '{User['contactoEmail']}', "
            + f"`ingresos` = {User['ingresos']}, `egresos` = {User['egresos']} "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteUser(self, id):
        database = self.createDatabaseObj()
        sql = f"delete from User where id={id};"
        rows = database.executeNonQueryRows(sql)
        return rows
