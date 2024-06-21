# This is the script for the game state machine 
class StateManager:
    def __init__(self, game):
        self.game = game 
        self.states = {}
        self.current_state = None 
        

    def add_state(self, state_name, state):
        # Adds a new state to the state manager.
        self.states[state_name] = state

    def change_state(self, state_name):
        # Changes the current state of the game to the given state name.
        if self.current_state:
            self.current_state.exit_state()
        self.current_state = self.states.get(state_name)
        if self.current_state:
            self.current_state.enter_state()

    def update(self, events):
        # Updates the current state.
        if self.current_state:
            self.current_state.update(events)

    def draw(self, screen):
        # Draws the current state.
        if self.current_state:
            self.current_state.draw(screen)

    def exit_state(self):
        # Exits the current state.
        if self.current_state:
            self.current_state.exit_state()
            self.current_state = None
    

    """bring in the main player position function here 
    def restart_game(self):
        self.player.position = pygame.math.Vector2(WIDTH / 2, HEIGHT / 2)
        self.asteroids.empty()
        """
    
    """def restart_state(self):
        if self.current_state:
            state_name = "title_screen"
            self.change_state(state_name)"""
    
    def restart_state(self, state_name=None):
        # Restarts the given state or the current state if no state name is provided.
        if state_name:
            # Restart a specific state by name
            if state_name in self.states:
                self.states[state_name].exit_state()
                # Reinitialize the state (assuming the state class has an initialization method)
                self.states[state_name].__init__(self.game)
                self.change_state(state_name)
        else:
            # Restart the current state
            if self.current_state:
                current_state_name = [name for name, state in self.states.items() if state == self.current_state][0]
                self.current_state.exit_state()
                self.current_state.__init__(self.game)
                self.change_state(current_state_name)


