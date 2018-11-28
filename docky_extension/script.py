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
t.sleep(0.5)
p.moveTo(docklet)
t.sleep(0.5)
p.click()
t.sleep(0.5)
p.moveTo(clipy_click)
t.sleep(0.5)
p.click()
t.sleep(0.5)
p.click()
t.sleep(0.5)
p.scroll(-5)
t.sleep(0.5)
p.click()
t.sleep(0.5)
p.click()
t.sleep(0.5)
p.scroll(-9)
t.sleep(0.5)
p.click()
t.sleep(0.5)
p.click()
t.sleep(0.5)
p.moveTo(close)
t.sleep(0.5)
p.click()

