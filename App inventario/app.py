import mysql.connector
import pandas as pd

conexion = mysql.connector.connect(
    host = "localhost",
    user = "miguelfnco",
    password= "Miguel_421",
    database = "inventario"
)

cursor = conexion.cursor()

#QUERIES DE MOBIL
sql_blend = """
INSERT INTO MOBIL_BLEND(VISCOSIDAD, PRESENTACION, PRECIO, STOCK)
VALUES (%s,%s,%s,%s)
"""
sql_multigrado = """
INSERT INTO MOBIL_MULTIGRADO(VISCOSIDAD, PRESENTACION, PRECIO, STOCK)
VALUES (%s,%s,%s,%s)
"""
sql_trc = """
INSERT INTO MOBIL_TRCPRO(VISCOSIDAD, PRESENTACION, PRECIO, STOCK)
VALUES (%s,%s,%s,%s)
"""
sql_monogrados = """
INSERT INTO MOBIL_MONOGRADOS(VISCOSIDAD, PRESENTACION, PRECIO, STOCK)
VALUES (%s,%s,%s,%s)
"""
sql_full = """
INSERT INTO MOBIL_FULL(VISCOSIDAD, PRESENTACION, PRECIO, STOCK)
VALUES (%s,%s,%s,%s)
"""
sql_mobil1 = """
INSERT INTO MOBIL_1(VISCOSIDAD, PRESENTACION, PRECIO, STOCK)
VALUES (%s,%s,%s,%s)
"""
sql_delvac = """
INSERT INTO MOBIL_DELVAC(VISCOSIDAD, PRESENTACION, PRECIO, STOCK)
VALUES (%s,%s,%s,%s)
"""

#QUERIES DEL CASTROL
sql_edge = """
INSERT INTO CASTROL_EDGE(VISCOSIDAD, PRESENTACION, PRECIO, STOCK)
VALUES (%s,%s,%s,%s)
"""
sql_gtxMin = """
INSERT INTO CASTROL_MINERAL(VISCOSIDAD, PRESENTACION, PRECIO, STOCK)
VALUES (%s,%s,%s,%s)
"""
sql_gtxFull = """
INSERT INTO CASTROL_FULL(VISCOSIDAD, PRESENTACION, PRECIO, STOCK)
VALUES (%s,%s,%s,%s)
"""

#QUERIES DE ROSHFRAN
sql_roshfran = """
INSERT INTO ROSHFRAN(VISCOSIDAD, PRESENTACION, PRECIO, STOCK_EN_PIEZAS)
VALUES (%s,%s,%s,%s)
"""

#QUERIES DE SEKURIT
sql_sekurit_cajas = """
INSERT INTO SEKURIT_CAJAS(VISCOSIDAD, PRESENTACION, DESCRIPCION, PRECIO, STOCK)
VALUES (%s,%s,%s,%s,%s)
"""
sql_sekurit_cubetas = """
INSERT INTO SEKURIT_CUBETAS(VISCOSIDAD, PRESENTACION, DESCRIPCION, PRECIO, STOCK)
VALUES (%s,%s,%s,%s,%s)
"""
sql_sekurit_grasas = """
INSERT INTO SEKURIT_GRASAS(COLOR,TIPO, PRESENTACION,PRECIO, STOCK)
VALUES (%s,%s,%s,%s,%s)
"""
sql_sekurit_quimicos = """
INSERT INTO SEKURIT_QUIMICOS(PRODUCTO, PRECIO, STOCK)
VALUES (%s,%s,%s)
"""

#QUERY BUJIAS
sql_bujias = """
INSERT INTO BUJIAS(CODIGO, CAJAS, PIEZAS, PRECIO)
VALUES (%s,%s,%s,%s)
"""

#QUERY CUBREVOLANTES
sql_cubrevolantes = """
INSERT INTO CUBREVOLANTES(TIPO, PRECIO, STOCK)
VALUES (%s,%s,%s)
"""

#QUERY TAPETES
sql_tapetes = """
INSERT INTO TAPETES(DESCRIPCION, COLOR, PRECIO, STOCK)
VALUES (%s,%s,%s,%s)
"""

#QUERY BARDHAL
sql_bardahl = """
INSERT INTO BARDHAL(PRESENTACION, VISCOSIDAD, PRECIO, STOCK)
VALUES (%s,%s,%s,%s)
"""

#QUERY LIMPIABRISAS
sql_parabrisas = """
INSERT INTO PARABRISAS(PRESENTACION, MARCA, PRECIO, STOCK)
VALUES (%s,%s,%s,%s)
"""

#QUERY FILTROS
sql_filtros = """
INSERT INTO FILTROS(CODIGO, TIPO, PRECIO, STOCK)
VALUES (%s,%s,%s,%s)
"""

#DATOS DEL MOBIL
datos_blend = [
    ("5/20", "litro", 73, 11),
    ("5/30", "litro", 73, 88),
    ("10/30", "litro", 73, 96),
    ("10/40", "litro", 73, 116),
    ("5/20", "garrafa", 312, 6),
    ("5/30", "garrafa", 312, 102),
    ("10/30", "garrafa", 312, 114),
    ("10/40", "garrafa", 312, 92)
]
datos_multigrado = [
    ("15/40", "litro", 96, 16),
    ("20/50", "litro", 96,  18),
    ("15/40", "garrafa", 475, 17),
    ("20/50", "garrafa", 475, 5),
    ("25/60", "litro", 96, 4),
    ("25/60", "garrafa", 470, 15)
]
datos_trcpro = [
    ("15/40", "litro", 109, 23),
    ("20/50", "litro", 109,  19),
    ("15/40", "garrafa", 520, 19),
    ("20/50", "garrafa", 520, 18)
]
datos_monogrados = [
    ("40", "litro",96 , 10),
    ("50", "litro",96 ,13),
    ("60", "litro",96 , 0),
    ("ATF", "litro",96 , 4),
    ("40", "garrafa",470 , 14),
    ("50", "garrafa",470 ,7),
    ("60", "garrafa",470 , 0),
    ("ATF", "garrafa",470 , 6),
]
datos_full = [
    ("0/20 SuperSint", "litro",97 ,7),
    ("5/30","litro",97 ,100),
    ("10/30","litro",97 , 29),
    ("0/20 SuperSint", "garrafa",442 ,10),
    ("5/30","garrafa",442 ,125),
    ("10/30","garrafa",442 , 39)
]
datos_mobil1 = [
    ("0/20 ", "litro",123 ,0),
    ("5/30","litro",123 ,26),
    ("0/20","garrafa",735 ,10),
    ("5/30 ", "garrafa",735 ,11)
]
datos_delvac = [
    ("15/40", "garrafa",390,6),
    ("20/50","garrafa",0,0),
    ("25/50","garrafa",0,0),
    ("15/40", "cubeta",1890,2),
    ("20/50","cubeta",1890,13),
    ("25/50","cubeta",1890,5)
]

#DATOS DEL CASTROL
datos_edge = [
    ("5/30","litro",135,12),
    ("5/40","litro",140,44),
    ("10/30","litro",132,22),
    ("5/30","garrafa",636,15),
    ("5/40","garrafa",645,22),
    ("10/30","garrafa",636,12)
]
datos_gtxmineral = [
    ("5/30","litro",109,40),
    ("10/30","litro",109,38),
    ("10/40","litro",109,23),
    ("15/40","litro",109,5),
    ("20/50","litro",109,40),
    ("25/60","litro",109,29),
    ("5/30","garrafa",523,30),
    ("10/30","garrafa",523,31),
    ("10/40","garrafa",523,11),
    ("15/40","garrafa",523,6),
    ("20/50","garrafa",523,26),
    ("25/60","garrafa",523,0)
]
datos_gtxfull = [
    ("5/30","litro",125,42),
    ("5/30","garrafa",590,54)
]

#DATOS DEL ROSHFRAN
datos_roshfran = [
    ("10/30","litro",65,0),
    ("10/40","litro",65,0),
    ("15/40","litro",65,0),
    ("20/50","litro",65,8),
    ("40","litro",65,128),
    ("50","litro",65,363),
    ("60","litro",65,133),
    ("DEXONIII","litro",76,48),
    ("10/30","garrafa",290,0),
    ("10/40","garrafa",290,0),
    ("15/40","garrafa",290,0),
    ("20/50","garrafa",290,0),
    ("40","garrafa",290,0),
    ("50","garrafa",290,0),
    ("60","garrafa",290,7),
    ("DEXONIII","garrafa",0,0)
]

#DATOS DEL SEKURIT
datos_sekurit_cajas = [
    ("5/30","litro","GASOLINA",70,10),
    ("10/30","litro","GASOLINA",58,17),
    ("15/40","litro","GASOLINA",55,12),
    ("20/50","litro","GASOLINA",55,12),
    ("25/50","litro","GASOLINA",55,13),
    ("40","litro","GASOLINA",58,21),
    ("50","litro","GASOLINA",58,15),
    ("60","litro","GASOLINA",58,12),
    ("25/50","litro","DIESEL",55,11),
    ("50","litro","DIESEL",55,17),
    ("DEXON","litro","SIN DESCRIPCION",55,18),
    ("DEXONIII","litro","SIN DESCRIPCION",55,32),
    ("MERCON5","litro","SIN DESCRIPCION",75,7),
    ("MERCON6","litro","SIN DESCRIPCION",75,4),
    ("CVT","litro","SIN DESCRIPCION",101,5),
    ("80/90","litro","SIN DESCRIPCION",76,7),
    ("2T","litro","MOTO DE 2 TIEMPOS",55,2),
    ("4T","litro","MOTO DE 4 TIEMPOS",55,7),
    ("GL140","litro","SIN DESCRIPCION",55,13),
    ("GL1 90","litro","SIN DESCRIPCION",58,11),
    ("H303","litro","SIN DESCRIPCION",0,7),
    ("5/30","garrafa","GASOLINA",0,0),
    ("10/30","garrafa","GASOLINA",0,0),
    ("15/40","garrafa","GASOLINA",198,15),
    ("20/50","garrafa","GASOLINA",198,3),
    ("25/50","garrafa","GASOLINA",198,3),
    ("40","garrafa","GASOLINA",198,12),
    ("50","garrafa","GASOLINA",198,6),
    ("60","garrafa","GASOLINA",198,19),
    ("25/50","garrafa","DIESEL",197,21),
    ("50","garrafa","DIESEL",197,9),
    ("DEXON","garrafa","SIN DESCRIPCION",193,4),
    ("DEXONIII","garrafa","SIN DESCRIPCION",198,6),
    ("MERCON5","garrafa","SIN DESCRIPCION",0,0),
    ("MERCON6","garrafa","SIN DESCRIPCION",0,0),
    ("CVT","garrafa","SIN DESCRIPCION",0,0),
    ("80/90","garrafa","SIN DESCRIPCION",0,0),
    ("2T","garrafa","MOTO DE 2 TIEMPOS 250 GRAMOS",0,8),
    ("4T","garrafa","MOTO DE 4 TIEMPOS",0,0),
    ("GL140","garrafa","SIN DESCRIPCION",0,0),
    ("GL1 90","garrafa","SIN DESCRIPCION",0,0),
    ("H303","garrafa","SIN DESCRIPCION",0,0)
    
]
datos_sekurit_cubetas = [
    ("40","19 Litros","DIESEL",788,1),
    ("50","19 Litros","DIESEL",788,6),
    ("15/40","19 Litros","DIESEL",788,2),
    ("25/50","19 Litros","DIESEL",788,6),
    ("20/50","19 Litros","GASOLINA",788,1),
    ("GL1 90","19 Litros","SIN DESCRIPCION",788,3),
    ("GL 140","19 Litros","SIN DESCRIPCION",788,3),
    ("H303","19 Litros","SIN DESCRIPCION",595,12)
]
datos_sekurit_grasas = [
    ("SIN COLOR","BALERO","15 KILOS",0,2),
    ("SIN COLOR","BALERO","40 GRAMOS",0,53),
    ("SIN COLOR","BALERO","3.5 kilos",239,5),
    ("ROJO","CHASIS","15 KILOS",877,1),
    ("ROJO","CHASIS","3.5 KILOS",228,3),
    ("AMBAR","CHASIS","15 KILOS",877,2),
    ("AMBAR","CHASIS","3.5 KILOS",228,4)
]
datos_sekurit_quimicos = [
    ("Inflallantas",50,3),
    ("Carbuclean",45,15),
    ("Arrancador",45,16),
    ("Aflojatodo",48,22),
    ("Limp. Cuerpo Aceleracion",62,2),
    ("Ant. Optimus",78.50,20),
    ("Ant. Concentrado",133,0),
]

#DATOS BUJIAS
datos_bujias = [
    ("ACDELCO 12637199",124,496,49.50,),
    ("ILKAR7B11-49129",1,4,49.50,),
    ("HONDA ILZKR7B11S",0,0,49.50,),
    ("KIA HYUNDAI SILZKR7C11S",221,884,49.50,),
    ("SIZFR6B8EG",0,0,49.50,),
    ("PLZKAR6A-11 5118",1467,5868,49.50,),
    ("3811",107,428,49.50,),
    ("VOLKSWAGEN",47,470,49.50,),
    ("DCPR7EIX 3144",492,123,49.50,),
    ("'90137",4,16,49.50,),
    ("6418",187,748,49.50,),
    ("BMW",3,30,49.50,)
]

#DATOS CUBREVOLANTES
datos_cubrevolantes = [
    ("VINIL",20,147),
    ("PIEL",0,0)
]

#DATOS TAPETES
datos_tapetes = [
    ("3 piezas de auto hule","NEGRO",120,120),
    ("4 piezas de auto","FALTANTE",128,100),
    ("3 piezas pick up","FALTANTE",120,58),
    ("armor all de 4 piezas","BEIGE",120,25),
    ("tapete alfombra de 4 piezas","NEGRO",120,5),
    ("tapete de plastico de 4 piezas","BEIGE",104,11),
    ("tapete de 4 piezas plastico ","GRIS",128,12),
    ("tapete metalico de 4 piezas","R/A/P",125,89),
    ("tapete de 4 piezas plastico ","NEGRO",104,0)
]

#DATOS BARDHAL
datos_bardahl = [
    ("Litro","Liquido de frenos",65,10)
]

#DATOS LIMPIABRISAS
datos_parabrisas = [
    ("17/19 RECTO","BRONX",26,50),
    ("11 RECTO","BRONX",19.50,50),
    ("26 RECTO","BRONX",38,50),
    ("20 CRUVO","BRONX",22,100),
    ("14 CURVO","BRONX",42,39),
    ("16 CURVO","BRONX",42,38),
    ("19/24 CURVO","BRONX",43,100),
    ("22 CURVO","BRONX",22.50,50),
    ("18 RECTO","RACING",24,289),
    ("19/21 RECTO","RACING",29,32),
    ("16 RECTO","RACING",26,47),
    ("22 RECTO","RACING",28,39),
    ("28 RECTO","RACING",79,50),
    ("14 RECTO","RACING",26,41),
    ("11 RECTO","RACING",23,11),
    ("24 RECTO","RACING",31,64),
    ("20 RECTO","RACING",29,50),
    ("16/24 CURVO","RACING",79,4),
    ("22 CURVO","RACING",56,45),
    ("26 CURVO","RACING",79,39),
    ("21 CURVO","RACING",35,5),
    ("24 CURVO","RACING",56,41),
    ("28 CURVO","RACING",64,0),
    ("14 CURVO","RACING",28,0)
]

#DATOS FILTROS
df_filtros = pd.read_excel("filtros.xlsx")
print(df_filtros)

datos_filtros = list(df_filtros.itertuples(index=False, name=None))

#QUERIES DEL MOBIL
cursor.executemany(sql_multigrado, datos_multigrado)
cursor.executemany(sql_trc, datos_trcpro)
cursor.executemany(sql_monogrados, datos_monogrados)
cursor.executemany(sql_full, datos_full)
cursor.executemany(sql_mobil1, datos_mobil1)
cursor.executemany(sql_delvac, datos_delvac)

# QUERIES DEL CASTROL 
cursor.executemany(sql_edge, datos_edge)
cursor.executemany(sql_gtxMin,datos_gtxmineral)
cursor.executemany(sql_gtxFull,datos_gtxfull)

#QUERIES ROSHFRAN
cursor.executemany(sql_roshfran, datos_roshfran)

#QUERIES DEL SEKURIT
cursor.executemany(sql_sekurit_cajas,datos_sekurit_cajas)
cursor.executemany(sql_sekurit_cubetas,datos_sekurit_cubetas)
cursor.executemany(sql_sekurit_grasas,datos_sekurit_grasas)
cursor.executemany(sql_sekurit_quimicos,datos_sekurit_quimicos)

#QUERIES BUJIAS
cursor.executemany(sql_bujias, datos_bujias)

#QUERIY CUBREVOLANTES
cursor.executemany(sql_cubrevolantes, datos_cubrevolantes)

#QUERY TAPETES
cursor.executemany(sql_tapetes,datos_tapetes)

#QUERY BARDHAL
cursor.executemany(sql_bardahl,datos_bardahl)

#QUERY LIMPIABRISAS
cursor.executemany(sql_parabrisas, datos_parabrisas)

#QUERY FILTROS
cursor.executemany(sql_filtros, datos_filtros)

conexion.commit()
print("DATOS INSERTADOS CORRECTAMENTE")