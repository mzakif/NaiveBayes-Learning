import pandas as pd
# read data train dan test dalam csv
trainData = pd.read_csv('TrainsetTugas1ML.csv')
testData = pd.read_csv('TestsetTugas1ML.csv')

# sorting data dan di jadikan group antara dua kelas utama
def split(data):
    traingroup = trainData.groupby('income')
    besar = traingroup.get_group('>50K')
    kecil = traingroup.get_group('<=50K')
    return besar, kecil

# membagi lebih kecil lagi berdasarkan attribute dan isi datanya
def groupMiniBesar(dataIncome,atribut,nama_data):
    if '>50K' == dataIncome:
        besargroup = besar.groupby(atribut)
        besarMini = besargroup.get_group(nama_data)
        return len(besarMini)
    else:
        kecilgroup = kecil.groupby(atribut)
        kecilMini = kecilgroup.get_group(nama_data)
        return len(kecilMini)

# mengambil label setiap kelas dan dimasukan kedalam list c
c = []
c = testData.columns.tolist()
# ------
besar, kecil = split(trainData)
peluangIncome = [len(besar)/len(trainData), len(kecil)/len(trainData)]
hasilOutput = []
for i in range(len(testData)):
    peluangA = (groupMiniBesar('>50K',c[1], testData[c[1]][i]) / len(besar))*(groupMiniBesar('>50K',c[2], testData[c[2]][i]) / len(besar))*(groupMiniBesar('>50K',c[3], testData[c[3]][i]) / len(besar))*(groupMiniBesar('>50K',c[4], testData[c[4]][i]) / len(besar))*(groupMiniBesar('>50K',c[5], testData[c[5]][i]) / len(besar))*(groupMiniBesar('>50K',c[6], testData[c[6]][i]) / len(besar))*(groupMiniBesar('>50K',c[7], testData[c[7]][i]) / len(besar))*peluangIncome[0]
    peluangB = (groupMiniBesar('<=50K',c[1], testData[c[1]][i]) / len(kecil))*(groupMiniBesar('<=50K',c[2], testData[c[2]][i]) / len(kecil))*(groupMiniBesar('<=50K',c[3], testData[c[3]][i]) / len(kecil))*(groupMiniBesar('<=50K',c[4], testData[c[4]][i]) / len(kecil))*(groupMiniBesar('<=50K',c[5], testData[c[5]][i]) / len(kecil))*(groupMiniBesar('<=50K',c[6], testData[c[6]][i]) / len(kecil))* (groupMiniBesar('<=50K',c[7], testData[c[7]][i]) / len(kecil))*peluangIncome[1]
    
    if (peluangA > peluangB):
        hasilOutput.append('>50K')
    else:
        hasilOutput.append('<=50K')

TebakanTugas1 = pd.DataFrame({'income' : hasilOutput}, index = testData['id'])
TebakanTugas1.to_csv("TebakanTugas1.csv")
print('berhasil')