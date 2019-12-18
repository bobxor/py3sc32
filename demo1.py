# Python3 exec(open("./demo1.py").read())

import time
import ssc32
ssc = ssc32.SSC32('COM8', 115200, count=16)
ssc[0].name = 'wrist'
ssc[1].name = 'thumb'
ssc[2].name = 'index'
ssc[3].name = 'mid'
ssc[4].name = 'ring'
ssc[5].name = 'thumbr'

wrist_servo = ssc[0]
thumb_servo = ssc[1]
index_servo = ssc[2]
mid_servo = ssc[3]
ring_servo = ssc[4]


thumb_servo.deg_min = 0
thumb_servo.deg_max = 90
thumb_servo.max = 2200
thumb_servo.min = 200
thumb_servo.reverse = True

index_servo.deg_min = 0
index_servo.deg_max = 90
index_servo.max = 2200
index_servo.min = 100

mid_servo.deg_min = 0
mid_servo.deg_max = 90
mid_servo.max = 2200
mid_servo.min = 100  
mid_servo.reverse = True

ring_servo.deg_min = 0
ring_servo.deg_max = 90
ring_servo.max = 2200
ring_servo.min = 100

def close_hand(move_time = 1500):
	for i in range (1,5):
		ssc[i].degrees = 90
		ssc.commit(time = move_time)
		time.sleep(0.1)

def open_hand(move_time = 1500):
	for i in range (1,5):
		ssc[i].degrees = 0
		ssc.commit(time = move_time)	
		time.sleep(0.1)

def seq_hand(move_time = 1500):
	for i in range (1,5):
		ssc[i].degrees = 90
		ssc.commit(time = move_time)	
		time.sleep((move_time / 1000.0) / 2)
		ssc[i].degrees = 0
		ssc.commit(time = move_time)	
		time.sleep((move_time/1000.0) / 2)
		
def mid_pose(move_time = 1500):
	for i in range(1,5):
		ssc[i].degrees = 90
	mid_servo.degrees = 0
	thumb_servo.degrees = 0
	ssc.commit(time = move_time)
	
def move( pos ):
	ssc[0].position = pos
	ssc.commit(time=1000)

def movech(index, pos ):
	ssc[index].position = pos
	ssc.commit(time=1000)

# print 'Movement done?', ssc.is_done()
