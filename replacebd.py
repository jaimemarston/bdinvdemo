import sqlite3


#nombretabla='gestionapp_articulo'
#nombretabla='gestionapp_material'
newline_indent = '\n   '
conn = sqlite3.connect("dbinventario.sqlite3")
#cursor      = con.cursor()
#Statement = "UPDATE " + nombretabla + " SET descolor = color "
#Statement = "update gestionapp_dmateriales set codpro = (select gestionapp_material.codigo  from gestionapp_material where gestionapp_material.descripcion = gestionapp_dmateriales.descripcion)"
#Statement = "update gestionapp_dcotizacion set codpro = (select gestionapp_articulo.codigo  from gestionapp_articulo where gestionapp_articulo.descripcion = gestionapp_dcotizacion.descripcion)"
res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
for name in res:
    table_names = name[0]
    if table_names[:11]=='gestionapp_':
       result = conn.execute("PRAGMA table_info('%s')" % table_names).fetchall()
       column_names = result
       Statement = "UPDATE " + table_names + " SET replace(descripcion,'A','K') " 
       cursor.execute(Statement)
       con.commit()

       print (table_names)
       print (column_names)
       

#Statement = "update gestionapp_dcotizacion set imptotal = precio * cantidad "
#Statement = "update gestionapp_dmateriales set imptotal = precio * cantidad "


con.close()
