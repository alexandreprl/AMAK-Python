import pygame

from amak import amak


class AMAKPygame:
    def __init__(self, amas, environment, width=640, height=480, fps=60):
        self._running = False
        self._display_surf = None
        self.fps = fps
        self.size = width, height
        self.amas = amas
        self.environment = environment
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("AMAK - Python")
        self.clock = pygame.time.Clock()
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

            self._display_surf.fill((0, 0, 0))
            self.environment.render(self._display_surf)

            for entity in self.amas.agents:
                if entity.surface and entity.rect:
                    self._display_surf.blit(entity.surface, entity.rect)

            pygame.display.update()
            self.clock.tick(self.fps)
        pygame.quit()


class AgentEntity(amak.Agent):
    def __init__(self, mas, initial_position, color=(255, 255, 255)):
        super().__init__(mas)
        self.surface = pygame.Surface((10, 10))
        self.surface.fill(color)
        self.rect = self.surface.get_rect(center=initial_position)

    def set_position(self, position):
        self.rect.center = position


class EnvironmentEntity:
    def __init__(self, initial_position, color=(255, 255, 255)):
        self.surface = pygame.Surface((10, 10))
        self.surface.fill(color)
        self.rect = self.surface.get_rect(center=initial_position)

    def set_position(self, position):
        self.rect.center = position

    def set_color(self, color):
        self.surface.fill(color)