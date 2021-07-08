import gpiozero as gz # gpio stands for General Purpose Input/Output
import time
total_temp = 0
for i in range(20):
	cpu_temp = gz.CPUTemperature().temperature
	cpu_temp = round(cpu_temp, 1)
	print(3 * i, "secs:", cpu_temp, 'degrees C')
	total_temp += cpu_temp
	time.sleep(3)
avg_temp = round(total_temp / 20, 1)
print("Avg temp", avg_temp)
