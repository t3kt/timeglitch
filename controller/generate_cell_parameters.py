def cook(scriptOP):
	if not scriptOP['hand_l:tx']:
		chop.clear()
		chop.copy(op('defaults'))
	playersin = scriptOP.inputs[0]
	handsin = scriptOP.inputs[1]
	activecount = 0
	firstactive = 0
	xbounds = scriptOP.par.value0x, scriptOP.par.value1x
	ybounds = scriptOP.par.value0y, scriptOP.par.value1y
	zbounds = scriptOP.par.value0z, scriptOP.par.value1z
	outbounds = 0, 1
	playername = op('cell')[1, 'player'].val
	active = 1 if playername else 0
	scriptOP.appendChan('active')[0] = active
	if not active:
		return
	scriptOP['hand_l:tx'] = scale(handsin[playername + '/hand_l:tx'], xbounds)
	scriptOP['hand_l:ty'] = scale(handsin[playername + '/hand_l:ty'], ybounds)
	scriptOP['hand_l:tz'] = scale(handsin[playername + '/hand_l:tz'], zbounds)
	scriptOP['hand_r:tx'] = scale(handsin[playername + '/hand_r:tx'], xbounds)
	scriptOP['hand_r:ty'] = scale(handsin[playername + '/hand_r:ty'], ybounds)
	scriptOP['hand_r:tz'] = scale(handsin[playername + '/hand_r:tz'], zbounds)

def scale(x, inrange):
	return (x - inrange[0])/(inrange[1] - inrange[0])
