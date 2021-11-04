from game.action import Action

class DrawActorsAction(Action):
    """A code template for drawing the actors. The responsibility of this
    class of objects is ...
    
    Stereotype:
        Controller

    Attributes:
        output_service (outputService): An instance of outputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            output_service (outputService): An instance of outputService.
        """
        
        self._output_service = output_service
    
    def execute(self, cast):
        """Draws the actors to the screen.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()
        
        for actor in cast.values():
            
            self._output_service.draw_actors(actor)

        self._output_service.flush_buffer()
