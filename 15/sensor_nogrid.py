import regex as re

sensors = {}
beacons = set()
#row = 10
row = 2000000
relevant_sensors = {}
sensor_dist_to_row = {}
sensor_coverage = {}
num_beacons = 0
total_coverage = 0

def coverage_range(sensor):
	return (sensor[0]-abs(relevant_sensors[sensor]-sensor_dist_to_row[sensor]),sensor[0]+abs(relevant_sensors[sensor]-sensor_dist_to_row[sensor]))#((relevant_sensors[sensor]-sensor_dist_to_row[sensor])*2)+1

def coverage_count(sensor):
	if sensor in sensor_coverage.keys() and sensor_coverage[sensor]:
		return len(range(*sensor_coverage[sensor]))+1
	else:
		return 0
	#return 0 if not sensor in sensor_coverage.keys() else len(range(*sensor_coverage[sensor]))+1

def overlap(sensor1,sensor2):
	global sensor_coverage
	# print("overlap",sensor1,sensor2)
	# if sensor2 == (2,0):
	# 	print("!!!",sensor2,sensor_coverage[sensor2],"!!!")
	sensor1_range,sensor2_range = sensor_coverage[sensor1],sensor_coverage[sensor2]
	overlap = 0
	if sensor1_range and sensor2_range:
		if sensor1_range[0] <= sensor2_range[0] and sensor1_range[1] >= sensor2_range[1]:
			#Sensor1 completly overlaps sensor2
			overlap = coverage_count(sensor2)
			sensor_coverage[sensor2] = None
#			print("total overlap",sensor1,sensor2,overlap)
		elif sensor1_range[0] <= sensor2_range[0] <= sensor1_range[1] <= sensor2_range[1]:
			#Sensor1 is to the left of sensor 2
			overlap = sensor2_range[0] - sensor1_range[1] + 1
			sensor_coverage[sensor2] = (sensor1_range[1] +1, sensor2_range[1])
#			print("overlap left",sensor1,sensor2,overlap)
		elif sensor1_range[1] >= sensor2_range[1] >= sensor1_range[0] >= sensor2_range[0]:
			#Sensor1 is to the right of sensor 2
			overlap = sensor2_range[1] + 1 - sensor1_range[0]
			sensor_coverage[sensor2] = (sensor2_range[0], sensor1_range[0] +1)
#			print("overlap right",sensor1,sensor2,overlap)
		else:
			#No overlap
#			print("No overlap",sensor1,sensor2)
			pass
	else:
		#No overlap
#		print("No overlap",sensor1,sensor2)
		pass
	return overlap
	# total_adjusted_dist = relevant_sensors[sensor1] - sensor_dist_to_row[sensor1] + relevant_sensors[sensor2] - sensor_dist_to_row[sensor2]
	# #print(relevant_sensors[sensor1],"-",sensor_dist_to_row[sensor1],"+",relevant_sensors[sensor2],"-", sensor_dist_to_row[sensor2],"=",total_adjusted_dist)
	# max_overlap = max(total_adjusted_dist - abs(sensor1[0] - sensor2[0]) +1,0)
	# #print(abs(sensor1[0]-sensor2[0]),max_overlap)
	# return max(0,min(sensor_coverage[sensor1],sensor_coverage[sensor2],max_overlap))

def distance(pos1,pos2):
	return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def set_coverage(row):
	global total_coverage,sensor_coverage,sensor_dist_to_row,relevant_sensors,num_beacons

	for sensor,(beacon,dist) in sensors.items():
		sensor_dist_to_row[sensor] = max(abs(sensor[1]-row),0)
		if abs(row - sensor[1]) <= dist:
			relevant_sensors[sensor] = dist
	for beacon in beacons:
		if beacon[1] == row:
			num_beacons += 1
	for sensor in relevant_sensors.keys():
		sensor_coverage[sensor] = coverage_range(sensor)
		#print(sensor,coverage_range(sensor),coverage_count(sensor))
		total_coverage += coverage_count(sensor)

for line in open("test_input.txt").read().strip().split("\n"):
	m = re.search("Sensor at x=(?P<sx>-?\d+), y=(?P<sy>-?\d+): closest beacon is at x=(?P<bx>-?\d+), y=(?P<by>-?\d+)",line)
	if m:
		print("sensor = {}, beacon = {}".format((m.group("sx"),m.group("sy")),(m.group("bx"),m.group("by"))))
		sx,sy,bx,by = int(m.group("sx")),int(m.group("sy")),int(m.group("bx")),int(m.group("by"))
		# if xmin == None or sx < xmin or bx < xmin:
		# 	xmin = min(sx,bx)
		# if xmax == None or sx > xmax or bx > xmax:
		# 	xmax = max(sx,bx)
		# if ymin == None or sy < ymin or by < ymin:
		# 	ymin = min(sy,by)
		# if ymax == None or sy > ymax or by > ymax:
		# 	ymax = max(sy,by)

		sensors[(sx,sy)] = ((bx,by),distance((sx,sy),(bx,by)))
		beacons.add((bx,by))




#print(relevant_sensors)
# for sensor,dist in sensor_dist_to_row.items():

# 	print(sensor,dist)

#print("Covered tiles")
set_coverage(row)
	
# print(total_coverage)
#print("-")

sensor_list = list(reversed(sorted(list(relevant_sensors.keys()),key=coverage_count)))

# print(overlap((8,7),(0,11)))
#print("coverage (2,0)",coverage_count((2,0)))
for i in range(len(sensor_list)):
	for j in range(i+1,len(sensor_list)):
		over_lap = overlap(sensor_list[i],sensor_list[j])
		#print(sensor_list[i],sensor_list[j],over_lap)
		total_coverage -= over_lap

# for pair in sensor_coverage.keys():
# 	total_coverage += coverage_count(pair)
print(total_coverage-num_beacons)

x,y = 0,0
while x in range(0,21):#4000001):
	set_coverage(x)
	#print(sensor_coverage.keys())
	while y in range(0,21):#4000001):
		nexty = y+1
		found = True
		for sensor,(beacon,dist) in sensors.items():
			#print(distance((x,y),(sensor)),dist)
			if sensor in sensor_coverage.keys() and distance((x,y),sensor) <= dist:
				found = False
				#nexty = sensor_coverage[sensor][1]
				break
		if found:
			print(x,y)
		y = nexty
	x += 1