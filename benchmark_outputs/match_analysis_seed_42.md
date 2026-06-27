# Bomberman AI Detailed Match Analysis
**Seed:** 42
**Roster:**
- **Agent 1 (player_1):** Backtracking
- **Agent 2 (player_2):** AndOrSearch
- **Agent 3 (player_3):** Minimax
- **Agent 4 (player_4):** Expectimax

========================================

## STEP 0
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# 1 . . # B . . . B B . . 2 #|
|# . # . . . . B . . B B . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . . B . . . B . . . #|
|# 3 . # B . . . B . . . . 4 #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (13, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 11) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 4):** ALIVE | Pos: (13, 11) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `DOWN` (took 14.43 ms)
- **Agent 2 (AndOrSearch):** chose `LEFT` (took 13.05 ms)
- **Agent 3 (Minimax):** chose `UP` (took 13.65 ms)
- **Agent 4 (Expectimax):** chose `UP` (took 13.03 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 1
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . 2 . #|
|# 1 # . . . . B . . B B . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# 3 . . . . B . . . B . . 4 #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 4):** ALIVE | Pos: (13, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 17.59 ms)
- **Agent 2 (AndOrSearch):** chose `DOWN` (took 15.89 ms)
- **Agent 3 (Minimax):** chose `RIGHT` (took 18.77 ms)
- **Agent 4 (Expectimax):** chose `LEFT` (took 16.74 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 2
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . 3 . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 16.24 ms)
- **Agent 2 (AndOrSearch):** chose `BOMB` (took 17.31 ms)
- **Agent 3 (Minimax):** chose `BOMB` (took 16.41 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.39 ms)

### Events during this step:
- 💣 **AndOrSearch** placed a bomb at (12, 2)
- 💣 **Minimax** placed a bomb at (2, 10)

----------------------------------------

## STEP 3
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . 3 . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 10) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.57 ms)
- **Agent 2 (AndOrSearch):** chose `DOWN` (took 15.04 ms)
- **Agent 3 (Minimax):** chose `LEFT` (took 13.66 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.48 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 4
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B B O . #|
|# B B # . . . B . B . B 2 B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# 3 O . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.40 ms)
- **Agent 2 (AndOrSearch):** chose `DOWN` (took 13.70 ms)
- **Agent 3 (Minimax):** chose `UP` (took 13.79 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.66 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 5
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B B O . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B 2 . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# 3 B B # . . # B # . # . . #|
|# . O . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.32 ms)
- **Agent 2 (AndOrSearch):** chose `DOWN` (took 14.62 ms)
- **Agent 3 (Minimax):** chose `UP` (took 13.47 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.11 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 6
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B B O . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . 2 B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# 3 B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . O . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (12, 5) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.51 ms)
- **Agent 2 (AndOrSearch):** chose `LEFT` (took 10.94 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 13.89 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.74 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 7
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B B O . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # 2 . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# 3 B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . O . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 5) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.87 ms)
- **Agent 2 (AndOrSearch):** chose `DOWN` (took 13.45 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 10.62 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.11 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 8
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B B O . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . 2 B . #|
|# . . B B B . . B . B . . . #|
|# 3 B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . O . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.19 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.00 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 14.02 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.25 ms)

### Events during this step:
- 💥 Bomb owned by **AndOrSearch** exploded at (12, 2) with range 1
- 💥 Bomb owned by **Minimax** exploded at (2, 10) with range 1
- 🧱 Brick destroyed at (2, 9)
- 🧱 Brick destroyed at (11, 2)

----------------------------------------

## STEP 9
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . * . #|
|# 1 # . . . . B . . B C * * #|
|# B B # . . . B . B . B * B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . 2 B . #|
|# . . B B B . . B . B . . . #|
|# 3 B # . . # . B B B # # . #|
|# . R B # . . # B # . # . . #|
|# * * * . . B . . . B . 4 . #|
|# . * # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.45 ms)
- **Agent 2 (AndOrSearch):** chose `BOMB` (took 13.22 ms)
- **Agent 3 (Minimax):** chose `BOMB` (took 17.59 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.97 ms)

### Events during this step:
- 💣 **AndOrSearch** placed a bomb at (11, 6)
- 💣 **Minimax** placed a bomb at (1, 8)

----------------------------------------

## STEP 10
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . 2 B . #|
|# . . B B B . . B . B . . . #|
|# 3 B # . . # . B B B # # . #|
|# . R B # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.02 ms)
- **Agent 2 (AndOrSearch):** chose `LEFT` (took 14.99 ms)
- **Agent 3 (Minimax):** chose `DOWN` (took 16.87 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.72 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 11
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . 2 O B . #|
|# . . B B B . . B . B . . . #|
|# O B # . . # . B B B # # . #|
|# 3 R B # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (10, 6) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.36 ms)
- **Agent 2 (AndOrSearch):** chose `LEFT` (took 12.52 ms)
- **Agent 3 (Minimax):** chose `RIGHT` (took 14.67 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.83 ms)

### Events during this step:
- 💎 **Minimax** collected **BOMB_RANGE** item (Range: 1 -> 2)

----------------------------------------

## STEP 12
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # 2 . O B . #|
|# . . B B B . . B . B . . . #|
|# O B # . . # . B B B # # . #|
|# . 3 B # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (9, 6) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 9) | Lives: 1 | Ammo: 0/1 | Range: 2
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.65 ms)
- **Agent 2 (AndOrSearch):** chose `UP` (took 14.58 ms)
- **Agent 3 (Minimax):** chose `DOWN` (took 12.97 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.85 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 13
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . 2 # . . B #|
|# B B B . B B B # . . O B . #|
|# . . B B B . . B . B . . . #|
|# O B # . . # . B B B # # . #|
|# . . B # . . # B # . # . . #|
|# . 3 . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (9, 5) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 10) | Lives: 1 | Ammo: 0/1 | Range: 2
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.80 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.27 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 13.34 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.98 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 14
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . 2 # . . B #|
|# B B B . B B B # . . O B . #|
|# . . B B B . . B . B . . . #|
|# O B # . . # . B B B # # . #|
|# . . B # . . # B # . # . . #|
|# . 3 . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (9, 5) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 10) | Lives: 1 | Ammo: 0/1 | Range: 2
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.19 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.05 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 13.64 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.33 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 15
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . 2 # . . B #|
|# B B B . B B B # . . O B . #|
|# . . B B B . . B . B . . . #|
|# O B # . . # . B B B # # . #|
|# . . B # . . # B # . # . . #|
|# . 3 . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (9, 5) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 10) | Lives: 1 | Ammo: 0/1 | Range: 2
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.41 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.97 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 11.96 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.04 ms)

### Events during this step:
- 💥 Bomb owned by **AndOrSearch** exploded at (11, 6) with range 1
- 💥 Bomb owned by **Minimax** exploded at (1, 8) with range 1
- 🧱 Brick destroyed at (12, 6)
- 🧱 Brick destroyed at (2, 8)

----------------------------------------

## STEP 16
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . 2 # * . B #|
|# B B B . B B B # . * * * . #|
|# * . B B B . . B . B * . . #|
|# * R # . . # . B B B # # . #|
|# * . B # . . # B # . # . . #|
|# . 3 . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (9, 5) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.47 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.26 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 19.60 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.63 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 17
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . 2 # . . B #|
|# B B B . B B B # . . . . . #|
|# . . B B B . . B . B . . . #|
|# . R # . . # . B B B # # . #|
|# . . B # . . # B # . # . . #|
|# . 3 . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (9, 5) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.95 ms)
- **Agent 2 (AndOrSearch):** chose `DOWN` (took 11.31 ms)
- **Agent 3 (Minimax):** chose `UP` (took 14.89 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.31 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 18
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # 2 . . . . #|
|# . . B B B . . B . B . . . #|
|# . R # . . # . B B B # # . #|
|# . 3 B # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (9, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 9) | Lives: 1 | Ammo: 1/1 | Range: 2
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.76 ms)
- **Agent 2 (AndOrSearch):** chose `RIGHT` (took 13.15 ms)
- **Agent 3 (Minimax):** chose `BOMB` (took 13.59 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.25 ms)

### Events during this step:
- 💣 **Minimax** placed a bomb at (2, 9)

----------------------------------------

## STEP 19
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . 2 . . . #|
|# . . B B B . . B . B . . . #|
|# . R # . . # . B B B # # . #|
|# . 3 B # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (10, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 9) | Lives: 1 | Ammo: 0/1 | Range: 2
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.97 ms)
- **Agent 2 (AndOrSearch):** chose `BOMB` (took 14.74 ms)
- **Agent 3 (Minimax):** chose `UP` (took 12.61 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.24 ms)

### Events during this step:
- 💣 **AndOrSearch** placed a bomb at (10, 6)
- 💎 **Minimax** collected **BOMB_RANGE** item (Range: 2 -> 3)

----------------------------------------

## STEP 20
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . 2 . . . #|
|# . . B B B . . B . B . . . #|
|# . 3 # . . # . B B B # # . #|
|# . O B # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (10, 6) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 8) | Lives: 1 | Ammo: 0/1 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.57 ms)
- **Agent 2 (AndOrSearch):** chose `RIGHT` (took 14.04 ms)
- **Agent 3 (Minimax):** chose `LEFT` (took 13.77 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.45 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 21
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . O 2 . . #|
|# . . B B B . . B . B . . . #|
|# 3 . # . . # . B B B # # . #|
|# . O B # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 0/1 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.35 ms)
- **Agent 2 (AndOrSearch):** chose `RIGHT` (took 10.91 ms)
- **Agent 3 (Minimax):** chose `UP` (took 11.60 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.10 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 22
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . O . 2 . #|
|# 3 . B B B . . B . B . . . #|
|# . . # . . # . B B B # # . #|
|# . O B # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (12, 6) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 7) | Lives: 1 | Ammo: 0/1 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.23 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.99 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 11.20 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.44 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 23
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . O . 2 . #|
|# 3 . B B B . . B . B . . . #|
|# . . # . . # . B B B # # . #|
|# . O B # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (12, 6) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 7) | Lives: 1 | Ammo: 0/1 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.67 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.39 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 10.99 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.72 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 24
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . O . 2 . #|
|# 3 . B B B . . B . B . . . #|
|# . . # . . # . B B B # # . #|
|# . O B # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (12, 6) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 7) | Lives: 1 | Ammo: 0/1 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.28 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.31 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 11.13 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.00 ms)

### Events during this step:
- 💥 Bomb owned by **Minimax** exploded at (2, 9) with range 2
- 🧱 Brick destroyed at (3, 9)

----------------------------------------

## STEP 25
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . O . 2 . #|
|# 3 * B B B . . B . B . . . #|
|# . * # . . # . B B B # # . #|
|# * * C # . . # B # . # . . #|
|# . * . . . B . . . B . 4 . #|
|# . * # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (12, 6) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 7) | Lives: 1 | Ammo: 1/1 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.90 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.00 ms)
- **Agent 3 (Minimax):** chose `BOMB` (took 12.55 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.01 ms)

### Events during this step:
- 💣 **Minimax** placed a bomb at (1, 7)
- 💥 Bomb owned by **AndOrSearch** exploded at (10, 6) with range 1
- 🧱 Brick destroyed at (10, 7)

----------------------------------------

## STEP 26
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # * * * 2 . #|
|# 3 . B B B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . C # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (12, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 7) | Lives: 1 | Ammo: 0/1 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.67 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.52 ms)
- **Agent 3 (Minimax):** chose `DOWN` (took 13.15 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.78 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 27
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . 2 . #|
|# O . B B B . . B . R . . . #|
|# 3 . # . . # . B B B # # . #|
|# . . C # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (12, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 0/1 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.50 ms)
- **Agent 2 (AndOrSearch):** chose `LEFT` (took 13.19 ms)
- **Agent 3 (Minimax):** chose `RIGHT` (took 13.16 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 17.61 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 28
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . 2 . . #|
|# O . B B B . . B . R . . . #|
|# . 3 # . . # . B B B # # . #|
|# . . C # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 8) | Lives: 1 | Ammo: 0/1 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.02 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.70 ms)
- **Agent 3 (Minimax):** chose `DOWN` (took 12.65 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.64 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 29
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . 2 . . #|
|# O . B B B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . 3 C # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 9) | Lives: 1 | Ammo: 0/1 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.82 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.98 ms)
- **Agent 3 (Minimax):** chose `RIGHT` (took 12.29 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.38 ms)

### Events during this step:
- 💎 **Minimax** collected **BOMB_CAPACITY** item (Capacity: 1 -> 2)

----------------------------------------

## STEP 30
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . 2 . . #|
|# O . B B B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . 3 # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (3, 9) | Lives: 1 | Ammo: 1/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.80 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.27 ms)
- **Agent 3 (Minimax):** chose `DOWN` (took 13.03 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.05 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 31
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . 2 . . #|
|# O . B B B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . 3 . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (3, 10) | Lives: 1 | Ammo: 1/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.55 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.47 ms)
- **Agent 3 (Minimax):** chose `BOMB` (took 12.58 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.40 ms)

### Events during this step:
- 💣 **Minimax** placed a bomb at (3, 10)
- 💥 Bomb owned by **Minimax** exploded at (1, 7) with range 3
- 🧱 Brick destroyed at (3, 7)
- 🧱 Brick destroyed at (1, 6)

----------------------------------------

## STEP 32
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# C B B . B B B # . . 2 . . #|
|# * * R B B . . B . R . . . #|
|# * . # . . # . B B B # # . #|
|# * . . # . . # B # . # . . #|
|# * . 3 . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (3, 10) | Lives: 1 | Ammo: 1/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.88 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.17 ms)
- **Agent 3 (Minimax):** chose `LEFT` (took 11.13 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.48 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 33
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# C B B . B B B # . . 2 . . #|
|# . . R B B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . 3 O . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 10) | Lives: 1 | Ammo: 1/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.88 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.30 ms)
- **Agent 3 (Minimax):** chose `UP` (took 12.12 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.21 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 34
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# C B B . B B B # . . 2 . . #|
|# . . R B B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . 3 . # . . # B # . # . . #|
|# . . O . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 9) | Lives: 1 | Ammo: 1/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.67 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.50 ms)
- **Agent 3 (Minimax):** chose `BOMB` (took 13.41 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.33 ms)

### Events during this step:
- 💣 **Minimax** placed a bomb at (2, 9)

----------------------------------------

## STEP 35
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# C B B . B B B # . . 2 . . #|
|# . . R B B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . 3 . # . . # B # . # . . #|
|# . . O . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 9) | Lives: 1 | Ammo: 0/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.27 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.86 ms)
- **Agent 3 (Minimax):** chose `UP` (took 12.84 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.83 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 36
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# C B B . B B B # . . 2 . . #|
|# . . R B B . . B . R . . . #|
|# . 3 # . . # . B B B # # . #|
|# . O . # . . # B # . # . . #|
|# . . O . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (2, 8) | Lives: 1 | Ammo: 0/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.15 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.13 ms)
- **Agent 3 (Minimax):** chose `LEFT` (took 11.21 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.72 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 37
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# C B B . B B B # . . 2 . . #|
|# . . R B B . . B . R . . . #|
|# 3 . # . . # . B B B # # . #|
|# . O . # . . # B # . # . . #|
|# . . O . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 0/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 16.65 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.62 ms)
- **Agent 3 (Minimax):** chose `UP` (took 12.73 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.41 ms)

### Events during this step:
- 💥 Bomb owned by **Minimax** exploded at (3, 10) with range 3
- 🧱 Brick destroyed at (6, 10)

----------------------------------------

## STEP 38
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# C B B . B B B # . . 2 . . #|
|# 3 . R B B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . O * # . . # B # . # . . #|
|# * * * * * R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 7) | Lives: 1 | Ammo: 1/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.86 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.26 ms)
- **Agent 3 (Minimax):** chose `BOMB` (took 13.24 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.88 ms)

### Events during this step:
- 💣 **Minimax** placed a bomb at (1, 7)

----------------------------------------

## STEP 39
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# C B B . B B B # . . 2 . . #|
|# 3 . R B B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . O . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 7) | Lives: 1 | Ammo: 0/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.25 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.01 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 12.99 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.46 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 40
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# C B B . B B B # . . 2 . . #|
|# 3 . R B B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . O . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 7) | Lives: 1 | Ammo: 0/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.80 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.69 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 12.44 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.25 ms)

### Events during this step:
- 💥 Bomb owned by **Minimax** exploded at (2, 9) with range 3
- 🧱 Brick destroyed at (2, 6)

----------------------------------------

## STEP 41
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# C C B . B B B # . . 2 . . #|
|# 3 * R B B . . B . R . . . #|
|# . * # . . # . B B B # # . #|
|# * * * # . . # B # . # . . #|
|# . * . . . R . . . B . 4 . #|
|# . * # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 7) | Lives: 1 | Ammo: 1/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.27 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.68 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 12.51 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.12 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 42
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# C C B . B B B # . . 2 . . #|
|# 3 . R B B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 7) | Lives: 1 | Ammo: 1/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.09 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.15 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 10.27 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.11 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 43
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# C C B . B B B # . . 2 . . #|
|# 3 . R B B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 7) | Lives: 1 | Ammo: 1/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.07 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.28 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 10.82 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.29 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 44
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# C C B . B B B # . . 2 . . #|
|# 3 . R B B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** ALIVE | Pos: (1, 7) | Lives: 1 | Ammo: 1/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.81 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.72 ms)
- **Agent 3 (Minimax):** chose `WAIT` (took 11.13 ms)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.05 ms)

### Events during this step:
- 💥 Bomb owned by **Minimax** exploded at (1, 7) with range 3
- 🧱 Brick destroyed at (4, 7)
- 🧱 Brick destroyed at (1, 5)
- 💀 **Minimax** died at (1, 7)!

----------------------------------------

## STEP 45
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# * B B B B . # . . # . . B #|
|# * C B . B B B # . . 2 . . #|
|# X * * R B . . B . R . . . #|
|# * . # . . # . B B B # # . #|
|# * . . # . . # B # . # . . #|
|# * . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.16 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.34 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.57 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 46
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.03 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.22 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.92 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 47
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.71 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.55 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.94 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 48
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.39 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.62 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.31 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 49
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.38 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.88 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.56 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 50
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.20 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.76 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.12 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 51
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.72 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.87 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.71 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 52
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.65 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.52 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.71 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 53
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.79 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.18 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.35 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 54
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.93 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.47 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.34 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 55
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.86 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.58 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.39 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 56
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.77 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.60 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.61 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 57
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.96 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.15 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.53 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 58
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.35 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.28 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.98 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 59
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.27 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.32 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.69 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 60
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.91 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.32 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.77 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 61
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 10.99 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.94 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.91 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 62
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.49 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.16 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.78 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 63
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.95 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 17.43 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.98 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 64
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.56 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.94 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.01 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 65
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.02 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.56 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.82 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 66
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.15 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.98 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.65 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 67
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.76 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.80 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.06 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 68
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.27 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.13 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.33 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 69
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.90 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.24 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.73 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 70
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.46 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.62 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.21 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 71
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.51 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.78 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.05 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 72
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.45 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.42 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.37 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 73
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.23 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.86 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.44 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 74
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.69 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.22 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.38 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 75
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.36 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.44 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.11 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 76
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.25 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.27 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.05 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 77
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.97 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.01 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.73 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 78
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.36 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.28 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.79 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 79
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.82 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.26 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.09 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 80
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.87 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.85 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.11 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 81
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.46 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.57 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.64 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 82
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.80 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.93 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.46 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 83
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 10.95 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 18.70 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 29.15 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 84
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 41.05 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 25.25 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 39.58 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 85
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 35.04 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 28.16 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 19.33 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 86
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 17.96 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 19.41 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 19.51 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 87
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 17.87 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.43 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.66 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 88
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.75 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 18.23 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.95 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 89
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.84 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.07 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 17.95 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 90
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.76 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.88 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.42 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 91
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.40 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.29 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.28 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 92
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.54 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.59 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.61 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 93
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 17.06 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.03 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.04 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 94
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.78 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.62 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.44 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 95
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.13 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.64 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.14 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 96
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.69 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.13 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.06 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 97
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.98 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.91 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 17.93 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 98
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.74 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.13 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.85 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 99
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.83 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.85 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.33 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 100
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.39 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.32 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.48 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 101
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.78 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.91 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.64 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 102
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.65 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.39 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.43 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 103
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.71 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 17.84 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.49 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 104
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.43 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.54 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 19.16 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 105
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.75 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 20.55 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.34 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 106
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.51 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.98 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.85 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 107
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.61 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.81 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.48 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 108
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.28 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.82 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.60 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 109
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.22 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.85 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.60 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 110
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.73 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.13 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.20 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 111
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.81 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.62 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.86 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 112
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.82 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.16 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.90 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 113
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.43 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.12 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.41 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 114
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.76 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.51 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.96 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 115
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.40 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 19.69 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 20.35 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 116
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.95 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 72.94 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 91.28 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 117
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 72.33 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 41.09 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 35.08 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 118
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 25.74 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 28.51 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 22.40 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 119
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 20.05 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 24.94 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 29.35 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 120
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 57.32 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 30.81 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 40.66 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 121
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 29.49 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 18.33 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 17.17 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 122
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.47 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.46 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.06 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 123
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.63 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.99 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.51 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 124
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.71 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.10 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.45 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 125
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.79 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.61 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.15 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 126
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.94 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.04 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.78 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 127
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.48 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.65 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.15 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 128
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.80 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.21 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.02 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 129
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.87 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.72 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.16 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 130
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.63 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.35 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.25 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 131
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.81 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.43 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.63 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 132
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.49 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.68 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.48 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 133
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.31 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.62 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.24 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 134
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 16.88 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.21 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.38 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 135
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.48 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.92 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.81 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 136
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.40 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.92 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.59 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 137
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.60 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.33 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.34 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 138
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.51 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.68 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.73 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 139
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 10.95 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.61 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.40 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 140
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.76 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.90 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.59 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 141
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.18 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.21 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.33 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 142
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 22.97 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.63 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.18 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 143
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 16.18 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.00 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.95 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 144
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.84 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.40 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.28 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 145
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.25 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.24 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.46 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 146
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.30 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.95 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.76 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 147
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.17 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.51 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.77 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 148
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.19 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.90 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.74 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 149
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.62 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.65 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.75 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 150
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.47 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.45 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.78 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 151
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.14 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 17.33 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.19 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 152
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.89 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.49 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.63 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 153
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.33 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.58 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 18.10 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 154
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.75 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.02 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.60 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 155
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.87 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.87 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.10 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 156
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 17.08 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.99 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.90 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 157
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.00 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.22 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.17 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 158
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.09 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.25 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.44 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 159
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.26 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.27 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.49 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 160
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 16.43 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 17.86 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 19.24 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 161
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 17.08 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.78 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 17.90 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 162
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 25.64 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.43 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 19.04 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 163
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.94 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.73 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 17.27 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 164
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.95 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.67 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.47 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 165
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.00 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.93 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 17.16 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 166
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 10.74 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.44 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.19 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 167
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.99 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.54 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.98 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 168
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . . . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.41 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.85 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.20 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 169
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.21 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.98 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.70 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 170
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.79 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.70 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 17.88 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 171
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 20.85 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.66 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 17.11 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 172
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.13 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.45 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 21.73 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 173
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 17.29 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.02 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.85 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 174
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.83 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.80 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.98 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 175
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.38 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.70 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.45 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 176
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 18.40 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.56 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.03 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 177
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.26 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.07 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.59 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 178
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.33 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.87 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.53 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 179
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.24 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.81 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.64 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 180
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 16.06 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.67 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.94 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 181
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 17.70 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 19.87 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 17.45 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 182
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 17.95 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 18.93 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.66 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 183
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.57 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.99 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 17.13 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 184
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.30 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.08 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.08 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 185
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.88 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.07 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.62 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 186
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.68 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.04 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.06 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 187
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.12 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.83 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.75 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 188
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.89 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.62 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.94 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 189
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.53 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.41 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.44 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 190
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.02 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.98 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.46 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 191
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.06 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.98 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.84 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 192
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.69 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 19.22 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.36 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 193
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.25 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.93 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.90 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 194
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.59 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.55 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.05 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 195
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.25 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.90 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.32 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 196
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.34 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.17 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.17 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 197
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.94 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.34 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.88 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 198
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.88 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.30 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.08 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 199
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.99 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.33 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.01 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 200
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.30 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.00 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.23 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 201
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.36 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.44 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.62 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 202
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.87 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.01 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.68 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 203
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C . # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 16.01 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.79 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.57 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 204
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 16.39 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.04 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.97 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 205
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 17.19 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 17.60 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.68 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 206
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.85 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 17.15 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 19.06 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 207
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.97 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.90 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.60 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 208
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.26 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.95 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.79 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 209
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.55 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.17 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.74 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 210
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.71 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.39 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.56 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 211
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.77 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 20.44 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.19 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 212
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.08 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.70 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 17.29 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 213
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.96 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.43 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.34 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 214
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.59 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 17.23 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.71 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 215
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.99 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.30 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.70 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 216
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.98 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.77 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.75 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 217
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.20 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.51 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.25 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 218
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 36.84 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 25.62 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.55 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 219
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.42 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.48 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.47 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 220
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.31 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.41 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.54 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 221
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.67 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.45 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.39 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 222
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.56 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.65 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.92 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 223
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.31 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.25 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.52 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 224
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.94 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.51 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.70 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 225
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.17 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.18 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.22 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 226
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 18.03 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.54 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.31 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 227
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.78 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.52 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.82 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 228
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.47 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.67 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.10 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 229
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 18.82 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 21.79 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.80 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 230
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.48 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.86 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.59 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 231
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.06 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.68 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.00 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 232
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.57 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.32 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.14 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 233
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.59 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.46 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.24 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 234
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.05 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.97 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.88 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 235
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.61 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.12 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.82 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 236
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.93 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.28 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.11 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 237
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.95 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.98 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.07 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 238
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.38 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.84 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.63 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 239
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.94 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.80 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.06 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 240
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.48 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.99 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.01 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 241
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.21 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.63 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.49 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 242
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.88 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.38 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.58 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 243
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.83 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.32 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.22 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 244
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.67 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.55 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.79 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 245
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.87 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.52 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.67 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 246
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.64 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.17 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.46 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 247
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.07 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.87 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.57 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 248
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . . # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.03 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.65 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.60 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 249
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.37 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.31 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.62 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 250
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.80 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.75 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.38 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 251
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.45 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.02 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.97 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 252
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.95 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.15 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.51 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 253
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.24 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.10 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.61 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 254
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.18 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.31 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.49 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 255
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.13 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.65 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.49 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 256
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.42 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.51 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.56 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 257
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 16.21 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 18.53 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.53 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 258
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.06 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.53 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 19.41 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 259
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 15.30 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.41 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 19.16 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 260
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 19.44 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.40 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 16.44 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 261
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.99 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 16.57 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.32 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 262
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B . # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.84 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.14 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.37 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 263
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.29 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.17 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.63 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 264
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.17 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.45 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.43 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 265
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.37 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.72 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.36 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 266
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.38 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.21 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.45 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 267
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.67 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.60 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.51 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 268
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 17.22 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.00 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.76 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 269
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.58 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.84 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.56 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 270
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.71 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.60 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.62 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 271
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.53 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.42 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.46 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 272
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.42 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.62 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.04 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 273
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.00 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 31.93 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.23 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 274
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.31 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.46 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.78 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 275
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.75 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.66 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.29 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 276
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.16 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.13 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.80 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 277
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.03 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.01 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.84 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 278
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 16.38 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 17.36 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 15.59 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 279
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.80 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.92 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.07 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 280
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.95 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.43 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.17 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 281
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.36 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.64 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.24 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 282
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.54 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 14.07 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.31 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 283
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.88 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.95 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.20 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 284
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.31 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.30 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.16 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 285
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.49 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.81 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.52 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 286
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.20 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.58 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.98 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 287
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.74 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.62 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.43 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 288
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.79 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.13 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.09 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 289
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.14 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.47 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.68 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 290
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.24 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.96 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.73 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 291
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.91 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.69 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.55 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 292
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.99 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.23 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.82 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 293
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.25 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 13.18 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 14.07 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 294
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 12.94 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.97 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.01 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 295
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 14.29 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.90 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 11.92 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 296
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 11.70 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.98 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.88 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 297
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.17 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 11.45 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.02 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 298
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 31.48 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 15.20 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 13.67 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 299
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# 1 # . . . . B . . B C . . #|
|# B B # . . . B . B . B . B #|
|# B B . # C # B R # # B . . #|
|# . B B B B . # . . # . . B #|
|# . C B . B B B # . . 2 . . #|
|# X . . R B . . B . R . . . #|
|# . . # . C # . B B B # # . #|
|# . C C # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . C # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Backtracking (Agent 1):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **AndOrSearch (Agent 2):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Minimax (Agent 3):** DEAD | Pos: (1, 7) | Lives: 0 | Ammo: 2/2 | Range: 3
- **Expectimax (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Backtracking):** chose `WAIT` (took 13.21 ms)
- **Agent 2 (AndOrSearch):** chose `WAIT` (took 12.10 ms)
- **Agent 3 (Minimax):** dead (forced STOP)
- **Agent 4 (Expectimax):** chose `WAIT` (took 12.56 ms)

### Events during this step:
- *No major events*

----------------------------------------

## Match Summary
🤝 **Match ended in a DRAW (or all dead) after 300 steps.**

### Final Stats Table:

| Rank | Agent Name | Agent ID | Survival Steps | Kills | Suicides | Bricks Destroyed | Items Picked | Avg Latency (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Backtracking** | player_1 | 300 | 0 | 0 | 0 | 0 | 14.68 |
| 2 | **AndOrSearch** | player_2 | 300 | 0 | 0 | 3 | 0 | 14.67 |
| 3 | **Expectimax** | player_4 | 300 | 0 | 0 | 0 | 0 | 14.72 |
| 4 | **Minimax** | player_3 | 45 | 0 | 1 | 9 | 3 | 13.22 |