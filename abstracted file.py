from abc import ABC, abstractmethod
class base(ABC):
    @abstractmethod
    def __init__(self):
        pass
class ad(ABC):
    @abstractmethod
    def __init__(self):pass

    def read_data_from_file(self, file_name):pass

    def signup(self):pass

    def read(self, total):pass

    def user_name(self, name, details):pass

    def password(self, current, details, k=2):pass

    def login(self, name):pass

    def add_theater(self):pass

    def write_dict_to_file(self, dictionary, filename):pass

    def read_dict_from_file(self, filename):pass

    def add_movie(self):pass

    def remove_movie(self):pass

    def update_movie_timing(self):pass

    def display_schedule(self):pass

class user1(ABC):
    @abstractmethod
    def __init__(self):pass

    def read_dict_from_file(self, filename):pass

