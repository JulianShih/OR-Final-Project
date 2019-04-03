#-*- coding:utf-8 -*-
from pulp import *

name = input('Please input FS Entry：\n(yuzuru nathan shoma kolyada cha jason jin tsao)\n')

Jumps = ['t4_base1', 't4_base2','s4_base1', 's4_base2',
		'lo4_base1', 'lo4_base2','f4_base1', 'f4_base2',
		'lz4_base1', 'lz4_base2', 
		't3_base1', 't3_base2','s3_base1', 's3_base2',
		'lo3_base1', 'lo3_base2','f3_base1', 'f3_base2', 
		'lz3_base1', 'lz3_base2', 
		'a3_base1','a3_base2','a2_base1', 'a2_base2',
		't3_combo1', 't3_combo2','s3_combo1', 's3_combo2',
		'lo3_combo1', 'lo3_combo2','f3_combo1', 'f3_combo2',
		't2_combo1', 't2_combo2','s2_combo1', 's2_combo2',
		'lo2_combo1', 'lo2_combo2','f2_combo1', 'f2_combo2']

base_value = {'t4_base1': 9.5,
         't4_base2': 9.5,  	
		 's4_base1': 9.7,
		 's4_base2': 9.7,
		 'lo4_base1':10.5,
		 'lo4_base2':10.5,
		 'f4_base1': 11,
		 'f4_base2': 11,
		 'lz4_base1': 11.5,
		 'lz4_base2': 11.5,
		 't3_base1': 4.2,
		 't3_base2': 4.2,
         's3_base1': 4.3,
         's3_base2': 4.3,	
		 'lo3_base1':4.9,
		 'lo3_base2':4.9,			 	
		 'f3_base1': 5.3,	
		 'f3_base2': 5.3,
         'lz3_base1': 5.9,
         'lz3_base2': 5.9,
		 'a3_base1': 8,
		 'a3_base2': 8,
		 'a2_base1': 3.3,
		 'a2_base2': 3.3,	
		 't3_combo1': 4.2,
		 't3_combo2': 4.2,
		 's3_combo1': 4.3,
		 's3_combo2': 4.3,
		 'lo3_combo1': 4.9,
		 'lo3_combo2': 4.9,
		 'f3_combo1': 5.3,
		 'f3_combo2': 5.3,
		 't2_combo1': 1.3,
		 't2_combo2': 1.3,
		 's2_combo1': 1.3,
		 's2_combo2': 1.3,
		 'lo2_combo1': 1.7,
		 'lo2_combo2': 1.7,
		 'f2_combo1': 1.8,
		 'f2_combo2': 1.8}
yuzuru = {'t4_base1': 0.75,
         't4_base2': 0.75,  	
		 's4_base1': 0.895,
		 's4_base2': 0.895,
		 'lo4_base1': 0.677,
		 'lo4_base2': 0.677,
		 'f4_base1': 0,
		 'f4_base2': 0,
		 'lz4_base1': 0.45,
		 'lz4_base2': 0.45,
		 't3_base1': 0,
		 't3_base2': 0,
         's3_base1': 0.75,
         's3_base2': 0.75,	
		 'lo3_base1': 1,
		 'lo3_base2': 1,			 	
		 'f3_base1': 0.863,	
		 'f3_base2': 0.863,
         'lz3_base1': 0.8,
         'lz3_base2': 0.8,
		 'a3_base1': 0.953,
		 'a3_base2': 0.953,
		 'a2_base1': 0,
		 'a2_base2': 0,	
		 't3_combo1': 0.964,
		 't3_combo2': 0.964,
		 's3_combo1': 1,
		 's3_combo2': 1,
		 'lo3_combo1': 0,
		 'lo3_combo2': 0,
		 'f3_combo1': 0,
		 'f3_combo2': 0,
		 't2_combo1': 0.875,
		 't2_combo2': 0.875,
		 's2_combo1': 0.834,
		 's2_combo2': 0.834,
		 'lo2_combo1': 0,
		 'lo2_combo2': 0,
		 'f2_combo1': 0,
		 'f2_combo2': 0}
nathan = {'t4_base1': 0.75,
         't4_base2': 0.75,  	
		 's4_base1': 0.75,
		 's4_base2': 0.75,
		 'lo4_base1': 0.34,
		 'lo4_base2': 0.34,
		 'f4_base1': 0.779,
		 'f4_base2': 0.779,
		 'lz4_base1': 0.796,
		 'lz4_base2': 0.796,
		 't3_base1': 0,
		 't3_base2': 0,
         's3_base1': 0.833,
         's3_base2': 0.833,	
		 'lo3_base1': 1,
		 'lo3_base2': 1,			 	
		 'f3_base1': 0.875,	
		 'f3_base2': 0.875,
         'lz3_base1': 0.93,
         'lz3_base2': 0.93,
		 'a3_base1': 0.774,
		 'a3_base2': 0.774,
		 'a2_base1': 0.833,
		 'a2_base2': 0.833,	
		 't3_combo1': 0.861,
		 't3_combo2': 0.861,
		 's3_combo1': 1,
		 's3_combo2': 1,
		 'lo3_combo1': 0,
		 'lo3_combo2': 0,
		 'f3_combo1': 0,
		 'f3_combo2': 0,
		 't2_combo1': 0.85,
		 't2_combo2': 0.85,
		 's2_combo1': 1,
		 's2_combo2': 1.,
		 'lo2_combo1': 0.888,
		 'lo2_combo2': 0.888,
		 'f2_combo1': 0,
		 'f2_combo2': 0}
shoma = {'t4_base1': 0.767,
         't4_base2': 0.767,  	
		 's4_base1': 0.875,
		 's4_base2': 0.875,
		 'lo4_base1': 0.65,
		 'lo4_base2': 0.65,
		 'f4_base1': 0.654,
		 'f4_base2': 0.654,
		 'lz4_base1': 0,
		 'lz4_base2': 0,
		 't3_base1': 0,
		 't3_base2': 0,
         's3_base1': 0.875,
         's3_base2': 0.875,
		 'lo3_base1': 0.95,
		 'lo3_base2': 0.95,	 	
		 'f3_base1': 0,
		 'f3_base2': 0,
         'lz3_base1': 0.714,
         'lz3_base2': 0.714,
		 'a3_base1':  0.862,
		 'a3_base2': 0.862,
		 'a2_base1': 0,
		 'a2_base2': 0,
		 't3_combo1': 0.863,
		 't3_combo2': 0.863,
		 's3_combo1': 0,
		 's3_combo2': 0,
		 'lo3_combo1': 0,
		 'lo3_combo2': 0,
		 'f3_combo1': 0.866,
		 'f3_combo2': 0.866,
		 't2_combo1': 0.921,
		 't2_combo2': 0.921,
		 's2_combo1': 0,
		 's2_combo2': 0,
		 'lo2_combo1':0,
		 'lo2_combo2':0,
		 'f2_combo1': 0,
		 'f2_combo2': 0}
kolyada = {'t4_base1': 0.797,
         't4_base2': 0.797,  	
		 's4_base1': 0.5,
		 's4_base2': 0.5,
		 'lo4_base1': 0,
		 'lo4_base2': 0,
		 'f4_base1': 0,
		 'f4_base2': 0,
		 'lz4_base1':0.526,
		 'lz4_base2':0.526,
		 't3_base1': 0.714,
		 't3_base2': 0.714,
         's3_base1': 0.944,
         's3_base2': 0.944,
		 'lo3_base1':0.875,
		 'lo3_base2':0.875, 	
		 'f3_base1': 0,
		 'f3_base2': 0,
         'lz3_base1':0.938, 
         'lz3_base2':0.938, 
		 'a3_base1': 0.464,
		 'a3_base2': 0.464,
		 'a2_base1': 0.5,
		 'a2_base2': 0.5,
		 't3_combo1': 0.96,
		 't3_combo2': 0.96,
		 's3_combo1': 0.937,
		 's3_combo2': 0.937,
		 'lo3_combo1': 0,
		 'lo3_combo2': 0,
		 'f3_combo1': 0,
		 'f3_combo2': 0,
		 't2_combo1': 0.98,
		 't2_combo2': 0.98,
		 's2_combo1': 1,
		 's2_combo2': 1,
		 'lo2_combo1': 0,
		 'lo2_combo2': 0,
		 'f2_combo1': 0,
		 'f2_combo2': 0}
cha = {'t4_base1': 0.6, 
         't4_base2': 0.6, 	
		 's4_base1': 0.55,
		 's4_base2': 0.55,
		 'lo4_base1': 0,
		 'lo4_base2': 0,
		 'f4_base1': 0,
		 'f4_base2': 0,
		 'lz4_base1':0,
		 'lz4_base2':0,
		 't3_base1': 0,
		 't3_base2': 0,
         's3_base1': 0,
         's3_base2': 0,
		 'lo3_base1':1,
		 'lo3_base2':1,	 	
		 'f3_base1': 0.667, 
		 'f3_base2': 0.667, 
         'lz3_base1':0.884, 
         'lz3_base2':0.884, 
		 'a3_base1': 0.868,
		 'a3_base2': 0.868,
		 'a2_base1': 0,
		 'a2_base2': 0,
		 't3_combo1': 0.833,
		 't3_combo2': 0.833,
		 's3_combo1': 0.4,
		 's3_combo2': 0.4,
		 'lo3_combo1': 0.85,
		 'lo3_combo2': 0.85,
		 'f3_combo1': 0,
		 'f3_combo2': 0,
		 't2_combo1': 0.834,
		 't2_combo2': 0.834,
		 's2_combo1': 0,
		 's2_combo2': 0,
		 'lo2_combo1':0,
		 'lo2_combo2':0,
		 'f2_combo1': 0,
		 'f2_combo2': 0}
jason = {'t4_base1': 0.125, 
         't4_base2': 0.125,  	
		 's4_base1': 0,
		 's4_base2': 0,
		 'lo4_base1': 0,
		 'lo4_base2': 0,
		 'f4_base1': 0, 
		 'f4_base2': 0, 
		 'lz4_base1':0,
		 'lz4_base2':0,
		 't3_base1': 0, 
		 't3_base2': 0, 
         's3_base1': 1, 
         's3_base2': 1, 
		 'lo3_base1':0.818,
		 'lo3_base2':0.818,	 	
		 'f3_base1': 0.9, 
		 'f3_base2': 0.9, 
         'lz3_base1':0.775, 
         'lz3_base2':0.775, 
		 'a3_base1': 0.711,
		 'a3_base2': 0.711,
		 'a2_base1': 0.974,
		 'a2_base2': 0.974,
		 't3_combo1': 0.815,
		 't3_combo2': 0.815,
		 's3_combo1': 0.778,
		 's3_combo2': 0.778,
		 'lo3_combo1': 0,
		 'lo3_combo2': 0,
		 'f3_combo1':  0,
		 'f3_combo2':  0,
		 't2_combo1': 0.868,
		 't2_combo2': 0.868,
		 's2_combo1': 0.833,
		 's2_combo2': 0.833,
		 'lo2_combo1':0.5,
		 'lo2_combo2':0.5,
		 'f2_combo1':  0,
		 'f2_combo2':  0}
jin = {'t4_base1': 0.614, 
         't4_base2': 0.614, 
		 's4_base1': 0.65,
		 's4_base2': 0.65,
		 'lo4_base1': 0,
		 'lo4_base2': 0,
		 'f4_base1': 0,
		 'f4_base2': 0,
		 'lz4_base1':0.75,
		 'lz4_base2':0.75,
		 't3_base1': 0, 
		 't3_base2': 0, 
         's3_base1': 0,
         's3_base2': 0,
		 'lo3_base1':0.5,
		 'lo3_base2':0.5, 	
		 'f3_base1': 0.833, 
		 'f3_base2': 0.833, 
         'lz3_base1':0.692, 
         'lz3_base2':0.692, 
		 'a3_base1': 0.824,
		 'a3_base2': 0.824,
		 'a2_base1': 0,
		 'a2_base2': 0,
		 't3_combo1': 0.789,
		 't3_combo2': 0.789,
		 's3_combo1': 0.778,
		 's3_combo2': 0.778,
		 'lo3_combo1':0,
		 'lo3_combo2':0,
		 'f3_combo1': 0,
		 'f3_combo2': 0,
		 't2_combo1': 0.571,
		 't2_combo2': 0.571,
		 's2_combo1': 0,
		 's2_combo2': 0,
		 'lo2_combo1':0,
		 'lo2_combo2':0,
		 'f2_combo1': 0,
		 'f2_combo2': 0}
tsao = {'t4_base1': 0.5, 
         't4_base2': 0.5, 
		 's4_base1': 0,
		 's4_base2': 0,
		 'lo4_base1': 0,
		 'lo4_base2': 0,
		 'f4_base1': 0,
		 'f4_base2': 0,
		 'lz4_base1': 0,
		 'lz4_base2': 0,
		 't3_base1': 0,
		 't3_base2': 0,
         's3_base1': 0.591, 
         's3_base2': 0.591, 
		 'lo3_base1':0.571,
		 'lo3_base2':0.571, 	
		 'f3_base1': 0.789,
		 'f3_base2': 0.789,
         'lz3_base1': 0.611, 
         'lz3_base2': 0.611, 
		 'a3_base1': 0.464,
		 'a3_base2': 0.464,
		 'a2_base1': 0.5,
		 'a2_base2': 0.5,
		 't3_combo1': 0.75,
		 't3_combo2': 0.75,
		 's3_combo1': 0,
		 's3_combo2': 0,
		 'lo3_combo1':0,
		 'lo3_combo2':0,
		 'f3_combo1': 0,
		 'f3_combo2': 0,
		 't2_combo1': 0.731,
		 't2_combo2': 0.731,
		 's2_combo1': 0,
		 's2_combo2': 0,
		 'lo2_combo1':0.667,
		 'lo2_combo2':0.667,
		 'f2_combo1': 0,
		 'f2_combo2': 0}

#定義問題
prob = pulp.LpProblem('The New Era On Ice', pulp.LpMaximize)
#利用dictionary 加入變數
jump_vars = LpVariable.dicts('Jump', Jumps, 0, cat='Binary')
#加入目標式
if name == 'yuzuru':
	prob += lpSum([base_value[i]*yuzuru[i]*jump_vars[i] for i in Jumps[0:40]])
if name == 'nathan':
	prob += lpSum([base_value[i]*nathan[i]*jump_vars[i] for i in Jumps[0:40]])
if name == 'shoma':
	prob += lpSum([base_value[i]*shoma[i]*jump_vars[i] for i in Jumps[0:40]])
if name == 'kolyada':
	prob += lpSum([base_value[i]*kolyada[i]*jump_vars[i] for i in Jumps[0:40]])
if name == 'cha':
	prob += lpSum([base_value[i]*cha[i]*jump_vars[i] for i in Jumps[0:40]])
if name == 'jason':
	prob += lpSum([base_value[i]*jason[i]*jump_vars[i] for i in Jumps[0:40]])
if name == 'jin':
	prob += lpSum([base_value[i]*jin[i]*jump_vars[i] for i in Jumps[0:40]])
if name == 'tsao':
	prob += lpSum([base_value[i]*tsao[i]*jump_vars[i] for i in Jumps[0:40]])

#加入限制式
prob += lpSum([jump_vars[i] for i in Jumps[0:24]]) == 7 #base
prob += lpSum([jump_vars[i] for i in Jumps[24:40]]) >= 1 #combo
prob += lpSum([jump_vars[i] for i in Jumps[24:40]]) <= 3 #combo
prob += (jump_vars['t4_base2'] + jump_vars['s4_base2'] + jump_vars['lo4_base2']
		+ jump_vars['f4_base2'] + jump_vars['lz4_base2'] 
		+ jump_vars['t3_base2'] + jump_vars['s3_base2'] + jump_vars['lo3_base2']
		+ jump_vars['f3_base2'] + jump_vars['lz3_base2']
		+ jump_vars['a3_base2'] + jump_vars['t3_combo2'] + jump_vars['s3_combo2']
		+ jump_vars['lo3_combo2'] + jump_vars['f3_combo2']) <= 2 #4.3rep
prob += (jump_vars['t4_base2'] + jump_vars['s4_base2'] + jump_vars['lo4_base2'] + jump_vars['f4_base2'] + jump_vars['lz4_base2']) <= 1  #4rep
prob += lpSum([jump_vars[i] for i in Jumps[20:24]]) >= 1 #Axel
prob += (jump_vars['t3_base1'] + jump_vars['t3_base2'] + jump_vars['t3_combo1'] + jump_vars['t3_combo2']) <= 2
prob += (jump_vars['s3_base1'] + jump_vars['s3_base2'] + jump_vars['s3_combo1'] + jump_vars['s3_combo2']) <= 2
prob += (jump_vars['lo3_base1'] + jump_vars['lo3_base2'] + jump_vars['lo3_combo1'] + jump_vars['lo3_combo2']) <= 2
prob += (jump_vars['f3_base1'] + jump_vars['f3_base2'] + jump_vars['f3_combo1'] + jump_vars['f3_combo2']) <= 2
prob += (jump_vars['t3_base1'] + jump_vars['t3_combo1'] + jump_vars['t3_base2'] + jump_vars['s3_base2'] + jump_vars['lo3_base2']
		+ jump_vars['f3_base2'] + jump_vars['lz3_base2']
		+ jump_vars['a3_base2'] + jump_vars['t3_combo2'] + jump_vars['s3_combo2']
		+ jump_vars['lo3_combo2'] + jump_vars['f3_combo2'])<=3
prob += (jump_vars['s3_base1'] + jump_vars['s3_combo1'] + jump_vars['t3_base2'] + jump_vars['s3_base2'] + jump_vars['lo3_base2']
		+ jump_vars['f3_base2'] + jump_vars['lz3_base2']
		+ jump_vars['a3_base2'] + jump_vars['t3_combo2'] + jump_vars['s3_combo2']
		+ jump_vars['lo3_combo2'] + jump_vars['f3_combo2'])<=3
prob += (jump_vars['lo3_base1'] + jump_vars['lo3_combo1'] + jump_vars['t3_base2'] + jump_vars['s3_base2'] + jump_vars['lo3_base2']
		+ jump_vars['f3_base2'] + jump_vars['lz3_base2']
		+ jump_vars['a3_base2'] + jump_vars['t3_combo2'] + jump_vars['s3_combo2']
		+ jump_vars['lo3_combo2'] + jump_vars['f3_combo2'])<=3
prob += (jump_vars['f3_base1'] + jump_vars['f3_combo1'] + jump_vars['t3_base2'] + jump_vars['s3_base2'] + jump_vars['lo3_base2']
		+ jump_vars['f3_base2'] + jump_vars['lz3_base2']
		+ jump_vars['a3_base2'] + jump_vars['t3_combo2'] + jump_vars['s3_combo2']
		+ jump_vars['lo3_combo2'] + jump_vars['f3_combo2'])<=3

#求解
prob.solve()

#查看目前解的狀態
print("Status:", LpStatus[prob.status])

program = []
singlejump=[]
combojump=[]

for i in Jumps:
	if jump_vars[i].varValue>0:
		print(jump_vars[i],"=",jump_vars[i].varValue)
		if 'base1' in jump_vars[i].name :
			singlejump.append(base_value[i])
		if 'base2' in jump_vars[i].name :
			program.append(base_value[i])
		if 'combo' in jump_vars[i].name :
			combojump.append(base_value[i])

combojump.sort(reverse=True)
singlejump.sort(reverse=True)
program += singlejump
for i in range(len(combojump)):
	program[i] += combojump[i]
print(program)
fs = [program[3],program[0],program[1],program[4],program[2]*1.1,program[5]*1.1,program[6]*1.1]
fsr = [round(x,3) for x in fs]
print("--------------------------")
print("Program:", fsr)
print("Optimal Jump TES:", round(sum(fs),3))