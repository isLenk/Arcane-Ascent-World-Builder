DRAW_MAP9:
	# Push return address to stack.
	addi	$sp, $sp, -4
	sw	$ra, 0($sp)
	jal PLACE_PLAYER_MAP9
	jal LOAD_SPIKES_MAP9
	jal LOAD_PICKUPS_MAP9
	li $t1, WALL_COLOR
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 5120
	move $a0, $t0
	addi $t0, $t0, 43524
	move $a1, $t0
	li $a2, 0
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 48132
	move $a0, $t0
	addi $t0, $t0, 1016
	move $a1, $t0
	li $a2, 500
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 37288
	move $a0, $t0
	addi $t0, $t0, 1108
	move $a1, $t0
	li $a2, 80
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 38844
	move $a0, $t0
	addi $t0, $t0, 1088
	move $a1, $t0
	li $a2, 60
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 40416
	move $a0, $t0
	addi $t0, $t0, 2588
	move $a1, $t0
	li $a2, 24
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 43500
	move $a0, $t0
	addi $t0, $t0, 4624
	move $a1, $t0
	li $a2, 12
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 11268
	move $a0, $t0
	addi $t0, $t0, 1080
	move $a1, $t0
	li $a2, 52
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 12804
	move $a0, $t0
	addi $t0, $t0, 2592
	move $a1, $t0
	li $a2, 28
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 5628
	move $a0, $t0
	addi $t0, $t0, 43524
	move $a1, $t0
	li $a2, 0
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 15876
	move $a0, $t0
	addi $t0, $t0, 7188
	move $a1, $t0
	li $a2, 16
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 6580
	move $a0, $t0
	addi $t0, $t0, 9288
	move $a1, $t0
	li $a2, 68
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 16340
	move $a0, $t0
	addi $t0, $t0, 7208
	move $a1, $t0
	li $a2, 36
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 24036
	move $a0, $t0
	addi $t0, $t0, 4632
	move $a1, $t0
	li $a2, 20
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 42092
	move $a0, $t0
	addi $t0, $t0, 5652
	move $a1, $t0
	li $a2, 16
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 40020
	move $a0, $t0
	addi $t0, $t0, 1604
	move $a1, $t0
	li $a2, 64
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 42112
	move $a0, $t0
	addi $t0, $t0, 2064
	move $a1, $t0
	li $a2, 12
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 42076
	move $a0, $t0
	addi $t0, $t0, 3088
	move $a1, $t0
	li $a2, 12
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 38484
	move $a0, $t0
	addi $t0, $t0, 1060
	move $a1, $t0
	li $a2, 32
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 15016
	move $a0, $t0
	addi $t0, $t0, 3212
	move $a1, $t0
	li $a2, 136
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 23556
	move $a0, $t0
	addi $t0, $t0, 15372
	move $a1, $t0
	li $a2, 8
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 39428
	move $a0, $t0
	addi $t0, $t0, 3080
	move $a1, $t0
	li $a2, 4
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 18640
	move $a0, $t0
	addi $t0, $t0, 4708
	move $a1, $t0
	li $a2, 96
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 23780
	move $a0, $t0
	addi $t0, $t0, 4672
	move $a1, $t0
	li $a2, 60
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 28916
	move $a0, $t0
	addi $t0, $t0, 3108
	move $a1, $t0
	li $a2, 32
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 23844
	move $a0, $t0
	addi $t0, $t0, 2100
	move $a1, $t0
	li $a2, 48
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 16316
	move $a0, $t0
	addi $t0, $t0, 4632
	move $a1, $t0
	li $a2, 20
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 6488
	move $a0, $t0
	addi $t0, $t0, 3164
	move $a1, $t0
	li $a2, 88
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 27988
	move $a0, $t0
	addi $t0, $t0, 1592
	move $a1, $t0
	li $a2, 52
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 26428
	move $a0, $t0
	addi $t0, $t0, 1060
	move $a1, $t0
	li $a2, 32
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 16256
	move $a0, $t0
	addi $t0, $t0, 1084
	move $a1, $t0
	li $a2, 56
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 32520
	move $a0, $t0
	addi $t0, $t0, 1088
	move $a1, $t0
	li $a2, 60
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 34068
	move $a0, $t0
	addi $t0, $t0, 4640
	move $a1, $t0
	li $a2, 28
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 34100
	move $a0, $t0
	addi $t0, $t0, 1548
	move $a1, $t0
	li $a2, 8
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 45344
	move $a0, $t0
	addi $t0, $t0, 2764
	move $a1, $t0
	li $a2, 200
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 28712
	move $a0, $t0
	addi $t0, $t0, 1072
	move $a1, $t0
	li $a2, 44
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 23700
	move $a0, $t0
	addi $t0, $t0, 1616
	move $a1, $t0
	li $a2, 76
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 46596
	move $a0, $t0
	addi $t0, $t0, 1052
	move $a1, $t0
	li $a2, 24
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 45632
	move $a0, $t0
	addi $t0, $t0, 2092
	move $a1, $t0
	li $a2, 40
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 11836
	move $a0, $t0
	addi $t0, $t0, 2668
	move $a1, $t0
	li $a2, 104
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 14908
	move $a0, $t0
	addi $t0, $t0, 2064
	move $a1, $t0
	li $a2, 12
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 12836
	move $a0, $t0
	addi $t0, $t0, 7192
	move $a1, $t0
	li $a2, 20
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 14964
	move $a0, $t0
	addi $t0, $t0, 1588
	move $a1, $t0
	li $a2, 48
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 22644
	move $a0, $t0
	addi $t0, $t0, 572
	move $a1, $t0
	li $a2, 56
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 23684
	move $a0, $t0
	addi $t0, $t0, 1040
	move $a1, $t0
	li $a2, 12
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 33296
	move $a0, $t0
	addi $t0, $t0, 1052
	move $a1, $t0
	li $a2, 24
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 34832
	move $a0, $t0
	addi $t0, $t0, 2064
	move $a1, $t0
	li $a2, 12
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 31348
	move $a0, $t0
	addi $t0, $t0, 2112
	move $a1, $t0
	li $a2, 60
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 33944
	move $a0, $t0
	addi $t0, $t0, 540
	move $a1, $t0
	li $a2, 24
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 30344
	move $a0, $t0
	addi $t0, $t0, 556
	move $a1, $t0
	li $a2, 40
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 30900
	move $a0, $t0
	addi $t0, $t0, 2580
	move $a1, $t0
	li $a2, 16
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 18616
	move $a0, $t0
	addi $t0, $t0, 1048
	move $a1, $t0
	li $a2, 20
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 44316
	move $a0, $t0
	addi $t0, $t0, 576
	move $a1, $t0
	li $a2, 60
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 43448
	move $a0, $t0
	addi $t0, $t0, 1588
	move $a1, $t0
	li $a2, 48
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 6372
	move $a0, $t0
	addi $t0, $t0, 1652
	move $a1, $t0
	li $a2, 112
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 10140
	move $a0, $t0
	addi $t0, $t0, 2072
	move $a1, $t0
	li $a2, 20
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 10128
	move $a0, $t0
	addi $t0, $t0, 1036
	move $a1, $t0
	li $a2, 8
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 15232
	move $a0, $t0
	addi $t0, $t0, 532
	move $a1, $t0
	li $a2, 16
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 6300
	move $a0, $t0
	addi $t0, $t0, 584
	move $a1, $t0
	li $a2, 68
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 9808
	move $a0, $t0
	addi $t0, $t0, 1564
	move $a1, $t0
	li $a2, 24
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 6148
	move $a0, $t0
	addi $t0, $t0, 32
	move $a1, $t0
	li $a2, 28
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 10376
	move $a0, $t0
	addi $t0, $t0, 1056
	move $a1, $t0
	li $a2, 28
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 12456
	move $a0, $t0
	addi $t0, $t0, 2080
	move $a1, $t0
	li $a2, 28
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 13512
	move $a0, $t0
	addi $t0, $t0, 1044
	move $a1, $t0
	li $a2, 16
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 19800
	move $a0, $t0
	addi $t0, $t0, 6152
	move $a1, $t0
	li $a2, 4
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 25440
	move $a0, $t0
	addi $t0, $t0, 2072
	move $a1, $t0
	li $a2, 20
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 17812
	move $a0, $t0
	addi $t0, $t0, 1576
	move $a1, $t0
	li $a2, 36
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 19876
	move $a0, $t0
	addi $t0, $t0, 2064
	move $a1, $t0
	li $a2, 12
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 22444
	move $a0, $t0
	addi $t0, $t0, 1544
	move $a1, $t0
	li $a2, 4
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 13604
	move $a0, $t0
	addi $t0, $t0, 1048
	move $a1, $t0
	li $a2, 20
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 18768
	move $a0, $t0
	addi $t0, $t0, 532
	move $a1, $t0
	li $a2, 16
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 19796
	move $a0, $t0
	addi $t0, $t0, 1028
	move $a1, $t0
	li $a2, 0
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 21856
	move $a0, $t0
	addi $t0, $t0, 3080
	move $a1, $t0
	li $a2, 4
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 13040
	move $a0, $t0
	addi $t0, $t0, 1572
	move $a1, $t0
	li $a2, 32
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 41348
	move $a0, $t0
	addi $t0, $t0, 536
	move $a1, $t0
	li $a2, 20
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 42376
	move $a0, $t0
	addi $t0, $t0, 2576
	move $a1, $t0
	li $a2, 12
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 5124
	move $a0, $t0
	addi $t0, $t0, 1016
	move $a1, $t0
	li $a2, 500
	li $a3, WALL_COLOR
	jal FILL
	li $t0, BASE_ADDRESS
	addi $t0, $t0, 6244
	move $a0, $t0
	addi $t0, $t0, 528
	move $a1, $t0
	li $a2, 12
	li $a3, WALL_COLOR
	jal FILL
	# Return to sender.
	lw	$ra, 0($sp)
	addi	$sp, $sp, 4
	jr	$ra
	