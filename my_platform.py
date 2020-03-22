import play
import pygame

play.set_backdrop('light green')
coin_sound = pygame.mixer.Sound('coin.wav')
sea_sound = pygame.mixer.Sound('sea.ogg')
pygame.display.set_caption('Platformer: The Stupidest Game Ever!')

gameover_text = play.new_text(words = 'GAME OVER', x = 0, y = play.screen.top - 100, font_size=50)
retry_button = play.new_text(words="RETRY", x = 0, y = play.screen.bottom + 200, font_size=50)

gameover_text.hide()
retry_button.hide()

sprite = play.new_circle(
    color= 'black', x = play.screen.left + 20, y = play.screen.top - 20, border_width=3, radius = 15
)

coins = []
platforms = []

def draw_platforms():
    platform1 = play.new_box(
        color = 'brown', border_width= 1, border_color= 'black', width = 150, height = 30, x = play.screen.left + 70, y = play.screen.top-170
    )
    platforms.append(platform1)

    platform2 = play.new_box(
        color = 'brown', border_width= 1, border_color= 'black', width = 250, height = 30, x = play.screen.left + 330, y = play.screen.top-150
    )
    platforms.append(platform2)

    platform3 = play.new_box(
        color = 'brown', border_width= 1, border_color= 'black', width = 100, height = 30, x = play.screen.left + 550, y = play.screen.top-150
    )
    platforms.append(platform3)
    
    platform4 = play.new_box(
        color = 'brown', border_width= 1, border_color= 'black', width = 130, height = 30, x = play.screen.left + 670, y = play.screen.top-170
    )
    platforms.append(platform4)

    platform5 = play.new_box(
        color = 'brown', border_width= 1, border_color= 'black', width = 150, height = 30, x = play.screen.left + 80, y = play.screen.top-300
    )
    platforms.append(platform5)

    platform6 = play.new_box(
        color = 'brown', border_width= 1, border_color= 'black', width = 250, height = 30, x = play.screen.left + 340, y = play.screen.top-280
    )
    platforms.append(platform6)

    platform7 = play.new_box(
        color = 'brown', border_width= 1, border_color= 'black', width = 100, height = 30, x = play.screen.left + 560, y = play.screen.top-300
    )
    platforms.append(platform7)
    
    platform8 = play.new_box(
        color = 'brown', border_width= 1, border_color= 'black', width = 130, height = 30, x = play.screen.left + 700, y = play.screen.top-260
    )
    platforms.append(platform8)
    for platform in platforms:
        platform.start_physics(can_move=False, stable=True, obeys_gravity=True, mass = 10)

def draw_coins():
    coin1 = play.new_circle(
        color = 'yellow', x = play.screen.left + 330, y = play.screen.top - 130, radius = 10
    )
    coins.append(coin1)
    coin2 = play.new_circle(
        color = 'yellow', x = play.screen.left + 700, y = play.screen.top - 130, radius = 10
    )
    coins.append(coin2)
    coin3 = play.new_circle(
        color = 'yellow', x = play.screen.left + 340, y = play.screen.top - 230, radius = 10
    )
    coins.append(coin3)
    coin4 = play.new_circle(
        color = 'yellow', x = play.screen.left + 700, y = play.screen.top - 230, radius = 10
    )
    coins.append(coin4)

score_txt = play.new_text(words='Score:', x=play.screen.right-100, y=play.screen.top-30, size=70)
score_num = 0
score = play.new_text(words=str(score_num), x=play.screen.right-30, y=play.screen.top-30, size=70)


text = play.new_text(words='Tap SPACE to jump, a/d to move', x=0, y=play.screen.bottom+60, size=70)

sea = play.new_box(
        color='blue', width=play.screen.width, height=50, x=0, y=play.screen.bottom+20
    )

@play.when_program_starts
def start():
    pygame.mixer_music.load('soundtrack.mp3')
    pygame.mixer_music.play()

    sprite.start_physics(can_move= True, stable = False, obeys_gravity=True, mass =50, friction=1.0, bounciness=0.5)

    draw_platforms()
    draw_coins()

@play.repeat_forever
async def game():
    global score
    global score_num
    if sprite.is_touching(sea):
        sea_sound.play()
        gameover_text.show()
        retry_button.show()        

    for c in coins:
        if c.is_touching(sprite):
            coin_sound.play()
            sprite.physics.y_speed = -1 *sprite.physics.y_speed
            c.hide()
            coins.remove(c)
            score.words = str(int(score.words) + 1)
                        
    if play.key_is_pressed('d'):
        sprite.physics.x_speed = 10
    elif play.key_is_pressed('a'):
        sprite.physics.x_speed = -10
    elif play.key_is_pressed('space'):
        sprite.physics.y_speed = 50
        await play.timer(seconds=1)
        sprite.physics.y_speed = 0
    await play.timer(seconds=1/60)

@retry_button.when_clicked
async def clicking():
    sprite.x = play.screen.left + 70
    sprite.y = play.screen.top-140
    sprite.show()
    score_num = 0
    score.words = '0'
    draw_coins()
    retry_button.hide()
    gameover_text.hide()


play.start_program()