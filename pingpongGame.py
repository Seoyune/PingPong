# 고칠 것들

import tkinter as tk
import random as rd

class Table:    
    def __init__(self, window, colour = 'skyblue',
                  width = 600, height = 400):
        
        self.width = width
        self.height = height
        self.colour = colour
        self.canvas = tk.Canvas(window, bg=self.colour, height = self.height, width = self.width)
        self.canvas.pack()
        font = ("monaco", 72)
        self.scoreboard = self.canvas.create_text(300, 65, font = font, fill = "black")
        self.canvas.create_line(self.width/2,0,self.width/2,self.height, 
                                 width = 2, fill = "black", dash = (15,23))
        self.canvas.create_line(0,self.height/2, self.width, self.height/2,
                                width = 2, fill = 'white')
        
    def draw_rectangle(self, rectangle):
        x1 = rectangle.x_posn
        x2 = rectangle.x_posn+rectangle.width
        y1 = rectangle.y_posn
        y2 = rectangle.y_posn+rectangle.height
        c = rectangle.colour
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill = c )
    
    def draw_oval(self, oval):
        x1 = Ball.Get_x_posn(oval)
        x2 = Ball.Get_x_posn(oval)+oval.width
        y1 = Ball.Get_y_posn(oval)
        y2 = Ball.Get_y_posn(oval)+oval.height
        c = oval.colour
        return self.canvas.create_oval(x1, y1, x2, y2, fill = c ) 
    
    def move_item(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)
    
    def draw_score(self, left, right):
        scores = str(right) + "   " + str(left)
        self.canvas.itemconfigure(self.scoreboard, text = scores)

class Ball:
    def __init__(self, table, width=24, height=24, colour = 'orange',
                 myx_speed = 10, myy_speed=0, myx_start = 288, myy_start = 188) :
        self.width = width
        self.height = height
        self.__x_posn = myx_start
        self.__y_posn = myy_start
        self.colour = colour
        
        self.x_start = myx_start
        self.y_start = myy_start
        self.x_speed = myx_speed
        self.y_speed = myy_speed
        self.table = table
        self.circle = self.table.draw_oval(self)

    def Get_x_posn(self):
        return self.__x_posn

    def Get_y_posn(self):
        return self.__y_posn

    def start_position(self):
        self.__x_posn = self.x_start
        self.__y_posn = self.y_start
        
    def start_ball(self, x_speed, y_speed):
        self.x_speed = -x_speed if rd.randint(0, 1) else x_speed
        self.y_speed = -y_speed if rd.randint(0, 1) else y_speed
        self.start_position()
        
    def move_next(self):
        self.__x_posn = self.__x_posn + self.x_speed
        self.__y_posn = self.__y_posn + self.y_speed
        #left
        if(self.__x_posn<=3):
            
            #벽에 튕길 떄 방향만 바꾸는 경우
            self.__x_posn=3
            self.x_speed = -self.x_speed
        #right    
        if(self.__x_posn >= (self.table.width - (self.width-3))):
            self.__x_posn = (self.table.width - (self.width-3))
            self.x_speed = -self.x_speed
        #top
        if(self.__y_posn<=3):
            self.__y_posn=3
            self.y_speed = -self.y_speed
        #bottom
        if(self.__y_posn >= (self.table.height - (self.height-3))):
            self.__y_posn = (self.table.height - (self.height-3))
            self.y_speed = -self.y_speed            
        #move_ball
        x1 = self.__x_posn
        x2 = self.__x_posn + self.width
        y1 = self.__y_posn
        y2 = self.__y_posn + self.height
        self.table.move_item(self.circle, x1, y1, x2, y2)
        
    def stop_ball(self):
        self.x_speed = 0
        self.y_speed = 0        

class Bat:
    def __init__(self, table, width = 18, height = 100, x_posn = 50,
                 y_posn = 150, colour = "red", x_speed = 3, y_speed = 20):
        self.width = width
        self.height = height
        self.x_posn = x_posn
        self.y_posn = y_posn
        self.colour = colour
        
        self.x_start=x_posn
        self.y_start = y_posn
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.table = table   
        self.rectangle = self.table.draw_rectangle(self)
        
    def move_up(self, master):
        self.y_posn = self.y_posn - self.y_speed
        if (self.y_posn <=0):
            self.y_posn = 0 
        x1 = self.x_posn
        x2 = self.x_posn + self.width
        y1 = self.y_posn
        y2 = self.y_posn + self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)
        
    def move_down(self, master):
        self.y_posn = self.y_posn + self.y_speed
        far_bottom = self.table.height - self.height
        if (self.y_posn >= far_bottom):
            self.y_posn = far_bottom
        x1 = self.x_posn
        x2 = self.x_posn + self.width
        y1 = self.y_posn
        y2 = self.y_posn + self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)
        
    def move_left(self, master):
        self.x_posn = self.x_posn - self.x_speed
        if (self.x_posn <=2):
            self.x_posn = 2
        x1 = self.x_posn
        x2 = self.x_posn + self.width
        y1 = self.y_posn
        y2 = self.y_posn + self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)
        
    def move_right(self, master):
        self.x_posn = self.x_posn + self.x_speed
        far_right = self.table.width - self.width 
        if (self.x_posn >= far_right):
            self.x_posn = far_right
        x1 = self.x_posn
        x2 = self.x_posn + self.width
        y1 = self.y_posn
        y2 = self.y_posn + self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)
        
    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start
        
    def detect_collision(self, ball):
        collision_direction = ""
        collision = False
        feel = 5
        
        top = self.y_posn
        bottom = self.y_posn + self.height
        left = self.x_posn
        right = self.x_posn + self.width
        v_centre = top + (self.height / 2) 
        
        top_b = Ball.Get_y_posn(ball)
        bottom_b = Ball.Get_y_posn(ball) + ball.height
        left_b = Ball.Get_x_posn(ball)
        right_b = Ball.Get_x_posn(ball) + ball.width
        r = (right_b - left_b) / 2
        v_centre_b = top_b + r
        
        if((bottom_b > top) and (top_b < bottom) and (right_b > left) and (left_b < right)):
            collision = True
        
        if(collision):
            
            if((top_b > top - r) and (bottom_b < bottom + r) and
               (right_b > right) and (left_b <= right)):
                collision_direction = "E"
                ball.x_speed = abs(ball.x_speed)
                
            elif((left_b > left - r) and (right_b < right + r) and
                 (bottom_b > bottom) and (top_b <= bottom)):
                collision_direction = "S"
                ball.y_speed = abs(ball.y_speed)
                
            elif((left_b > left - r) and (right_b < right + r) and
                 (top_b < top) and (bottom_b >= top)):
                collision_direction = "N"
                ball.y_speed = -abs(ball.y_speed)
            
            elif((top_b > top - r) and (bottom_b < bottom + r) and
               (left_b < left) and (right_b >= left)):
                collision_direction = "W"
                ball.x_speed = -abs(ball.x_speed)
                
            else:
                collision_direction = "None"
            
            # Sweet Spot 적용하는 코드
            
            if((collision_direction == "W" or collision_direction == "E")):
                adjustment = (-(v_centre - v_centre_b)) / (self.height / 2)
                ball.y_speed = feel * adjustment

            return (collision, collision_direction) 
        
class LeftBat(Bat):
    def move_left(self, master):
        return super().move_left(master)

    def move_right(self, master):
        self.x_posn = self.x_posn + self.x_speed
        far_right = self.table.width/2 - self.width - my_ball.width
        if (self.x_posn >= far_right):
            self.x_posn = far_right
        x1 = self.x_posn
        x2 = self.x_posn + self.width
        y1 = self.y_posn
        y2 = self.y_posn + self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2) 

class RightBat(Bat):
    def move_left(self, master):
        self.x_posn = self.x_posn - self.x_speed
        far_left = self.table.width/2 + my_ball.width
        if (self.x_posn <= far_left):
            self.x_posn = far_left
        x1 = self.x_posn
        x2 = self.x_posn + self.width
        y1 = self.y_posn
        y2 = self.y_posn + self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2) 

    def move_right(self, master):
        return super().move_right(master)              

# 시작하기 버튼의 커맨드, 메뉴 버튼 적용하여 객체 생성 및 키보드와 바인딩, 화면 설정        
def start_game():
    global first_serve
    first_serve = False
    global score_left
    score_left = 0
    global score_right
    score_right = 0

    global my_ball
    global my_table
    global bat_L
    global bat_R

    global x_velocity 
    global max_score
    global ball_color
    global table_color
    global bat_L_color
    global bat_R_color
        
    x_velocity = flag2 
    max_score = flag1 
    ball_color = flag3
    table_color = flag6
    bat_L_color = flag4
    bat_R_color = flag5

    my_table = Table(window, colour=table_color)    
    my_ball = Ball(table = my_table, colour=ball_color,myx_speed = x_velocity) #  생략
    bat_L = LeftBat(table=my_table, x_posn = 20, colour=bat_L_color)
    bat_R = RightBat(table=my_table, x_posn=575, colour=bat_R_color)    

    window.bind("<space>", continue_game)   

    window.bind("w", bat_L.move_up)
    window.bind("s", bat_L.move_down)
    window.bind("a", bat_L.move_left)
    window.bind("d", bat_L.move_right)

    window.bind("o", bat_R.move_up)
    window.bind("l", bat_R.move_down)
    window.bind(";", bat_R.move_right)
    window.bind("k", bat_R.move_left)     
    
    Start.place_forget()
    Exit.configure(height=2,width=6,bg='red3',fg='black',activeforeground='',activebackground='red4')
    Exit.place(x=540,y=470)
    label.place_forget()
    label2.place(x=0,y=0)
    menubutton.place_forget()
    menubutton2.place_forget()
    menubutton3.place_forget()
    menubutton4.place_forget()
    menubutton5.place_forget()
    menubutton6.place_forget() 
    
    game_flow()
    window.mainloop()        
# SPACE 바인딩된 커맨드, 승부 결정되는 경우는 못씀, 공 속도 -, 공, 채 위치 초기화    
def continue_game(master): 
    global score_left
    global score_right 
    if (score_left == "Win" or score_left == "Lose"):
        return
    if my_ball.x_speed == 0:
        my_ball.start_ball(x_speed = x_velocity, y_speed = 0)    
    my_table.draw_score(score_left, score_right)

# 승패 결정난 후에 점수 초기화 하고 다시 시작
def restart_game(): 
    global score_right
    global score_left
    if (score_left == "Win" or score_left == "Lose"):
        score_left = 0
        score_right = 0
    my_table.draw_score(score_left, score_right)
    ReStart.place_forget()

# 시간에 따른 객체 이동 및 충돌 표현
def game_flow():
    global first_serve
    global score_left
    global score_right
    global my_ball 
    global max_score 
    # 첫 서브
    if(first_serve == False):
        my_ball.stop_ball()
        first_serve = True 
    # 공 - 라켓 충돌
    bat_L.detect_collision(my_ball)   
    bat_R.detect_collision(my_ball)
    # 공 - 왼쪽벽 충돌 
    if( Ball.Get_x_posn(my_ball) <= 3):
        my_ball.stop_ball()
        my_ball.start_position()
        bat_L.start_position()
        bat_R.start_position()
        my_table.move_item(bat_L.rectangle, 17, 150, 35, 250)
        my_table.move_item(bat_R.rectangle, 575, 150, 593, 250)
        #득점하면 표기
        score_left = score_left + 1
        if(score_left >= max_score):
            score_left = "Win"
            score_right = "Lose"
            ReStart.place(x=450,y=470)
        first_serve = True
        my_table.draw_score(score_left, score_right)
    #공 - 오른쪽벽 충돌     
    if(Ball.Get_x_posn(my_ball) + my_ball.width >= my_table.width - 2):
        my_ball.stop_ball()
        my_ball.start_position()
        bat_L.start_position()
        bat_R.start_position()
        my_table.move_item(bat_L.rectangle, 17, 150, 35, 250)
        my_table.move_item(bat_R.rectangle, 575, 150, 593, 250)
        score_right = score_right + 1
        if(score_right >= max_score):
            score_right = "Win"
            score_left = "Lose"
            ReStart.place(x=450,y=470)
        first_serve = True
        my_table.draw_score(score_left, score_right)
        # 반복 실행하고 50ms마다 출력
    my_ball.move_next()
    window.after(50, game_flow)

def SetMax1():
    global flag1
    flag1 = 5
def SetMax2():
    global flag1
    flag1 = 10
def SetMax3():
    global flag1
    flag1 = 15

def SetSlow():
    global flag2
    flag2 = 7
def SetFast():
    global flag2
    flag2 = 10
def SetFFast():
    global flag2
    flag2 = 13

def ball_red():
    global flag3
    flag3 = 'red4'
def ball_orange():
    global flag3
    flag3 = 'chocolate2'
def ball_white():
    global flag3
    flag3 = 'ghost white'

def left_red():
    global flag4
    flag4 = 'red'
def left_black():
    global flag4
    flag4 = 'gray25'
def left_brown():
    global flag4
    flag4 = 'saddle brown'

def right_red():
    global flag5
    flag5 = 'red'
def right_black():
    global flag5
    flag5 = 'gray25'
def right_brown():
    global flag5
    flag5 = 'saddle brown'

def table_blue():
    global flag6
    flag6 = 'blue4'
def table_sky():
    global flag6
    flag6 = 'deep sky blue'
def table_green():
    global flag6
    flag6 = 'dark green'    

window = tk.Tk()
window.geometry("640x540+100+100")
window.resizable(False, False)
window.title("Seoyune's Ping Pong")

image1=tk.PhotoImage(file="bg3.png")

label=tk.Label(window, image=image1)
label.place(x=0,y=0)

image2=tk.PhotoImage(file="bg5.png")
label2 = tk.Label(window,image=image2)
label.place(x=0,y=0)
font1 = ("monaco",36)
title = tk.Label(window, text=" Seoyune's Ping Pong ",anchor="center",
                font=font1, relief='groove',bg='skyblue',bd=2)
title.pack(side="top")

SetMax2()
SetFast()
ball_orange()
left_red()
right_black()
table_sky()
RadV1 = tk.IntVar()
RadV2 = tk.IntVar()
RadV3 = tk.IntVar()
RadV4 = tk.IntVar()
RadV5 = tk.IntVar()
RadV6 = tk.IntVar()
menubutton=tk.Menubutton(text="몇점만점", relief="raised", direction="below",background='skyblue',
                            activebackground='skyblue2', width=18,height=3)
menu=tk.Menu(menubutton, tearoff=0)
menubutton.place(x=50,y=100)
menu.add_radiobutton(label="5점", variable=RadV1, activebackground='NavajoWhite2' ,activeforeground='black', command=SetMax1)
menu.add_radiobutton(label="10점", variable=RadV1,activebackground='NavajoWhite3', command=SetMax2)
menu.add_radiobutton(label="15점", variable=RadV1,activebackground='NavajoWhite4', command=SetMax3)
menubutton["menu"]=menu

menubutton2=tk.Menubutton(text="공의 빠르기", relief="raised", direction="below",background='skyblue',
                            activebackground='skyblue2',width=18,height=3)
menubutton2.place(x=240,y=100)
menu2=tk.Menu(menubutton2, tearoff=0)
menu2.add_radiobutton(label="느림", variable=RadV2,activebackground='NavajoWhite2' ,activeforeground='black',command=SetSlow)
menu2.add_radiobutton(label="보통", variable=RadV2,activebackground='NavajoWhite3' ,command=SetFast)
menu2.add_radiobutton(label="빠름", variable=RadV2,activebackground='NavajoWhite4' ,command=SetFFast)
menubutton2["menu"]=menu2

menubutton3 = tk.Menubutton(text="공의 색깔", relief="raised", direction="below",background='skyblue',
                            activebackground='skyblue2',width=18,height=3)
menubutton3.place(x=430,y=100)
menu3=tk.Menu(menubutton3,tearoff=0)
menu3.add_radiobutton(label="빨간색",variable=RadV3, activebackground='red4' ,command=ball_red)
menu3.add_radiobutton(label="주황색",variable=RadV3, activebackground='chocolate2' ,command=ball_orange)
menu3.add_radiobutton(label="흰색",variable=RadV3, activebackground='snow2' ,activeforeground='black', command=ball_white)
menubutton3["menu"]=menu3

menubutton4 = tk.Menubutton(text="왼쪽 채 색깔", relief="raised", direction="below",background='skyblue',
                            activebackground='skyblue2',width=18,height=3)
menubutton4.place(x=50,y=200)
menu4=tk.Menu(menubutton4,tearoff=0)
menu4.add_radiobutton(label="빨간색",variable=RadV4, activebackground='red' ,command=left_red)
menu4.add_radiobutton(label="검은색",variable=RadV4, activebackground='gray25' ,command=left_black)
menu4.add_radiobutton(label="갈색",variable=RadV4,activebackground='saddle brown' ,command=left_brown)
menubutton4["menu"]=menu4

menubutton5 = tk.Menubutton(text="오른쪽 채 색깔", relief="raised", direction="below",background='skyblue',
                            activebackground='skyblue2',width=18,height=3)
menubutton5.place(x=240,y=200)
menu5=tk.Menu(menubutton5,tearoff=0)
menu5.add_radiobutton(label="빨간색",variable=RadV5, activebackground='red' ,command=right_red)
menu5.add_radiobutton(label="검은색",variable=RadV5, activebackground='gray25' ,command=right_black)
menu5.add_radiobutton(label="갈색",variable=RadV5,activebackground='saddle brown' ,command=right_brown)
menubutton5["menu"]=menu5

menubutton6 = tk.Menubutton(text="탁구대 색깔", relief="raised", direction="below",background='skyblue',
                            activebackground='skyblue2',width=18,height=3)
menubutton6.place(x=430,y=200)
menu6=tk.Menu(menubutton6,tearoff=0)
menu6.add_radiobutton(label="파란색",variable=RadV6, activebackground='blue4' ,command=table_blue)
menu6.add_radiobutton(label="하늘색",variable=RadV6, activebackground='deep sky blue' ,command=table_sky)
menu6.add_radiobutton(label="초록색",variable=RadV6, activebackground='dark green' ,command=table_green)
menubutton6["menu"]=menu6

Start = tk.Button(window, text ="게임 시작", bg = "red", font=20, foreground='white', command=start_game
                  ,width=12, height=4, activebackground='red4')
Start.place(x=128,y=380)
Exit = tk.Button(window, text="나가기",bg="gray20", font=20, foreground='white', command=window.destroy
                 ,width=12,height=4,activebackground='gray40')
Exit.place(x=380,y=380)
ReStart = tk.Button(window, text="다시!", bg="green2",font=20, command=restart_game
                    ,activebackground='green4',width=6,height=2)
window.mainloop()