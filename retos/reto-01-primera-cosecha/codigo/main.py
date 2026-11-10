while True:
	for i in range(get_world_size()):
		harvest()
		if i == 2:
			plant(Entities.Bush)
		move(North)
	move(East)