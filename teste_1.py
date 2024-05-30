import pyautogui as pg
import time

time.sleep(3)
print(pg.position())

#pg.moveTo(878, 1046, 4)
pg.leftClick(912, 1049, 1, 3)
time.sleep(1)
pg.typewrite('www.valor.com.br')
time.sleep(1)
pg.press('enter')