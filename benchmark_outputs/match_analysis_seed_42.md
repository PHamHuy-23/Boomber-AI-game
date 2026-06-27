# Bomberman AI Detailed Match Analysis
**Seed:** 42
**Roster:**
- **Agent 1 (player_1):** Minimax
- **Agent 2 (player_2):** Expectimax
- **Agent 3 (player_3):** A*
- **Agent 4 (player_4):** BFS

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
- **Minimax (Agent 1):** ALIVE | Pos: (1, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (13, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (1, 11) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (13, 11) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `RIGHT` (took 12.04 ms)
- **Agent 2 (Expectimax):** chose `LEFT` (took 10.19 ms)
- **Agent 3 (A*):** chose `UP` (took 23.91 ms)
- **Agent 4 (BFS):** chose `UP` (took 14.38 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 1
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . 1 . # B . . . B B . 2 . #|
|# . # . . . . B . . B B . . #|
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
- **Minimax (Agent 1):** ALIVE | Pos: (2, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (13, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `RIGHT` (took 10.78 ms)
- **Agent 2 (Expectimax):** chose `DOWN` (took 11.81 ms)
- **Agent 3 (A*):** chose `RIGHT` (took 22.63 ms)
- **Agent 4 (BFS):** chose `LEFT` (took 15.49 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 2
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . 1 # B . . . B B . . . #|
|# . # . . . . B . . B B 2 . #|
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
- **Minimax (Agent 1):** ALIVE | Pos: (3, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (2, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `DOWN` (took 11.74 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.64 ms)
- **Agent 3 (A*):** chose `RIGHT` (took 21.98 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 19.70 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 3
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # 1 . . . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . 3 . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (3, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `RIGHT` (took 12.46 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.29 ms)
- **Agent 3 (A*):** chose `RIGHT` (took 20.54 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 21.61 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 4
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . 1 . . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . 3 . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (4, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `RIGHT` (took 11.46 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.22 ms)
- **Agent 3 (A*):** chose `RIGHT` (took 21.12 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.64 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 5
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.24 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.83 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.69 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.69 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 6
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 13.14 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.53 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.26 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.38 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 7
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.84 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 14.05 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.36 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.92 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 8
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 13.45 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.82 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.71 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.48 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 9
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.88 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.34 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.00 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.16 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 10
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.45 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.65 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.27 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.35 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 11
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.09 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.02 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.06 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.19 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 12
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.93 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.82 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.01 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.18 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 13
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.39 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.63 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.24 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.08 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 14
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.28 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.79 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.97 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.06 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 15
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.48 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.79 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.09 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.89 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 16
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.14 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.11 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.53 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.40 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 17
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.72 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.72 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.43 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.93 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 18
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.59 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.31 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.18 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.51 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 19
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.03 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.41 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.82 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.21 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 20
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.27 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.85 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.01 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.03 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 21
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.16 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.05 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.59 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.24 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 22
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.20 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.20 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.11 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.95 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 23
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.51 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.84 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.27 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.74 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 24
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.82 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.85 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.27 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.75 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 25
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.10 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.81 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.60 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.39 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 26
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.20 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.01 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.65 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 19.72 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 27
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.37 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.98 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.05 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.28 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 28
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.05 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.78 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.96 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.45 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 29
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.99 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.42 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.62 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 19.17 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 30
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 13.58 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.89 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.51 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.18 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 31
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.87 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.23 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.74 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.32 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 32
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.24 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.14 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.95 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.68 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 33
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.80 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.61 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.39 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.86 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 34
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.53 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.83 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.73 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 21.09 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 35
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.02 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.07 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.46 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.98 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 36
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.93 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.21 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.86 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.72 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 37
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 13.01 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.37 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.45 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.11 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 38
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.54 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.13 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.24 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.82 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 39
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.36 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.45 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.02 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.53 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 40
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.09 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.98 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.35 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.24 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 41
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.17 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.08 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.61 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.54 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 42
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.16 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.92 ms)
- **Agent 3 (A*):** chose `WAIT` (took 26.54 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.46 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 43
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.37 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.98 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.86 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.62 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 44
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.22 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.27 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.92 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.50 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 45
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.90 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.06 ms)
- **Agent 3 (A*):** chose `WAIT` (took 26.11 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.27 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 46
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.93 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.94 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.88 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.85 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 47
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.52 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.93 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.84 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.89 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 48
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.97 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.96 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.07 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.62 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 49
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 13.51 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.77 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.61 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 27.21 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 50
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 13.10 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.42 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.18 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.77 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 51
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.37 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.98 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.18 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.28 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 52
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.95 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.96 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.99 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.47 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 53
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.08 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.76 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.31 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.02 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 54
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.69 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.07 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.54 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.99 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 55
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.70 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.34 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.03 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.31 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 56
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.16 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.92 ms)
- **Agent 3 (A*):** chose `WAIT` (took 28.03 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 19.81 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 57
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.35 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.61 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.43 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 20.22 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 58
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.47 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.01 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.09 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.84 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 59
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.67 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.19 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.42 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.89 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 60
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.18 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.77 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.80 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.93 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 61
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.33 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.39 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.65 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.14 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 62
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.12 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.51 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.52 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.52 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 63
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.67 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.47 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.93 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.76 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 64
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.83 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.65 ms)
- **Agent 3 (A*):** chose `WAIT` (took 46.56 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 34.91 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 65
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 15.14 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 19.51 ms)
- **Agent 3 (A*):** chose `WAIT` (took 46.80 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 26.07 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 66
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 13.23 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 19.92 ms)
- **Agent 3 (A*):** chose `WAIT` (took 34.36 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 23.76 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 67
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 25.96 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.88 ms)
- **Agent 3 (A*):** chose `WAIT` (took 32.49 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 23.97 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 68
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 15.83 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 16.06 ms)
- **Agent 3 (A*):** chose `WAIT` (took 31.80 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 20.77 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 69
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 17.15 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 18.25 ms)
- **Agent 3 (A*):** chose `WAIT` (took 27.83 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 21.22 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 70
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 13.50 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 15.77 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.07 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.74 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 71
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.73 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.44 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.88 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.95 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 72
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.46 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.79 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.31 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 19.28 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 73
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.39 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.53 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.74 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.37 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 74
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.54 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.68 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.42 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.29 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 75
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.27 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.04 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.91 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.59 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 76
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.62 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.66 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.73 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.87 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 77
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.16 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.98 ms)
- **Agent 3 (A*):** chose `WAIT` (took 26.79 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.02 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 78
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.31 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.97 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.84 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.21 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 79
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.70 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.39 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.56 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.79 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 80
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.77 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.87 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.89 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.59 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 81
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.31 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.82 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.42 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.59 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 82
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.93 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.15 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.00 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 29.88 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 83
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 24.49 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 26.91 ms)
- **Agent 3 (A*):** chose `WAIT` (took 31.41 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 28.68 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 84
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 37.65 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 44.13 ms)
- **Agent 3 (A*):** chose `WAIT` (took 57.73 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 53.24 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 85
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 23.52 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 20.37 ms)
- **Agent 3 (A*):** chose `WAIT` (took 39.13 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 20.81 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 86
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 13.76 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.26 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.92 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.64 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 87
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.41 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.98 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.46 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.57 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 88
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.77 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.92 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.59 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.73 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 89
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.86 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.28 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.16 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.31 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 90
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.59 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.94 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.40 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.08 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 91
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.34 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.24 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.32 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.51 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 92
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 13.62 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 17.07 ms)
- **Agent 3 (A*):** chose `WAIT` (took 31.12 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.17 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 93
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 13.19 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.98 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.78 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.32 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 94
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.84 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.78 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.39 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.02 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 95
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 13.09 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.36 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.20 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.42 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 96
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.67 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.83 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.99 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.72 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 97
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.23 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.01 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.73 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.68 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 98
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.98 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.63 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.59 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.53 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 99
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.94 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.23 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.68 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.52 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 100
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.29 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.75 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.44 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.15 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 101
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.19 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.66 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.94 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.98 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 102
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.31 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.66 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.51 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 21.85 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 103
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.26 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.86 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.52 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.85 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 104
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.50 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.42 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.48 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.22 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 105
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.48 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.55 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.66 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.37 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 106
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.44 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.29 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.85 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.25 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 107
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.88 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.24 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.91 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.61 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 108
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.01 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.62 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.41 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.14 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 109
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.22 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.76 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.22 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.20 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 110
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.89 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.34 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.71 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.91 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 111
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.01 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.86 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.76 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.24 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 112
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.20 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.20 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.07 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.10 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 113
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.66 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.36 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.36 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 15.41 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 114
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.22 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.94 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.67 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.13 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 115
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.86 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.81 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.93 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.78 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 116
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.76 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.63 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.25 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.41 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 117
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.14 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.12 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.06 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.99 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 118
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.09 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.84 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.05 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 15.92 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 119
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.74 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.33 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.79 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.38 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 120
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.21 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.92 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.01 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.60 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 121
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.29 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.59 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.63 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.63 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 122
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.10 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.30 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.89 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.70 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 123
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 13.13 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.12 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.93 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.71 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 124
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.44 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.66 ms)
- **Agent 3 (A*):** chose `WAIT` (took 27.83 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.60 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 125
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.51 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.53 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.47 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.34 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 126
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.88 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.82 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.23 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 20.15 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 127
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.81 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.21 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.41 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.51 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 128
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.96 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.93 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.96 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.49 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 129
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.04 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.90 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.39 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.72 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 130
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.70 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.67 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.12 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.48 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 131
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.93 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.75 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.28 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.49 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 132
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.96 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.38 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.19 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.23 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 133
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.58 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.14 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.38 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.93 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 134
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.69 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.98 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.43 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.77 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 135
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.22 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.93 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.22 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.19 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 136
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.24 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.09 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.58 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.54 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 137
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.09 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.78 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.29 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.49 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 138
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.45 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.47 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.92 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.55 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 139
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.88 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.65 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.75 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 19.58 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 140
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . R # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.07 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.68 ms)
- **Agent 3 (A*):** chose `UP` (took 21.47 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.53 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 141
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . R # . B B B # # . #|
|# . B B # 3 . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.32 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.75 ms)
- **Agent 3 (A*):** chose `UP` (took 20.12 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.00 ms)

### Events during this step:
- 💎 **A*** collected **BOMB_RANGE** item (Range: 1 -> 2)

----------------------------------------

## STEP 142
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . 3 # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 8) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.48 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.44 ms)
- **Agent 3 (A*):** chose `DOWN` (took 22.56 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.67 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 143
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # 3 . # B # . # . . #|
|# . . . . . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 9) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.54 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.85 ms)
- **Agent 3 (A*):** chose `DOWN` (took 19.19 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.73 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 144
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.86 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.47 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.74 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.80 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 145
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.40 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.52 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.34 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.03 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 146
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.94 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.71 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.43 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.38 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 147
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.81 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.46 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.74 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.61 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 148
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.16 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.90 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.81 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.36 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 149
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.20 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.88 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.16 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.40 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 150
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.94 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.77 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.51 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 20.58 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 151
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.12 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.93 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.63 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.60 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 152
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.96 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.15 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.64 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.39 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 153
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.07 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.82 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.90 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.72 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 154
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.17 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.70 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.79 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.26 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 155
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.49 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.21 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.96 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.12 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 156
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.26 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.09 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.93 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.34 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 157
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.88 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.39 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.24 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.20 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 158
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.46 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.45 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.82 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.70 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 159
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.34 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.60 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.58 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.97 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 160
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.02 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.40 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.72 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.08 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 161
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.86 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.71 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.91 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.32 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 162
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.02 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.68 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.61 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.12 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 163
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.95 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.01 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.92 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.10 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 164
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.70 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.26 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.67 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.28 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 165
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.38 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.07 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.15 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.30 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 166
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.33 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.01 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.10 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.96 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 167
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.71 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.28 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.30 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.53 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 168
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.21 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.32 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.75 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 19.06 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 169
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.14 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.80 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.75 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.68 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 170
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.92 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.87 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.77 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.74 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 171
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.88 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.21 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.96 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.04 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 172
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.84 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.30 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.34 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.06 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 173
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.48 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.04 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.13 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.37 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 174
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.67 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.11 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.21 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.91 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 175
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.59 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.32 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.97 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 15.54 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 176
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.79 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.51 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.75 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.15 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 177
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.71 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.70 ms)
- **Agent 3 (A*):** chose `WAIT` (took 20.99 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.32 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 178
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.40 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.63 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.03 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.03 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 179
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.63 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.86 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.34 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.02 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 180
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.01 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.25 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.03 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.55 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 181
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.14 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.80 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.48 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.98 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 182
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.62 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.98 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.06 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.46 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 183
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # C . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.75 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.04 ms)
- **Agent 3 (A*):** chose `LEFT` (took 26.18 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.00 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 184
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # C . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . 3 . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (4, 10) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.61 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.99 ms)
- **Agent 3 (A*):** chose `BOMB` (took 23.15 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.44 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (4, 10)

----------------------------------------

## STEP 185
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # C . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . 3 . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (4, 10) | Lives: 1 | Ammo: 0/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.14 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.73 ms)
- **Agent 3 (A*):** chose `RIGHT` (took 16.67 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.31 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 186
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # C . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . O 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 0/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.75 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.12 ms)
- **Agent 3 (A*):** chose `UP` (took 16.97 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.17 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 187
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # C . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # 3 . # B # . # . . #|
|# . . . O . B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 9) | Lives: 1 | Ammo: 0/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `RIGHT` (took 12.08 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.38 ms)
- **Agent 3 (A*):** chose `DOWN` (took 20.07 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.40 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 188
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . . 1 B . . B B 2 . #|
|# B B # C . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . O 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (6, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 0/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `DOWN` (took 12.17 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.82 ms)
- **Agent 3 (A*):** chose `DOWN` (took 18.57 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.62 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 189
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . . . B . . B B 2 . #|
|# B B # C . 1 B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . O . B . . . B . 4 . #|
|# . . # B 3 . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (6, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 11) | Lives: 1 | Ammo: 0/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `UP` (took 12.96 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.21 ms)
- **Agent 3 (A*):** chose `UP` (took 20.13 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 20.00 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 190
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . . 1 B . . B B 2 . #|
|# B B # C . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . O 3 B . . . B . 4 . #|
|# . . # B . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (6, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 0/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `DOWN` (took 13.25 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.33 ms)
- **Agent 3 (A*):** chose `DOWN` (took 33.15 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 21.86 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (4, 10) with range 2
- 🧱 Brick destroyed at (4, 11)
- 🧱 Brick destroyed at (6, 10)

----------------------------------------

## STEP 191
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . . . B . . B B 2 . #|
|# B B # C . 1 B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . * * * * R . . . B . 4 . #|
|# . . # * 3 . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (6, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 11) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `LEFT` (took 16.10 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 14.86 ms)
- **Agent 3 (A*):** chose `RIGHT` (took 22.13 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 19.48 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 192
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . . . B . . B B 2 . #|
|# B B # C 1 . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . . R . . . B . 4 . #|
|# . . # . . 3 . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (6, 11) | Lives: 1 | Ammo: 1/1 | Range: 2
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `LEFT` (took 12.98 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 18.49 ms)
- **Agent 3 (A*):** chose `UP` (took 28.62 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 22.09 ms)

### Events during this step:
- 💎 **Minimax** collected **BOMB_CAPACITY** item (Capacity: 1 -> 2)
- 💎 **A*** collected **BOMB_RANGE** item (Range: 2 -> 3)

----------------------------------------

## STEP 193
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . . . B . . B B 2 . #|
|# B B # 1 . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . . 3 . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (4, 3) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (6, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `RIGHT` (took 15.38 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.80 ms)
- **Agent 3 (A*):** chose `LEFT` (took 30.52 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 19.44 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 194
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . . . B . . B B 2 . #|
|# B B # . 1 . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 3) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `UP` (took 14.78 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 14.20 ms)
- **Agent 3 (A*):** chose `WAIT` (took 30.57 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 19.56 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 195
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.92 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.80 ms)
- **Agent 3 (A*):** chose `WAIT` (took 27.25 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.25 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 196
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.93 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.85 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.36 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.79 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 197
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.54 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.08 ms)
- **Agent 3 (A*):** chose `WAIT` (took 26.66 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 20.72 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 198
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.18 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.37 ms)
- **Agent 3 (A*):** chose `WAIT` (took 27.70 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.72 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 199
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.36 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.63 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.94 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.03 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 200
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.66 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.14 ms)
- **Agent 3 (A*):** chose `WAIT` (took 26.05 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 86.95 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 201
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 34.25 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 19.60 ms)
- **Agent 3 (A*):** chose `WAIT` (took 30.20 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.64 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 202
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 14.09 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 13.80 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.75 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.04 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 203
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.20 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.67 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.71 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.86 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 204
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.42 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.67 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.61 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.99 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 205
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.23 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.23 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.59 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.51 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 206
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.54 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.70 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.48 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.62 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 207
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.80 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.60 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.62 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.34 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 208
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.57 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.31 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.12 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.61 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 209
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.94 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.76 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.45 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.23 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 210
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.37 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.37 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.36 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.87 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 211
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.88 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.83 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.75 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 15.42 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 212
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B . . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.42 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.33 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.25 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 15.35 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 213
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.30 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.30 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.98 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.60 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 214
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.44 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.27 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.96 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.73 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 215
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.55 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.79 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.73 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.88 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 216
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.92 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.02 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.35 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.01 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 217
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.81 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.45 ms)
- **Agent 3 (A*):** chose `WAIT` (took 28.70 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.49 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 218
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.26 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.10 ms)
- **Agent 3 (A*):** chose `WAIT` (took 26.83 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.20 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 219
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.44 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.71 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.98 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.19 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 220
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . C . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.40 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.14 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.96 ms)
- **Agent 4 (BFS):** chose `DOWN` (took 14.33 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 221
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . . . #|
|# . . # . . . . B . C . 4 . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 11) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.28 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.47 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.28 ms)
- **Agent 4 (BFS):** chose `LEFT` (took 15.24 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 222
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . . . #|
|# . . # . . . . B . C 4 . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (11, 11) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.98 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.33 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.67 ms)
- **Agent 4 (BFS):** chose `LEFT` (took 14.80 ms)

### Events during this step:
- 💎 **BFS** collected **BOMB_CAPACITY** item (Capacity: 1 -> 2)

----------------------------------------

## STEP 223
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . . . #|
|# . . # . . . . B . 4 . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 11) | Lives: 1 | Ammo: 2/2 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.45 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.62 ms)
- **Agent 3 (A*):** chose `WAIT` (took 26.52 ms)
- **Agent 4 (BFS):** chose `BOMB` (took 13.68 ms)

### Events during this step:
- 💣 **BFS** placed a bomb at (10, 11)

----------------------------------------

## STEP 224
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . . . #|
|# . . # . . . . B . 4 . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 11) | Lives: 1 | Ammo: 1/2 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.45 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.76 ms)
- **Agent 3 (A*):** chose `WAIT` (took 18.54 ms)
- **Agent 4 (BFS):** chose `RIGHT` (took 12.27 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 225
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . . . #|
|# . . # . . . . B . O 4 . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (11, 11) | Lives: 1 | Ammo: 1/2 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.90 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.50 ms)
- **Agent 3 (A*):** chose `WAIT` (took 19.68 ms)
- **Agent 4 (BFS):** chose `RIGHT` (took 12.88 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 226
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . . . #|
|# . . # . . . . B . O . 4 . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 11) | Lives: 1 | Ammo: 1/2 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.40 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.06 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.13 ms)
- **Agent 4 (BFS):** chose `UP` (took 14.15 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 227
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B . 4 . #|
|# . . # . . . . B . O . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/2 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.71 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.72 ms)
- **Agent 3 (A*):** chose `WAIT` (took 31.73 ms)
- **Agent 4 (BFS):** chose `LEFT` (took 15.89 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 228
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B 4 . . #|
|# . . # . . . . B . O . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (11, 10) | Lives: 1 | Ammo: 1/2 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.60 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.65 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.20 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 13.84 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 229
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . B 4 . . #|
|# . . # . . . . B . O . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (11, 10) | Lives: 1 | Ammo: 1/2 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.82 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.50 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.18 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 13.37 ms)

### Events during this step:
- 💥 Bomb owned by **BFS** exploded at (10, 11) with range 1
- 🧱 Brick destroyed at (10, 10)

----------------------------------------

## STEP 230
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . R 4 . . #|
|# . . # . . . . B * * * . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (11, 10) | Lives: 1 | Ammo: 2/2 | Range: 1

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.39 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.16 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.00 ms)
- **Agent 4 (BFS):** chose `LEFT` (took 14.76 ms)

### Events during this step:
- 💎 **BFS** collected **BOMB_RANGE** item (Range: 1 -> 2)

----------------------------------------

## STEP 231
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . 4 . . . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.72 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.52 ms)
- **Agent 3 (A*):** chose `WAIT` (took 26.10 ms)
- **Agent 4 (BFS):** chose `RIGHT` (took 16.96 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 232
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . 4 . . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (11, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.63 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.46 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.78 ms)
- **Agent 4 (BFS):** chose `RIGHT` (took 17.59 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 233
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.46 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.59 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.26 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.67 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 234
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.59 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.89 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.20 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.31 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 235
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.15 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.68 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.56 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.88 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 236
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.74 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.21 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.55 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.37 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 237
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.31 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.33 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.34 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.20 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 238
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 13.18 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.47 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.01 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.65 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 239
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.71 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.66 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.80 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.76 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 240
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.37 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.04 ms)
- **Agent 3 (A*):** chose `WAIT` (took 27.32 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.37 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 241
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.89 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.67 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.99 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.61 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 242
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.25 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.14 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.89 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.73 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 243
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.19 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.62 ms)
- **Agent 3 (A*):** chose `WAIT` (took 27.11 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.61 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 244
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.17 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.17 ms)
- **Agent 3 (A*):** chose `WAIT` (took 26.89 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.23 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 245
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.67 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.83 ms)
- **Agent 3 (A*):** chose `WAIT` (took 27.52 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.99 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 246
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.58 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.53 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.65 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 22.11 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 247
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.00 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.83 ms)
- **Agent 3 (A*):** chose `WAIT` (took 27.22 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.03 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 248
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.35 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.14 ms)
- **Agent 3 (A*):** chose `WAIT` (took 27.68 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.45 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 249
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.57 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.88 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.48 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.45 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 250
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.06 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.79 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.79 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.01 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 251
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.09 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.55 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.61 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.36 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 252
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.42 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.80 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.62 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.10 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 253
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.63 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.58 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.40 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.29 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 254
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.97 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.13 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.99 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.14 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 255
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.74 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.30 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.98 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.07 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 256
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.39 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.84 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.89 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.16 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 257
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.63 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.40 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.89 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.06 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 258
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.66 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.82 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.76 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.35 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 259
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.19 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.32 ms)
- **Agent 3 (A*):** chose `WAIT` (took 26.05 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.62 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 260
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.56 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.62 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.31 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.50 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 261
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.65 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.67 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.95 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.39 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 262
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.30 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.50 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.70 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.63 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 263
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.20 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.69 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.91 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.02 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 264
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 13.53 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.79 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.07 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.43 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 265
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.35 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.59 ms)
- **Agent 3 (A*):** chose `WAIT` (took 26.10 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.46 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 266
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.17 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.53 ms)
- **Agent 3 (A*):** chose `WAIT` (took 28.33 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.77 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 267
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . C . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.25 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.58 ms)
- **Agent 3 (A*):** chose `RIGHT` (took 24.33 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.71 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 268
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . . 3 . . . . . 4 . #|
|# . . # . . C . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (6, 10) | Lives: 1 | Ammo: 1/1 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.66 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.20 ms)
- **Agent 3 (A*):** chose `DOWN` (took 21.00 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.69 ms)

### Events during this step:
- 💎 **A*** collected **BOMB_CAPACITY** item (Capacity: 1 -> 2)

----------------------------------------

## STEP 269
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . . . . . . . . 4 . #|
|# . . # . . 3 . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (6, 11) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.42 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.71 ms)
- **Agent 3 (A*):** chose `UP` (took 21.30 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.48 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 270
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . . 3 . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (6, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.04 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.61 ms)
- **Agent 3 (A*):** chose `LEFT` (took 26.40 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.73 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 271
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.55 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.84 ms)
- **Agent 3 (A*):** chose `WAIT` (took 26.13 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.31 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 272
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.79 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.50 ms)
- **Agent 3 (A*):** chose `WAIT` (took 29.03 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.23 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 273
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.44 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.20 ms)
- **Agent 3 (A*):** chose `WAIT` (took 26.86 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.38 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 274
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.54 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.37 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.74 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.85 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 275
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.57 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.53 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.10 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.63 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 276
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.61 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.24 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.64 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 18.05 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 277
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.52 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.59 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.07 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.87 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 278
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.66 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.89 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.93 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 16.35 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 279
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.19 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.84 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.51 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.30 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 280
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.65 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.29 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.48 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 17.49 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 281
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . R . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.06 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.82 ms)
- **Agent 3 (A*):** chose `WAIT` (took 25.89 ms)
- **Agent 4 (BFS):** chose `DOWN` (took 16.21 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 282
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . . . #|
|# . . # . . . . B . R . 4 . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 11) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.27 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.77 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.32 ms)
- **Agent 4 (BFS):** chose `LEFT` (took 16.46 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 283
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . . . #|
|# . . # . . . . B . R 4 . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (11, 11) | Lives: 1 | Ammo: 2/2 | Range: 2

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.78 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.07 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.43 ms)
- **Agent 4 (BFS):** chose `LEFT` (took 15.46 ms)

### Events during this step:
- 💎 **BFS** collected **BOMB_RANGE** item (Range: 2 -> 3)

----------------------------------------

## STEP 284
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . . . #|
|# . . # . . . . B . 4 . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 11) | Lives: 1 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.34 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.02 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.00 ms)
- **Agent 4 (BFS):** chose `BOMB` (took 15.04 ms)

### Events during this step:
- 💣 **BFS** placed a bomb at (10, 11)

----------------------------------------

## STEP 285
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . . . #|
|# . . # . . . . B . 4 . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 11) | Lives: 1 | Ammo: 1/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.27 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.41 ms)
- **Agent 3 (A*):** chose `WAIT` (took 18.02 ms)
- **Agent 4 (BFS):** chose `RIGHT` (took 12.80 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 286
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . . . #|
|# . . # . . . . B . O 4 . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (11, 11) | Lives: 1 | Ammo: 1/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.88 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.98 ms)
- **Agent 3 (A*):** chose `WAIT` (took 21.57 ms)
- **Agent 4 (BFS):** chose `RIGHT` (took 11.78 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 287
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . . . #|
|# . . # . . . . B . O . 4 . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 11) | Lives: 1 | Ammo: 1/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.48 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.71 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.73 ms)
- **Agent 4 (BFS):** chose `UP` (took 13.38 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 288
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . O . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.91 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.61 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.73 ms)
- **Agent 4 (BFS):** chose `UP` (took 12.64 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 289
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # 4 . #|
|# . . . . 3 . . . . . . . . #|
|# . . # . . . . B . O . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 9) | Lives: 1 | Ammo: 1/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.18 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.14 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.00 ms)
- **Agent 4 (BFS):** chose `DOWN` (took 13.95 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 290
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B B # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . B . O . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 1/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.64 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.49 ms)
- **Agent 3 (A*):** chose `WAIT` (took 26.95 ms)
- **Agent 4 (BFS):** chose `UP` (took 13.80 ms)

### Events during this step:
- 💥 Bomb owned by **BFS** exploded at (10, 11) with range 3
- 🧱 Brick destroyed at (10, 8)
- 🧱 Brick destroyed at (8, 11)

----------------------------------------

## STEP 291
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B R # # . #|
|# . B B # . . # B # * # 4 . #|
|# . . . . 3 . . . . * . . . #|
|# . . # . . . . * * * * * * #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 9) | Lives: 1 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.38 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.98 ms)
- **Agent 3 (A*):** chose `WAIT` (took 26.65 ms)
- **Agent 4 (BFS):** chose `RIGHT` (took 11.82 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 292
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B R # # . #|
|# . B B # . . # B # . # . 4 #|
|# . . . . 3 . . . . . . . . #|
|# . . # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (13, 9) | Lives: 1 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.03 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.26 ms)
- **Agent 3 (A*):** chose `WAIT` (took 22.08 ms)
- **Agent 4 (BFS):** chose `DOWN` (took 14.73 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 293
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B R # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . . 4 #|
|# . . # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (13, 10) | Lives: 1 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.97 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.44 ms)
- **Agent 3 (A*):** chose `WAIT` (took 24.00 ms)
- **Agent 4 (BFS):** chose `LEFT` (took 15.99 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 294
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B R # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . . 4 . #|
|# . . # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (12, 10) | Lives: 1 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.04 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.45 ms)
- **Agent 3 (A*):** chose `WAIT` (took 23.04 ms)
- **Agent 4 (BFS):** chose `LEFT` (took 18.73 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 295
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B R # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . 3 . . . . . 4 . . #|
|# . . # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (5, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (11, 10) | Lives: 1 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.13 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.03 ms)
- **Agent 3 (A*):** chose `RIGHT` (took 22.24 ms)
- **Agent 4 (BFS):** chose `LEFT` (took 16.25 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 296
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B R # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . . 3 . . . 4 . . . #|
|# . . # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (6, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 10) | Lives: 1 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.77 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.43 ms)
- **Agent 3 (A*):** chose `RIGHT` (took 21.27 ms)
- **Agent 4 (BFS):** chose `LEFT` (took 16.82 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 297
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B R # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . . . 3 . 4 . . . . #|
|# . . # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (7, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (9, 10) | Lives: 1 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.49 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.43 ms)
- **Agent 3 (A*):** chose `BOMB` (took 22.54 ms)
- **Agent 4 (BFS):** chose `LEFT` (took 16.41 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (7, 10)

----------------------------------------

## STEP 298
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B R # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . . . 3 4 . . . . . #|
|# . . # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (7, 10) | Lives: 1 | Ammo: 1/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (8, 10) | Lives: 1 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.46 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.31 ms)
- **Agent 3 (A*):** chose `RIGHT` (took 17.49 ms)
- **Agent 4 (BFS):** chose `BOMB` (took 13.59 ms)

### Events during this step:
- 💣 **BFS** placed a bomb at (8, 10)

----------------------------------------

## STEP 299
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B R # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . . . O 4 . . . . . #|
|# . . # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (8, 10) | Lives: 1 | Ammo: 1/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (8, 10) | Lives: 1 | Ammo: 1/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.81 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.80 ms)
- **Agent 3 (A*):** chose `RIGHT` (took 17.76 ms)
- **Agent 4 (BFS):** chose `RIGHT` (took 13.51 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 300
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B R # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . . . O O 4 . . . . #|
|# . . # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (9, 10) | Lives: 1 | Ammo: 1/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (9, 10) | Lives: 1 | Ammo: 1/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.60 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.87 ms)
- **Agent 3 (A*):** chose `RIGHT` (took 16.60 ms)
- **Agent 4 (BFS):** chose `RIGHT` (took 12.37 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 301
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B R # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . . . O O . 4 . . . #|
|# . . # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (10, 10) | Lives: 1 | Ammo: 1/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 10) | Lives: 1 | Ammo: 1/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.76 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.42 ms)
- **Agent 3 (A*):** chose `UP` (took 16.90 ms)
- **Agent 4 (BFS):** chose `UP` (took 14.79 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 302
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B R # # . #|
|# . B B # . . # B # 4 # . . #|
|# . . . . . . O O . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (10, 9) | Lives: 1 | Ammo: 1/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 9) | Lives: 1 | Ammo: 1/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.47 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.00 ms)
- **Agent 3 (A*):** chose `UP` (took 20.02 ms)
- **Agent 4 (BFS):** chose `UP` (took 13.52 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 303
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B 4 # # . #|
|# . B B # . . # B # . # . . #|
|# . . . . . . O O . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (10, 8) | Lives: 1 | Ammo: 1/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 8) | Lives: 1 | Ammo: 1/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.28 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.81 ms)
- **Agent 3 (A*):** chose `DOWN` (took 16.80 ms)
- **Agent 4 (BFS):** chose `DOWN` (took 12.54 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (7, 10) with range 3
- 💥 Bomb owned by **BFS** exploded at (8, 10) with range 3
- 🧱 Brick destroyed at (8, 9)

----------------------------------------

## STEP 304
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B . # # . #|
|# . B B # . . # C # 4 # . . #|
|# . . . * * * * * * * * . . #|
|# . C # . . . * * . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (10, 9) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 9) | Lives: 1 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.13 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.38 ms)
- **Agent 3 (A*):** chose `UP` (took 15.94 ms)
- **Agent 4 (BFS):** chose `DOWN` (took 12.30 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 305
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B 3 # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . . . 4 . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (10, 8) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 10) | Lives: 1 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.37 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.88 ms)
- **Agent 3 (A*):** chose `DOWN` (took 19.15 ms)
- **Agent 4 (BFS):** chose `UP` (took 16.50 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 306
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B . # # . #|
|# . B B # . . # C # 4 # . . #|
|# . . . . . . . . . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (10, 9) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 9) | Lives: 1 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.27 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.21 ms)
- **Agent 3 (A*):** chose `DOWN` (took 17.72 ms)
- **Agent 4 (BFS):** chose `UP` (took 14.89 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 307
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B 4 # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . . . 3 . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (10, 10) | Lives: 1 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 8) | Lives: 1 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.47 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.33 ms)
- **Agent 3 (A*):** chose `BOMB` (took 26.68 ms)
- **Agent 4 (BFS):** chose `DOWN` (took 12.61 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (10, 10)

----------------------------------------

## STEP 308
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B . # # . #|
|# . B B # . . # C # 4 # . . #|
|# . . . . . . . . . 3 . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (10, 10) | Lives: 1 | Ammo: 1/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 9) | Lives: 1 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.55 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.69 ms)
- **Agent 3 (A*):** chose `LEFT` (took 19.83 ms)
- **Agent 4 (BFS):** chose `BOMB` (took 12.57 ms)

### Events during this step:
- 💣 **BFS** placed a bomb at (10, 9)

----------------------------------------

## STEP 309
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B . # # . #|
|# . B B # . . # C # 4 # . . #|
|# . . . . . . . . 3 O . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (9, 10) | Lives: 1 | Ammo: 1/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 9) | Lives: 1 | Ammo: 1/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.58 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.26 ms)
- **Agent 3 (A*):** chose `LEFT` (took 17.76 ms)
- **Agent 4 (BFS):** chose `UP` (took 11.68 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 310
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B 4 # # . #|
|# . B B # . . # C # O # . . #|
|# . . . . . . . 3 . O . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (8, 10) | Lives: 1 | Ammo: 1/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 8) | Lives: 1 | Ammo: 1/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.35 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.64 ms)
- **Agent 3 (A*):** chose `DOWN` (took 16.19 ms)
- **Agent 4 (BFS):** chose `BOMB` (took 11.19 ms)

### Events during this step:
- 💣 **BFS** placed a bomb at (10, 8)

----------------------------------------

## STEP 311
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B 4 # # . #|
|# . B B # . . # C # O # . . #|
|# . . . . . . . . . O . . . #|
|# . C # . . . . 3 . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (8, 11) | Lives: 1 | Ammo: 1/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 8) | Lives: 1 | Ammo: 0/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.62 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.03 ms)
- **Agent 3 (A*):** chose `UP` (took 17.94 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 11.43 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 312
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B 4 # # . #|
|# . B B # . . # C # O # . . #|
|# . . . . . . . 3 . O . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (8, 10) | Lives: 1 | Ammo: 1/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 8) | Lives: 1 | Ammo: 0/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.22 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.59 ms)
- **Agent 3 (A*):** chose `DOWN` (took 18.10 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 11.18 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 313
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . B . . . #|
|# . B # . . # . B B 4 # # . #|
|# . B B # . . # C # O # . . #|
|# . . . . . . . . . O . . . #|
|# . C # . . . . 3 . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** ALIVE | Pos: (8, 11) | Lives: 1 | Ammo: 1/2 | Range: 3
- **BFS (Agent 4):** ALIVE | Pos: (10, 8) | Lives: 1 | Ammo: 0/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.96 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.63 ms)
- **Agent 3 (A*):** chose `UP` (took 16.79 ms)
- **Agent 4 (BFS):** chose `WAIT` (took 10.83 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (10, 10) with range 3
- 💥 Bomb owned by **BFS** exploded at (10, 9) with range 3
- 💥 Bomb owned by **BFS** exploded at (10, 8) with range 3
- 🧱 Brick destroyed at (10, 7)
- 🧱 Brick destroyed at (9, 8)
- 💀 **A*** died at (8, 10)!
- 💀 **BFS** died at (10, 8)!

----------------------------------------

## STEP 314
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . * . . . #|
|# . B # . . # . B * X # # . #|
|# . B B # . . # C # * # . . #|
|# . . . . . . * X * * * * * #|
|# . C # . . . . . . * . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.66 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.14 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 315
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.60 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.63 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 316
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.46 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.07 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 317
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.49 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.96 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 318
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.88 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.06 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 319
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.37 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.85 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 320
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.09 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.74 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 321
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.86 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.50 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 322
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.65 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.88 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 323
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.66 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.41 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 324
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # . . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.83 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.79 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 325
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.66 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.72 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 326
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.54 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.24 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 327
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.32 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.54 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 328
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.24 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.71 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 329
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.57 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.38 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 330
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.62 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.21 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 331
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.21 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.00 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 332
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.21 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.81 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 333
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.96 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.66 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 334
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.03 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.23 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 335
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.70 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.53 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 336
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.67 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.26 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 337
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.95 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.34 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 338
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.41 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.85 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 339
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.64 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.21 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 340
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . . #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.49 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.63 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 341
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.89 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.95 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 342
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.15 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 14.21 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 343
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.83 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.42 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 344
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.56 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.30 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 345
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.86 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.24 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 346
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.78 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.88 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 347
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.78 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.94 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 348
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.35 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.09 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 349
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.79 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.55 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 350
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.40 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.66 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 351
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.39 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.68 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 352
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.98 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.90 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 353
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.95 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.32 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 354
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.81 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.24 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 355
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.19 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.25 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 356
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.34 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.65 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 357
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.88 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.18 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 358
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.63 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.05 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 359
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.89 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.61 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 360
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . . # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.58 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.33 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 361
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.00 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.02 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 362
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.02 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.86 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 363
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.99 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.72 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 364
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.79 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.53 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 365
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.61 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.85 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 366
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.34 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.85 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 367
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.20 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.52 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 368
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.99 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.85 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 369
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.22 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.42 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 370
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.62 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.19 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 371
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.07 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.41 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 372
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.33 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.96 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 373
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.93 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.46 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 374
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.69 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.12 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 375
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.55 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.97 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 376
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.47 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.15 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 377
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.00 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.98 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 378
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.05 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.34 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 379
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.95 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.31 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 380
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.63 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.27 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 381
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.89 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.40 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 382
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.17 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.25 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 383
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.62 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.02 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 384
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.46 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.71 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 385
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.22 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.11 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 386
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.75 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.51 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 387
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.12 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.60 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 388
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.23 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 59.98 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 389
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 21.11 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.59 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 390
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B . # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.37 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.65 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 391
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.08 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.63 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 392
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.95 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.26 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 393
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.48 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.42 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 394
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.32 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.06 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 395
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . . . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.28 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.16 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 396
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.79 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.51 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 397
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.83 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.70 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 398
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.70 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.87 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 399
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.94 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.72 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 400
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.34 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.22 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 401
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.78 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.91 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 402
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.35 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.26 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 403
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.58 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.90 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 404
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.64 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.62 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 405
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.59 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.71 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 406
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.30 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.84 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 407
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.28 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.67 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 408
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.27 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.76 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 409
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.35 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.26 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 410
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.70 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.41 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 411
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.19 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.09 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 412
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.14 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.39 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 413
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . . # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.27 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.88 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 414
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.64 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.30 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 415
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.23 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.64 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 416
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.54 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.49 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 417
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.07 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.35 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 418
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.73 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.17 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 419
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.78 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.41 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 420
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.88 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.28 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 421
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.38 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.53 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 422
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.78 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.45 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 423
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.89 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.94 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 424
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.20 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.68 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 425
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.11 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.43 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 426
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.96 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.40 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 427
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.04 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.04 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 428
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.48 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.54 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 429
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.07 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.26 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 430
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.74 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.42 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 431
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.81 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.59 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 432
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.03 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.57 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 433
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.24 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.10 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 434
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.32 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.26 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 435
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.46 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.78 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 436
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.69 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.52 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 437
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.17 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.30 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 438
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.14 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.72 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 439
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.60 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.62 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 440
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.27 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.17 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 441
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.31 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.28 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 442
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.49 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.50 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 443
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.82 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.14 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 444
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.21 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.55 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 445
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.88 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.48 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 446
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.96 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.70 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 447
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.09 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.81 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 448
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.67 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.33 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 449
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.34 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.03 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 450
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.17 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.45 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 451
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.29 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.39 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 452
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.21 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.71 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 453
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.70 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.67 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 454
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.58 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.99 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 455
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.42 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.90 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 456
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.16 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.34 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 457
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.32 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.46 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 458
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.44 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.46 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 459
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.60 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.09 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 460
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.09 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.44 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 461
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.73 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.95 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 462
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.38 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.62 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 463
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.62 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.50 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 464
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.80 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.41 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 465
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.32 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.30 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 466
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.02 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.59 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 467
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # . # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.99 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.54 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 468
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.25 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.80 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 469
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.59 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.14 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 470
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.17 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.27 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 471
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C . # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.85 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.14 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 472
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.73 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.94 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 473
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.28 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.50 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 474
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.63 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.77 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 475
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 12.20 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.37 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 476
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.24 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.00 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 477
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.16 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.87 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 478
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.99 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.33 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 479
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # . . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.94 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.99 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 480
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.13 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.11 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 481
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . . B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.56 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.94 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 482
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.86 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.38 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 483
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.48 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.13 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 484
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.27 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.78 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 485
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.53 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.32 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 486
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.34 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.15 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 487
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.36 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.08 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 488
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.91 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.52 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 489
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.32 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.23 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 490
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.55 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.07 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 491
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.10 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.78 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 492
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.22 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.84 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 493
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.74 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.41 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 494
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.16 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.15 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 495
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.18 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.37 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 496
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.04 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 9.51 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 497
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 11.68 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 12.25 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 498
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 9.60 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 11.08 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 499
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . C R # B . R . B B C . . #|
|# . # R . 1 . B . . B B 2 . #|
|# B B # . . . B . B . B . B #|
|# B B R # R # B . # # B . . #|
|# B B B B B . # . R # . . B #|
|# B B B . B B B # . . . B . #|
|# . . B B B . R B . . . . C #|
|# . B # . C # . B . X # # . #|
|# . B B # . . # C # . # R . #|
|# . . . . . . . X . . . . . #|
|# . C # . . . . . . . . . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **Minimax (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **Expectimax (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 3):** DEAD | Pos: (8, 10) | Lives: 0 | Ammo: 2/2 | Range: 3
- **BFS (Agent 4):** DEAD | Pos: (10, 8) | Lives: 0 | Ammo: 2/2 | Range: 3

### Actions Decided:
- **Agent 1 (Minimax):** chose `WAIT` (took 10.70 ms)
- **Agent 2 (Expectimax):** chose `WAIT` (took 10.23 ms)
- **Agent 3 (A*):** dead (forced STOP)
- **Agent 4 (BFS):** dead (forced STOP)

### Events during this step:
- *No major events*

----------------------------------------

## Match Summary
🤝 **Match ended in a DRAW (or all dead) after 500 steps.**

### Final Stats Table:

| Rank | Agent Name | Agent ID | Survival Steps | Kills | Suicides | Bricks Destroyed | Items Picked | Avg Latency (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Minimax** | player_1 | 500 | 0 | 0 | 0 | 1 | 11.38 |
| 2 | **Expectimax** | player_2 | 500 | 0 | 0 | 0 | 0 | 11.61 |
| 3 | **A*** | player_3 | 314 | 0 | 1 | 2 | 3 | 23.59 |
| 4 | **BFS** | player_4 | 314 | 0 | 1 | 6 | 3 | 17.5 |