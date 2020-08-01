import json


class GameStats():
    """跟踪每一局游戏的统计信息"""
    def __init__(self, sets):
        """初始化统计信息"""
        self.sets = sets
        self.reset_stats()

        # 判断游戏的活动状态
        self.game_active = False

        # 最高分
        self.high_score = 0
        # json 文件中的历史最高分
        self.history_high_score = 0

        # 初始化最高分
        self.get_stored_high_score()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.fighter_left = self.sets.fighter_max_num
        self.score = 0
        self.level = 1

    def get_stored_high_score(self):
        """从 json 文件加载 历史最高分"""
        try:
            # Python 在当前执行的文件所在的目录中查找指定的文件
            filename = 'history_high_score.json'
            with open(filename) as file_obj:
                data = json.load(file_obj)
        except:
            # 如果读取数据失败(文件不存在或格式错误)，则使用默认值
            pass
        else:
            # 防止获取 history_high_score 属性失败
            try:
                # 如果为 0 或者是文件读取错误，则使用默认值
                if data['history_high_score'] > 0:
                    self.high_score = data['history_high_score']
                    self.history_high_score = data['history_high_score']
            except:
                # 文件数据格式没有 history_high_score 属性
                pass