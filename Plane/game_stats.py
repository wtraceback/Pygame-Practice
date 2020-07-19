class GameStats():
    """跟踪每一局游戏的统计信息"""
    def __init__(self, sets):
        """初始化统计信息"""
        self.sets = sets
        self.reset_stats()

        # 判断游戏的活动状态
        self.game_active = False

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.fighter_left = self.sets.fighter_max_num
        self.score = 0