import random
# Tenemos una lista llamada matriculas de 20 matrículas de coche. Sacar aleatoriamente 5 y ponerlas en
# otra lista llamada elegidas.
matriculas = [
"4821 BRT",
"0735 CLM",
"9158 FGS",
"2206 HPR",
"6540 JTV",
"3829 KRS",
"0471 LCN",
"8910 MTP",
"5637 NDR",
"7094 PSM",
"1358 RBT",
"8642 SJL",
"3127 TMW",
"4765 VNR",
"5891 WPR",
"6403 XMT",
"7518 YRL",
"9082 ZBW",
"0279 BKS",
"3950 HLD" ]
# Tenemos un diccionario llamado caducidades con esas 20 matrículas y el número de meses que hace que
# le ha caducado la itv.
caducidades = {
'4821 BRT': 4,
'0735 CLM': 2,
'9158 FGS': 6,
'2206 HPR': 1,
'6540 JTV': 8,
'3829 KRS': 3,
'0471 LCN': 5,
'8910 MTP': 7,
'5637 NDR': 2,
'7094 PSM': 6,
'1358 RBT': 4,
'8642 SJL': 8,
'3127 TMW': 1,
'4765 VNR': 7,
'5891 WPR': 3,
'6403 XMT': 5,
'7518 YRL': 2,
'9082 ZBW': 8,
'0279 BKS': 1,
'3950 HLD': 6
}
#Elegir 5 matriculas
#Declaro la lista de matriculas
elegidas = []

for i in range(5):
    #Utilizo random.choice(lista) para seleccionar 5 opciones alieatorias
    elegidas.append(random.choice(matriculas))

print("Elegidas", elegidas)



#Generar un nuevo diccionarrio llamado multas