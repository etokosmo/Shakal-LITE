from random import sample
from dataclasses import dataclass


@dataclass
class Player:
    name: int  # [1-4]
    position_i: int
    position_j: int
    gold: int = 0  # количество золота
    pass_count: int = 0  # пропуск хода: 0-нет 1-да
    nickname: str = ""  # никнейм - заполняется с фронта


class WalkerGame:
    list_of_value = ['empty', 'trap', 'move', 'gold']  # значения ячеек

    def __init__(self, count_of_players):
        self.game_size = 5  # размер поля
        self.count_of_players = count_of_players  # количество игроков - заполняется с фронта
        self.player_1 = Player(name=1, position_i=0, position_j=0)  # распределение игроков по углам поля
        self.player_2 = Player(name=2, position_i=self.game_size - 1,
                               position_j=self.game_size - 1)  # распределение игроков по углам поля
        self.player_3 = Player(name=3, position_i=0,
                               position_j=self.game_size - 1)  # распределение игроков по углам поля
        self.player_4 = Player(name=4, position_i=self.game_size - 1,
                               position_j=0)  # распределение игроков по углам поля
        self.counter = 1  # счетчик ходов, используется для перехода хода
        self.game_field = []  # поле
        self.player_turn = self.player_1  # игрок, чья очередь ходить. Изначально 1-ый игрок
        self.message = ""  # сообщение об произошедшем событии
        self.message_container = []  # список из всех сообщений
        if count_of_players == 1:  # Заолняем список из игроков для фронта <section id='gold_players'>
            self.players_container = [self.player_1]
        elif count_of_players == 2:
            self.players_container = [self.player_1, self.player_2]
        elif count_of_players == 3:
            self.players_container = [self.player_1, self.player_2, self.player_3]
        elif count_of_players == 4:
            self.players_container = [self.player_1, self.player_2, self.player_3, self.player_4]

    def start(self):
        """Создает поле размером game_size*game_size, заполняет клетки значениями и запуск self.get_can_player_position для первого игрока"""
        game_field_list = sample(self.list_of_value,
                                 counts=[13 - self.count_of_players - (2 * self.count_of_players + 1) + 1, 7, 5,
                                         2 * self.count_of_players + 1],
                                 k=self.game_size ** 2 - self.count_of_players)  # полный набор значений ячеек
        self.game_field = [[[0, "disabled", 0, 0] for _ in range(self.game_size)] for _ in range(self.game_size)]
        """заполняем каждую ячейку 4 значениями:
        1 - есть ли игрок в клетке и какой [0,1,2,3,4]
        2 - возможность походить ["disabled","can_move"] -> нет/да -> для css
        3 - открыта или закрыта ячейка [0,1]
        4 - значение ячейки ['start','empty','trap','move','gold']
        """
        for i in range(self.game_size):  # переопределяем 1 и 4 ячейки
            for j in range(self.game_size):  # 1: есть ли игрок в клетке и какой 4: значение ячейки
                if not i and not j:
                    self.game_field[i][j][0] = self.player_1.name
                    self.game_field[i][j][3] = 'start'
                elif i == self.game_size - 1 and j == self.game_size - 1 and self.count_of_players >= 2:
                    self.game_field[i][j][0] = self.player_2.name
                    self.game_field[i][j][3] = 'start'
                elif not i and j == self.game_size - 1 and self.count_of_players >= 3:
                    self.game_field[i][j][0] = self.player_3.name
                    self.game_field[i][j][3] = 'start'
                elif i == self.game_size - 1 and not j and self.count_of_players == 4:
                    self.game_field[i][j][0] = self.player_4.name
                    self.game_field[i][j][3] = 'start'
                else:
                    self.game_field[i][j][3] = game_field_list.pop()
        self.get_can_player_position(self.player_turn)  # Запускаем куда можно идти для первого игрока

    def turn_to_play(self):
        """Переход хода от игрока к другому игроку"""
        count_of_players = self.count_of_players
        for players in [self.player_1, self.player_2, self.player_3, self.player_4]:
            if players.name == self.counter % count_of_players + 1:
                if players.pass_count == 1:
                    self.counter += 1
                    players.pass_count = 0
                    return self.turn_to_play()
                else:
                    self.counter += 1
                    return players

    def get_can_player_position(self, player):
        """Возвращает поле с клетками на которые можно перейти. Принимает игрока, который должен сделть ход"""
        for i in range(self.game_size):
            for j in range(self.game_size):
                self.game_field[i][j][1] = "disabled"  # Проставляем всем клеткам значение disabled
        position_i = player.position_i
        position_j = player.position_j
        for mi in range(-1, 2):
            for mj in range(-1, 2):
                if 0 <= position_i + mi < self.game_size and 0 <= position_j + mj < self.game_size:
                    self.game_field[position_i + mi][position_j + mj][
                        1] = "can_move"  # Проставляем вокруг игровой клетки значение can_move
        self.game_field[position_i][position_j][1] = "disabled"  # Сама игровая клетка disabled
        return self.game_field

    def to_start_position(self, player):
        """Возвращает игрока на поле старт"""
        if player.name == 1:
            self.player_1.position_i = 0
            self.player_1.position_j = 0
            self.game_field[0][0][0] = 1
        elif player.name == 2:
            self.player_2.position_i = self.game_size - 1
            self.player_2.position_j = self.game_size - 1
            self.game_field[self.game_size - 1][self.game_size - 1][0] = 2
        elif player.name == 3:
            self.player_3.position_i = 0
            self.player_3.position_j = self.game_size - 1
            self.game_field[0][self.game_size - 1][0] = 3
        elif player.name == 4:
            self.player_4.position_i = self.game_size - 1
            self.player_4.position_j = 0
            self.game_field[self.game_size - 1][0][0] = 4

    def move(self, move_position_i, move_position_j):
        """Принимает координаты на которые будет ходить игрок и производит движение на эту клетку"""
        player = self.player_turn  # Обозначение игрока, который делает ход
        self.game_field[player.position_i][player.position_j][0] = 0 # Убираем игрока с его клетки
        if self.game_field[move_position_i][move_position_j][2] == 0:
            if self.game_field[move_position_i][move_position_j][3] == 'start':
                self.value_start(player)
            elif self.game_field[move_position_i][move_position_j][3] == 'gold':
                player.gold += 1
                self.value_gold(player)
            elif self.game_field[move_position_i][move_position_j][3] == 'empty':
                self.value_empty(player)
            elif self.game_field[move_position_i][move_position_j][3] == 'move':
                self.game_field[move_position_i][move_position_j][2] = 1
                self.game_field[move_position_i][move_position_j][0] = player.name
                player.position_i = move_position_i
                player.position_j = move_position_j
                self.get_can_player_position(self.player_turn)
                self.value_move(player)
                return None
            elif self.game_field[move_position_i][move_position_j][3] == 'trap':
                player.pass_count = 1
                self.value_trap(player)
            self.game_field[move_position_i][move_position_j][2] = 1
        else:
            if self.game_field[move_position_i][move_position_j][0]:
                self.to_start_position(self.who_is_it(self.game_field[move_position_i][move_position_j][0]))
                self.value_start(self.who_is_it(self.game_field[move_position_i][move_position_j][0]))
            if self.game_field[move_position_i][move_position_j][3] == 'move':
                self.game_field[move_position_i][move_position_j][0] = player.name
                player.position_i = move_position_i
                player.position_j = move_position_j
                self.get_can_player_position(self.player_turn)
                self.value_move(player)
                return None
            elif self.game_field[move_position_i][move_position_j][3] == 'trap':
                player.pass_count = 1
                self.value_trap(player)
        self.game_field[move_position_i][move_position_j][0] = player.name  # Игрок переходит на клетку
        player.position_i = move_position_i  # Игрок переходит на клетку
        player.position_j = move_position_j  # Игрок переходит на клетку
        self.player_turn = self.turn_to_play()  # Смена игрока
        self.get_can_player_position(self.player_turn)  # Показывет клетки на которые может перейти новый игрок

    def who_is_it(self, number):
        """Принимает номер игрока, возвращает самого игрока"""
        if number == 1:
            return self.player_1
        elif number == 2:
            return self.player_2
        elif number == 3:
            return self.player_3
        elif number == 4:
            return self.player_4

    def value_trap(self, player):
        """Месседж события и добавление его в контейнер"""
        self.message = f"Игрок {player.nickname} попал к людоеду. Он Пропускает один ход"
        self.message_container.insert(0, self.message)

    def value_empty(self, player):
        """Месседж события и добавление его в контейнер"""
        self.message = "Это пустая клетка. Ничего не произошло"
        self.message_container.insert(0, self.message)

    def value_start(self, player):
        """Месседж события и добавление его в контейнер"""
        self.message = f"Игрока {player.nickname} отбросило на клетку старт"
        self.message_container.insert(0, self.message)

    def value_gold(self, player):
        """Месседж события и добавление его в контейнер"""
        self.message = f"Игрок {player.nickname} получил +1 мешочек с золотом"
        self.message_container.insert(0, self.message)

    def value_move(self, player):
        """Месседж события и добавление его в контейнер"""
        self.message = f"Игрок {player.nickname} получил право на еще один ход"
        self.message_container.insert(0, self.message)
