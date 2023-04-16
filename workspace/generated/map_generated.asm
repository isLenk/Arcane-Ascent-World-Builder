DRAW_MAP9:
	# Push return address to stack.
	addi	$sp, $sp, -4
	sw	$ra, 0($sp)
	jal PLACE_PLAYER_MAP9
	jal LOAD_SPIKES_MAP9
	jal LOAD_PICKUPS_MAP9
	li $t1, WALL_COLOR
	# Return to sender.
	lw	$ra, 0($sp)
	addi	$sp, $sp, 4
	jr	$ra
	