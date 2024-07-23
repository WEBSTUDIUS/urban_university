from user import User
from video import Video
from time import sleep


class UrTube:
    users = User.users
    videos = Video.videos
    current_user = None

    def log_in(self, nickname, password):
        if self.current_user and self.current_user != nickname:
            return (f'Sorry, {nickname}! {self.current_user.nickname} is already logged in to this session! '
                    f'Please log out before new log in')
        for user in self.users:
            if nickname == user.nickname:
                if hash(password) == user.password:
                    self.current_user = user
                    return f'Login successful, {nickname}!'
                return 'Password incorrect!'
        return f'Please, register, {nickname}'

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                return f'{nickname} is already registered. Log in'
        new_user = User(nickname, hash(password), age)
        User.users.append(new_user)
        self.current_user = new_user
        return f'User {nickname} successfully registered!'

    def log_out(self):
        print(f'Goodbye, {self.current_user.nickname}! See you later!')
        self.current_user = None

    def check_adult(self, adult_mode):
        if adult_mode and self.current_user.age < 18:
            return False
        return True

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                Video.videos.append(video)
                print(f'Video "{video.title}" was added.')
            else:
                print(f'VIdeo "{video.title}" is already exists in database.')

    def get_videos(self, search_word):
        result = []
        for movie in self.videos:
            if movie.title.lower().__contains__(search_word.lower()):
                result.append(movie.title)

        return result

    def watch_video(self, movie_name):
        if self.current_user is None:
            print('Please, log in to watch videos')
            return

        for movie in self.videos:
            if movie.title == movie_name:
                if not self.check_adult(movie.adult_mode):
                    print(f'Your age is less than 18. You cant watch videos, please go home and drink some milk.')
                    return
                print(f'Okay, lets play "{movie_name}"')
                for i in range(movie.time_now, movie.duration):
                    sleep(1)
                    print(i + 1, end=' ')
                print('==THE END==')
                return
        print(f'Video "{movie_name}" was not found in our database. You can add it')

        return


# CHECK
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
