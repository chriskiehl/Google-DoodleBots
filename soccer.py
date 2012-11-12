import time
import win32api, win32con
import ImageGrab
import sys, os

# -------------------------------------------------#
# NOTE: All coordinates are specific to my screen  #
#       at my resolution. I made these with the    #
#		the quickness on my lunchbreak, so no      #
#       padding was accounted for. So, you'll need #
#       to adjust the values for your resolution   #
#		if you want it to run.                     #
# -------------------------------------------------#

# Location of doodle: http://www.google.com/doodles/soccer-2012


def grab(size=(457, 328, 811, 381)):
	imgData = ImageGrab.grab(size).getdata()
	for i in range(0, len(imgData),7):
		if isHit(imgData[i]):
			print "hit!"
			win32api.SetCursorPos((456+(i%354), 300))
			if isAirball():
				print 'air ball'
				click()

def isHit(pixelVal):
	return pixelVal == (107, 150, 52) or pixelVal == (95,133,46)

def isAirball(index, imageData):
	return index > 354*12 and (255,255,255) not in imageData and 
						(95, 133, 46) in imageData

	
def press(x, delay=None):
    win32api.keybd_event(VK_CODE[x], 0,0,0)
    if delay:
    	time.sleep(delay)
    win32api.keybd_event(VK_CODE[x],0 ,win32con.KEYEVENTF_KEYUP ,0)

def click_retry(cord=(630,350)):
    win32api.SetCursorPos(cord)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def play():
	VK_CODE = {'left_arrow':0x25,
			'spacebar':0x20,
           	'right_arrow':0x27}
	
	print "Start!!"
	click_retry()
	s = time.time()
	while 1:
		grab()
	

if __name__ == '__main__':
	play()
	print 'Execution finished'