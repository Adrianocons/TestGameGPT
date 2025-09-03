import pygame
from .game import Game

TILE_SIZE = 48
COLORS = {
    'land': (34, 139, 34),
    'water': (65, 105, 225),
    'village': (205, 133, 63),
    'grid': (0, 0, 0),
}
PLAYER_COLORS = [
    (220, 20, 60),
    (30, 144, 255),
    (255, 215, 0),
    (138, 43, 226),
]

def draw_map(surface: pygame.Surface, game: Game) -> None:
    for y in range(game.map.height):
        for x in range(game.map.width):
            tile = game.map.get_tile(x, y)
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            color = COLORS['land'] if tile.terrain == 'land' else COLORS['water']
            if tile.village:
                color = COLORS['village']
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, COLORS['grid'], rect, 1)
            if tile.unit:
                player_color = PLAYER_COLORS[tile.unit.player % len(PLAYER_COLORS)]
                pygame.draw.circle(surface, player_color, rect.center, TILE_SIZE // 3)

def main() -> None:
    pygame.init()
    game = Game()
    width, height = game.map.width * TILE_SIZE, game.map.height * TILE_SIZE
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Polythorogue')
    clock = pygame.time.Clock()

    running = True
    need_redraw = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.step()
                    need_redraw = True
        if need_redraw:
            draw_map(screen, game)
            pygame.display.flip()
            need_redraw = False
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
