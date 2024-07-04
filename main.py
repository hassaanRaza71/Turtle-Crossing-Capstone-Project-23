import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(player.move_up,"Up")
car_manager=CarManager()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    if player.ycor()>=FINISH_LINE_Y:
        player.restart()
        scoreboard.increase_level()
        car_manager.level_up()
    for car in car_manager.all_cars:
        if player.distance(car)<=20:
            game_is_on=False
            scoreboard.game_over()
            



screen.mainloop()