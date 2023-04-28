import pygame

pygame.init()

# 设置窗口大小和标题
window_size = (400, 300)
window_title = "专注时钟"
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

# 定义计时器参数
font = pygame.font.Font(None, 36)
time_limit = 25 * 60  # 25分钟
start_time = pygame.time.get_ticks()

# 循环，直到用户关闭窗口
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # 计算已经过去的时间
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time

    # 计算剩余时间
    remaining_time = time_limit - elapsed_time
    if remaining_time < 0:
        remaining_time = 0

    # 将剩余时间转换成分钟和秒
    minutes = int(remaining_time / 1000 / 60)
    seconds = int((remaining_time / 1000) % 60)

    # 显示剩余时间
    text = font.render("{:02d}:{:02d}".format(minutes, seconds), True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(text, (150, 130))

    # 更新屏幕
    pygame.display.flip()

    # 判断时间是否到了
    if elapsed_time >= time_limit * 1000:
        # 时间到了，退出循环
        break

pygame.quit()
quit()
