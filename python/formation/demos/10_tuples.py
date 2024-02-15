
def recupere_nombre_et_carre(nombre) :
    return nombre, nombre ** 2

x, x2 = recupere_nombre_et_carre(5)

print("nombre", x, "et son carré", x2)

mon_tuple = (1, 2, 3, 4, 5)
print(mon_tuple)

mon_tuple1, mon_tuple2, mon_tuple3, mon_tuple4, mon_tuple5 = mon_tuple
print(mon_tuple1, mon_tuple2, mon_tuple3, mon_tuple4, mon_tuple5)

var1, _, var3, _, var5 = mon_tuple
print(var1, var3, var5)

_, carre = recupere_nombre_et_carre(3)
print("nombre carré de 3 =", carre)

var4 = mon_tuple[3]
print(var4)
