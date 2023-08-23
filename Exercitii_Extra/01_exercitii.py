'''
1. This is a function to find the highest common factor of two numbers

 def hcf(x,y):
        x=abs(x)
        y=abs(y)
        smaller = y if x>y else x
        s = smaller
        while s>0:
            if x%s==0 and y%s==0:
                break
            s-=1
        return s
Make it a static method in the Fraction class that you had written in earlier exercise.
'''

# @staticmethod
#     def hcf(x,y):
#         x=abs(x)
#         y=abs(y)
#         smaller = y if x>y else x
#         s = smaller
#         while s>0:
#             if x%s==0 and y%s==0:
#                 break
#             s-=1
#         return s


'''

2. In your Fraction class, write a private instance method _reduce
 that reduces a fraction to its lowest terms.
 To reduce a Fraction to its lowest terms you have to divide the numerator
 and denominator by the highest common factor. Call this method in __init__and also call
it on the resultant fraction in methods multiply and add.
'''


class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1
        self._reduce()

    def show(self):
        print(f'{self.nr}/{self.dr}')

    def multiply(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.nr, self.dr * other.dr)
        f._reduce()
        return f

    def add(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
        f._reduce()
        return f

    def _reduce(self):
        h = Fraction.hcf(self.nr, self.dr)
        if h == 0:
            return

        self.nr //= h
        self.dr //= h

    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1
        return s


f1 = Fraction(6, 36)
f1.show()
f2 = Fraction(2, -12)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5)
f3.show()
f3 = f1.multiply(5)
f3.show()

print('#' * 50)

'''
1. In the following class, write code for the methods __eq__, __lt__, __le__.

'''


class Time:
    def __init__(self, h, m, s):
        self._h = h
        self._m = m
        self._s = h

    # Read-only field accessors
    @property
    def hours(self):
        return self._h

    @property
    def minutes(self):
        return self._m

    @property
    def seconds(self):
        return self._s

    def __eq__(self, other):
        return True if _cmp(self, other) == 0 else False

    def __lt__(self, other):
        return True if _cmp(self, other) == 1 else False

    def __le__(self, other):
        return True if (_cmp(self, other) == 0 or _cmp(self, other) == 1) else False


def _cmp(time1, time2):
    if time1._h < time2._h:
        return 1
    if time1._h > time2._h:
        return -1
    if time1._m < time2._m:
        return 1
    if time1._m > time2._m:
        return -1
    if time1._s < time2._s:
        return 1
    if time1._s > time2._s:
        return -1
    return 0


t1 = Time(13, 10, 5)
t2 = Time(5, 15, 30)
t3 = Time(5, 15, 30)
print(t1 < t2)
print(t1 > t2)
print(t1 == t2)
print(t2 == t3)

print('#' * 50)

'''
2. Implement __add__ and __radd__ methods for the following class Length.
'''


class Length:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return f'{self.feet} {self.inches}'

    def add_length(self, L):
        f = self.feet + L.feet
        i = self.inches + L.inches
        if i >= 12:
            i = i - 12
        f += 1
        return Length(f, i)

    def add_inches(self, inches):
        f = self.feet + inches // 12
        i = self.inches + inches % 12
        if i >= 12:
            i = i - 12
        f += 1
        return Length(f, i)

    def __add__(self, other):
        if isinstance(other, Length):
            return self.add_length(other)
        if isinstance(other, int):
            return self.add_inches(other)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)


length1 = Length(2, 10)
length2 = Length(3, 5)

print(length1 + length2)
print(length1 + 2)
print(length1 + 20)
print(20 + length1)

print('#' * 50)
'''
1. Create a class named Course that has instance variables title, instructor, price, lectures,
users(list type), ratings, avg_rating. Implement the methods __str__, new_user_enrolled,
received_a_rating and show_details. From the above class, inherit two classes VideoCourse
and PdfCourse. The class VideoCourse has instance variable length_video and PdfCourse has
instance variable pages.
'''


class Course:
    def __init__(self, title, instructor, price, lectures):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = []
        self.ratings = 0
        self.avg_rating = 0

    def __str__(self):
        return f'{self.title} by {self.instructor}'

    def new_user_enrolled(self, user):
        self.users.append(user)

    def received_a_rating(self, new_rating):
        self.new_rating = new_rating
        self.avg_rating = (self.avg_rating * self.ratings + new_rating) / (self.ratings + 1)
        self.ratings += 1

    def show_details(self):
        print('Numele cursului : ', self.title)
        print('Trainer : ', self.instructor)
        print('Pret : ', self.price)
        print('Numarul lectiilor : ', self.lectures)
        print('Cursanti : ', self.users)
        print('Media aprecierilor : ', self.avg_rating)


class VideoCourse(Course):
    def __init__(self, length_video, title, instructor, price, lectures):
        self.length_video = length_video
        super().__init__(title, instructor, price, lectures)

    def show_details(self):
        super().show_details()
        print('Curs Video : ', self.length_video)


class PdfCourse(Course):
    def __init__(self, pages, title, instructor, price, lectures):
        self.pages = pages
        super().__init__(title, instructor, price, lectures)

    def show_details(self):
        super().show_details()
        print('Curs PDF : ', self.pages)


vc = VideoCourse('Learn C++', 'Jack', 30, 50, 10)
vc.new_user_enrolled('Allen')
vc.new_user_enrolled('Max')
vc.new_user_enrolled('Tom')
vc.received_a_rating(3)
vc.received_a_rating(5)
vc.received_a_rating(4)
vc.show_details()

print()

pc = PdfCourse('Learn Java', 'Jim', 35, 50, 1000)
pc.new_user_enrolled('Allen')
pc.new_user_enrolled('Mary')
pc.new_user_enrolled('JIm')
pc.received_a_rating(5)
pc.received_a_rating(4)
pc.received_a_rating(4.5)
pc.show_details()

print('#' * 40)

'''
4. In the following inheritance hierarchy we have written code to add 'S' to 
id of Student, 'T' to id of Teacher and both 'T' and 'S' to id of Teaching Assistant.
What will be the output of this code. If the code does not work as intended, what 
changes we need to make.
'''


class Person:
    def __init__(self, id):
        self.id = id


class Teacher(Person):
    def __init__(self, id):
        super().__init__(id)
        self.id += 'T'



class Student(Person):
    def __init__(self, id):
        super().__init__(id)
        self.id += 'S'

class TeachingAssistant(Student, Teacher):
    def __init__(self, id):
        super().__init__(id)


x = TeachingAssistant('2675')
print(x.id)
y = Student('4567')
print(y.id)
z = Teacher('3421')
print(z.id)
p = Person('5749')
print(p.id)

print('#' * 40)


class Test:
    pass


t1 = Test()
t2 = Test()
print(t1 == t2, end=' ')
print(type(t1) == type(t2), end=' ')


class Test:
    def method1(self, x):
        self.x = x

    def method2(self):
        x += 10

    def display(self):
        print(self.x)


t = Test()
t.method1(5)
t.method2()
t.display()

