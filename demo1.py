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
thumbr_servo = ssc[5]

wrist_servo.deg_min = 0
wrist_servo.deg_max = 90
wrist_servo.max = 2200
wrist_servo.min = 100
wrist_servo.reverse = True


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

thumbr_servo.deg_min = 0
thumbr_servo.deg_max = 90
thumbr_servo.max = 1400
thumbr_servo.min = 100
thumbr_servo.reverse = True


def demo1():
	movechdeg(0,0)
	wait_till_done()
	seq_hand(300)
	wait_till_done()
	seq_hand_rev(300)
	wait_till_done()
	close_hand(300)
	wait_till_done()
	open_hand(300)
	wait_till_done()
	pinch(300)
	wait_till_done()
	open_hand(300)
	wait_till_done()
	term_t_up(500)
	wait_till_done()
	movechdeg(0,0)
	wait_till_done()
	movechdeg(0,90)
	wait_till_done()
	open_hand(300)
	movechdeg(0,0)
	wait_till_done()
	
	

def wait_till_done():
	# Todo: implement timeout.
	while not ssc.is_done():
		time.sleep(0.1)

def pinch(move_time = 1000):
	thumbr_servo.degrees = 90
	thumb_servo.degrees = 90
	index_servo.degrees = 90
	ssc.commit(time = move_time)
	

def close_hand(move_time = 1500):
	for i in range (1,5):
		ssc[i].degrees = 90
		ssc.commit(time = move_time)
		time.sleep(0.1)

def open_hand(move_time = 1500):
	for i in range (1,6):
		ssc[i].degrees = 0
		ssc.commit(time = move_time)	
		time.sleep(0.1)

def seq_hand(move_time = 1500):
	for i in range (1,5):
		ssc[i].degrees = 90
		ssc.commit(time = move_time)	
		time.sleep((move_time / 1000.0) / 1)
		ssc[i].degrees = 0
		ssc.commit(time = move_time)	
		time.sleep((move_time/1000.0) / 1)
		
def seq_hand_rev(move_time = 1500):
	for i in range (4,0,-1):
		ssc[i].degrees = 90
		ssc.commit(time = move_time)	
		time.sleep((move_time / 1000.0) / 1)
		ssc[i].degrees = 0
		ssc.commit(time = move_time)	
		time.sleep((move_time/1000.0) / 1)

def term_t_up(move_time = 1000):
	ssc[1].degrees = 0
	thumbr_servo.degrees = 0
	ssc.commit(time = move_time)	
	
	for i in range(4,1,-1):
		ssc[i].degrees = 90
		ssc.commit(time = move_time)	
		time.sleep((move_time / 1000.0) / 3)
		
def mid_fing(move_time = 1500):
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
	
def movechdeg(index, degree):
	ssc[index].degrees = degree
	ssc.commit(time=1000)

# print 'Movement done?', ssc.is_done()
