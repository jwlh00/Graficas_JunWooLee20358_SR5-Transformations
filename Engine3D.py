from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, unlit, gourad, toon, glow, textureBlend

width = 960
height = 540

rend = Renderer(width, height)

rend.dirLight = V3(1,0,0)

def interface_principal():
    global num
    print('1:Medium Shot. \n2:Low Shot. \n3:High Angle. \n4:Dutch Angle.')
    x = False
    while not x:
      try:
          num=input("\nIngrese el numero de la opcion deseada: ")
          num = int(num)
          x = True
      except Exception:
          print("\nEl valor ingresado, no es un número, por favor ingrese un número nuevamente")
    while num < 1 or num > 4:
        print('numero fuera de rango, por favor ingresar otra vez:')
        num = input('Ingrese el numero de lo que quiere hacer')
        
interface_principal()
       
if num == 1:
    #Medium Shot
    print("Medium Shot")
    rend.glLookAt(V3(0, 0, -10), V3(5.3, 0, 1))

elif num == 2:
    #Low Angle
    print("Low Angle")
    rend.glLookAt(V3(0, 0, -10), V3(5.3, -5, 1))

elif num == 3:
    #High Angle
    print("High Angle")
    rend.glLookAt(V3(0, 0, -10), V3(5.3, 5, 1))
    
elif num == 4:
    #Dutch Angle
    print("Dutch Angle")
    rend.glLookAt(V3(0, 0, -10), V3(5.3, 0, 0))
    rend.glViewMatrix(translate=V3(0, 0, 1), rotate=V3(0,0,-40))
else:
    pass



rend.active_texture = Texture("models/model_normal.bmp")
rend.active_shader = gourad
rend.glLoadModel("models/model.obj",
                 translate = V3(0, 0, -10),
                 scale = V3(3,3,3),
                 rotate = V3(0,0,0))



rend.glFinish("output.bmp")

