# Bomberman AI Detailed Match Analysis
**Seed:** 99
**Fog of War:** Disabled
**Roster:**
- **Agent 1 (player_1):** SimulatedAnnealing
- **Agent 2 (player_2):** HillClimbing
- **Agent 3 (player_3):** Greedy
- **Agent 4 (player_4):** A*

========================================

## STEP 0
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# 1 . B . # B B . B B B . 2 #|
|# . . . . . . . . B . # . . #|
|# . B B # B B . . . . B . . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B B . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B B . #|
|# 3 . . B . . # B B . # . 4 #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (1, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (13, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 11) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (13, 11) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `RIGHT` (took 26.75 ms)
- **Agent 2 (HillClimbing):** chose `DOWN` (took 20.14 ms)
- **Agent 3 (Greedy):** chose `UP` (took 17.36 ms)
- **Agent 4 (A*):** chose `LEFT` (took 19.80 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 1
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . 1 B . # B B . B B B . . #|
|# . . . . . . . . B . # . 2 #|
|# . B B # B B . . . . B . . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B B . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B B B . . B B B . #|
|# . . . B . . # B B . # 4 . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (13, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 11) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 27.67 ms)
- **Agent 2 (HillClimbing):** chose `DOWN` (took 19.59 ms)
- **Agent 3 (Greedy):** chose `UP` (took 20.02 ms)
- **Agent 4 (A*):** chose `BOMB` (took 23.39 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (12, 11)

----------------------------------------

## STEP 2
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . 1 B . # B B . B B B . . #|
|# . . . . . . . . B . # . . #|
|# . B B # B B . . . . B . 2 #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B B . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B B . #|
|# . . . B . . # B B . # 4 . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (13, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 11) | Lives: 1 | Ammo: 0/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 23.66 ms)
- **Agent 2 (HillClimbing):** chose `LEFT` (took 17.61 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.95 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 15.74 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 3
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . 1 B . # B B . B B B . . #|
|# . . . . . . . . B . # . . #|
|# . B B # B B . . . . B 2 . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B B . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B B . #|
|# . . . B . . # B B . # O 4 #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (13, 11) | Lives: 1 | Ammo: 0/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `LEFT` (took 25.42 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.82 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.72 ms)
- **Agent 4 (A*):** chose `UP` (took 17.46 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 4
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# 1 . B . # B B . B B B . . #|
|# . . . . . . . . B . # . . #|
|# . B B # B B . . . . B 2 . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B B . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B B 4 #|
|# . . . B . . # B B . # O . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (1, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (13, 10) | Lives: 1 | Ammo: 0/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.11 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.57 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.88 ms)
- **Agent 4 (A*):** chose `UP` (took 17.55 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 5
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# 1 . B . # B B . B B B . . #|
|# . . . . . . . . B . # . . #|
|# . B B # B B . . . . B 2 . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B B . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # 4 #|
|# . B # . B B B . . B B B . #|
|# . . . B . . # B B . # O . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (1, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (13, 9) | Lives: 1 | Ammo: 0/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `RIGHT` (took 21.28 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.00 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 17.92 ms)
- **Agent 4 (A*):** chose `UP` (took 19.86 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 6
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . 1 B . # B B . B B B . . #|
|# . . . . . . . . B . # . . #|
|# . B B # B B . . . . B 2 . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B B . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B 4 #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B B . #|
|# . . . B . . # B B . # O . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (13, 8) | Lives: 1 | Ammo: 0/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.07 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.52 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.12 ms)
- **Agent 4 (A*):** chose `UP` (took 20.76 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 7
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . 1 B . # B B . B B B . . #|
|# . . . . . . . . B . # . . #|
|# . B B # B B . . . . B 2 . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B B . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B 4 #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B B . #|
|# . . . B . . # B B . # O . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (13, 7) | Lives: 1 | Ammo: 0/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `DOWN` (took 22.76 ms)
- **Agent 2 (HillClimbing):** chose `RIGHT` (took 16.56 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 21.22 ms)
- **Agent 4 (A*):** chose `UP` (took 20.91 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (12, 11) with range 1
- 🧱 Brick destroyed at (12, 10)

----------------------------------------

## STEP 8
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . 1 . . . . . . B . # . . #|
|# . B B # B B . . . . B . 2 #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B B . # #|
|# . . # . # B # B . . . . 4 #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # * * #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (13, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (13, 6) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.54 ms)
- **Agent 2 (HillClimbing):** chose `DOWN` (took 14.34 ms)
- **Agent 3 (Greedy):** chose `UP` (took 21.95 ms)
- **Agent 4 (A*):** chose `LEFT` (took 22.01 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 9
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . 1 . . . . . . B . # . . #|
|# . B B # B B . . . . B . . #|
|# . . . . # # . . B # B . 2 #|
|# B . # B . . B . . B B . # #|
|# . . # . # B # B . . . 4 . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (13, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 6) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.88 ms)
- **Agent 2 (HillClimbing):** chose `LEFT` (took 16.98 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 22.16 ms)
- **Agent 4 (A*):** chose `UP` (took 24.96 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 10
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . 1 . . . . . . B . # . . #|
|# . B B # B B . . . . B . . #|
|# . . . . # # . . B # B 2 . #|
|# B . # B . . B . . B B 4 # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 5) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.41 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 17.98 ms)
- **Agent 3 (Greedy):** chose `UP` (took 19.73 ms)
- **Agent 4 (A*):** chose `BOMB` (took 23.39 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (12, 5)

----------------------------------------

## STEP 11
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . 1 . . . . . . B . # . . #|
|# . B B # B B . . . . B . . #|
|# . . . . # # . . B # B 2 . #|
|# B . # B . . B . . B B 4 # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 5) | Lives: 1 | Ammo: 0/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 26.06 ms)
- **Agent 2 (HillClimbing):** chose `UP` (took 16.80 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 21.44 ms)
- **Agent 4 (A*):** chose `UP` (took 25.58 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 12
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . 1 . . . . . . B . # . . #|
|# . B B # B B . . . . B 2 . #|
|# . . . . # # . . B # B 4 . #|
|# B . # B . . B . . B B O # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 0/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.75 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 16.89 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.82 ms)
- **Agent 4 (A*):** chose `UP` (took 19.76 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 13
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . 1 . . . . . . B . # . . #|
|# . B B # B B . . . . B 4 . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B B O # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 0/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `RIGHT` (took 21.74 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 16.72 ms)
- **Agent 3 (Greedy):** chose `UP` (took 20.59 ms)
- **Agent 4 (A*):** chose `UP` (took 24.70 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 14
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . . 1 . . . . . B . # 4 . #|
|# . B B # B B . . . . B 2 . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B B O # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 0/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 26.07 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.32 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 22.41 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 24.21 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 15
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . . 1 . . . . . B . # . 4 #|
|# . B B # B B . . . . B 2 . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B B O # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (13, 2) | Lives: 1 | Ammo: 0/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.71 ms)
- **Agent 2 (HillClimbing):** chose `UP` (took 17.00 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.98 ms)
- **Agent 4 (A*):** chose `WAIT` (took 21.25 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 16
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . . 1 . . . . . B . # 2 4 #|
|# . B B # B B . . . . B . . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B B O # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (13, 2) | Lives: 1 | Ammo: 0/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.51 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.55 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 23.56 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.30 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (12, 5) with range 1
- 🧱 Brick destroyed at (11, 5)

----------------------------------------

## STEP 17
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . . 1 . . . . . B . # 2 4 #|
|# . B B # B B . . . . B . . #|
|# . . . . # # . . B # B * . #|
|# B . # B . . B . . B C * # #|
|# . . # . # B # B . . . * . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (13, 2) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 24.37 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.82 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.60 ms)
- **Agent 4 (A*):** chose `LEFT` (took 23.00 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 18
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . . 1 . . . . . B . # 4 . #|
|# . B B # B B . . . . B . . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B C . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `RIGHT` (took 25.60 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.34 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 21.48 ms)
- **Agent 4 (A*):** chose `DOWN` (took 23.50 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 19
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . . . 1 . . . . B . # 2 . #|
|# . B B # B B . . . . B 4 . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B C . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `RIGHT` (took 26.20 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.17 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.91 ms)
- **Agent 4 (A*):** chose `BOMB` (took 21.92 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (12, 3)

----------------------------------------

## STEP 20
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . . . . 1 . . . B . # 2 . #|
|# . B B # B B . . . . B 4 . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B C . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 0/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 24.18 ms)
- **Agent 2 (HillClimbing):** chose `UP` (took 16.47 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 17.26 ms)
- **Agent 4 (A*):** chose `DOWN` (took 20.40 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 21
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B 2 . #|
|# . . . . 1 . . . B . # . . #|
|# . B B # B B . . . . B O . #|
|# . . . . # # . . B # B 4 . #|
|# B . # B . . B . . B C . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 0/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `RIGHT` (took 22.87 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 16.26 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 21.72 ms)
- **Agent 4 (A*):** chose `DOWN` (took 22.15 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 22
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B 2 . #|
|# . . . . . 1 . . B . # . . #|
|# . B B # B B . . . . B O . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B C 4 # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (6, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 5) | Lives: 1 | Ammo: 0/1 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.27 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.50 ms)
- **Agent 3 (Greedy):** chose `UP` (took 19.12 ms)
- **Agent 4 (A*):** chose `LEFT` (took 22.41 ms)

### Events during this step:
- 💎 **A*** collected **BOMB_CAPACITY** item (Capacity: 1 -> 2)

----------------------------------------

## STEP 23
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B 2 . #|
|# . . . . . 1 . . B . # . . #|
|# . B B # B B . . . . B O . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B 4 . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (6, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 5) | Lives: 1 | Ammo: 1/2 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `RIGHT` (took 20.92 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.55 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 19.72 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 22.63 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 24
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B 2 . #|
|# . . . . . . 1 . B . # . . #|
|# . B B # B B . . . . B O . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B . 4 # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (7, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 5) | Lives: 1 | Ammo: 1/2 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `RIGHT` (took 22.51 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.30 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.76 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.12 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 25
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B 2 . #|
|# . . . . . . . 1 B . # . . #|
|# . B B # B B . . . . B O . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B . 4 # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (8, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 5) | Lives: 1 | Ammo: 1/2 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.24 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 20.72 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 19.97 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.58 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (12, 3) with range 1
- 🧱 Brick destroyed at (11, 3)

----------------------------------------

## STEP 26
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B 2 . #|
|# . . . . . . . 1 B . # * . #|
|# . B B # B B . . . . C * * #|
|# . . . . # # . . B # B * . #|
|# B . # B . . B . . B . 4 # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (8, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 5) | Lives: 1 | Ammo: 2/2 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `UP` (took 22.42 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.75 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.90 ms)
- **Agent 4 (A*):** chose `LEFT` (took 25.93 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 27
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B 1 B B B 2 . #|
|# . . . . . . . . B . # . . #|
|# . B B # B B . . . . C . . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B 4 . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (8, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 5) | Lives: 1 | Ammo: 2/2 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.01 ms)
- **Agent 2 (HillClimbing):** chose `DOWN` (took 16.06 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 19.93 ms)
- **Agent 4 (A*):** chose `BOMB` (took 27.55 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (11, 5)

----------------------------------------

## STEP 28
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B 1 B B B . . #|
|# . . . . . . . . B . # 2 . #|
|# . B B # B B . . . . C . . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B 4 . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (8, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 5) | Lives: 1 | Ammo: 1/2 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.89 ms)
- **Agent 2 (HillClimbing):** chose `UP` (took 17.42 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.76 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 24.08 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 29
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B 1 B B B 2 . #|
|# . . . . . . . . B . # . . #|
|# . B B # B B . . . . C . . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B O 4 # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (8, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 5) | Lives: 1 | Ammo: 1/2 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.32 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.50 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.81 ms)
- **Agent 4 (A*):** chose `UP` (took 22.06 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 30
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B 1 B B B 2 . #|
|# . . . . . . . . B . # . . #|
|# . B B # B B . . . . C . . #|
|# . . . . # # . . B # B 4 . #|
|# B . # B . . B . . B O . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (8, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 1/2 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.47 ms)
- **Agent 2 (HillClimbing):** chose `DOWN` (took 20.97 ms)
- **Agent 3 (Greedy):** chose `UP` (took 19.69 ms)
- **Agent 4 (A*):** chose `UP` (took 23.82 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 31
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B 1 B B B . . #|
|# . . . . . . . . B . # 2 . #|
|# . B B # B B . . . . C 4 . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B O . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (8, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/2 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `DOWN` (took 24.74 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 19.28 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 19.58 ms)
- **Agent 4 (A*):** chose `BOMB` (took 26.59 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (12, 3)

----------------------------------------

## STEP 32
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . . . . . . . 1 B . # 2 . #|
|# . B B # B B . . . . C 4 . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B O . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (8, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 0/2 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `UP` (took 28.06 ms)
- **Agent 2 (HillClimbing):** chose `UP` (took 15.50 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 19.00 ms)
- **Agent 4 (A*):** chose `LEFT` (took 23.71 ms)

### Events during this step:
- 💎 **A*** collected **BOMB_CAPACITY** item (Capacity: 2 -> 3)

----------------------------------------

## STEP 33
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B 1 B B B 2 . #|
|# . . . . . . . . B . # . . #|
|# . B B # B B . . . . 4 O . #|
|# . . . . # # . . B # B . . #|
|# B . # B . . B . . B O . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (8, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 3) | Lives: 1 | Ammo: 1/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.28 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.78 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 20.32 ms)
- **Agent 4 (A*):** chose `LEFT` (took 21.27 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (11, 5) with range 1
- 🧱 Brick destroyed at (10, 5)
- 🧱 Brick destroyed at (11, 4)

----------------------------------------

## STEP 34
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B 1 B B B 2 . #|
|# . . . . . . . . B . # . . #|
|# . B B # B B . . . 4 . O . #|
|# . . . . # # . . B # C . . #|
|# B . # B . . B . . * * * # #|
|# . . # . # B # B . . * . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (8, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 3) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.81 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.36 ms)
- **Agent 3 (Greedy):** chose `UP` (took 23.83 ms)
- **Agent 4 (A*):** chose `LEFT` (took 24.93 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 35
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B 1 B B B 2 . #|
|# . . . . . . . . B . # . . #|
|# . B B # B B . . 4 . . O . #|
|# . . . . # # . . B # C . . #|
|# B . # B . . B . . . . . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (8, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 3) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `DOWN` (took 28.24 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.18 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 18.78 ms)
- **Agent 4 (A*):** chose `LEFT` (took 21.47 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 36
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B 2 . #|
|# . . . . . . . 1 B . # . . #|
|# . B B # B B . 4 . . . O . #|
|# . . . . # # . . B # C . . #|
|# B . # B . . B . . . . . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (8, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 3) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 27.24 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.22 ms)
- **Agent 3 (Greedy):** chose `UP` (took 21.17 ms)
- **Agent 4 (A*):** chose `BOMB` (took 22.81 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (8, 3)

----------------------------------------

## STEP 37
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B 2 . #|
|# . . . . . . . 1 B . # . . #|
|# . B B # B B . 4 . . . O . #|
|# . . . . # # . . B # C . . #|
|# B . # B . . B . . . . . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (8, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 3) | Lives: 1 | Ammo: 1/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `LEFT` (took 21.10 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 16.10 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 23.46 ms)
- **Agent 4 (A*):** chose `DOWN` (took 23.10 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (12, 3) with range 1

----------------------------------------

## STEP 38
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B 2 . #|
|# . . . . . . 1 . B . # * . #|
|# . B B # B B . O . . * * * #|
|# . . . . # # . 4 B # C * . #|
|# B . # B . . B . . . . . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (7, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 4) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `BOMB` (took 24.37 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.33 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.38 ms)
- **Agent 4 (A*):** chose `LEFT` (took 21.32 ms)

### Events during this step:
- 💣 **SimulatedAnnealing** placed a bomb at (7, 2)

----------------------------------------

## STEP 39
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B 2 . #|
|# . . . . . . 1 . B . # . . #|
|# . B B # B B . O . . . . . #|
|# . . . . # # 4 . B # C . . #|
|# B . # B . . B . . . . . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (7, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (7, 4) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `LEFT` (took 21.75 ms)
- **Agent 2 (HillClimbing):** chose `DOWN` (took 16.59 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.61 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 23.92 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 40
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . . . . . 1 O . B . # 2 . #|
|# . B B # B B . O . . . . . #|
|# . . . . # # . 4 B # C . . #|
|# B . # B . . B . . . . . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (6, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 4) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `LEFT` (took 20.81 ms)
- **Agent 2 (HillClimbing):** chose `DOWN` (took 15.17 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.80 ms)
- **Agent 4 (A*):** chose `DOWN` (took 20.60 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 41
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . . . . 1 . O . B . # . . #|
|# . B B # B B . O . . . 2 . #|
|# . . . . # # . . B # C . . #|
|# B . # B . . B 4 . . . . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 5) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `LEFT` (took 22.16 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 23.71 ms)
- **Agent 3 (Greedy):** chose `UP` (took 30.29 ms)
- **Agent 4 (A*):** chose `BOMB` (took 30.03 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (8, 5)

----------------------------------------

## STEP 42
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . . . 1 . . O . B . # . . #|
|# . B B # B B . O . . . 2 . #|
|# . . . . # # . . B # C . . #|
|# B . # B . . B 4 . . . . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 5) | Lives: 1 | Ammo: 1/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 28.74 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 16.85 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 21.61 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 22.55 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (8, 3) with range 1

----------------------------------------

## STEP 43
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . . . 1 . . O * B . # . . #|
|# . B B # B B * * * . . 2 . #|
|# . . . . # # . * B # C . . #|
|# B . # B . . B O 4 . . . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 5) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 31.65 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.85 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.45 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 24.20 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 44
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B B . B B B . . #|
|# . . . 1 . . O . B . # . . #|
|# . B B # B B . . . . . 2 . #|
|# . . . . # # . . B # C . . #|
|# B . # B . . B O . 4 . . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 5) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.55 ms)
- **Agent 2 (HillClimbing):** chose `DOWN` (took 19.89 ms)
- **Agent 3 (Greedy):** chose `UP` (took 22.14 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 20.95 ms)

### Events during this step:
- 💥 Bomb owned by **SimulatedAnnealing** exploded at (7, 2) with range 1
- 🧱 Brick destroyed at (7, 1)

----------------------------------------

## STEP 45
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B * . B B B . . #|
|# . . . 1 . * * * B . # . . #|
|# . B B # B B * . . . . . . #|
|# . . . . # # . . B # C 2 . #|
|# B . # B . . B O . . 4 . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 5) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `LEFT` (took 22.78 ms)
- **Agent 2 (HillClimbing):** chose `LEFT` (took 16.42 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 17.95 ms)
- **Agent 4 (A*):** chose `UP` (took 23.96 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 46
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . 1 . . . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . B # 4 . . #|
|# B . # B . . B O . . . . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (11, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 4) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.88 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.21 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.41 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 36.30 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 47
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . 1 . . . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . B # 2 4 . #|
|# B . # B . . B O . . . . # #|
|# . . # . # B # B . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (11, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 35.22 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 25.14 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 33.29 ms)
- **Agent 4 (A*):** chose `BOMB` (took 34.28 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (12, 4)
- 💥 Bomb owned by **A*** exploded at (8, 5) with range 1
- 🧱 Brick destroyed at (7, 5)
- 🧱 Brick destroyed at (8, 6)

----------------------------------------

## STEP 48
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . 1 . . . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . * B # 2 4 . #|
|# B . # B . . * * * . . . # #|
|# . . # . # B # * . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (11, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `LEFT` (took 33.57 ms)
- **Agent 2 (HillClimbing):** chose `DOWN` (took 24.11 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 20.80 ms)
- **Agent 4 (A*):** chose `LEFT` (took 30.88 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 49
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . 1 . . . . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . B # 4 O . #|
|# B . # B . . . . . . 2 . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (11, 5) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 4) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `UP` (took 21.76 ms)
- **Agent 2 (HillClimbing):** chose `LEFT` (took 17.93 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 19.96 ms)
- **Agent 4 (A*):** chose `DOWN` (took 21.86 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 50
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . 1 B . # B . . B B B . . #|
|# . . . . . . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . B # . O . #|
|# B . # B . . . . . 2 4 . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (10, 5) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 5) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.25 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 16.48 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.56 ms)
- **Agent 4 (A*):** chose `BOMB` (took 23.15 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (11, 5)

----------------------------------------

## STEP 51
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . 1 B . # B . . B B B . . #|
|# . . . . . . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . B # . O . #|
|# B . # B . . . . . 2 4 . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 1) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (10, 5) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 5) | Lives: 1 | Ammo: 1/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `DOWN` (took 23.45 ms)
- **Agent 2 (HillClimbing):** chose `LEFT` (took 18.72 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 17.30 ms)
- **Agent 4 (A*):** chose `LEFT` (took 26.05 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 52
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . 1 . . . . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . B # . O . #|
|# B . # B . . . . 2 4 O . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (9, 5) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 5) | Lives: 1 | Ammo: 1/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `RIGHT` (took 26.44 ms)
- **Agent 2 (HillClimbing):** chose `LEFT` (took 18.76 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.61 ms)
- **Agent 4 (A*):** chose `LEFT` (took 24.19 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 53
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . 1 . . . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . B # . O . #|
|# B . # B . . . 2 4 . O . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (8, 5) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 5) | Lives: 1 | Ammo: 1/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.05 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 16.83 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.29 ms)
- **Agent 4 (A*):** chose `BOMB` (took 23.18 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (9, 5)
- 💥 Bomb owned by **A*** exploded at (12, 4) with range 1

----------------------------------------

## STEP 54
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . 1 . . . . . B . # . . #|
|# . B B # B B . . . . . * . #|
|# . . . . # # . . B # * * * #|
|# B . # B . . . 2 4 . O * # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . B . B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (8, 5) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 5) | Lives: 1 | Ammo: 1/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 28.18 ms)
- **Agent 2 (HillClimbing):** chose `BOMB` (took 25.74 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 20.67 ms)
- **Agent 4 (A*):** chose `DOWN` (took 23.36 ms)

### Events during this step:
- 💣 **HillClimbing** placed a bomb at (8, 5)

----------------------------------------

## STEP 55
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . 1 . . . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . B # . . . #|
|# B . # B . . . 2 O . O . # #|
|# . . # . # B # . 4 . . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (8, 5) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 6) | Lives: 1 | Ammo: 1/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `LEFT` (took 25.38 ms)
- **Agent 2 (HillClimbing):** chose `UP` (took 17.18 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.63 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 20.55 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 56
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . 1 . . . . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . 2 B # . . . #|
|# B . # B . . . O O . O . # #|
|# . . # . # B # R . 4 . . . #|
|# . # B B . . . . B . B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (8, 4) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 6) | Lives: 1 | Ammo: 1/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 27.38 ms)
- **Agent 2 (HillClimbing):** chose `UP` (took 16.87 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 19.82 ms)
- **Agent 4 (A*):** chose `DOWN` (took 20.86 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (11, 5) with range 1

----------------------------------------

## STEP 57
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . 1 . . . . . . B . # . . #|
|# . B B # B B . 2 . . . . . #|
|# . . . . # # . . B # * . . #|
|# B . # B . . . O O * * * # #|
|# . . # . # B # R . . * . . #|
|# . # B B . . . . B 4 B B . #|
|# . B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (8, 3) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 7) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 24.76 ms)
- **Agent 2 (HillClimbing):** chose `UP` (took 16.07 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.11 ms)
- **Agent 4 (A*):** chose `BOMB` (took 19.02 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (10, 7)

----------------------------------------

## STEP 58
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . 1 . . . . . 2 B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . B # . . . #|
|# B . # B . . . O O . . . # #|
|# . . # . # B # R . . . . . #|
|# . # B B . . . . B 4 B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (8, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 7) | Lives: 1 | Ammo: 1/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `RIGHT` (took 25.37 ms)
- **Agent 2 (HillClimbing):** chose `LEFT` (took 15.60 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.57 ms)
- **Agent 4 (A*):** chose `UP` (took 24.32 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 59
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . 1 . . . 2 . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . B # . . . #|
|# B . # B . . . O O . . . # #|
|# . . # . # B # R . 4 . . . #|
|# . # B B . . . . B O B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (7, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 6) | Lives: 1 | Ammo: 1/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `RIGHT` (took 24.89 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 16.26 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.34 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 26.55 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (9, 5) with range 1
- 💥 Bomb owned by **HillClimbing** exploded at (8, 5) with range 1
- 🧱 Brick destroyed at (9, 4)

----------------------------------------

## STEP 60
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 1 . . 2 . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . * C # . . . #|
|# B . # B . . * * * * . . # #|
|# . . # . # B # * * . 4 . . #|
|# . # B B . . . . B O B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (7, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.09 ms)
- **Agent 2 (HillClimbing):** chose `LEFT` (took 20.63 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.82 ms)
- **Agent 4 (A*):** chose `UP` (took 22.24 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 61
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 1 . 2 . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . 4 . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . B O B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (6, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 5) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `RIGHT` (took 26.18 ms)
- **Agent 2 (HillClimbing):** chose `LEFT` (took 15.79 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 18.07 ms)
- **Agent 4 (A*):** chose `UP` (took 28.31 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 62
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # 4 . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . B O B B . #|
|# . B B B . # B B . B B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 4) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 23.62 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.88 ms)
- **Agent 3 (Greedy):** chose `UP` (took 20.08 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 30.28 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 63
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . 4 . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . B O B B . #|
|# 3 B B B . # B B . B B B . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 2/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.19 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.19 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 19.59 ms)
- **Agent 4 (A*):** chose `UP` (took 28.86 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (10, 7) with range 1
- 🧱 Brick destroyed at (11, 7)
- 🧱 Brick destroyed at (9, 7)
- 🧱 Brick destroyed at (10, 8)

----------------------------------------

## STEP 64
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . 4 . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . * . . . #|
|# . # B B . . . . C * R B . #|
|# . B B B . # B B . * B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 3/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.50 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.81 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 28.70 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.08 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 65
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . 4 . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . C . R B . #|
|# . B B B . # B B . . B B . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 3/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.20 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 17.29 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.73 ms)
- **Agent 4 (A*):** chose `DOWN` (took 29.19 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 66
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . 4 . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . C . R B . #|
|# . B B B . # B B . . B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 3/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.79 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.97 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 17.84 ms)
- **Agent 4 (A*):** chose `LEFT` (took 30.76 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 67
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # 4 . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . C . R B . #|
|# . B B B . # B B . . B B . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 4) | Lives: 1 | Ammo: 3/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.00 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.68 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.24 ms)
- **Agent 4 (A*):** chose `DOWN` (took 26.27 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 68
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . 4 . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . C . R B . #|
|# . B B B . # B B . . B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 5) | Lives: 1 | Ammo: 3/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.63 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.65 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 17.72 ms)
- **Agent 4 (A*):** chose `DOWN` (took 26.21 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 69
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . 4 . . #|
|# . # B B . . . . C . R B . #|
|# . B B B . # B B . . B B . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 3/3 | Range: 1

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.29 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.45 ms)
- **Agent 3 (Greedy):** chose `UP` (took 17.54 ms)
- **Agent 4 (A*):** chose `DOWN` (took 23.34 ms)

### Events during this step:
- 💎 **A*** collected **BOMB_RANGE** item (Range: 1 -> 2)

----------------------------------------

## STEP 70
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . C . 4 B . #|
|# . B B B . # B B . . B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 7) | Lives: 1 | Ammo: 3/3 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.91 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.43 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 23.72 ms)
- **Agent 4 (A*):** chose `BOMB` (took 24.20 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (11, 7)

----------------------------------------

## STEP 71
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . C . 4 B . #|
|# . B B B . # B B . . B B . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 7) | Lives: 1 | Ammo: 2/3 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.93 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.03 ms)
- **Agent 3 (Greedy):** chose `UP` (took 17.71 ms)
- **Agent 4 (A*):** chose `LEFT` (took 21.45 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 72
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . C 4 O B . #|
|# . B B B . # B B . . B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 7) | Lives: 1 | Ammo: 2/3 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 26.87 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.69 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.52 ms)
- **Agent 4 (A*):** chose `DOWN` (took 21.19 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 73
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . C . O B . #|
|# . B B B . # B B . 4 B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 8) | Lives: 1 | Ammo: 2/3 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 23.09 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.91 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 20.98 ms)
- **Agent 4 (A*):** chose `BOMB` (took 26.46 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (10, 8)

----------------------------------------

## STEP 74
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . C . O B . #|
|# . B B B . # B B . 4 B B . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 8) | Lives: 1 | Ammo: 1/3 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 27.60 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.39 ms)
- **Agent 3 (Greedy):** chose `UP` (took 19.11 ms)
- **Agent 4 (A*):** chose `LEFT` (took 22.06 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 75
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . C . O B . #|
|# . B B B . # B B 4 O B B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 8) | Lives: 1 | Ammo: 1/3 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 24.80 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.57 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 19.88 ms)
- **Agent 4 (A*):** chose `DOWN` (took 21.41 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 76
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . C . O B . #|
|# . B B B . # B B . O B B . #|
|# 3 . . B # . . . 4 . # # . #|
|# . B # . B B B . . B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 9) | Lives: 1 | Ammo: 1/3 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.74 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.97 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 19.75 ms)
- **Agent 4 (A*):** chose `DOWN` (took 23.68 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (11, 7) with range 2
- 🧱 Brick destroyed at (11, 8)
- 🧱 Brick destroyed at (12, 7)

----------------------------------------

## STEP 77
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . * . # #|
|# . . # . # B # . . . * . . #|
|# . # B B . . . . * * * C . #|
|# . B B B . # B B . O * B . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B B B . 4 B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 10) | Lives: 1 | Ammo: 2/3 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.54 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 16.48 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.72 ms)
- **Agent 4 (A*):** chose `BOMB` (took 26.49 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (9, 10)

----------------------------------------

## STEP 78
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . C . #|
|# . B B B . # B B . O . B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B . 4 B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 10) | Lives: 1 | Ammo: 1/3 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 24.64 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.93 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 19.89 ms)
- **Agent 4 (A*):** chose `LEFT` (took 20.07 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 79
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . C . #|
|# . B B B . # B B . O . B . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B 4 O B B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 10) | Lives: 1 | Ammo: 1/3 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 23.26 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.53 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 22.18 ms)
- **Agent 4 (A*):** chose `BOMB` (took 19.74 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (8, 10)
- 💥 Bomb owned by **A*** exploded at (10, 8) with range 2
- 🧱 Brick destroyed at (8, 8)
- 🧱 Brick destroyed at (10, 10)
- 🧱 Brick destroyed at (12, 8)

----------------------------------------

## STEP 80
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . * . . . #|
|# . # B B . . . . . * . C . #|
|# . B B B . # B C * * * R . #|
|# 3 . . B # . . . . * # # . #|
|# . B # . B B B 4 O * B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 10) | Lives: 1 | Ammo: 1/3 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.81 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.72 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 19.17 ms)
- **Agent 4 (A*):** chose `UP` (took 20.52 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 81
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . C . #|
|# . B B B . # B C . . . R . #|
|# . . . B # . . 4 . . # # . #|
|# 3 B # . B B B O O . B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 1/3 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.19 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.37 ms)
- **Agent 3 (Greedy):** chose `UP` (took 17.24 ms)
- **Agent 4 (A*):** chose `UP` (took 20.35 ms)

### Events during this step:
- 💎 **A*** collected **BOMB_CAPACITY** item (Capacity: 3 -> 4)

----------------------------------------

## STEP 82
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . C . #|
|# . B B B . # B 4 . . . R . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B B O O . B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 8) | Lives: 1 | Ammo: 2/4 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.91 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.54 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.12 ms)
- **Agent 4 (A*):** chose `UP` (took 31.80 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 83
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . 4 . . . C . #|
|# 3 B B B . # B . . . . R . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B B O O . B R . #|
|# . . . B . . # B B . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 7) | Lives: 1 | Ammo: 2/4 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 61.36 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 28.78 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 32.98 ms)
- **Agent 4 (A*):** chose `UP` (took 51.53 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (9, 10) with range 2
- 💥 Bomb owned by **A*** exploded at (8, 10) with range 2
- 🧱 Brick destroyed at (9, 11)
- 🧱 Brick destroyed at (11, 10)
- 🧱 Brick destroyed at (8, 11)
- 🧱 Brick destroyed at (7, 10)

----------------------------------------

## STEP 84
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # 4 . . . . . #|
|# . # B B . . . . . . . C . #|
|# . B B B . # B * * . . R . #|
|# 3 . . B # . . * * . # # . #|
|# . B # . B B R * * * R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 6) | Lives: 1 | Ammo: 4/4 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 48.86 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 22.35 ms)
- **Agent 3 (Greedy):** chose `UP` (took 34.34 ms)
- **Agent 4 (A*):** chose `UP` (took 51.43 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 85
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . 4 . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . C . #|
|# 3 B B B . # B . . . . R . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 5) | Lives: 1 | Ammo: 4/4 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 32.33 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 22.62 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 28.18 ms)
- **Agent 4 (A*):** chose `UP` (took 30.37 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 86
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . 4 C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . C . #|
|# . B B B . # B . . . . R . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 4) | Lives: 1 | Ammo: 4/4 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 32.18 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 18.56 ms)
- **Agent 3 (Greedy):** chose `UP` (took 22.79 ms)
- **Agent 4 (A*):** chose `UP` (took 28.87 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 87
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B . 4 . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . C . #|
|# 3 B B B . # B . . . . R . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 3) | Lives: 1 | Ammo: 4/4 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.58 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 17.39 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 23.15 ms)
- **Agent 4 (A*):** chose `LEFT` (took 72.14 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 88
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . . . B . # . . #|
|# . B B # B B 4 . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . C . #|
|# . B B B . # B . . . . R . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (7, 3) | Lives: 1 | Ammo: 4/4 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 31.15 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.10 ms)
- **Agent 3 (Greedy):** chose `UP` (took 21.16 ms)
- **Agent 4 (A*):** chose `UP` (took 27.63 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 89
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . 4 . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . C . #|
|# 3 B B B . # B . . . . R . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (7, 2) | Lives: 1 | Ammo: 4/4 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.44 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.27 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 19.35 ms)
- **Agent 4 (A*):** chose `BOMB` (took 22.59 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (7, 2)

----------------------------------------

## STEP 90
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . . 2 . 4 . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . C . #|
|# . B B B . # B . . . . R . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (7, 2) | Lives: 1 | Ammo: 3/4 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `LEFT` (took 22.32 ms)
- **Agent 2 (HillClimbing):** chose `LEFT` (took 17.25 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.43 ms)
- **Agent 4 (A*):** chose `DOWN` (took 20.01 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 91
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . O . B . # . . #|
|# . B B # B B 4 . . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . C . #|
|# . B B B . # B . . . . R . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (7, 3) | Lives: 1 | Ammo: 3/4 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.73 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.63 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 21.12 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 22.91 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 92
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . O . B . # . . #|
|# . B B # B B . 4 . . . . . #|
|# . . . . # # . . C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . C . #|
|# . B B B . # B . . . . R . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 3) | Lives: 1 | Ammo: 3/4 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.30 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 18.12 ms)
- **Agent 3 (Greedy):** chose `UP` (took 23.07 ms)
- **Agent 4 (A*):** chose `DOWN` (took 27.94 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 93
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . O . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . 4 C # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . C . #|
|# 3 B B B . # B . . . . R . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 4) | Lives: 1 | Ammo: 3/4 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.72 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.86 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 19.11 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 30.73 ms)

### Events during this step:
- 💎 **A*** collected **BOMB_CAPACITY** item (Capacity: 4 -> 5)

----------------------------------------

## STEP 94
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . O . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . 4 # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . C . #|
|# . B B B . # B . . . . R . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 4) | Lives: 1 | Ammo: 4/5 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 44.86 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.86 ms)
- **Agent 3 (Greedy):** chose `UP` (took 29.48 ms)
- **Agent 4 (A*):** chose `DOWN` (took 23.23 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 95
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . O . B . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . 4 . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . C . #|
|# 3 B B B . # B . . . . R . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 5) | Lives: 1 | Ammo: 4/5 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.81 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 16.01 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 20.41 ms)
- **Agent 4 (A*):** chose `DOWN` (took 25.03 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (7, 2) with range 2
- 🧱 Brick destroyed at (9, 2)

----------------------------------------

## STEP 96
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B * . B B B . . #|
|# . . . 2 * * * * * . # . . #|
|# . B B # B B * . . . . . . #|
|# . . . . # # * . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . 4 . . . . #|
|# . # B B . . . . . . . C . #|
|# . B B B . # B . . . . R . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 6) | Lives: 1 | Ammo: 5/5 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.56 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.46 ms)
- **Agent 3 (Greedy):** chose `UP` (took 17.78 ms)
- **Agent 4 (A*):** chose `DOWN` (took 27.62 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 97
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . 4 . . C . #|
|# 3 B B B . # B . . . . R . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 7) | Lives: 1 | Ammo: 5/5 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.36 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.12 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 20.60 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 34.99 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 98
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . 4 . C . #|
|# . B B B . # B . . . . R . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 7) | Lives: 1 | Ammo: 5/5 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.61 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.64 ms)
- **Agent 3 (Greedy):** chose `UP` (took 17.70 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 29.08 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 99
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . 4 C . #|
|# 3 B B B . # B . . . . R . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 7) | Lives: 1 | Ammo: 5/5 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.45 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.79 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 17.72 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 22.04 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 100
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . 4 . #|
|# . B B B . # B . . . . R . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 7) | Lives: 1 | Ammo: 5/5 | Range: 2

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.81 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.55 ms)
- **Agent 3 (Greedy):** chose `UP` (took 19.61 ms)
- **Agent 4 (A*):** chose `DOWN` (took 28.60 ms)

### Events during this step:
- 💎 **A*** collected **BOMB_RANGE** item (Range: 2 -> 3)

----------------------------------------

## STEP 101
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . . . #|
|# 3 B B B . # B . . . . 4 . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 8) | Lives: 1 | Ammo: 5/5 | Range: 3

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 24.65 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.32 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 19.76 ms)
- **Agent 4 (A*):** chose `LEFT` (took 22.96 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 102
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . . . #|
|# . B B B . # B . . . 4 . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 8) | Lives: 1 | Ammo: 5/5 | Range: 3

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.49 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.60 ms)
- **Agent 3 (Greedy):** chose `UP` (took 19.08 ms)
- **Agent 4 (A*):** chose `LEFT` (took 32.22 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 103
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . . . #|
|# 3 B B B . # B . . 4 . . . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 8) | Lives: 1 | Ammo: 5/5 | Range: 3

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 23.10 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.81 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 18.49 ms)
- **Agent 4 (A*):** chose `LEFT` (took 34.40 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 104
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . . . #|
|# . B B B . # B . 4 . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 8) | Lives: 1 | Ammo: 5/5 | Range: 3

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 23.21 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.63 ms)
- **Agent 3 (Greedy):** chose `UP` (took 20.28 ms)
- **Agent 4 (A*):** chose `DOWN` (took 33.07 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 105
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . . . #|
|# 3 B B B . # B . . . . . . #|
|# . . . B # . . . 4 . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 9) | Lives: 1 | Ammo: 5/5 | Range: 3

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.34 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.04 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 25.31 ms)
- **Agent 4 (A*):** chose `DOWN` (took 54.01 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 106
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . . . #|
|# . B B B . # B . . . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B R . 4 . R R . #|
|# . . . B . . # R C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 10) | Lives: 1 | Ammo: 5/5 | Range: 3

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 56.78 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 25.18 ms)
- **Agent 3 (Greedy):** chose `UP` (took 29.79 ms)
- **Agent 4 (A*):** chose `DOWN` (took 61.19 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 107
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . . . #|
|# 3 B B B . # B . . . . . . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # R 4 . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 11) | Lives: 1 | Ammo: 5/5 | Range: 3

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 49.26 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 24.80 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 33.63 ms)
- **Agent 4 (A*):** chose `LEFT` (took 29.69 ms)

### Events during this step:
- 💎 **A*** collected **BOMB_RANGE** item (Range: 3 -> 4)

----------------------------------------

## STEP 108
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . . . #|
|# . B B B . # B . . . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B R . . . R R . #|
|# . . . B . . # 4 . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 11) | Lives: 1 | Ammo: 5/5 | Range: 4

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 33.94 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 20.87 ms)
- **Agent 3 (Greedy):** chose `UP` (took 23.30 ms)
- **Agent 4 (A*):** chose `UP` (took 22.45 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 109
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . . . #|
|# 3 B B B . # B . . . . . . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B R 4 . . R R . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 10) | Lives: 1 | Ammo: 5/5 | Range: 4

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 24.55 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.39 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 17.15 ms)
- **Agent 4 (A*):** chose `LEFT` (took 25.39 ms)

### Events during this step:
- 💎 **A*** collected **BOMB_RANGE** item (Range: 4 -> 5)

----------------------------------------

## STEP 110
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . . . #|
|# . B B B . # B . . . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B 4 . . . R R . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (7, 10) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.26 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.18 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 18.19 ms)
- **Agent 4 (A*):** chose `BOMB` (took 25.02 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (7, 10)

----------------------------------------

## STEP 111
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . . . #|
|# . B B B . # B . . . . . . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B B 4 . . . R R . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (7, 10) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 28.47 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.79 ms)
- **Agent 3 (Greedy):** chose `UP` (took 21.45 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 20.30 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 112
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . . . #|
|# . B B B . # B . . . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B O 4 . . R R . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 10) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 27.44 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.41 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.27 ms)
- **Agent 4 (A*):** chose `UP` (took 20.21 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 113
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . . . #|
|# . B B B . # B . . . . . . #|
|# 3 . . B # . . 4 . . # # . #|
|# . B # . B B O . . . R R . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 23.65 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 17.32 ms)
- **Agent 3 (Greedy):** chose `UP` (took 29.52 ms)
- **Agent 4 (A*):** chose `UP` (took 68.05 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 114
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . . . #|
|# 3 B B B . # B 4 . . . . . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B O . . . R R . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 8) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 44.67 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.94 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 20.31 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 27.58 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 115
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . . . . . . #|
|# . B B B . # B . 4 . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B B O . . . R R . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 8) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `LEFT` (took 23.47 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.15 ms)
- **Agent 3 (Greedy):** chose `UP` (took 17.54 ms)
- **Agent 4 (A*):** chose `UP` (took 26.35 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 116
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . 1 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . 4 . . . . #|
|# 3 B B B . # B . . . . . . #|
|# . . . B # . . . . . # # . #|
|# . B # . B B O . . . R R . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 7) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.88 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 17.08 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 19.32 ms)
- **Agent 4 (A*):** chose `BOMB` (took 31.89 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (9, 7)
- 💥 Bomb owned by **A*** exploded at (7, 10) with range 5
- 🧱 Brick destroyed at (6, 10)
- 🧱 Brick destroyed at (7, 8)

----------------------------------------

## STEP 117
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . 1 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . 4 . . . . #|
|# . B B B . # C . . . . . . #|
|# 3 . . B # . * . . . # # . #|
|# . B # . B * * * * * * * . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 7) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `RIGHT` (took 27.26 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 17.69 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.07 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 21.46 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 118
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . O 4 . . . #|
|# . B B B . # C . . . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 7) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 28.07 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.45 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 18.64 ms)
- **Agent 4 (A*):** chose `UP` (took 20.29 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 119
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . 4 . . . #|
|# . # B B . . . . O . . . . #|
|# . B B B . # C . . . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 6) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 27.97 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 17.42 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 29.79 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 32.74 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 120
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . 4 . . #|
|# . # B B . . . . O . . . . #|
|# . B B B . # C . . . . . . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 29.00 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 19.45 ms)
- **Agent 3 (Greedy):** chose `UP` (took 22.13 ms)
- **Agent 4 (A*):** chose `UP` (took 35.17 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 121
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . 4 . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . O . . . . #|
|# . B B B . # C . . . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 5) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 33.01 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 21.38 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 25.22 ms)
- **Agent 4 (A*):** chose `UP` (took 42.31 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 122
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # 4 . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B B . . . . O . . . . #|
|# . B B B . # C . . . . . . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 4) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 33.42 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.90 ms)
- **Agent 3 (Greedy):** chose `UP` (took 19.80 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 28.85 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (9, 7) with range 5
- 🧱 Brick destroyed at (4, 7)

----------------------------------------

## STEP 123
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . * . # . . #|
|# . B B # B B . . * . . . . #|
|# . . . . # # . . * # . 4 . #|
|# B . # B . . . . * . . . # #|
|# . . # . # B # . * . . . . #|
|# . # B * * * * * * * * * * #|
|# . B B B . # C . * . . . . #|
|# 3 . . B # . . . * . # # . #|
|# . B # . B . . . * . . . . #|
|# . . . B . . # . * . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.99 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.84 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 17.73 ms)
- **Agent 4 (A*):** chose `UP` (took 30.09 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 124
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . 4 . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B . . . . . . . . . . #|
|# . B B B . # C . . . . . . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.47 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.56 ms)
- **Agent 3 (Greedy):** chose `UP` (took 16.08 ms)
- **Agent 4 (A*):** chose `DOWN` (took 21.40 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 125
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . 4 . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B . . . . . . . . . . #|
|# . B B B . # C . . . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.32 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.09 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 17.03 ms)
- **Agent 4 (A*):** chose `DOWN` (took 26.07 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 126
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . 4 # #|
|# . . # . # B # . . . . . . #|
|# . # B . . . . . . . . . . #|
|# . B B B . # C . . . . . . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 5) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.53 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.15 ms)
- **Agent 3 (Greedy):** chose `UP` (took 17.16 ms)
- **Agent 4 (A*):** chose `LEFT` (took 23.99 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 127
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . 4 . # #|
|# . . # . # B # . . . . . . #|
|# . # B . . . . . . . . . . #|
|# . B B B . # C . . . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 5) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.36 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.36 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 17.97 ms)
- **Agent 4 (A*):** chose `DOWN` (took 24.54 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 128
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . 4 . . #|
|# . # B . . . . . . . . . . #|
|# . B B B . # C . . . . . . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.95 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.54 ms)
- **Agent 3 (Greedy):** chose `UP` (took 17.85 ms)
- **Agent 4 (A*):** chose `LEFT` (took 25.58 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 129
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . 4 . . . #|
|# . # B . . . . . . . . . . #|
|# . B B B . # C . . . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 6) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.55 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.17 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 17.66 ms)
- **Agent 4 (A*):** chose `LEFT` (took 27.17 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 130
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . 4 . . . . #|
|# . # B . . . . . . . . . . #|
|# . B B B . # C . . . . . . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 6) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 23.94 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.37 ms)
- **Agent 3 (Greedy):** chose `UP` (took 20.95 ms)
- **Agent 4 (A*):** chose `BOMB` (took 27.11 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (9, 6)

----------------------------------------

## STEP 131
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . 4 . . . . #|
|# . # B . . . . . . . . . . #|
|# . B B B . # C . . . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 6) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 31.91 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.66 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 19.94 ms)
- **Agent 4 (A*):** chose `DOWN` (took 21.93 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 132
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . O . . . . #|
|# . # B . . . . . 4 . . . . #|
|# . B B B . # C . . . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 7) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 23.87 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.76 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 18.48 ms)
- **Agent 4 (A*):** chose `LEFT` (took 26.52 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 133
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . O . . . . #|
|# . # B . . . . 4 . . . . . #|
|# . B B B . # C . . . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 7) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.73 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.86 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 18.04 ms)
- **Agent 4 (A*):** chose `BOMB` (took 26.28 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (8, 7)

----------------------------------------

## STEP 134
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . O . . . . #|
|# . # B . . . . 4 . . . . . #|
|# . B B B . # C . . . . . . #|
|# . . . B # . . . . . # # . #|
|# 3 B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 10) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 7) | Lives: 1 | Ammo: 3/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 29.75 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.59 ms)
- **Agent 3 (Greedy):** chose `UP` (took 16.95 ms)
- **Agent 4 (A*):** chose `DOWN` (took 22.82 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 135
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . O . . . . #|
|# . # B . . . . O . . . . . #|
|# . B B B . # C 4 . . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 8) | Lives: 1 | Ammo: 3/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 26.63 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.52 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.67 ms)
- **Agent 4 (A*):** chose `LEFT` (took 21.66 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 136
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . B B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . O . . . . #|
|# . # B . . . . O . . . . . #|
|# . B B B . # 4 . . . . . . #|
|# 3 . . B # . . . . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (7, 8) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.71 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 16.53 ms)
- **Agent 3 (Greedy):** chose `UP` (took 17.68 ms)
- **Agent 4 (A*):** chose `DOWN` (took 25.57 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (9, 6) with range 5
- 🧱 Brick destroyed at (9, 1)

----------------------------------------

## STEP 137
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . * . # . . #|
|# . B B # B B . . * . . . . #|
|# . . . . # # . . * # . . . #|
|# B . # B . . . . * . . . # #|
|# . . # . # B # * * * * * * #|
|# . # B . . . . O * . . . . #|
|# 3 B B B . # . . * . . . . #|
|# . . . B # . 4 . * . # # . #|
|# . B # . B . . . * . . . . #|
|# . . . B . . # . * . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (7, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.14 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.48 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 17.42 ms)
- **Agent 4 (A*):** chose `LEFT` (took 24.89 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 138
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B . . . . O . . . . . #|
|# . B B B . # . . . . . . . #|
|# 3 . . B # 4 . . . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (6, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.59 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.06 ms)
- **Agent 3 (Greedy):** chose `RIGHT` (took 17.64 ms)
- **Agent 4 (A*):** chose `DOWN` (took 22.42 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 139
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # B . . . . O . . . . . #|
|# . B B B . # . . . . . . . #|
|# . 3 . B # . . . . . # # . #|
|# . B # . B 4 . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (2, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (6, 10) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.58 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.35 ms)
- **Agent 3 (Greedy):** chose `RIGHT` (took 17.32 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 21.24 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (8, 7) with range 5
- 🧱 Brick destroyed at (3, 7)

----------------------------------------

## STEP 140
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . * . . # . . #|
|# . B B # B B . * . . . . . #|
|# . . . . # # . * . # . . . #|
|# B . # B . . . * . . . . # #|
|# . . # . # B # * . . . . . #|
|# . # * * * * * * * * * * * #|
|# . B B B . # . * . . . . . #|
|# . . 3 B # . . * . . # # . #|
|# . B # . B . 4 * . . . . . #|
|# . . . B . . # * . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (3, 9) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (7, 10) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.84 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.51 ms)
- **Agent 3 (Greedy):** chose `BOMB` (took 18.26 ms)
- **Agent 4 (A*):** chose `LEFT` (took 24.44 ms)

### Events during this step:
- 💣 **Greedy** placed a bomb at (3, 9)

----------------------------------------

## STEP 141
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B B B . # . . . . . . . #|
|# . . 3 B # . . . . . # # . #|
|# . B # . B 4 . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (3, 9) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (6, 10) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.57 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.59 ms)
- **Agent 3 (Greedy):** chose `LEFT` (took 15.69 ms)
- **Agent 4 (A*):** chose `UP` (took 22.21 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 142
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B B B . # . . . . . . . #|
|# . 3 O B # 4 . . . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (2, 9) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (6, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 24.04 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.78 ms)
- **Agent 3 (Greedy):** chose `LEFT` (took 14.32 ms)
- **Agent 4 (A*):** chose `WAIT` (took 22.53 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 143
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B B B . # . . . . . . . #|
|# 3 . O B # 4 . . . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 9) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (6, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.77 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.27 ms)
- **Agent 3 (Greedy):** chose `UP` (took 17.81 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 19.77 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 144
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# 3 B B B . # . . . . . . . #|
|# . . O B # . 4 . . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 8) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (7, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 24.53 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.85 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.92 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 23.38 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 145
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# 3 # . . . . . . . . . . . #|
|# . B B B . # . . . . . . . #|
|# . . O B # . . 4 . . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 7) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.93 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.07 ms)
- **Agent 3 (Greedy):** chose `UP` (took 18.29 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 26.49 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 146
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# 3 . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B B B . # . . . . . . . #|
|# . . O B # . . . 4 . # # . #|
|# . B # . B . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 6) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.68 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.95 ms)
- **Agent 3 (Greedy):** chose `RIGHT` (took 15.30 ms)
- **Agent 4 (A*):** chose `DOWN` (took 30.26 ms)

### Events during this step:
- 💥 Bomb owned by **Greedy** exploded at (3, 9) with range 1
- 🧱 Brick destroyed at (4, 9)
- 🧱 Brick destroyed at (3, 8)

----------------------------------------

## STEP 147
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . 3 # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . * * R # . . . . . # # . #|
|# . B # . B . . . 4 . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (2, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 10) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.25 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.27 ms)
- **Agent 3 (Greedy):** chose `UP` (took 15.43 ms)
- **Agent 4 (A*):** chose `BOMB` (took 26.44 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (9, 10)

----------------------------------------

## STEP 148
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . . # # . . . # . . . #|
|# B 3 # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . B . . . 4 . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (2, 5) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 10) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 27.77 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.77 ms)
- **Agent 3 (Greedy):** chose `UP` (took 17.37 ms)
- **Agent 4 (A*):** chose `UP` (took 19.40 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 149
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . 3 . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . 4 . # # . #|
|# . B # . B . . . O . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (2, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 9) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 28.55 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.28 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.86 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 21.12 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 150
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . 3 . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . . 4 # # . #|
|# . B # . B . . . O . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (2, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 9) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.55 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.16 ms)
- **Agent 3 (Greedy):** chose `RIGHT` (took 17.87 ms)
- **Agent 4 (A*):** chose `UP` (took 24.23 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 151
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . 3 . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . 4 . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . B . . . O . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (3, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 8) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.20 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.24 ms)
- **Agent 3 (Greedy):** chose `RIGHT` (took 18.74 ms)
- **Agent 4 (A*):** chose `UP` (took 21.67 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 152
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . 4 . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . B . . . O . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 7) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.51 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.97 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.35 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 23.94 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 153
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . 4 . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . B . . . O . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 7) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.87 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.09 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.18 ms)
- **Agent 4 (A*):** chose `UP` (took 25.26 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (9, 10) with range 5
- 🧱 Brick destroyed at (5, 10)

----------------------------------------

## STEP 154
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . * . . . # #|
|# . . # . # B # . * . 4 . . #|
|# . # . . . . . . * . . . . #|
|# . B C B . # . . * . . . . #|
|# . . . R # . . . * . # # . #|
|# . B # . R * * * * * * * * #|
|# . . . B . . # . * . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.21 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.18 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 19.67 ms)
- **Agent 4 (A*):** chose `WAIT` (took 30.57 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 155
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . 4 . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.86 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.98 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.73 ms)
- **Agent 4 (A*):** chose `LEFT` (took 30.19 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 156
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . 4 . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# . . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 6) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.03 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 26.28 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 23.76 ms)
- **Agent 4 (A*):** chose `DOWN` (took 36.22 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 157
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . 4 . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 7) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 28.24 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.70 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.29 ms)
- **Agent 4 (A*):** chose `LEFT` (took 30.14 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 158
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . 4 . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 7) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.38 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.75 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.19 ms)
- **Agent 4 (A*):** chose `DOWN` (took 31.15 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 159
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . 4 . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 8) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.75 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.77 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 13.60 ms)
- **Agent 4 (A*):** chose `LEFT` (took 27.83 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 160
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . 4 . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 8) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.03 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.51 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.40 ms)
- **Agent 4 (A*):** chose `DOWN` (took 29.10 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 161
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.86 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.98 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.70 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.85 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 162
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.71 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.39 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.08 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.01 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 163
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.34 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.81 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.87 ms)
- **Agent 4 (A*):** chose `WAIT` (took 30.86 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 164
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.15 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.89 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.52 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.55 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 165
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.82 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.64 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.16 ms)
- **Agent 4 (A*):** chose `WAIT` (took 22.89 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 166
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.77 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.99 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.44 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.18 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 167
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.29 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.04 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.26 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.76 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 168
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.81 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.37 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.29 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.56 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 169
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.30 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 10.70 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.02 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.84 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 170
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.47 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.16 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.20 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.17 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 171
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.93 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.96 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.21 ms)
- **Agent 4 (A*):** chose `WAIT` (took 30.01 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 172
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.44 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.39 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.55 ms)
- **Agent 4 (A*):** chose `WAIT` (took 24.32 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 173
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.92 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.16 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.16 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.17 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 174
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.95 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.31 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.52 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.77 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 175
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.47 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.98 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.15 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.94 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 176
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.53 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.34 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.99 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.31 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 177
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.92 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.43 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.07 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.56 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 178
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.25 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 10.75 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.78 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.48 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 179
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.75 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.94 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.31 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.12 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 180
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . R . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.84 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.46 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.51 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 27.93 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 181
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . 4 . # # . #|
|# . B # . R . . . R . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.62 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.40 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.69 ms)
- **Agent 4 (A*):** chose `DOWN` (took 19.84 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 182
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . 4 . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 10) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.86 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.33 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.02 ms)
- **Agent 4 (A*):** chose `UP` (took 21.41 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 183
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . 4 . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.02 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.34 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.28 ms)
- **Agent 4 (A*):** chose `LEFT` (took 27.95 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 184
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.58 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.76 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.01 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.10 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 185
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.27 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.33 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.26 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.58 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 186
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.27 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.64 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.49 ms)
- **Agent 4 (A*):** chose `WAIT` (took 24.17 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 187
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.65 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 10.99 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.30 ms)
- **Agent 4 (A*):** chose `WAIT` (took 28.16 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 188
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.34 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 23.75 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 41.50 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.14 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 189
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.21 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.29 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 13.67 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.52 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 190
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.86 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.65 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.09 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.97 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 191
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.61 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.20 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.03 ms)
- **Agent 4 (A*):** chose `WAIT` (took 24.33 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 192
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.22 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.00 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.70 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.79 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 193
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.20 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.13 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 13.31 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.02 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 194
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.93 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.51 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.88 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.27 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 195
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 28.19 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.39 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.41 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.67 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 196
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.03 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.42 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.82 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.07 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 197
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 23.01 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 10.76 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.24 ms)
- **Agent 4 (A*):** chose `WAIT` (took 29.19 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 198
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.66 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.32 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.08 ms)
- **Agent 4 (A*):** chose `WAIT` (took 24.29 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 199
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.68 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.29 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.62 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.74 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 200
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.91 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.69 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.56 ms)
- **Agent 4 (A*):** chose `WAIT` (took 24.42 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 201
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.26 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.36 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.30 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.11 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 202
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.36 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.53 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.08 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.47 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 203
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.23 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.78 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.91 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.52 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 204
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.82 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 10.66 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.72 ms)
- **Agent 4 (A*):** chose `WAIT` (took 28.20 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 205
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.80 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.23 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.55 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.67 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 206
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.07 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.92 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.74 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.18 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 207
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.28 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 10.77 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.39 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.25 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 208
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.67 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.82 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.20 ms)
- **Agent 4 (A*):** chose `WAIT` (took 24.34 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 209
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.42 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.75 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.93 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.66 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 210
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.70 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.58 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.83 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.63 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 211
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.25 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.08 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.67 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.30 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 212
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.87 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.67 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.76 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.57 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 213
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.17 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.03 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.56 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.44 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 214
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.05 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.61 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 13.28 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.17 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 215
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.28 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.79 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.60 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.93 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 216
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.61 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.54 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.55 ms)
- **Agent 4 (A*):** chose `WAIT` (took 24.54 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 217
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.70 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.77 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.49 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.52 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 218
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.73 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.39 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.81 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.01 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 219
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.83 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.42 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.96 ms)
- **Agent 4 (A*):** chose `WAIT` (took 30.05 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 220
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.00 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.28 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.94 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.38 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 221
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.67 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.95 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.16 ms)
- **Agent 4 (A*):** chose `WAIT` (took 31.01 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 222
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.36 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.84 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.65 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.26 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 223
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.37 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.88 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.14 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.63 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 224
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.87 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.45 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.08 ms)
- **Agent 4 (A*):** chose `WAIT` (took 30.83 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 225
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 23.52 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 10.94 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.04 ms)
- **Agent 4 (A*):** chose `WAIT` (took 28.45 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 226
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.89 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.82 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.55 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.10 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 227
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.61 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.11 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.89 ms)
- **Agent 4 (A*):** chose `WAIT` (took 28.71 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 228
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.76 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.34 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.53 ms)
- **Agent 4 (A*):** chose `WAIT` (took 30.43 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 229
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.92 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.52 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.07 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.84 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 230
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.01 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 10.96 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.99 ms)
- **Agent 4 (A*):** chose `WAIT` (took 29.88 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 231
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.93 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.74 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.41 ms)
- **Agent 4 (A*):** chose `WAIT` (took 28.08 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 232
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.72 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 10.93 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.35 ms)
- **Agent 4 (A*):** chose `WAIT` (took 28.52 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 233
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.56 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.04 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.87 ms)
- **Agent 4 (A*):** chose `WAIT` (took 24.76 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 234
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.37 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.33 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.05 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.04 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 235
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.00 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.82 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.99 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.39 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 236
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.26 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.73 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.48 ms)
- **Agent 4 (A*):** chose `WAIT` (took 24.15 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 237
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.49 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.82 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.28 ms)
- **Agent 4 (A*):** chose `WAIT` (took 22.89 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 238
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.70 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 10.74 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.88 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.36 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 239
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.45 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.23 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.14 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.92 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 240
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.99 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.24 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.48 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.60 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 241
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.11 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.32 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 13.71 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.81 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 242
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.67 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.63 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.82 ms)
- **Agent 4 (A*):** chose `WAIT` (took 24.78 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 243
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.10 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.30 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.64 ms)
- **Agent 4 (A*):** chose `WAIT` (took 29.15 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 244
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.43 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.74 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.53 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.69 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 245
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.79 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 10.70 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.54 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.60 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 246
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.99 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.14 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.35 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.16 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 247
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.67 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.64 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.97 ms)
- **Agent 4 (A*):** chose `WAIT` (took 24.88 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 248
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.64 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.48 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 16.85 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.80 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 249
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.79 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.55 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.72 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.21 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 250
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 23.10 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.22 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 22.28 ms)
- **Agent 4 (A*):** chose `WAIT` (took 24.50 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 251
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . . . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.43 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.01 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.34 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.95 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 252
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.59 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.46 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.43 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.75 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 253
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.76 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.33 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.75 ms)
- **Agent 4 (A*):** chose `WAIT` (took 28.70 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 254
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.71 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 10.89 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.30 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.29 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 255
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.24 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.61 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.07 ms)
- **Agent 4 (A*):** chose `WAIT` (took 28.10 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 256
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.37 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.45 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 17.96 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.94 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 257
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.05 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 15.88 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 27.66 ms)
- **Agent 4 (A*):** chose `WAIT` (took 24.52 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 258
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `LEFT` (took 22.47 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.51 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 13.72 ms)
- **Agent 4 (A*):** chose `WAIT` (took 25.76 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 259
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . 1 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . . . 3 # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.85 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.20 ms)
- **Agent 3 (Greedy):** chose `LEFT` (took 15.25 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.48 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 260
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . 1 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . . 3 . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (3, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 23.36 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.45 ms)
- **Agent 3 (Greedy):** chose `LEFT` (took 17.70 ms)
- **Agent 4 (A*):** chose `WAIT` (took 32.60 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 261
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . 1 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . 3 . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (2, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.66 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.67 ms)
- **Agent 3 (Greedy):** chose `LEFT` (took 17.15 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.05 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 262
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . 1 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# 3 . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.84 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.31 ms)
- **Agent 3 (Greedy):** chose `UP` (took 16.08 ms)
- **Agent 4 (A*):** chose `WAIT` (took 24.60 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 263
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . 1 2 . . . . . . # . . #|
|# 3 B B # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 21.34 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.72 ms)
- **Agent 3 (Greedy):** chose `UP` (took 15.79 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.05 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 264
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# 3 . 1 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.67 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 14.53 ms)
- **Agent 3 (Greedy):** chose `RIGHT` (took 17.46 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.03 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 265
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . 3 1 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.64 ms)
- **Agent 2 (HillClimbing):** chose `LEFT` (took 17.12 ms)
- **Agent 3 (Greedy):** chose `BOMB` (took 18.07 ms)
- **Agent 4 (A*):** chose `WAIT` (took 29.54 ms)

### Events during this step:
- 💣 **Greedy** placed a bomb at (2, 2)

----------------------------------------

## STEP 266
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . 3 2 . . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `RIGHT` (took 19.94 ms)
- **Agent 2 (HillClimbing):** chose `RIGHT` (took 16.76 ms)
- **Agent 3 (Greedy):** chose `LEFT` (took 16.59 ms)
- **Agent 4 (A*):** chose `WAIT` (took 18.88 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 267
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# 3 O . 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.76 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.49 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 15.86 ms)
- **Agent 4 (A*):** chose `WAIT` (took 19.83 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 268
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . O . 2 . . . . . . # . . #|
|# 3 B B # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 3) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.65 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.26 ms)
- **Agent 3 (Greedy):** chose `DOWN` (took 14.09 ms)
- **Agent 4 (A*):** chose `WAIT` (took 28.73 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 269
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . O . 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# 3 . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (1, 4) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.34 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.50 ms)
- **Agent 3 (Greedy):** chose `RIGHT` (took 13.00 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.80 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 270
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . O . 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . 3 . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (2, 4) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 18.93 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.51 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 15.09 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.17 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 271
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . O . 2 . . . . . . # . . #|
|# . B B # B B . . . . . C . #|
|# . 3 . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (2, 4) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.84 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 13.38 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 14.79 ms)
- **Agent 4 (A*):** chose `WAIT` (took 28.43 ms)

### Events during this step:
- 💥 Bomb owned by **Greedy** exploded at (2, 2) with range 1
- 🧱 Brick destroyed at (2, 3)

----------------------------------------

## STEP 272
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . * B . # B . . C B B . . #|
|# * * * 2 . . . . . . # . . #|
|# . * B # B B . . . . . C . #|
|# . 3 . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (2, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 16.86 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.38 ms)
- **Agent 3 (Greedy):** chose `RIGHT` (took 15.35 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.31 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 273
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . . B # B B . . . . . C . #|
|# . . 3 . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (3, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.47 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.34 ms)
- **Agent 3 (Greedy):** chose `LEFT` (took 18.80 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.46 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 274
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . . B # B B . . . . . C . #|
|# . 3 . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (2, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.98 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.10 ms)
- **Agent 3 (Greedy):** chose `UP` (took 19.51 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.32 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 275
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . . 2 . . . . . . # . . #|
|# . 3 B # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (2, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.27 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.24 ms)
- **Agent 3 (Greedy):** chose `UP` (took 17.21 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.90 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 276
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . 3 . 2 . . . . . . # . . #|
|# . . B # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.42 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.18 ms)
- **Agent 3 (Greedy):** chose `RIGHT` (took 17.11 ms)
- **Agent 4 (A*):** chose `WAIT` (took 22.60 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 277
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . 3 2 . . . . . . # . . #|
|# . . B # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `LEFT` (took 17.28 ms)
- **Agent 2 (HillClimbing):** chose `LEFT` (took 14.54 ms)
- **Agent 3 (Greedy):** chose `BOMB` (took 16.12 ms)
- **Agent 4 (A*):** chose `WAIT` (took 29.18 ms)

### Events during this step:
- 💣 **Greedy** placed a bomb at (3, 2)

----------------------------------------

## STEP 278
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . 3 . . . . . . . # . . #|
|# . . B # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `LEFT` (took 18.72 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.35 ms)
- **Agent 3 (Greedy):** chose `RIGHT` (took 13.71 ms)
- **Agent 4 (A*):** chose `WAIT` (took 18.98 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 279
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . 1 2 3 . . . . . . # . . #|
|# . . B # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (4, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `DOWN` (took 17.51 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 10.18 ms)
- **Agent 3 (Greedy):** chose `RIGHT` (took 17.50 ms)
- **Agent 4 (A*):** chose `WAIT` (took 21.11 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 280
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . 2 . 3 . . . . . # . . #|
|# . 1 B # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (5, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 17.82 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 10.52 ms)
- **Agent 3 (Greedy):** chose `RIGHT` (took 15.88 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.49 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 281
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . 2 . . 3 . . . . # . . #|
|# . 1 B # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (6, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.51 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.67 ms)
- **Agent 3 (Greedy):** chose `RIGHT` (took 15.02 ms)
- **Agent 4 (A*):** chose `WAIT` (took 28.18 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 282
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . 2 . . . 3 . . . # . . #|
|# . 1 B # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (7, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.30 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 12.27 ms)
- **Agent 3 (Greedy):** chose `RIGHT` (took 14.91 ms)
- **Agent 4 (A*):** chose `WAIT` (took 26.23 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 283
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . B . # B . . C B B . . #|
|# . . 2 . . . . 3 . . # . . #|
|# . 1 B # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (8, 2) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 19.88 ms)
- **Agent 2 (HillClimbing):** chose `WAIT` (took 11.83 ms)
- **Agent 3 (Greedy):** chose `WAIT` (took 18.63 ms)
- **Agent 4 (A*):** chose `WAIT` (took 23.22 ms)

### Events during this step:
- 💥 Bomb owned by **Greedy** exploded at (3, 2) with range 1
- 🧱 Brick destroyed at (3, 1)
- 🧱 Brick destroyed at (3, 3)
- 💀 **HillClimbing** died at (3, 2)!

----------------------------------------

## STEP 284
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . R . # B . . C B B . . #|
|# . * X * . . . 3 . . # . . #|
|# . 1 C # B B . . . . . C . #|
|# . . . . # # . . . # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (8, 2) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 20.19 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `DOWN` (took 19.00 ms)
- **Agent 4 (A*):** chose `WAIT` (took 27.33 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 285
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . R . # B . . C B B . . #|
|# . . X . . . . . . . # . . #|
|# . 1 C # B B . 3 . . . C . #|
|# . . . . # # . . R # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . C #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . 4 . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (8, 3) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 9) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `RIGHT` (took 19.29 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `DOWN` (took 18.26 ms)
- **Agent 4 (A*):** chose `UP` (took 23.78 ms)

### Events during this step:
- 💎 **SimulatedAnnealing** collected **BOMB_CAPACITY** item (Capacity: 1 -> 2)

----------------------------------------

## STEP 286
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . R . # B . . C B B . . #|
|# . . X . . . . . . . # . . #|
|# . . 1 # B B . . . . . C . #|
|# . . . . # # . 3 R # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . C #|
|# . B C B . # . 4 . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 3) | Lives: 1 | Ammo: 2/2 | Range: 1
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (8, 4) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 8) | Lives: 1 | Ammo: 5/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `DOWN` (took 25.02 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `DOWN` (took 68.12 ms)
- **Agent 4 (A*):** chose `BOMB` (took 48.10 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (8, 8)

----------------------------------------

## STEP 287
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . R . # B . . C B B . . #|
|# . . X . . . . . . . # . . #|
|# . . . # B B . . . . . C . #|
|# . . 1 . # # . . R # . . . #|
|# B . # B . . . 3 . . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . . . . . . C #|
|# . B C B . # . 4 . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 4) | Lives: 1 | Ammo: 2/2 | Range: 1
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (8, 5) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 8) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `UP` (took 96.65 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `RIGHT` (took 25.72 ms)
- **Agent 4 (A*):** chose `UP` (took 46.02 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 288
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . R . # B . . C B B . . #|
|# . . X . . . . . . . # . . #|
|# . . 1 # B B . . . . . C . #|
|# . . . . # # . . R # . . . #|
|# B . # B . . . . 3 . . . # #|
|# . . # . # B # . . . . . . #|
|# . # . . . . . 4 . . . . C #|
|# . B C B . # . O . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 3) | Lives: 1 | Ammo: 2/2 | Range: 1
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (9, 5) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (8, 7) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.41 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `DOWN` (took 18.43 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 20.75 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 289
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . R . # B . . C B B . . #|
|# . . X . . . . . . . # . . #|
|# . . 1 # B B . . . . . C . #|
|# . . . . # # . . R # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . 3 . . . . #|
|# . # . . . . . . 4 . . . C #|
|# . B C B . # . O . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 3) | Lives: 1 | Ammo: 2/2 | Range: 1
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (9, 6) | Lives: 1 | Ammo: 1/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 7) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 22.11 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `BOMB` (took 19.83 ms)
- **Agent 4 (A*):** chose `BOMB` (took 22.54 ms)

### Events during this step:
- 💣 **Greedy** placed a bomb at (9, 6)
- 💣 **A*** placed a bomb at (9, 7)

----------------------------------------

## STEP 290
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . R . # B . . C B B . . #|
|# . . X . . . . . . . # . . #|
|# . . 1 # B B . . . . . C . #|
|# . . . . # # . . R # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . 3 . . . . #|
|# . # . . . . . . 4 . . . C #|
|# . B C B . # . O . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 3) | Lives: 1 | Ammo: 2/2 | Range: 1
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (9, 6) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (9, 7) | Lives: 1 | Ammo: 3/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 30.45 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `RIGHT` (took 16.01 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 21.11 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 291
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . R R . # B . . C B B . . #|
|# . . X . . . . . . . # . . #|
|# . . 1 # B B . . . . . C . #|
|# . . . . # # . . R # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . O 3 . . . #|
|# . # . . . . . . O 4 . . C #|
|# . B C B . # . O . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 3) | Lives: 1 | Ammo: 2/2 | Range: 1
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (10, 6) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 7) | Lives: 1 | Ammo: 3/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `UP` (took 35.29 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `RIGHT` (took 18.37 ms)
- **Agent 4 (A*):** chose `UP` (took 21.26 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 292
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . R R . # B . . C B B . . #|
|# . . 1 . . . . . . . # . . #|
|# . . . # B B . . . . . C . #|
|# . . . . # # . . R # . . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . O 4 3 . . #|
|# . # . . . . . . O . . . C #|
|# . B C B . # . O . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (10, 6) | Lives: 1 | Ammo: 3/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 29.85 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `UP` (took 20.75 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 21.78 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (8, 8) with range 5

----------------------------------------

## STEP 293
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . R R . # B . . C B B . . #|
|# . . 1 . . . . . . . # . . #|
|# . . . # B B . * . . . C . #|
|# . . . . # # . * R # . . . #|
|# B . # B . . . * . . 3 . # #|
|# . . # . # B # * O . 4 . . #|
|# . # . . . . . * O . . . C #|
|# . B C B . # * * * * * * * #|
|# . . . R # . . * . . # # . #|
|# . B # . R . . * . . . . . #|
|# R . . B . . # * C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 2) | Lives: 1 | Ammo: 2/2 | Range: 1
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (11, 5) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `UP` (took 24.82 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `UP` (took 14.92 ms)
- **Agent 4 (A*):** chose `BOMB` (took 24.63 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (11, 6)
- 💎 **SimulatedAnnealing** collected **BOMB_RANGE** item (Range: 1 -> 2)

----------------------------------------

## STEP 294
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . R 1 . # B . . C B B . . #|
|# . . X . . . . . . . # . . #|
|# . . . # B B . . . . . C . #|
|# . . . . # # . . R # 3 . . #|
|# B . # B . . . . . . . . # #|
|# . . # . # B # . O . 4 . . #|
|# . # . . . . . . O . . . C #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (3, 1) | Lives: 1 | Ammo: 2/2 | Range: 2
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (11, 4) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 6) | Lives: 1 | Ammo: 3/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `LEFT` (took 30.80 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `RIGHT` (took 16.29 ms)
- **Agent 4 (A*):** chose `UP` (took 20.17 ms)

### Events during this step:
- 💎 **SimulatedAnnealing** collected **BOMB_RANGE** item (Range: 2 -> 3)

----------------------------------------

## STEP 295
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . 1 . . # B . . C B B . . #|
|# . . X . . . . . . . # . . #|
|# . . . # B B . . . . . C . #|
|# . . . . # # . . R # . 3 . #|
|# B . # B . . . . . . 4 . # #|
|# . . # . # B # . O . O . . #|
|# . # . . . . . . O . . . C #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . C . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 1) | Lives: 1 | Ammo: 2/2 | Range: 3
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 0/1 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (11, 5) | Lives: 1 | Ammo: 3/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 27.68 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `UP` (took 15.95 ms)
- **Agent 4 (A*):** chose `RIGHT` (took 20.63 ms)

### Events during this step:
- 💥 Bomb owned by **Greedy** exploded at (9, 6) with range 1
- 💥 Bomb owned by **A*** exploded at (9, 7) with range 5
- 💎 **Greedy** collected **BOMB_CAPACITY** item (Capacity: 1 -> 2)

----------------------------------------

## STEP 296
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . 1 . . # B . . C B B . . #|
|# . . X . . . . . * . # . . #|
|# . . . # B B . . * . . 3 . #|
|# . . . . # # . . * # . . . #|
|# B . # B . . . . * . . 4 # #|
|# . . # . # B # * * * O . . #|
|# . # . * * * * * * * * * * #|
|# . B C B . # . . * . . . . #|
|# . . . R # . . . * . # # . #|
|# . B # . R . . . * . . . . #|
|# R . . B . . # . * . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 1) | Lives: 1 | Ammo: 2/2 | Range: 3
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 2/2 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 5) | Lives: 1 | Ammo: 4/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 23.27 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `DOWN` (took 19.88 ms)
- **Agent 4 (A*):** chose `BOMB` (took 18.66 ms)

### Events during this step:
- 💣 **A*** placed a bomb at (12, 5)

----------------------------------------

## STEP 297
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . 1 . . # B . . C B B . . #|
|# . . X . . . . . . . # . . #|
|# . . . # B B . . . . . . . #|
|# . . . . # # . . . # . 3 . #|
|# B . # B . . . . . . . 4 # #|
|# . . # . # B # . . . O . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 1) | Lives: 1 | Ammo: 2/2 | Range: 3
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 2/2 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 5) | Lives: 1 | Ammo: 3/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.58 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `BOMB` (took 20.92 ms)
- **Agent 4 (A*):** chose `UP` (took 21.58 ms)

### Events during this step:
- 💣 **Greedy** placed a bomb at (12, 4)

----------------------------------------

## STEP 298
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . 1 . . # B . . C B B . . #|
|# . . X . . . . . . . # . . #|
|# . . . # B B . . . . . . . #|
|# . . . . # # . . . # . 4 . #|
|# B . # B . . . . . . . O # #|
|# . . # . # B # . . . O . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 1) | Lives: 1 | Ammo: 2/2 | Range: 3
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 1/2 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 4) | Lives: 1 | Ammo: 3/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `DOWN` (took 31.47 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `UP` (took 15.92 ms)
- **Agent 4 (A*):** chose `UP` (took 18.39 ms)

### Events during this step:
- *No major events*

----------------------------------------

## STEP 299
### Board State:
```
+-----------------------------+
|# # # # # # # # # # # # # # #|
|# . . . . # B . . C B B . . #|
|# . 1 X . . . . . . . # . . #|
|# . . . # B B . . . . . 4 . #|
|# . . . . # # . . . # . O . #|
|# B . # B . . . . . . . O # #|
|# . . # . # B # . . . O . . #|
|# . # . . . . . . . . . . . #|
|# . B C B . # . . . . . . . #|
|# . . . R # . . . . . # # . #|
|# . B # . R . . . . . . . . #|
|# R . . B . . # . . . # . . #|
|# # # # # # # # # # # # # # #|
+-----------------------------+
```
- **SimulatedAnnealing (Agent 1):** ALIVE | Pos: (2, 2) | Lives: 1 | Ammo: 2/2 | Range: 3
- **HillClimbing (Agent 2):** DEAD | Pos: (3, 2) | Lives: 0 | Ammo: 1/1 | Range: 1
- **Greedy (Agent 3):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 1/2 | Range: 1
- **A* (Agent 4):** ALIVE | Pos: (12, 3) | Lives: 1 | Ammo: 3/5 | Range: 5

### Actions Decided:
- **Agent 1 (SimulatedAnnealing):** chose `WAIT` (took 25.40 ms)
- **Agent 2 (HillClimbing):** dead (forced STOP)
- **Agent 3 (Greedy):** chose `LEFT` (took 14.89 ms)
- **Agent 4 (A*):** chose `LEFT` (took 23.05 ms)

### Events during this step:
- 💥 Bomb owned by **A*** exploded at (11, 6) with range 5
- 💀 **Greedy** died at (11, 3)!
- 💀 **A*** died at (11, 3)!

----------------------------------------

## Match Summary
🏆 **Winner:** **SimulatedAnnealing (player_1)**

### Final Stats Table:

| Rank | Agent Name | Agent ID | Survival Steps | Kills | Suicides | Bricks Destroyed | Items Picked | Avg Latency (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **SimulatedAnnealing** | player_1 | 300 | 0 | 0 | 1 | 3 | 22.78 |
| 2 | **Greedy** | player_3 | 300 | 1 | 0 | 5 | 1 | 18.33 |
| 3 | **A*** | player_4 | 300 | 1 | 1 | 27 | 12 | 26.05 |
| 4 | **HillClimbing** | player_2 | 284 | 0 | 0 | 0 | 0 | 14.46 |