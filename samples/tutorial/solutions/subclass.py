#------------------------------------------------------------------------------
# subclass.py (Section 9.2)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Copyright 2017, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

import cx_Oracle

class MyConnection(cx_Oracle.Connection):

    def __init__(self):
        print("Connecting to database")
        return super(MyConnection, self).__init__("pythonhol", "welcome", "localhost/orclpdb")

    def cursor(self):
        return MyCursor(self)

class MyCursor(cx_Oracle.Cursor):

   def execute(self, statement, args):
       print("Executing:", statement)
       print("Arguments:")
       for argIndex, arg in enumerate(args):
           print("  Bind", argIndex + 1, "has value", repr(arg))
           return super(MyCursor, self).execute(statement, args)

   def fetchone(self):
       print("Fetchone()")
       return super(MyCursor, self).fetchone()

con = MyConnection()
cur = con.cursor()

cur.execute("select count(*) from emp where deptno = :bv", (10,))
count, = cur.fetchone()
print("Number of rows:", count)
