import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'  # Current drawing color
    draw_mode = 'circle'  # Drawing mode:  'circle', 'rect', or 'eraser'
    drawing = False
    start_pos = (0, 0) 

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # Change drawing color
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

                # Change drawing mode
                elif event.key == pygame.K_c: # 'C' for circles
                    draw_mode = 'circle'
                elif event.key == pygame.K_v: # 'V' for rectangles
                    draw_mode = 'rect'
                elif event.key == pygame.K_e: # 'E' for eraser
                    draw_mode = 'eraser'

            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos
                drawing = True

            if event.type == pygame.MOUSEBUTTONUP and drawing:
                end_pos = event.pos

                if draw_mode == 'rect':
                    width = abs(end_pos[0] - start_pos[0])
                    height = abs(end_pos[1] - start_pos[1])
                    pygame.draw.rect(screen, get_color(mode), (start_pos[0], start_pos[1], width, height))

                elif draw_mode == 'circle':
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, get_color(mode), start_pos, radius)

                drawing = False

            if event.type == pygame.MOUSEMOTION and drawing and draw_mode == 'eraser':
                pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)

        pygame.display.flip()
        clock.tick(60)

def get_color(mode):
    """Returns the color based on the selected mode"""
    if mode == 'blue':
        return (0, 0, 255)
    elif mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    return (255, 255, 255)  

main()