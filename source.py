from tkinter import Tk, Label, Button, Frame


COLOR = dict(
    yellow_light='#C5BE90',
    yellow_normal='#938D65',
    blue_light='#CCC7EC',
    blue_normal='#6C75A9',
    dark_light='#202020',
    dark='#181818',
    red='#BB0000'
)


TEXT = dict(
    head_start="Привет :)",
    sub_start="Предлагаю тебе сыграть в простую игру!",
    capt_start="Правила игры:",
    center_start=("В стопке 20 спичек. Можно брать по 1, 2 или 3 спички.\n"
                  "Выигрывает тот, кто забирает последние."),

    head_game="Твой ход",
    capt_game="Осталось:",
    bot_head_game="Ход компьютера",

    head_game_over="Ты проиграл :(",
    sub_game_over="Не отчаивайся, однажды ты раскроешь секрет!"
)

game_score = 20


class Position:
    groups = {
        #    columns   |   rows
        'A': [[0],         [0, 1]],
        'B': [[0, 1, 3],   [0]],
        'C': [[0, 1, 2],   [0, 1]],
        'W': [[0],         [0, 1, 2]]
    }

    net = {
        #     row | column | sticky | padx | pady
        'A1': [0,   0,       'S',       0,    0],
        'A2': [1,   0,       'N',       0,    0],
        'B1': [0,   0,       'NE',     20,    0],
        'B2': [0,   0,       'E',      20,    0],
        'B3': [0,   1,       'NW',      0,    0],
        'B4': [0,   2,       'NW',      0,    0],
        'B5': [0,   3,       'NW',      0,    0],
        'C1': [1,   0,       'S',      10,   10],
        'C2': [1,   1,       'S',      10,   10],
        'C3': [1,   2,       'S',      10,   10],
        'C4': [0,   1,       'S',       0,    0],
        'C5': [1,   1,       'N',       0,   10],
        'W0': [0,   0,       'S',      10,    0],
        'W1': [1,   0,       'S',      10,    0],
        'W2': [2,   0,       'S',      10,    0]
    }

    def __init__(self, group=None):
        self.group = group
        self.cell = None

        if self.group is not None:
            self.columnconfigure(
                Position.groups[self.group][0], weight=1, minsize=0
            )

            self.rowconfigure(
                Position.groups[self.group][1], weight=1, minsize=0
            )

    def mount(self, cell):
        self.cell = cell
        self.grid(row=Position.net[self.cell][0],
                  column=Position.net[self.cell][1],
                  sticky=Position.net[self.cell][2],
                  padx=Position.net[self.cell][3],
                  pady=Position.net[self.cell][4])


class DefaultWindow(Tk, Position):
    def __init__(self):
        Tk.__init__(self)
        Position.__init__(self, group='W')

        self.title('Игра "Спички"')
        self.resizable(True, True)
        self.configure(bg=COLOR['dark'])

        self.width = int(self.winfo_screenwidth() * 0.5)
        self.height = int(self.winfo_screenheight() * 0.5)

        self.x = self.width - (self.width // 2)
        self.y = self.height - (self.height // 2)

        self.geometry('{}x{}+{}+{}'.format(self.width,
                                           self.height,
                                           self.x,
                                           self.y))

    def start(self):
        self.mainloop()

    def stop(self):
        self.quit()


class DefaultFrame(Frame, Position):
    def __init__(self, group):
        self.position = None
        self.group = group

        Frame.__init__(self)
        Position.__init__(self, self.group)

        self.configure(borderwidth=10, bg=COLOR['dark'])

    def custom(self, position=None):
        self.position = position

        if self.position is not None:
            self.mount(self.position)


class LabelWidget(Label, Position):
    def __init__(self, master):
        self.master = master
        self.style = None
        self.position = None
        self.content = None

        Label.__init__(self, self.master)
        Position.__init__(self)

        self.configure(
            font='Arial 12',
            justify='left',
            bg=COLOR['dark'],
            fg=COLOR['blue_normal']
        )

    def custom(self, style=None, position=None, content=None):
        self.style = style
        self.position = position
        self.content = content

        if self.style == 'H1':
            self.configure(font=('Arial Black', 50),
                           fg=COLOR['blue_light'],
                           justify='center')

        if self.style == 'H2':
            self.configure(font=('Arial Black', 26),
                           fg=COLOR['blue_light'],
                           justify='center',
                           pady=46,
                           padx=12)

        if self.style == 'H3':
            self.configure(font='Arial 12',
                           fg=COLOR['blue_light'],
                           justify='center')

        if self.style == 'Match':
            self.configure(font=('Arial Bold', 28),
                           fg=COLOR['yellow_normal'])

        if self.style == 'Take Match':
            self.configure(font=('Arial Bold', 28),
                           fg=COLOR['red'])

        if self.style == 'Empty Place':
            self.configure(font=('Arial Bold', 28),
                           fg=COLOR['dark_light'])

        if self.content is not None:
            self.configure(text=self.content)

        if self.position is not None:
            self.mount(self.position)


class ButtonWidget(Button, Position):
    def __init__(self, master):
        self.master = master
        self.style = None
        self.position = None
        self.content = None
        self.command = None

        Button.__init__(self, self.master)
        Position.__init__(self)

        self.configure(
            activebackground=COLOR['yellow_normal'],
            bg=COLOR['yellow_light'],
            fg=COLOR['dark'],
            font=('Arial Black', 12),
            justify='center',
            width=20,
            height=2
        )

    def custom(self, style=None, position=None, content=None, command=None):
        self.style = style
        self.position = position
        self.content = content
        self.command = command

        if self.command is not None:
            self.configure(command=self.command)

        if self.content is not None:
            self.configure(text=self.content)

        if self.position is not None:
            self.mount(self.position)


window = DefaultWindow()

frame_top = DefaultFrame(group='A')
frame_center = DefaultFrame(group='B')
frame_bottom = DefaultFrame(group='C')

lbl_head = LabelWidget(master=frame_top)
lbl_sub = LabelWidget(master=frame_top)
lbl_capt = LabelWidget(master=frame_center)
lbl_center = LabelWidget(master=frame_center)
lbl_take_match = LabelWidget(master=frame_center)
lbl_test = LabelWidget(master=frame_center)

btn_start = ButtonWidget(master=frame_bottom)
btn_exit = ButtonWidget(master=frame_bottom)
btn_1 = ButtonWidget(master=frame_bottom)
btn_2 = ButtonWidget(master=frame_bottom)
btn_3 = ButtonWidget(master=frame_bottom)


def score_output(score, empty=False):
    str_score = str()
    for i in range(score // 5):
        for j in range(5):
            str_score += " i"
        str_score += " "
    for i in range(score % 5):
        str_score += " i"
    if empty is True:
        return str_score[(game_score * 2) + (game_score // 5)::]
    else:
        return str_score


def take_match(n):
    rest = game_score % 5
    if n > rest:
        str_match = str()
        for i in range(n - rest):
            str_match += " i"
        str_match += " "
        str_match += " i" * rest
        return str_match
    else:
        return " i" * n


def computer_step(n):
    lbl_take_match.grid_remove()

    lbl_test.custom(content=score_output(20, empty=True),
                    style='Empty Place',
                    position='B5')

    lbl_head.custom(content=TEXT['bot_head_game'], style='H2')
    window.after(1500, lambda: action_match(4 - n, step='human'))


def action_match(n, step):
    global game_score
    if game_score != 0:
        lbl_take_match.custom(content=take_match(n),
                              style='Take Match',
                              position='B4')

        game_score -= n
        lbl_center.custom(content=score_output(game_score))
        btn_1.grid_remove()
        btn_2.grid_remove()
        btn_3.grid_remove()

    if step == 'bot':
        window.after(500, lambda: computer_step(n))

    if step == 'human':
        window.after(500, player_step)


def player_step():
    global game_score
    if game_score == 0:
        game_score = 20
        lbl_head.custom(content=TEXT['head_game_over'], style='H2')
        lbl_sub.custom(content=TEXT['sub_game_over'], position='A2')
        btn_start.custom(content='РЕВАНШ', position='C4', command=player_step)
        btn_exit.custom(content='ВЫЙТИ', position='C5', command=window.stop)
    else:
        lbl_take_match.grid_remove()

        lbl_test.custom(content=score_output(20, empty=True),
                        style='Empty Place',
                        position='B5')

        lbl_head.custom(content=TEXT['head_game'], style='H2')
        lbl_capt.custom(content=TEXT['capt_game'], position='B2')
        lbl_center.custom(content=score_output(game_score), style='Match')

        lbl_sub.grid_remove()
        btn_start.grid_remove()
        btn_exit.grid_remove()

        btn_1.custom(content='1',
                     position='C1',
                     command=lambda: action_match(1, step='bot'))

        btn_2.custom(content='2',
                     position='C2',
                     command=lambda: action_match(2, step='bot'))

        btn_3.custom(content='3',
                     position='C3',
                     command=lambda: action_match(3, step='bot'))


def main():
    lbl_head.custom(style='H1', content=TEXT['head_start'], position='A1')
    lbl_sub.custom(style='H3', content=TEXT['sub_start'], position='A2')
    lbl_capt.custom(style='H3', content=TEXT['capt_start'], position='B1')
    lbl_center.custom(content=TEXT['center_start'], position='B3')

    btn_start.custom(content='ПОЕХАЛИ', position='C4', command=player_step)
    btn_exit.custom(content='ВЫЙТИ', position='C5', command=window.stop)

    frame_top.custom(position='W0')
    frame_center.custom(position='W1')
    frame_bottom.custom(position='W2')

    window.start()


main()
