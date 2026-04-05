#Set the counts to zero.
totalRain = 0.0
totalWind = 0.0
count = 0

#Let user enter datas in same line.
data = input().split()

#Make sure data is in float.
rain = float(data[0])

#While loop to add data to list.
while rain != -1.0:
    wind = float(data[1])
    totalRain += rain
    totalWind += wind
    count += 1
    data = input().split()
    rain = float(data[0])

#Calculate the average and severity level.
averageRain = totalRain / count
averageWind = totalWind / count
severity = (averageRain * 10) + averageWind

#Print result.
print("The average rain is:", averageRain, "inches")
print(f"The average wind is:", averageWind, "mph")
print(f"The weather severity for these", count, "readings is:", severity)