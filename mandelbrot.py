print("for git")	
from PIL import Image
from numpy import complex

WIDTH = 1024
HIGH = 1024
SCALER = 3

def mandelbrot(x, y):
    c0 = complex(x, y)
    c = 0
    for i in range(1, 1000):
        if abs(c) > 2:
            if i >666 :
                return (255, 255, i%255)
            elif i > 333:
                return(255, i%255, 0)
            else:
                return(i%255, 0, 0)
        c = c * c + c0
    return (0, 0, 0)

img = Image.new('RGB', (WIDTH, HIGH))
pixels = img.load()
  
for x in range(img.size[0]):
    print("%.2f %%" % (x / WIDTH * 100.0)) 
    for y in range(img.size[1]):
        pixels[x, y] = mandelbrot(SCALER*(x-0.75*WIDTH)/WIDTH,SCALER*(y-0.5*HIGH)/HIGH) 

print("100.00 % - Mandelbrot set rendering done!")
img.show()
img.save("mandelbrot.jpg")
