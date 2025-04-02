import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'  # Current drawing color
    draw_mode = 'circle'  # Drawing mode:  'circle', 'rect', 'square', 'triangle', 'equilateral', 'rhombus', or 'eraser'
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
                elif event.key == pygame.K_c:  # 'C' for circles
                    draw_mode = 'circle'
                elif event.key == pygame.K_v:  # 'V' for rectangles
                    draw_mode = 'rect'
                elif event.key == pygame.K_e:  # 'E' for eraser
                    draw_mode = 'eraser'
                elif event.key == pygame.K_q:  # 'Q' for square
                    draw_mode = 'square'
                elif event.key == pygame.K_t:  # 'T' for right triangle
                    draw_mode = 'triangle'
                elif event.key == pygame.K_y:  # 'Y' for equilateral triangle
                    draw_mode = 'equilateral'
                elif event.key == pygame.K_d:  # 'D' for rhombus
                    draw_mode = 'rhombus'

            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos
                drawing = True

            if event.type == pygame.MOUSEBUTTONUP and drawing:
                end_pos = event.pos

                if draw_mode == 'rect':
                    width = abs(end_pos[0] - start_pos[0])
                    height = abs(end_pos[1] - start_pos[1])
                    pygame.draw.rect(screen, get_color(mode), (start_pos[0], start_pos[1], width, height))

                elif draw_mode == 'square':
                    side_length = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, get_color(mode), (start_pos[0], start_pos[1], side_length, side_length))

                elif draw_mode == 'circle':
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, get_color(mode), start_pos, radius)

                elif draw_mode == 'triangle':
                    pygame.draw.polygon(screen, get_color(mode), [start_pos, (end_pos[0], start_pos[1]), (start_pos[0], end_pos[1])])

                elif draw_mode == 'equilateral':
                    side_length = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    height = side_length * (3 ** 0.5) / 2
                    points = [
                        (start_pos[0], start_pos[1]),
                        (start_pos[0] + side_length, start_pos[1]),
                        (start_pos[0] + side_length / 2, start_pos[1] - height)
                    ]
                    pygame.draw.polygon(screen, get_color(mode), points)

                elif draw_mode == 'rhombus':
                    width = abs(end_pos[0] - start_pos[0])
                    height = abs(end_pos[1] - start_pos[1])
                    points = [
                        (start_pos[0] + width / 2, start_pos[1]),
                        (start_pos[0], start_pos[1] + height / 2),
                        (start_pos[0] + width / 2, start_pos[1] + height),
                        (start_pos[0] + width, start_pos[1] + height / 2)
                    ]
                    pygame.draw.polygon(screen, get_color(mode), points)

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
    return (255, 255, 255)  # Default to white

main()