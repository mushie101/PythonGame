import pygame

def score_list_function(num):
    score_list[n-1] = num
    return score_list

class python_game_characters():
    def __init__(self, num=1):
        self.single_player=True
        self.player_number=num
        self.health=100
        self.points=0
        self.screen_width = 750
        self.screen_height = 750
        self.boat=[[True, 0],[True, 187.5],[True, 375],[True, 562.5]]
        self.width=58
        self.height=80
        self.x=392
        self.y=512
        self.velocity=4
        self.run=True
        self.isWalk=False
        self.left=False
        self.character_movements_animation()
        self.game_setup()

    def final_result(self):
        if score_list[0] > score_list[1]: 
            winner = 1
        else:
            winner = 2
        self.win_text=self.font_.render(('Player {0} wins'.format(winner)),1,(255,255,0))
        self.win.blit(self.win_text, (550,600))

    def timer_implementation(self):
        if self.timer_start == False:
            self.start_time=pygame.time.get_ticks()
        else:
            self.seconds=(pygame.time.get_ticks()-self.start_time)/1000
            self.timer_text=self.font_.render('Timer:-{0}'.format(self.seconds//1),1,(255,255,255))
            self.win.blit(self.timer_text,(600,600))

    def display_points(self):
        self.win.blit(self.points_text, (20,720))

    def game_end_handler(self):
        self.end = True
        self.timer_start = False
        self.display_points()
        self.win.blit(self.reset_text, (200, 700))
        pygame.display.update()
        keys=pygame.key.get_pressed()
        if self.player_number == 2:
            self.final_result()
        if keys[pygame.K_r]:
            main(1)
        elif keys[pygame.K_q]:
            pygame.quit()
        elif keys[pygame.K_n]:
            n=2
            main(2)

    def extra_descriptors(self):
        self.font_ = pygame.font.SysFont('comicsans', 20, True, True)
        player_text = self.font_.render(("Player {0}".format(self.player_number)),1,(0,0,255))
        health_text = self.font_.render("Health:-",1,(255,255,255))
        self.lose_text=self.font_.render('You Have Lost!!!',1,(255,0,255))
        self.win_text=self.font_.render('You Have Won!!!',1,(255,0,255))
        if n == 1:  self.reset_text=self.font_.render('Press R to Play again Q to quit and N for next player',1,(255,0,0))
        elif n == 2: self.reset_text=self.font_.render('Press R to Play again Q to quit',1,(255,0,0))
        self.points_text=self.font_.render(('Points:-{0}'.format(self.points)),1,(255,255,0))
        self.win.blit(player_text, (20,600))
        self.win.blit(health_text, (20,640))
        pygame.draw.rect(self.win, (0,255,0), (20,675,self.health,15))
        pygame.draw.rect(self.win, (255,255,0), (20,675,100,15),2)

    def win_check(self):
        score_list_function(self.points)
        self.points=self.health*420-((self.seconds*69)//1)
        self.win.blit(self.win_text, (300,600))
        pygame.display.update()
        self.game_end_handler()

    def game_lost(self):
        self.points=0
        score_list_function(self.points)
        self.win.blit(self.lose_text, (300,600))
        pygame.display.update()
        self.game_end_handler()

    def fire_collision(self):
        if self.health > 0:
            self.health -= 1
        

    def check_collision(self):
        bridge_counter=0
        river_counter=0
        self.timer_implementation()
        for i in range(9):
            if i%2 == 0:
                for j in range(5):
                    if bridge_counter%2==0:
                        if (self.x-((j*150))<=62 and self.x-((j*150))>=-30) and ((self.y-((i)*64))<=62 and (self.y-((i)*64))>=-30):
                            self.fire_collision()
                    else:
                        if (self.x-((j*150)+64)<=62 and self.x-((j*150)+64)>=-30) and ((self.y-((i)*64))<=62 and (self.y-((i)*64))>=-30):
                            self.fire_collision()
                bridge_counter+=1
            else:
                if ((self.x-self.boat[river_counter][1]<=62 and self.x-self.boat[river_counter][1]>=-30)and(self.y-i*64<=62 and self.y-i*64>=-30)):
                    self.health=0
                river_counter+=1
        if self.health == 0:
            self.game_lost()
        if self.y <= 32:
            self.win_check()
        if self.seconds >= 20:
            self.game_lost()
        

    def move_boat(self):
        boat_velocity = 2.5
        river_count=0
        for i in self.boat:
            if i[0]==True and i[1]+boat_velocity>self.screen_width:
                i[0]=False
            if i[0]==False and i[1]<boat_velocity:
                i[0]=True
            if i[0] == True:
                i[1]+=boat_velocity
            else:
                i[1]-=boat_velocity
            boat_velocity-=0.5
            pygame.draw.rect(self.win, (0,255,0), [(i[1]),(2*river_count+1)*64,64,64])
            river_count+=1


    def render_obstacles(self):
        bridge_counter=0
        river_counter=0
        for i in range(9):
            if i % 2 == 0:
                for j in range(5):
                    if bridge_counter%2 == 0:
                        pygame.draw.rect(self.win, (255,0,0), [(j*150),(i*64),64,64])
                    else:
                        pygame.draw.rect(self.win, (255,0,0), [(j*150)+64,(i*64),64,64])
                bridge_counter+=1
            else:
                self.move_boat()

    def surroundings(self):
        self.river_height=self.bridge_height=64
        self.bridge_width=64
        self.river_width=250
        for j in range(((self.screen_height*8)//10)//(self.river_height)):
            if j % 2 == 1:
                for i in range(self.screen_width//self.river_width+1):
                    self.win.blit((pygame.image.load('./sprites/Ocean_SpriteSheet.png')),(self.river_width*i,(self.river_height*j)))
            else:
                for i in range((self.screen_width//self.bridge_width)+1):
                    self.win.blit((pygame.transform.rotate(pygame.image.load('./sprites/bridge.png'),90)),(self.bridge_width*i,(self.bridge_height*j)))

    def game_setup(self):
        n=self.player_number
        self.timer_start=False
        self.end = False
        self.player_index=1
        self.seconds=0
        pygame.init()
        self.win=pygame.display.set_mode((self.screen_width,self.screen_height))
        pygame.display.set_caption("River cross 1 v 1")
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run=False
                    pygame.quit()
            self.user_movement_input()
    
    def character_drawing(self):
        self.win.fill((0,0,0))
        self.extra_descriptors()
        # self.timer-=1
        # self.win.blit(self.timer_text,(600,600))
        # pygame.display.update()
        self.surroundings()
        self.render_obstacles()
        if self.walkcount+1 > 30:  self.walkcount=0
        if self.idle_count+1 > 20: self.idle_count=0
        if self.isWalk == True and self.left==False:    self.win.blit(self.run_right[self.walkcount//5], (self.x,self.y))
        elif self.left==True:    self.win.blit(self.run_left[self.walkcount//5], (self.x,self.y))
        else:   self.win.blit(self.idle[self.idle_count//5], (self.x, self.y))
        self.check_collision()
        pygame.display.update()
    
    def user_movement_input(self):
        keys=pygame.key.get_pressed()
        self.walkcout=0
        self.idle_count=0
        if self.end == False:
            if keys[pygame.K_LEFT] and self.x > self.velocity:                                                 self.x-=self.velocity; self.walkcount+=1; self.isWalk=True; self.idle_count=0; self.left=True; self.timer_start=True
            elif keys[pygame.K_RIGHT] and self.x < self.screen_width-self.width-self.velocity:                 self.x+=self.velocity; self.walkcount+=1; self.isWalk=True; self.idle_count=0; self.left=False; self.timer_start=True
            elif keys[pygame.K_UP] and self.y > self.velocity:                                                 self.y-=self.velocity; self.walkcount=0;  self.isWalk=False; self.idle_count+=1; self.timer_start=True
            elif keys[pygame.K_DOWN] and self.y < self.screen_height*0.8-0.75*self.height:                     self.y+=self.velocity; self.walkcount=0;  self.isWalk=False; self.idle_count+=1; self.timer_start=True
            else:                                                                                              self.walkcount=0; self.isWalk=False; self.idle_count+=1
        self.character_drawing()

    def character_movements_animation(self):
        self.idle=[pygame.image.load('./sprites/idle_0.png'),pygame.image.load('./sprites/idle_1.png'),pygame.image.load('./sprites/idle_2.png'),pygame.image.load('./sprites/idle_3.png')]
        self.run_right=[pygame.image.load('./sprites/run_0.png'), pygame.image.load('./sprites/run_1.png'), pygame.image.load('./sprites/run_2.png'),pygame.image.load('./sprites/run_3.png'),pygame.image.load('./sprites/run_4.png'),pygame.image.load('./sprites/run_5.png')]
        self.run_left=[]
        for i in range(6):
            self.run_left.append(pygame.transform.flip(self.run_right[i], True, False))
# ---------------------------------------------Python Game environment------------------------------------------------
# ---------------------------------------------Driver Function------------------------------------------------

def main(num):
    global n
    n = num
    global score_list
    if num == 1:    score_list=[None,None]
    ob=python_game_characters(num)

if __name__ == '__main__':
    main(1)