
class Shot:
    def __init__(self, position_x, position_y) -> None:
        self.position_x = position_x
        self.position_y = position_y


class ShotPlayer(Shot):
    instances = []
    def __init__(self, position_x, position_y) -> None:
        super().__init__(position_x, position_y)
        self.select_img = "./images/bala_player.png"
        self.instances.append(self)

    def move_up(self):
        self.position_y -= 1

class ShotEnemy(Shot):
    def __init__(self, position_x, position_y) -> None:
        super().__init__(position_x, position_y)
        self.select_img = "./images/bala_enemy.png"

    def move_up(self):
        self.position_y -= 1