from bmp import Bitmap, SaveBmp

WIDTH = 512
HEIGHT = 512

mandelbrot = Bitmap(WIDTH,HEIGHT)

mandelXscale = (-2.00,0.47)
mandelYscale = (-1.12,1.12)

class colorRGB:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

def colorLerp(rgb1, rgb2, t):
    r = int(rgb1.r + (rgb2.r-rgb1.r) * t)
    g = int(rgb1.g + (rgb2.g-rgb1.g) * t)
    b = int(rgb1.b + (rgb2.b-rgb1.b) * t)
    return colorRGB(r,g,b)

def putPixel(x,y,rgb):
    mandelbrot.SetPx(y,x,rgb.r,rgb.g,rgb.b)

for Py in range(HEIGHT):
        for Px in range(WIDTH):
            x0 = mandelXscale[0] + (mandelXscale[1] - mandelXscale[0]) * Px/WIDTH  # lerp(a,b,t) = a + (b - a) * t
            y0 = mandelYscale[0] + (mandelYscale[1] - mandelYscale[0]) * Py/HEIGHT
            
            x = 0.0
            y = 0.0
            x2= 0.0
            y2= 0.0

            iteration = 0
            max_iteration = 1000

            while (x2 + y2 <= 4 and iteration < max_iteration):
                y = (x+x)*y + y0
                x = x2-y2+x0
                x2 = x**2
                y2 = y**2
                iteration = iteration+1

            if iteration == max_iteration:
                putPixel(Py,Px,colorRGB(0,0,0))
            else:
                col2 = colorRGB(0,255,255)
                col1 = colorRGB(0,1,1)
                putPixel(Px,Py,colorLerp(col1, col2, (iteration%40)/40))

SaveBmp(mandelbrot,"mandel.bmp")
