import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0] # there's only one
        bricks = cast["brick"]
        
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                bricks.remove(brick)
                velocity = ball.get_velocity()
                x = velocity.get_x()
                y = velocity.get_y()
                x *= random.choice(constants.DIRECTION)
                y *= -1

                velocity = Point(x, y)
                ball.set_velocity(velocity)

        ball_position = ball.get_position()
        ball_velocity = ball.get_velocity()
        x1 = ball_position.get_x()
        y1 = ball_position.get_y()
        x2 = ball_velocity.get_x()
        y2 = ball_velocity.get_y()

        if x1 < 2: 
            x2 *= -1
            
        if x1 > (constants.MAX_X - 2):
            x2 *= -1
            
        if y1 < 2: 
            y2 *= -1
        
        #if y1 > (constants.MAX_Y ):
        #    y2 *= -1
        #    y1 = 20
        
        paddle_position = paddle.get_position()
        paddle_x = paddle_position.get_x()
        paddle_y = paddle_position.get_y()
                         
        if paddle_x < 0: 
            paddle_x = 0
            
        if paddle_x > 69:
            paddle_x = 69

        paddle_length = 11

        if y1 == paddle_y:
            length = paddle_x
            for n in range(paddle_length):
                if x1 == length:
                    x2 *= random.choice(constants.DIRECTION)    
                    y2 *= -1
                length += 1

        ball_velocity = Point(x2, y2)
        ball.set_velocity(ball_velocity)
        paddle_position = Point(paddle_x, paddle_y)
        paddle.set_position(paddle_position)
        