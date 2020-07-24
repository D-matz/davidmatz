import cv2
import numpy as np
from numpy import asarray
import svgwrite

cam = cv2.VideoCapture("graves.webm")
blueside = False
limit = 1300
pathwidth = 1

linesdrawn = []

def dist(x1, y1, x2, y2):
	a = y2 - y1
	b = x2 - x1
	return (a * a) + (b * b)

def draw(dwg, points, blueside, thisframe, totalframes):
	#print(thisframe, totalframes, points)
	grad_red = [['#d9241e'],['#ff7d6a','#a52d22'],['#ff9e8e','#d9241e','#54221b'],['#fcc6be','#ff3f32','#a52d22','#54221b'],['#fcc6be','#ff7d6a','#d9241e','#762920','#2f1512']]
	grad_blue = [['#4e66ff'],['#8d9dff','#0022fc'],['#a7b3ff','#4e66ff','#001ac0'],['#a7b3ff','#5b71ff','#001fe6','#001182'],['#c9d0ff','#6a7dff','#2c49ff','#001ac0','#000d63']]

	color = '#fbecea'
	if(blueside):
		color = '#c9d0ff'
		if(thisframe < 5): color = grad_blue[totalframes][thisframe]
	else:
		if(thisframe < 5): color = grad_red[totalframes][thisframe]

	#print(thisframe, totalframes, color)

	dwg.add(dwg.circle(center=(points[0],points[1]),
		r=pathwidth/2,
		fill=color))

	line = dwg.add(dwg.line(
		start = (points[0], points[1]),
		end = (points[2], points[3]),
		stroke = color,
		stroke_width = pathwidth,
		fill = 'none'))

def find_rect(row, col):
	x1 = col[0]
	y1 = row[1]
	if(x1 > row[0] + 21): x1 = x1 - 42
	if(y1 > col[1] + 12): y1 = y1 - 24
	#print(row, col, x1, y1)
	return [x1, y1]


#given x and y ranges, find either lightest row in array
#rect comes as upper left corner (x1, y1), bottom right corner (x2, y2)
#return x1, y1 of rectangle and min sum
def search_h(rect, offwhite):
	len = 42
	x1 = 0
	y1 = 0
	minsum = 999999999
	for y in range(rect[1], rect[3]):
		rowsum = 0
		for x in range(rect[0], rect[0] + len):
			rowsum = rowsum + offwhite[y][x]
		for x in range(rect[0] + 1, rect[2] - len):
			rowsum = rowsum - offwhite[y][x-1] + offwhite[y][x+len-1]
			if(rowsum < minsum):
				minsum = rowsum
				x1 = x
				y1 = y
	return([x1, y1, minsum])

def search_v(rect, offwhite, len):
	x1 = 0
	y1 = 0
	minsum = 999999999
	for x in range(rect[0], rect[2]):
		colsum = 0
		for y in range(rect[1], rect[1] + len):
			colsum = colsum + offwhite[y][x]
		for y in range(rect[1] + 1, rect[3] - len):
			colsum = colsum - offwhite[y-1][x] + offwhite[y+len-1][x]
			if(colsum < minsum):
				minsum = colsum
				x1 = x
				y1 = y
	return([x1, y1, minsum])

def checkbar(array, cutoff):
	latest = 0
	for x in range(0, 27):
		colcol = 0
		for y in range(0, 3):
			colcol = colcol + sum(array[y][x])
		if(colcol > cutoff): latest = x
	return latest/26

i = 0
name = 'path.svg'
if(blueside): name = 'path2.svg'
dwg = svgwrite.Drawing(name, profile='tiny')
corner = [143, -4]
if(blueside): corner = [-13, 149]
stupid_cam = 0
wait_draw_x = [0 for i in range(limit + 1)]
wait_draw_y = [0 for i in range(limit + 1)]
wait_draw_x[0] = (corner[0] + 21) * 3
wait_draw_y[0] = (corner[1] + 13) * 3
top_prox = 0
mid_prox = 0
bot_prox = 0
fwd_prox = 0
buffspawn = [0, 0]
crabspawn = [0, 0]
clear_hp = [0] * limit
while(i < limit):
	ret, frame = cam.read()
	if ret:
		if(blueside):
			healthbar = frame[206:210, 20:48]
			manabar = frame[212:216, 20:48]
		else:
			healthbar = frame[206:210, 1103:1131]
			manabar = frame[212:216, 1103:1131]
		hp = checkbar(healthbar, 400)
		clear_hp[i] = hp
		i = i + 1
		mana = checkbar(manabar, 400)
		#cv2.imwrite('health/'+str(i)+'.jpg', frame[540:720, 972:1152])
		if(i == 254): buffspawn = [-1, -1]
		if(hp + mana > 0):
			if(stupid_cam == 0):
				minimap = frame[540:720, 972:1152]
				arr = asarray(minimap)
				rows, cols = (180, 180)
				diffs = [[0 for i in range(cols)] for j in range(rows)]
				for y in range(0, 180):
					for x in range(0, 180):
						total = sum(arr[y][x])
						dif = 765 - total
						diffs[y][x] = dif * dif
				horizontal = True
				search_space = [135, 10, 180, 30]
				if(blueside): search_space = [0, 140, 45, 160]
				base_row = search_h(search_space, diffs)
				if(blueside): search_space = [20, 140, 45, 180]
				else: search_space = [135, 0, 155, 30]
				base_col = search_v(search_space, diffs, 24)
				sx1 = corner[0] - 20
				sx2 = corner[0] + 62
				sy1 = corner[1] - 20
				sy2 = corner[1] + 44
				if(sx1 < 0): sx1 = 0
				if(sx2 > 180): sx2 = 180
				if(sy1 < 0): sy1 = 0
				if(sy2 > 180): sy2 = 180
				search_space = [sx1, sy1, sx2, sy2]
				near_row = search_h(search_space, diffs)
				near_col = search_v(search_space, diffs, 24)
				row = near_row
				col = near_col
				near_low = (near_row[2] + near_col[2])
				base_low = base_row[2] + base_col[2]
				base_low = base_low / 2
				lower_low = near_low
				if(near_low > base_low):
					row = base_row
					col = base_col
					lower_low = base_low
				if(lower_low < 3000000):
					corner = find_rect(row, col)
					#line = [line[2], line[3], (corner[0]+21)*3, (corner[1]+13)*3]
					wait_draw_x[i] = (corner[0]+21)*3
					wait_draw_y[i] = (corner[1]+13)*3
					if(dist(25, 25, corner[0], corner[1]) < 3200): top_prox = top_prox + 1
					if(dist(90, 90, corner[0], corner[1]) < 3200): mid_prox = mid_prox + 1
					if(dist(150, 150, corner[0], corner[1]) < 3200): bot_prox = bot_prox + 1
					if(blueside):
						if(corner[0] > corner[1] + 10): fwd_prox = fwd_prox + 1
					else:
						if(corner[1] > corner[0] + 10): fwd_prox = fwd_prox + 1
					# draw(dwg, line, blueside, i, limit + 600)
					if(i == 254): buffspawn = corner
					if(i == 1320): crabspawn = corner
				else:
					wait_draw_x[i] = 0
					wait_draw_y[i] = 0
				print(i, round(hp), round(mana), base_row, base_col, near_row, near_col, corner, near_low)
			else:
				print('waiting for camera')
				stupid_cam = stupid_cam - 1
		else:
			print('dead')
			stupid_cam = 5
	else:
		break
print(clear_hp)
print(top_prox, mid_prox, bot_prox, fwd_prox)
print(buffspawn)
print(crabspawn)

def linearize(line_list):
	#print(line_list)
	numlines = len(line_list)
	if(numlines == 0): return []
	first = line_list[0]
	last = line_list[-1]
	xd = (last[2] - first[0])/numlines
	yd = (last[3] - first[1])/numlines
	start = line_list[0]
	start[2] = start[0] + xd
	start[3] = start[1] + yd
	line_list[0] = start
	s = range(1, numlines)
	for straighten in s:
		last_line = line_list[straighten-1]
		line_list[straighten] = [last_line[2], last_line[3], last_line[2] + xd, last_line[3] + yd, line_list[straighten][4]]
	return line_list

def lineptdist(point, to):
	x1 = to[0]
	y1 = to[1]
	x2 = to[2]
	y2 = to[3]
	if(x2-x1 == 0):
		xd = point[2] - x1
		return xd * xd 
	else:
		a = (y2-y1)/(x2-x1)
		if(a == 0):
			#print('horizontal points line')
			yd = point[3] - x2
			return yd * yd
		else:
			b = -1/a
			c = y1 - (a*x1)
			cx = point[2]
			cy = point[3]
			d = cy - (b*cx)
			int_x = (d-c)/(a-b)
			int_y = (a*int_x)+c
			d1 = int_x - cx
			d2 = int_y - cy
			return (d1*d1)+(d2*d2) 

def addline(line_list, dwg, line, blueside, colortotal):
	line_list.append(line)
	x1 = line_list[0][0]
	y1 = line_list[0][1]
	x2 = line[2]
	y2 = line[3]
	distsum = 0
	numlines = len(line_list)
	check = range(1, numlines-1)
	for pt in check:
		distsum = distsum + lineptdist(line_list[pt], [x1, y1, x2, y2])
	distsum = distsum/numlines
	if(distsum > 10):
		drawlines(line_list, dwg, blueside, colortotal)
		line_list = []
	return line_list

def drawlines(line_list, dwg, blueside, colortotal):
	if(len(line_list) > 0):
		newline = [line_list[0][0], line_list[0][1], line_list[-1][2], line_list[-1][3], line_list[0][4]]
#		for check_overlap in linesdrawn:
#			on_line = lineptdist(check_overlap)
#			change_x = 1
#			change_y = 1
#			while(on_line < 10):
#				on_line = lineptdist[check_overlap, newline]
#				newline[0] = newline
#		linesdrawn.append(newline)
#		print(newline)
		draw(dwg, newline, blueside, newline[4], colortotal)

bases = 0
distances = [0 for i in range(limit + 1)]
last_x = wait_draw_x[0]
last_y = wait_draw_y[0]
for i in range(1, limit):
	if(wait_draw_x[i] + wait_draw_y[i] != 0):
		d1 = wait_draw_x[i] - last_x
		d2 = wait_draw_y[i] - last_y
		distances[i] = (d1*d1) + (d2*d2)
		if(distances[i] > 8000):
			bases = bases + 1
		last_x = wait_draw_x[i]	
		last_y = wait_draw_y[i]	

colortotal = bases
drawcolor = 0
last_x = wait_draw_x[0]
last_y = wait_draw_y[0]
currentlines = []

for i in range(1, limit):
	drawcolor = drawcolor
	if(wait_draw_x[i] + wait_draw_y[i] != 0):
		if(distances[i] > 8000):
#			print('GOING BACK')
			drawcolor = drawcolor + 1
			drawlines(currentlines, dwg, blueside, colortotal)
			currentlines = []
		else:
			line = [last_x, last_y, wait_draw_x[i], wait_draw_y[i], drawcolor]
			currentlines = addline(currentlines, dwg, line, blueside, colortotal)
		last_y = wait_draw_y[i]	
		last_x = wait_draw_x[i]	
drawlines(currentlines, dwg, blueside, colortotal)

dwg.save()
cam.release()
cv2.destroyAllWindows()
print('bh <? dn')
