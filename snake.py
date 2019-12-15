import random
import curses

s = curses.initscr()
curses.noecho()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

score=0
scoreboard = [0, sw/2]

food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PLUS)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    if key == curses.KEY_DOWN and next_key == curses.KEY_UP:
        next_key = key
    elif key == curses.KEY_UP and next_key == curses.KEY_DOWN:
        next_key = key
    elif key == curses.KEY_LEFT and next_key == curses.KEY_RIGHT:
        next_key = key
    elif key == curses.KEY_RIGHT and next_key == curses.KEY_LEFT:
        next_key = key
    key = key if next_key == -1 else next_key
  
    if snake[0][0] in [0, sh-1] or snake[0][1]  in [0, sw-1]:
        curses.endwin()
        quit()
    
    if snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            score += 1
            nf = [
                random.randint(1, sh-2),
                random.randint(1, sw-2)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PLUS)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')
    
#    w.addch(int(scoreboard[0]), int(scoreboard[1]), str(score)) 
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
