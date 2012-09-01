import time
import win32api, win32con

VK_CODE = {'left_arrow':0x25,
		   'spacebar': 0x20,
           'right_arrow':0x27}

def press(x):
    win32api.keybd_event(VK_CODE[x], 0,0,0)
    win32api.keybd_event(VK_CODE[x],0 ,win32con.KEYEVENTF_KEYUP ,0)

def play():
	time.sleep(2)
	s = time.time()
	while time.time() - s < 10:
		press("left_arrow")
		press("right_arrow")
		press("left_arrow")
		press("right_arrow")
		press('spacebar')  

if __name__ == '__main__':
	play()