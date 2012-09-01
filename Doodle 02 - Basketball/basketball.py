import time
import win32api, win32con

# -------------------------------------------------#
# NOTE: All coordinates are specific to my screen  #
#       at my resolution. I made these with the    #
#		the quickness on my lunchbreak, so no      #
#       padding was accounted for. So, you'll need #
#       to adjust the values for your resolution   #
#		if you want it to run.                     #
# -------------------------------------------------#

# Doodle: http://www.google.com/doodles/basketball-2012

VK_CODE = {'left_arrow':0x25,
		   'spacebar':0x20,
           'right_arrow':0x27}

def press(x, delay=None):
    win32api.keybd_event(VK_CODE[x], 0,0,0)
    if delay:
    	time.sleep(delay)
    win32api.keybd_event(VK_CODE[x],0 ,win32con.KEYEVENTF_KEYUP ,0)

def click_retry(cord=(574, 279)):
    win32api.SetCursorPos(cord)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def play():
	time.sleep(2)
	print "Start!!"
	click_retry()
	time.sleep(.2)
	s = time.time()
	for i in range(5):
		print "First position"
		press('spacebar', .32) 
		# time.sleep(1)
	for i in range(4):
		print "Second position!"
		press('spacebar', .48) 
		# time.sleep(1)
	for i in range(4):
		print "Third position"
		press('spacebar', .65) 
		# time.sleep(1)
	for i in range(4):
		print "Fourth position"
		press('spacebar', .76) 
		# time.sleep(1)

if __name__ == '__main__':
	play()