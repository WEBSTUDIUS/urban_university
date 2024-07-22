from Module_5.m5_hard.user import User
from Module_5.m5_hard.video import Video


class UrTube(User, Video):

    def __init__(self, users, videos, current_user, nickname, password, age):
        super().__init__(nickname, password, age)
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        # password compares with HASH
        pass

    def register(self, nickname, password, age):
        pass

    def log_out(self, nickname):
        pass

    def add(self, Video):
        pass

    def get_videos(self, search_word):
        pass

    def watch_video(self, movie_name):
        pass
