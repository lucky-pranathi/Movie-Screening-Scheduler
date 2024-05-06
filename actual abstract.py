import json
from abstract_test import *
class A(base):
    def __init__(self):
        print('Enter 1 for Administrator login (Password is mandatory)\nEnter 2 for user login\nEnter 0 to exit')
        num=int(input())
        if num==1:
            schedule=admin()
        elif num==2:
            client=user()
        elif num==0:
            exit()
        else:
            print('Enter valid input')
            A().__init__()
class admin(ad):
    def __init__(self):
        self.theaters = {}
        a = int(input('Enter 1, for new Admin Sign-up\nEnter 2, if already a user for login\n'))
        if a == 1:
            self.signup()
        elif a == 2:
            name = input('Enter the username:')
            self.login(name)
        else:
            print('Enter valid input')
            self.__init__()

    def read_data_from_file(self, file_name):
        with open(file_name, 'r') as file:
            data = file.readlines()
        nested_list = []
        for line in data:
            line = line.strip()
            elements = line.split(',')
            nested_list.append(elements)
        return nested_list

    def signup(self):
        name = input('Enter the username:')
        pw = input('Enter the pin:')
        pw1 = input('Re-enter the pin:')
        if pw == pw1:
            tot=name+','+pw
            self.read(tot)
        else:
            print('Enter valid pin')
            self.__init__()

    def read(self, total):
        with open('word.txt', 'a+') as file:
            file.write(total)
        print('Account created successfully')
        A().__init__()

    def user_name(self,name,details):
        j = 0
        for i in range(len(details)):
            if name == details[i][0]:
                current = i
                j += 1
            else:
                pass
        if j == 0:
            print('Username not found')
            A().__init__()
        return current

    def password(self,current,details,k=2):
        password = input('Enter the pin:')
        for j in range(3, 0, -1):
            if password == details[current][1]:
                return password
            else:
                k -= 1
                print('Password incorrect, try again !')
                print('You have ', k+1, 'chances left.')
                password=input('Enter the pin:')
                if k == 0:
                    print('Password of username not found')
                    A().__init__()
    def login(self,name):
        file_name = "word.txt"
        details = self.read_data_from_file(file_name)
        current=self.user_name(name,details)
        password=self.password(current,details)
        def operation():
            n = int(input('\nEnter 1 for adding theater\nEnter 2 for adding movie\nEnter 3 for removing movie\nEnter 4 for updating movie timings\nEnter 5 for displaying\nEnter 0 for exit\n'))
            if n == 1:
                self.add_theater()
                operation()
            elif n == 2:
                self.add_movie()
                operation()
            elif n == 3:
                self.remove_movie()
                operation()
            elif n == 4:
                self.update_movie_timing()
                operation()
            elif n == 5:
                self.display_schedule()
                operation()
            elif n == 0:
                A().__init__()
            else:
                print('Enter valid input')
                operation()
        operation()
    def add_theater(self):
        filename = 'data.json'
        self.theaters = self.read_dict_from_file(filename)
        theater_id = input('Enter theater id')
        if theater_id in self.theaters.keys():
            print('Theater id already present')
            return
        else:
            theater_name = input('Enter theater name')
            self.theaters[theater_id] = {"name": theater_name, "schedule": []}
            print('Theater added successfully.\n')
            file_name = "data.json"
            self.write_dict_to_file(self.theaters, file_name)
            return

    def write_dict_to_file(self,dictionary, filename):
        with open(filename, 'w') as file:
            json.dump(dictionary, file)

    def read_dict_from_file(self,filename):
        with open(filename, 'r') as file:
            dictionary = json.load(file)
        return dictionary

    def add_movie(self):
        filename = 'data.json'
        self.theaters = self.read_dict_from_file(filename)
        theater_id = input('Enter theater id')
        if theater_id in self.theaters.keys():
            movie_name = input('Enter movie name')
            screening_time = input('Enter screen time')
            self.theaters[theater_id]["schedule"].append({"movie": movie_name, "time": screening_time})
            file_name = "data.json"
            self.write_dict_to_file(self.theaters, file_name)
        else:
            print("Theater not found.")
        return

    def remove_movie(self):
        filename = 'data.json'
        self.theaters = self.read_dict_from_file(filename)
        theater_id = input('Enter theater id')
        movie_name = input('Enter movie name')
        if theater_id in self.theaters:
            count = 0
            for screening in self.theaters[theater_id]["schedule"]:
                if screening["movie"] == movie_name:
                    self.theaters[theater_id]["schedule"].remove(screening)
                    file_name = "data.json"
                    self.write_dict_to_file(self.theaters, file_name)
                    print("Movie removed successfully.")
                    return
                count += 1
            print("Movie not found.")
            return
        else:
            print("Theater not found.")
            return
    def update_movie_timing(self):
        filename = 'data.json'
        self.theaters = self.read_dict_from_file(filename)
        theater_id=input('Enter theater id')
        movie_name=input('Enter movie name')
        new_time=input('Enter new timings')
        if theater_id in self.theaters:
            for screening in self.theaters[theater_id]["schedule"]:
                if screening["movie"] == movie_name:
                    screening["time"] = new_time
                    print("Screening time updated successfully.")
                    file_name = "data.json"
                    self.write_dict_to_file(self.theaters, file_name)
                    return
            print("Movie not found.")
            return
        else:
            print("Theater not found.")
            return

    def display_schedule(self):
        filename='data.json'
        self.theaters=self.read_dict_from_file(filename)
        print("Screening Schedule:")
        for theater_id, theater_info in self.theaters.items():
            print(f"Theater ID: {theater_id}, Name: {theater_info['name']}")
            print("Schedule:")
            for screening in theater_info["schedule"]:
                print(f"Movie: {screening['movie']}, Time: {screening['time']}")
            print()
        return

class user(user1):
    def __init__(self):
        filename='data.json'
        self.theaters=self.read_dict_from_file(filename)
        print("Screening Schedule:")
        for theater_id, theater_info in self.theaters.items():
            print(f"Theater ID: {theater_id}, Name: {theater_info['name']}")
            print("Schedule:")
            for screening in theater_info["schedule"]:
                print(f"Movie: {screening['movie']}, Time: {screening['time']}")
            print()
        A().__init__()

    def read_dict_from_file(self,filename):
        with open(filename, 'r') as file:
            dictionary = json.load(file)
        return dictionary
