from blinkt import set_pixel, clear, set_all, show, NUM_PIXELS, get_pixel, set_brightness
import time

minuto = 60
# Duração da sessão de trampolim em minutos
DURACAO_SESSAO = 1
COR_MAX = 255
STEP = 5

def sinalDeTroca():
    for i in range(20):
        set_all(0,COR_MAX,0)
        show()
        time.sleep(0.3)
        clear()
        show()
        time.sleep(0.3)
    
def versao1():
    clear()
    show()
    while True:
        sinalDeTroca()
        for i in range(NUM_PIXELS):
            set_pixel(i,i*(COR_MAX//(NUM_PIXELS-1)),COR_MAX-(i*(COR_MAX//(NUM_PIXELS-1))),0)
            show()
            print((DURACAO_SESSAO*minuto)//NUM_PIXELS)
            time.sleep((DURACAO_SESSAO*minuto)//NUM_PIXELS)
        clear()
        show()
    
def versao2():
    clear()
    show()
    while True:
        sinalDeTroca()
        for i in range(NUM_PIXELS):
            if i < 4:
                set_pixel(i,i*(COR_MAX//((NUM_PIXELS//2)-1)),COR_MAX,0)
            else:
                set_pixel(i,COR_MAX,COR_MAX-(i-4)*(COR_MAX//((NUM_PIXELS//2)-1)),0)
            show()
            time.sleep((DURACAO_SESSAO*minuto)//NUM_PIXELS)
        clear()
        show()
        
def loopCoresCondicoes():
    clear()
    show()
    color = {'red': COR_MAX,'green':0,'blue':0}
    for i in range(NUM_PIXELS):
        set_pixel(i,color['red'],color['green'],color['blue'])
    show()
    # Calculate next color
    while True:
        if color['red'] == COR_MAX:
            if color['blue'] > 0:
                color['blue'] -=STEP
            else:
                if color['green'] < COR_MAX:
                    color['green'] +=STEP
                else:
                    color['red'] -= STEP
        if color['green'] == COR_MAX:
            if color['red'] > 0:
                color['red'] -= STEP
            else:
                if color['blue'] < COR_MAX:
                    color['blue'] += STEP
                else:
                    color['green'] -= STEP
        if color['blue'] == COR_MAX:
            if color['green'] > 0:
                color['green'] -= STEP
            else:
                if color['red'] < COR_MAX:
                    color['red'] += STEP
                else:
                    color['blue'] -= STEP
        for i in range(NUM_PIXELS-1):
            pixel = get_pixel(i+1)
            set_pixel(i,pixel[0],pixel[1],pixel[2])
        set_pixel(NUM_PIXELS-1,color['red'],color['green'],color['blue'])
        #print(f"r: {color['red']} | g: {color['green']} | b: {color['blue']}")
        show()

set_brightness(1)
versao2()
