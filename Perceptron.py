#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import math
random.randint
import sys
import pygame
from pygame import gfxdraw
pygame.init()
win_w = 300
win_h = 300
setpix = gfxdraw.pixel
window = pygame.display.set_mode((win_w, win_h))
#генерирует массив
i = 0
class_p1 = []
class_p2 = []
while i < 50:
  i = i+1  
  class_p1 = [[int(random.gauss(100.0,25.0)),int(random.gauss(100.0,25.0))]] + class_p1
  class_p2 = [[int(random.gauss(200.0,25.0)),int(random.gauss(200.0,25.0))]] + class_p2
#рисует массив
def draw_points():
    for vec in class_p1:
        i = vec[0]
        j = vec[1]
        color = (255, 0, 0)
        pygame.draw.circle(window, color, (i,j), 2)
 
    for vec in class_p2:
        i = vec[0]
        j = vec[1]
        color = (0, 255, 0)
        pygame.draw.circle(window, color, (i,j), 2)
#стаит метки и сливает в один массив
class_p1_met = map(lambda x: x + [1], class_p1)
class_p2_met = map(lambda x: x + [-1], class_p2)
vec_met = class_p1_met + class_p2_met
#генерирует случайные параметры (для обучения)
def gen_perceptron_params():
    W = [random.gauss(0.0,1.0),random.gauss(0.0,1.0)]
    b = random.gauss(0.0,20.0)
    return [W[0],W[1],b]
#высчитывает линию и ее ошибки
def perc(vec):
  error = 0
  params = gen_perceptron_params()
  for z in vec:
    if (z[0]*params[0] + z[1]*params[1] + params[2]) >= 0:
      y = 1
      if y != z[2]:
        error = error + 1
    else:
      y = -1
      if y != z[2]:
        error = error + 1
  return [params + [error]]
#цикл обучения
def lerning(vecc):
  i = 0
  lern = []
  while i < 10000:
    lern = lern + perc(vec_met)
    i = i + 1
  return lern
a = lerning(vec_met)
#выборка модели с минальным числом ошибок
def perc_lern(g):
  min_d = 50
  min_par = 0
  for d in g:
    if d[3] < min_d:
      min_d = d[3]
      min_par = d[0:3]
  return min_par
#оптимальная модель
params = perc_lern(a)
#Набор прямых которые являются границами экрана
screen_lines = [[(0,0),(0,win_h)],
               [(0,0),(win_w,0)],
               [(0,win_h),(win_w,win_h)],
               [(win_w,0),(win_w,win_h)]]
#Возвращает вектор (координаты точки пересечения)если есть пересечение линии
#заданной двумя точками и линии заданной уравнением как у перцептрона
#Если нет пересечения то возвращает False
#line_a = [[x1,y1],[x2,y2]]
#line_b = [A,B,C]
def intersect(line_a, line_b):
    x1 = line_a[0][0]
    y1 = line_a[0][1]
    x2 = line_a[1][0]
    y2 = line_a[1][1]
   
    A = line_b[0]
    B = line_b[1]
    C = line_b[2]
   
    if x1 == x2:
        y = (-B*x1-C)/A
        sol = [x1,y]
    elif y1 == y2:
        x = (-C-A*y1)/B
        sol = [x,y1]
    else:
        sol = solvelin((y1-y2),(x2-x1),(x1*y2-x2*y1),A,B,C)
   
    print sol, 'sol'
   
    x = sol[0]
    y = sol[1]
   
    #Проверяем находится ли точка пересечения на первой прямой (между точками)
    if (((x2 >= x) and (x >= x1)) or ((x1 >= x) and (x >= x2))) and (((y2 >= y) and (y >= y1)) or ((y1 >= y) and (y >= y2))):
        return sol
    else:
        return False
#!Рисует линию которая соответствует перцептрону с набором параметров передающимся в аргументе
def draw_peceptron_line(params):
    points = []
    #Находим пересечения линии перцептрона с границами экрана
    for l in screen_lines:
        sol = intersect(l,params)
        if sol:
            points.append(sol)
    print "Точки пересечения ",points
    #Если найдено хотя бы две точки пересечения то прямая находится внутри экрана и её можно нарисовать
    if len(points) >= 2:
        pygame.draw.line(window, (100,100,190), map(int,points[0]), map(int,points[1]), 3)

#Нарисуем точки кластеров а поверх них линию перецептрона
window.fill((30,80,30))
draw_points()
draw_peceptron_line(params)
pygame.display.flip()
 
def react_to_events():
    pygame.time.wait(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        else:
            pass#print event
while True:
    react_to_events()
