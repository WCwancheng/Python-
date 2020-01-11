import os,random
import pygame as pg

MAX_SHOTS = 5
SCREENRECT = pg.Rect(0, 0, 480, 640)

class GameState:
    NONE = 0,
    GAME = 1,
    END = 2,

#玩家
class Player(pg.sprite.Sprite):
    hp = 10
    speed = 10
    bounce = 24
    image = None
    reloading = None
    def __init__(self,image,player_rect,init_pos):
        pg.sprite.Sprite.__init__(self)
        print("玩家")
        self.image = image
        self.rect = player_rect
        self.rect.topleft = init_pos
        self.origtop = self.rect.top
        self.reloading = None
        self.bullets = pg.sprite.Group()
        print(self.rect.top)
        self.facing = -1
    
    def Move(self,order):
        if order == 'up':
            self.rect.top += 1
        elif order == 'down':  
            self.rect.top -= 1
        elif order == 'left':  
            self.rect.move_ip(-1*self.speed,0)
        elif order == 'right':  
            self.rect.move_ip(1*self.speed,0)

        self.rect = self.rect.clamp(SCREENRECT)
        self.rect.top = self.origtop - (self.rect.left // self.bounce % 2)

    def Shoot(self,bullet_img):
        print("玩家射击")
        #生成子弹
        bullet = Bullet(bullet_img,self.rect.midtop)
        self.bullets.add(bullet)
        self.reloading = 0

class Enemy(pg.sprite.Sprite):
    hp = 10
    speed = 3
    image = None
    def __init__(self,image,init_pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
    
    def Move(self):
        self.rect.top += self.speed

class Bullet(pg.sprite.Sprite):
    speed = 10
    image = None
    def __init__(self,image,init_pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        print(init_pos)
        print("子弹")

    def Move(self):
        self.rect.top -= self.speed
    
class Explosion(pg.sprite.Sprite):
    defaultlife = 12
    def __init__(self,image,actor):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(center = actor.rect.center)
        self.life = self.defaultlife
    
    def update(self):
        self.life = self.life - 1
        self.image = self.image
        if self.life <= 0:
            self.kill()

def main():
    pg.init()
    screen = pg.display.set_mode(SCREENRECT.size)
    pg.display.set_caption('1111')
    enemies1 = pg.sprite.Group()
    explsion_group = pg.sprite.Group()

    shoot_sound = pg.mixer.Sound("/Volumes/Dpan/PythonTest/Python-/PlaneGame/car_door.wav")#写成自己的绝对路径
    boom_sound = pg.mixer.Sound("/Volumes/Dpan/PythonTest/Python-/PlaneGame/boom.wav")
    
    if pg.mixer:
        pg.mixer.music.load("/Volumes/Dpan/PythonTest/Python-/PlaneGame/house_lo.wav")
        pg.mixer.music.play(-1)

    enemy_frequency = 0

    player_img = pg.image.load("/Volumes/Dpan/PythonTest/Python-/PlaneGame/player1.gif") 
    player_img = pg.transform.flip(player_img,1,0)
    player = Player(player_img,pg.Rect(0,100,100,100),[240,550])

    bullet_img = pg.image.load("/Volumes/Dpan/PythonTest/Python-/PlaneGame/shot.gif")

    enemy_img = pg.image.load("/Volumes/Dpan/PythonTest/Python-/PlaneGame/alien1.png")

    explosion_img = pg.image.load("/Volumes/Dpan/PythonTest/Python-/PlaneGame/explosion1.gif")

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,255,0))

    image_bg = pg.image.load("/Volumes/Dpan/PythonTest/Python-/PlaneGame/background.gif")
    image_bg.convert()
    image_bg = pg.transform.scale(image_bg,SCREENRECT.size)
    background.blit(image_bg,(0,0))
    screen.blit(background,(0,0))
    pg.display.update()

    shot = 0
    score = 0

    running = True
    while running:
        screen.fill((0))
        screen.blit(background,(0,0))
        screen.blit(player.image,player.rect)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        keystate = pg.key.get_pressed()

        if enemy_frequency % 50 == 0:
            enemy_pos = [random.randint(0,480 - 50),0]
            enemy = Enemy(enemy_img,enemy_pos)
            enemies1.add(enemy)

        enemy_frequency += 1
        if enemy_frequency >= 100:
            enemy_frequency = 0

        for eme in enemies1:
            eme.Move()
            if pg.sprite.collide_circle(eme,player):
                exp = Explosion(explosion_img,eme)
                explsion_group.add(exp)
                if pg.mixer:
                    boom_sound.play()
                player.hp -= 1
                if player.hp <= 0:
                    running = False
                enemies1.remove(eme)
                break

            for bul in player.bullets:
                if pg.sprite.collide_circle(eme,bul):
                    exp = Explosion(explosion_img,eme)
                    explsion_group.add(exp)
                    if pg.mixer:
                        boom_sound.play()
                    score += 1
                    enemies1.remove(eme)
                    player.bullets.remove(bul)
                    break

            if eme.rect.top > 640:
                enemies1.remove(eme)

        fireing = keystate[pg.K_SPACE]
        if fireing and shot <= MAX_SHOTS and not player.reloading:
            player.Shoot(bullet_img)
            if pg.mixer:
                shoot_sound.play()
        player.reloading = fireing

        for bullet_s in player.bullets:
            bullet_s.Move()
            if bullet_s.rect.bottom < 0:
                player.bullets.remove(bullet_s) 

        for exp in explsion_group:
            exp.update()
            if exp.life <=0 :
                explsion_group.remove(exp)

        player.bullets.draw(screen)
        enemies1.draw(screen)
        explsion_group.draw(screen)

        #得分
        score_font = pg.font.Font(None,36)
        score_text = score_font.render(str(score),True,(120,120,120))
        text_rect = score_text.get_rect()
        text_rect.topleft = [20,20]
        screen.blit(score_text,text_rect)

        #玩家生命
        player_hp_text = score_font.render(str('HP: %d' % player.hp),True,(200,120,120))
        player_hp_rect = player_hp_text.get_rect()
        player_hp_rect.topleft = [20,500]
        screen.blit(player_hp_text,player_hp_rect)

        pg.display.update()
        if keystate[pg.K_RIGHT]:
            player.Move('right')
        elif keystate[pg.K_LEFT]:
            player.Move('left')
        elif keystate[pg.K_UP]:
            player.Move('up')
        elif keystate[pg.K_DOWN]:
            player.Move('down')

    pg.quit()

if __name__=='__main__':
    main()