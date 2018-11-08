#!/usr/bin/python3

import pyautogui as p
import time as t

docky = (437, 767)
docky_click = (440, 720)
docklet = (559, 223)
close = (826, 578)
clipy_click = (826, 508)

# starting the automation

p.moveTo(docky)
t.sleep(0.5)
p.moveTo(docky_click)
t.sleep(0.5)
p.click()
p.moveTo(docklet)
p.click()
p.moveTo(clipy_click)
p.click()
p.click()
p.scroll(-5)
p.click()
p.click()
p.scroll(-9)
p.click()
p.click()
p.moveTo(close)
p.click()

