import timeit
weight = []
profit = []
nama = []
sumtotalkendaraan = 0
i = 0
#fungsiuntukmemvalidasiberatdanprofitdarimasingmasingkendaraan
def validasiberatdanprofit(sumvehicle,typevehicle):
    for j in range(int(sumofvehicle)):
        if(typeofvehicle == 'Mobil'):
            berat = 1085
            valueprofit = 159000
            weight.append(berat)
            profit.append(valueprofit)
            nama.append(typeofvehicle)
        elif(typeofvehicle == 'Motor'):
            berat = 109
            valueprofit = 24000
            weight.append(berat)
            profit.append(valueprofit)
            nama.append(typeofvehicle)
        elif(typeofvehicle == 'Truck'):
            berat = 2500
            valueprofit = 395000
            weight.append(berat)
            profit.append(valueprofit)
            nama.append(typeofvehicle)
        elif(typeofvehicle =='Bus'):
            berat = 5500
            valueprofit = 495000
            weight.append(berat)
            profit.append(valueprofit)
            nama.append(typeofvehicle)
        elif(typeofvehicle =='Tronton'):
            berat = 7200
            valueprofit = 690000
            weight.append(berat)
            profit.append(valueprofit)
            nama.append(typeofvehicle)
#mencaridenganmenggunakangreedyalgorithm
def greedyalgorithm(M , profit , weight , n):
    total_mobil = 0
    total_motor = 0
    total_bus = 0
    total_tronton = 0
    total_truck = 0
    terpakai = 0
    start = timeit.default_timer()
    Xi = []
    maximum_profit = 0
    maximum = M
    print('Kendaraan yang terpilih : ')
    for i in range(n):
        if weight[i] > maximum :
            break
        Xi.append(1)
        maximum = maximum - weight[i]
        print(nama[i],profit[i],weight[i],'Kg')
        terpakai = terpakai + weight[i]
        if(nama[i] == 'Mobil'):
            total_mobil = total_mobil + 1
        elif(nama[i] == 'Motor'):
            total_motor = total_motor + 1
        elif(nama[i] == 'Truck'):
            total_truck = total_truck + 1
        elif(nama[i] == 'Bus'):
            total_bus = total_bus + 1
        elif(nama[i] == "Tronton"):
            total_tronton = total_tronton + 1
        maximum_profit = maximum_profit + profit[i]
    print('Kendaraan yang terpilih',total_mobil,'Mobil,',total_motor,'Motor,',total_truck,'Truck,',total_bus,'Bus,dan',total_tronton,'Tronton')
    print('Kapasitas yang terpakai : ',terpakai,'Kg')
    print('Maximum Profit yang Bisa Didapatkan dengan Greedy Algorithm : Rp.',maximum_profit)
    print('Kapasitas yang masih tersedia : ',maximum,'Kg')
    stop = timeit.default_timer()
    print("Hasil Eksekusi %s seconds " % (stop - start))

#mencaridenganmenggunakandynammicprogramming
def DynamicProgramming(M , weight , profit , n):
    total_mobil = 0
    total_motor = 0
    total_bus = 0
    total_truck = 0
    total_tronton = 0
    start = timeit.default_timer()
    terpakai = 0
    K = [[0 for w in range(M + 1)] 
            for i in range(n + 1)] 
    # Build table K[][] in bottom 
    # up manner 
    for i in range(n + 1): 
        for w in range(M + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif weight[i - 1] <= w: 
                K[i][w] = max(profit[i - 1] + K[i - 1][w - weight[i - 1]], K[i - 1][w]) 
            else: 
                K[i][w] = K[i - 1][w]
    maximum_profit = K[n][M] 
    arr_solution = K[n][M] 
    w = M 
    print('Kendaraan yang terpilih : ')
    for i in range(n, 0, -1): 
        if arr_solution <= 0: 
            break
        if arr_solution == K[i - 1][w]: 
            continue
        else: 
            print(nama[i-1],weight[i - 1],profit[i-1])
            if(nama[i-1] == 'Mobil'):
                total_mobil = total_mobil + 1
            elif(nama[i-1] == 'Motor'):
                total_motor = total_motor + 1
            elif(nama[i-1] == 'Truck'):
                total_truck = total_truck + 1
            elif(nama[i-1] == 'Bus'):
                total_bus = total_bus + 1
            elif(nama[i-1] == "Tronton"):
                total_tronton = total_tronton + 1
            terpakai = terpakai + weight[i - 1] 
            arr_solution = arr_solution - profit[i - 1] 
            w = w - weight[i - 1]
    print('Terdapat',total_mobil,'Mobil,',total_motor,'Motor,',total_truck,'Truck,',total_bus,'Bus, dan',total_tronton,'Tronton')
    print('Kapasitas yang terpakai : ',terpakai,'Kg')  
    print('Maximum Profit yang Bisa Didapatkan dengan Dynamic Programming : Rp.',maximum_profit) 
    print('Kapasitas yang masih Tersedia ',w,'Kg')
    stop = timeit.default_timer()
    print("Hasil Eksekusi %s seconds " % (stop - start)) 

#mainprogram
sumofType = input('Banyak Tipe Kendaraan yang Ada : ')
maxloadkapal = int(input('Berat Maksimum Load Kapal : '))
while(i < int(sumofType)):
    typeofvehicle = input('Jenis Kendaraan : ')
    sumofvehicle = input('Jumlah : ')
    validasiberatdanprofit(sumofvehicle,typeofvehicle)
    sumtotalkendaraan = sumtotalkendaraan + int(sumofvehicle)
    i = i + 1;
print('Metode Yang Tersedia Untuk Menghitung Keuntungan Maximum')
print('1. Greedy Algorithm')
print('2. Dynammic Programming')
tipe = input('Pilih Metode Yang Ingin Digunakan : ')
if(int(tipe) == 1):
    greedyalgorithm(maxloadkapal,profit,weight,sumtotalkendaraan)
elif(int(tipe) == 2):
    DynamicProgramming(maxloadkapal,weight,profit,sumtotalkendaraan)