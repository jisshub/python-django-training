class Table:
    def __init__(self, tblname, tblsize):
        self.tblname = tblname
        self.tblsize = tblsize

    def funcfirst(self):
        self.tblname = 'customer'
        self.tblsize = '20kb'

    @property
    def databaseinfo(self):
        return f"{self.tblname} {self.tblsize}"

    def colinfo(self, col, rows):
        self.columns = col
        self.rows = rows

    @property
    def colinfonew(self):
        return f"Columns: {self.columns} and Rows: {self.rows}"

    def whole(self):
        return f"cols: {self.columns}, rows: {self.rows}, name: {self.tblname}, size: {self.tblsize}"
