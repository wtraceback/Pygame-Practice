class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, sets):
        """初始化统计信息"""
        self.sets = sets
        self.reset_stats()

        # 游戏启动时处于活动状态
        self.game_active = True
        
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.life_left = self.sets.life_limit
        self.level = 1