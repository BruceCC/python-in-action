import pygame
import random

# 定义一些颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 定义一些常量
WIDTH = 20
HEIGHT = 20
MARGIN = 5

# 初始化pygame
pygame.init()

# 设置窗口大小
WINDOW_SIZE = [20 * WIDTH + 10, 20 * HEIGHT + 10]
screen = pygame.display.set_mode(WINDOW_SIZE)

# 设置标题
pygame.display.set_caption("贪吃蛇")


# 定义一个函数来绘制蛇
def draw_snake(snake_list):
    for pos in snake_list:
        pygame.draw.rect(screen, WHITE, [pos[0], pos[1], WIDTH, HEIGHT])


# 定义一个函数来绘制食物
def draw_food(food_pos):
    pygame.draw.rect(screen, RED, [food_pos[0], food_pos[1], WIDTH, HEIGHT])


# 定义一个函数来生成食物的位置
def generate_food():
    return [random.randrange(WIDTH, WINDOW_SIZE[0] - WIDTH, WIDTH),
            random.randrange(HEIGHT, WINDOW_SIZE[1] - HEIGHT, HEIGHT)]


# 定义一个函数来检查蛇是否吃到了食物
def check_eat(snake_list, food_pos):
    if len(snake_list) > 0:  # 检查蛇头列表是否为空
        if snake_list[0][0] == food_pos[0] and snake_list[0][1] == food_pos[1]:
            return True
    return False


# 定义一个函数来检查蛇是否撞到了自己
def check_collision(snake_list):
    if len(snake_list) > 1:  # 检查蛇身列表是否为空
        if snake_list[0] in snake_list[1:]:
            return True
    return False


# 定义一个函数来更新蛇的位置
def update_snake(snake_list, direction):
    if len(snake_list) > 0:  # 检查蛇头列表是否为空
        if direction == "UP":
            new_head = [snake_list[0][0], snake_list[0][1] - HEIGHT]
        elif direction == "DOWN":
            new_head = [snake_list[0][0], snake_list[0][1] + HEIGHT]
        elif direction == "LEFT":
            new_head = [snake_list[0][0] - WIDTH, snake_list[0][1]]
        elif direction == "RIGHT":
            new_head = [snake_list[0][0] + WIDTH, snake_list[0][1]]
        snake_list.insert(0, new_head)
    return snake_list


# 定义一个函数来检查蛇是否撞到了边界
def check_boundary(snake_list):
    if len(snake_list) > 0:  # 检查蛇头列表是否为空
        if snake_list[0][0] < 0 or snake_list[0][0] >= WINDOW_SIZE[0] or snake_list[0][1] < 0 or snake_list[0][1] >= \
                WINDOW_SIZE[1]:
            return True
    return False


# 定义一个函数来更新游戏状态
'''
@Description: 根据蛇的位置列表、食物位置和蛇的方向来更新游戏状态
@Param: snake_list - 蛇的位置列表；food_pos - 食物位置；direction - 蛇的方向
@return: 如果游戏结束返回False，否则返回更新后的蛇的位置列表和新的食物位置
@author: <a href="mailto:author@chinaums.com">author</a>
@date: 2023-11-09 14:02:57
'''
def update_game(snake_list, food_pos, direction):
    if check_eat(snake_list, food_pos):
        food_pos = generate_food()
    else:
        if len(snake_list) > 0:  # 检查蛇的列表是否为空
            snake_list.pop()
    if check_collision(snake_list) or check_boundary(snake_list):
        return False
    snake_list = update_snake(snake_list, direction)
    return snake_list, food_pos


# 定义一个函数来运行游戏
def run_game():
    # 初始化蛇的位置和方向
    snake_list = [[100, 100]]
    direction = "RIGHT"

    # 初始化食物的位置
    food_pos = generate_food()

    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = "UP"
                elif event.key == pygame.K_DOWN:
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT:
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    direction = "RIGHT"

        # 更新游戏状态
        result = update_game(snake_list, food_pos, direction)
        if result is False:
            break
        else:
            snake_list, food_pos = result

        # 绘制背景
        screen.fill(BLACK)

        # 绘制蛇和食物
        draw_snake(snake_list)
        draw_food(food_pos)

        # 更新屏幕
        pygame.display.flip()

        # 控制游戏速度
        pygame.time.Clock().tick(10)


# 运行游戏
run_game()
