
Instructions: Place in 'LOAD_LEVEL_DATA_[LEVELNUM]:'


PLACE_EXIT:



PLACE_PLAYER_MAP9:
	# Push return address to stack.
	addi	$sp, $sp, -4
	sw	$ra, 0($sp)
	la $a0, player_data
	jal LOAD_DATA
	li $t0, BASE_ADDRESS
	la $a0, player_data
	jal SAVE_DATA
	# Return to sender.
	lw	$ra, 0($sp)
	addi	$sp, $sp, 4
	jr	$ra
	

LOAD_SPIKES_MAP9:
	# Push return address to stack.
	addi	$sp, $sp, -4
	sw	$ra, 0($sp)
	# Return to sender.
	lw	$ra, 0($sp)
	addi	$sp, $sp, 4
	jr	$ra
	

LOAD_PICKUPS_MAP9:
	# Push return address to stack.
	addi	$sp, $sp, -4
	sw	$ra, 0($sp)
	# Load Level Data
	la $a0, level_data
	jal LOAD_DATA
	li $t0, 0
	sw $t0, 0(PICKUP_POINTER)
	sw $t0, 4(PICKUP_POINTER)
	la $a0, level_data
	jal SAVE_DATA
	# Return to sender.
	lw	$ra, 0($sp)
	addi	$sp, $sp, 4
	jr	$ra
	



	
	BRUSH_TOOL_RESULT:
	# Push return address to stack.
	addi	$sp, $sp, -4
	sw	$ra, 0($sp)
	addi $sp, $sp, -4
	sw $a0, 0($sp)
	# Drawing Layer 1
	li $a3, 0x006757aa
	lw $t0, 0($sp)
	addi $t0, $t0, 17316
	move $a0, $t0
	addi $t0, $t0, 8284
	move $a1, $t0
	li $a2, 88
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 25600
	move $a0, $t0
	addi $t0, $t0, 29696
	move $a1, $t0
	li $a2, 508
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 19968
	move $a0, $t0
	addi $t0, $t0, 5240
	move $a1, $t0
	li $a2, 116
	jal FILL
	
	li $a3, 0x006d5daf
	lw $t0, 0($sp)
	addi $t0, $t0, 50600
	move $a0, $t0
	addi $t0, $t0, 4
	move $a1, $t0
	li $a2, 0
	jal FILL
	
	li $a3, 0x009093dc
	lw $t0, 0($sp)
	addi $t0, $t0, 2868
	move $a0, $t0
	addi $t0, $t0, 8756
	move $a1, $t0
	li $a2, 48
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 4456
	move $a0, $t0
	addi $t0, $t0, 6236
	move $a1, $t0
	li $a2, 88
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 5380
	move $a0, $t0
	addi $t0, $t0, 4144
	move $a1, $t0
	li $a2, 44
	jal FILL
	
	# Drawing Layer 2
	li $a3, 0x006d5daf
	lw $t0, 0($sp)
	addi $t0, $t0, 31232
	move $a0, $t0
	addi $t0, $t0, 10240
	move $a1, $t0
	li $a2, 508
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 29696
	move $a0, $t0
	addi $t0, $t0, 1176
	move $a1, $t0
	li $a2, 148
	jal FILL
	
	li $a3, 0x009093dc
	lw $t0, 0($sp)
	addi $t0, $t0, 20564
	move $a0, $t0
	addi $t0, $t0, 2580
	move $a1, $t0
	li $a2, 16
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 21608
	move $a0, $t0
	addi $t0, $t0, 1600
	move $a1, $t0
	li $a2, 60
	jal FILL
	
	li $a3, 0x00ac9ad5
	lw $t0, 0($sp)
	addi $t0, $t0, 23624
	move $a0, $t0
	addi $t0, $t0, 560
	move $a1, $t0
	li $a2, 44
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 21584
	move $a0, $t0
	addi $t0, $t0, 1540
	move $a1, $t0
	li $a2, 0
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 9988
	move $a0, $t0
	addi $t0, $t0, 560
	move $a1, $t0
	li $a2, 44
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 11048
	move $a0, $t0
	addi $t0, $t0, 2060
	move $a1, $t0
	li $a2, 8
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 12084
	move $a0, $t0
	addi $t0, $t0, 1076
	move $a1, $t0
	li $a2, 48
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 11112
	move $a0, $t0
	addi $t0, $t0, 1096
	move $a1, $t0
	li $a2, 68
	jal FILL
	
	# Drawing Layer 3
	li $a3, 0x007a6aba
	lw $t0, 0($sp)
	addi $t0, $t0, 38912
	move $a0, $t0
	addi $t0, $t0, 1212
	move $a1, $t0
	li $a2, 184
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 40448
	move $a0, $t0
	addi $t0, $t0, 11264
	move $a1, $t0
	li $a2, 508
	jal FILL
	
	# Drawing Layer 4
	li $a3, 0x00292a47
	lw $t0, 0($sp)
	addi $t0, $t0, 41724
	move $a0, $t0
	addi $t0, $t0, 11016
	move $a1, $t0
	li $a2, 260
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 39200
	move $a0, $t0
	addi $t0, $t0, 2272
	move $a1, $t0
	li $a2, 220
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 38300
	move $a0, $t0
	addi $t0, $t0, 612
	move $a1, $t0
	li $a2, 96
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 33228
	move $a0, $t0
	addi $t0, $t0, 4660
	move $a1, $t0
	li $a2, 48
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 45640
	move $a0, $t0
	addi $t0, $t0, 3768
	move $a1, $t0
	li $a2, 180
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 50176
	move $a0, $t0
	addi $t0, $t0, 1608
	move $a1, $t0
	li $a2, 68
	jal FILL
	
	li $a3, 0x00293624
	lw $t0, 0($sp)
	addi $t0, $t0, 52224
	move $a0, $t0
	addi $t0, $t0, 13312
	move $a1, $t0
	li $a2, 508
	jal FILL
	
	# Drawing Layer 5
	li $a3, 0x001c1c27
	lw $t0, 0($sp)
	addi $t0, $t0, 44820
	move $a0, $t0
	addi $t0, $t0, 7352
	move $a1, $t0
	li $a2, 180
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 49736
	move $a0, $t0
	addi $t0, $t0, 2252
	move $a1, $t0
	li $a2, 200
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 50688
	move $a0, $t0
	addi $t0, $t0, 1096
	move $a1, $t0
	li $a2, 68
	jal FILL
	
	li $a3, 0x005b7550
	lw $t0, 0($sp)
	addi $t0, $t0, 52224
	move $a0, $t0
	addi $t0, $t0, 4096
	move $a1, $t0
	li $a2, 508
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 56724
	move $a0, $t0
	addi $t0, $t0, 2156
	move $a1, $t0
	li $a2, 104
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 56592
	move $a0, $t0
	addi $t0, $t0, 4128
	move $a1, $t0
	li $a2, 28
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 56368
	move $a0, $t0
	addi $t0, $t0, 2708
	move $a1, $t0
	li $a2, 144
	jal FILL
	
	# Drawing Layer 6
	li $a3, 0x0087486d
	lw $t0, 0($sp)
	addi $t0, $t0, 44184
	move $a0, $t0
	addi $t0, $t0, 8752
	move $a1, $t0
	li $a2, 44
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 45200
	move $a0, $t0
	addi $t0, $t0, 7688
	move $a1, $t0
	li $a2, 4
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 47244
	move $a0, $t0
	addi $t0, $t0, 5636
	move $a1, $t0
	li $a2, 0
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 39060
	move $a0, $t0
	addi $t0, $t0, 5172
	move $a1, $t0
	li $a2, 48
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 38024
	move $a0, $t0
	addi $t0, $t0, 572
	move $a1, $t0
	li $a2, 56
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 39044
	move $a0, $t0
	addi $t0, $t0, 1552
	move $a1, $t0
	li $a2, 12
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 39548
	move $a0, $t0
	addi $t0, $t0, 2060
	move $a1, $t0
	li $a2, 8
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 41072
	move $a0, $t0
	addi $t0, $t0, 524
	move $a1, $t0
	li $a2, 8
	jal FILL
	
	li $a3, 0x00181716
	lw $t0, 0($sp)
	addi $t0, $t0, 53016
	move $a0, $t0
	addi $t0, $t0, 1096
	move $a1, $t0
	li $a2, 68
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 53600
	move $a0, $t0
	addi $t0, $t0, 1544
	move $a1, $t0
	li $a2, 4
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 53520
	move $a0, $t0
	addi $t0, $t0, 1544
	move $a1, $t0
	li $a2, 4
	jal FILL
	
	li $a3, 0x00121212
	lw $t0, 0($sp)
	addi $t0, $t0, 54552
	move $a0, $t0
	addi $t0, $t0, 584
	move $a1, $t0
	li $a2, 68
	jal FILL
	
	# Drawing Layer 7
	li $a3, 0x001b1b1b
	lw $t0, 0($sp)
	addi $t0, $t0, 40608
	move $a0, $t0
	addi $t0, $t0, 3112
	move $a1, $t0
	li $a2, 36
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 44196
	move $a0, $t0
	addi $t0, $t0, 36
	move $a1, $t0
	li $a2, 32
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 40100
	move $a0, $t0
	addi $t0, $t0, 32
	move $a1, $t0
	li $a2, 28
	jal FILL
	
	li $a3, 0x00887e6e
	lw $t0, 0($sp)
	addi $t0, $t0, 54600
	move $a0, $t0
	addi $t0, $t0, 520
	move $a1, $t0
	li $a2, 4
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 54564
	move $a0, $t0
	addi $t0, $t0, 520
	move $a1, $t0
	li $a2, 4
	jal FILL
	
	li $a3, 0x00ab9f8d
	lw $t0, 0($sp)
	addi $t0, $t0, 53576
	move $a0, $t0
	addi $t0, $t0, 520
	move $a1, $t0
	li $a2, 4
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 53540
	move $a0, $t0
	addi $t0, $t0, 520
	move $a1, $t0
	li $a2, 4
	jal FILL
	
	li $a3, 0x00c0b4a1
	lw $t0, 0($sp)
	addi $t0, $t0, 49480
	move $a0, $t0
	addi $t0, $t0, 3592
	move $a1, $t0
	li $a2, 4
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 49444
	move $a0, $t0
	addi $t0, $t0, 3592
	move $a1, $t0
	li $a2, 4
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 48928
	move $a0, $t0
	addi $t0, $t0, 12
	move $a1, $t0
	li $a2, 8
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 48968
	move $a0, $t0
	addi $t0, $t0, 12
	move $a1, $t0
	li $a2, 8
	jal FILL
	
	# Drawing Layer 8
	li $a3, 0x00eaeaea
	lw $t0, 0($sp)
	addi $t0, $t0, 41128
	move $a0, $t0
	addi $t0, $t0, 1032
	move $a1, $t0
	li $a2, 4
	jal FILL
	lw $t0, 0($sp)
	addi $t0, $t0, 41148
	move $a0, $t0
	addi $t0, $t0, 1032
	move $a1, $t0
	li $a2, 4
	jal FILL
	
	# Drawing Layer 9
	# Drawing Layer 10
	# Drawing Layer 11
	addi	$sp, $sp, 4
	# Return to sender.
	lw	$ra, 0($sp)
	addi	$sp, $sp, 4
	jr	$ra
	

