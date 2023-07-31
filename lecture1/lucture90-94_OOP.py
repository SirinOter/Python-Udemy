class Student:
    pass

student_1 = Student()
student_2 = Student()

student_1.first_name = 'Eric'
student_1.last_name = 'Roby'
student_1.major = 'Computer Science'

student_2.first_name = 'John'
student_2.last_name = 'Miller'
student_2.major = 'Math'


print(student_1.major)
print(student_2.major)


class Worker:
    pass


class Worker:
    school = 'Online School'
    number_of_workers = 0

    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

        Worker.number_of_workers+=1

    def greetings(self):
        return f'Hello, I am {self.first_name} {self.last_name}'

    class FactoryWorker(Worker):
        def __init__(self, first_name, last_name, major):
            super().__init__(first_name, last_name)
            self.major = major



            
    

    def fullname_with_major(self):
        return f'{self.first_name} {self.last_name} is a {self.major} major!'

    def fullname_major_school(self):
        return f'{self.first_name} {self.last_name} is a ' \
               f'{self.major} major, going to {self.school}'
    @classmethod
    def set_online_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def split_workers(cls, worker_str):
        first_name, last_name, major = worker_str.split('.')
        return cls(first_name, last_name, major)


class FactoryWorker:
    pass


worker_1 = FactoryWorker('Eric', 'Roby', 'Computer Science')
worker_2 = Worker('John', 'Miller', 'Math')


print(worker_1.first_name)
print(worker_2.last_name)

print(worker_1.fullname_with_major())
print(Worker.fullname_with_major(worker_2))

print(worker_2.school)

print(f'Number of workers = {Worker.number_of_workers}')

print(worker_1.school)

Worker.set_online_school('Google Hangouts for class!')

print(worker_2.school)

new_worker ='Adil.Yutzy.English'

worker_3 = Worker.split_workers(new_worker)
print(worker_3.fullname_major_school())

print(worker_1.greetings())
print(worker_2.greetings())


