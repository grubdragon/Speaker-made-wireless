import wave
import time
import socket
ip = '192.168.43.184'#ip of connected Arduino
waveFile = wave.open('bird.wav', 'r')
t = 1./waveFile.getframerate()
length = waveFile.getnframes()
sampwid = waveFile.getsampwidth()

print(t,1/t,length,sampwid)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,80))

def send(data):
    n = s.send(data)
    if n==0:
        print("Sorry rahega")
        exit()

for i in xrange(0,length):
    waveData = waveFile.readframes(1)[0]
    send(waveData)
    #print("Sent: %d" % ord(waveData))
    time.sleep(t-0.000002)

s.close()
