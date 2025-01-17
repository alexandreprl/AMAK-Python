import pygame


class AMAKPygame:
    def __init__(self, amas, environment):
        self._running = False
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        self.amas = amas
        self.environment = environment
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("AMAK - Python")
        self.start()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def start(self):
        if not self._running:
            self._running = True
            self.on_execute()

    def on_execute(self):
        while self._running and not self.amas.is_ready_to_stop():
            for event in pygame.event.get():
                self.on_event(event)
            self.amas.cycle()
            self.environment.cycle()

        pygame.quit()
