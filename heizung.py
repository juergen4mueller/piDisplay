import serial
import time

ser = serial.Serial("/dev/ttyUSB0", timeout=2)
ser.open()

for i in range(10):
    ser.write([255, 4+i,1])
    time.sleep(3)
    
ser.close()

#read status
for i in range(16):
    data = [0xFF, 0xA1+i,1]
    print("send: ", data)
    ser.write(data)
    time.sleep(0.54)
    
    
for i in range(16):
    data = [0xFF, 0xA1,0]
    print("send: ", data)
    ser.write(data)
    time.sleep(1)

data = [0xFF, 0xA1+i,0]
print("send: ", data)
ser.write(data)
data = [0xFF, 0xA1,0]
print("send: ", data)
ser.write(data)
data = [0xFF, 0xA1+i,0]
print("send: ", data)
ser.write(data)
data = [0xFF, 0xA1,0]
print("send: ", data)
ser.write(data)



import serial
import time

ser = serial.Serial("/dev/ttyUSB0", timeout=2)
ser.open()

for i in range(100):
    print(ser.read(10))
    time.sleep(0.5)
    


    
    
    
stty -F /dev/ttyUSB0 9600 

echo -e '\xff\x01\x01' > /dev/ttyUSB0