'''
Задача 4 (1.25т.)
Turtle е библиотека в Python, която предоставя опростен начин за рисуване чрез графичен интерфейс. С нея може да се създават различни форми, фигури и анимации, като се използва костенурка - виртуален курсор, който се движи по екрана и оставя следи. Вашата задача днес е вдъхновена именно от нея и е следната:

Създайте клас Turtle.

При създаване на обект от класа Turtle трябва да бъдат приети 2 параметъра - x и y, координатите на стартовата точка на вашата костенурка по оста x и оста y. Ако такива не бъдат подадени, се приема, че стартовата точка е с координати (0,0).

Имплементирайте метод get_current_position, който да връща tuple с координатите на настоящата позиция на костенурката.

Костенурката трябва да може да се движи. За целта трябва да бъде написан метод move, който да приема произволен брой аргументи - команди за движение. Ако се подаде невалидна команда (т.е. различна от позволените) да се покаже на конзолата съобщение Invalid command: {command}, но да не се прекъсва хода на метода. Вашата костенурка може да изпълнява само следните 4 движения:

up - премества се 1 стъпка нагоре по координатната система
down - премества се 1 стъпка надолу по координатната система
left - премества се 1 стъпка наляво по координатната система
right - премества се 1 стъпка надясно по координатната система
Костенурката може да има различни конфигурации. Тя може да рисува в определен цвят, да оставя диря с точно определена дебелина и т.н. Имплементирайте метод configure_turtle, който да приема произволен брой аргументи - конфигурационните параметри и техните стойности. Да се връща низ от вида Current configuration: {P}:{V} | {P}:{V} |..., където P е името на конфигурационния параметър, а V е неговата стойност.

Трябва да можем да проверим дали сме изобразили точно определна рисунка. Под рисунка разбираме конкретна последователност от команди. Вашата задача е да имплементирате метод check_for_drawing, който приема последователност от команди (рисунка) и връща bool, който индикира дали такава е била нарисувана.

Пример за рисунка: [up, up, up, right, right, down, left, left].
Като за финал пренапишете __str__, така че да връща следното съобщение: Turtle is at position ({x}, {y}) and has moved {count} times since start
'''

class Turtle:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.count = 0
        self.moves = []

    def get_current_position(self):
        return self.x, self.y

    def move(self, *moves):
        for move in moves:
            if move == 'up':
                self.y += 1
            elif move == 'down':
                self.y -= 1
            elif move == 'right':
                self.x += 1
            elif move == 'left':
                self.x -= 1
            else:
                print(f'Invalid command: {move}')
                continue

            self.count += 1
            self.moves.append(move)

    def configure_turtle(self, **kwargs):
        config_str = 'Current configuration:'

        for key, value in kwargs.items():
            config_str += f' {key}:{value} |'

        return config_str

    def check_for_drawing(self, moves):
        return "".join(moves) in "".join(self.moves)

    def __str__(self):
        return f'Turtle is at position ({self.x},{self.y}) and has moved {self.count} times since start'

# Test Case 1: Test Turtle Initialization with default coordinates (0, 0)
t1 = Turtle()
assert t1.x == 0 and t1.y == 0, "Initial position should be (0,0)"
assert str(t1) == "Turtle is at position (0,0) and has moved 0 times since start", "String representation is incorrect"

# Test Case 2: Test move method with valid moves
t1.move('up', 'right', 'down', 'left')
assert t1.x == 0 and t1.y == 0, "Turtle should return to (0,0) after up, right, down, left"
assert len(t1.moves) == 4, "Turtle should have 4 moves recorded"
assert str(t1) == "Turtle is at position (0,0) and has moved 4 times since start", "String representation after 4 moves is incorrect"

# Test Case 3: Test move method with invalid move
t1.move('right', 'testing', 'right', 'left')
assert len(t1.moves) == 7, "Invalid move should not be added to the move list"
assert str(t1) == "Turtle is at position (1,0) and has moved 7 times since start", "Invalid move should not affect the position or count of moves"

# Test Case 4: Test Turtle Initialization with custom coordinates
t2 = Turtle(3, 4)
assert t2.x == 3 and t2.y == 4, "Initial position should be (3,4)"
assert str(t2) == "Turtle is at position (3,4) and has moved 0 times since start", "String representation with custom initial coordinates is incorrect"

# Test Case 5: Test move method with different valid moves
t2.move('up', 'up', 'right')
assert t2.x == 4 and t2.y == 6, "Turtle should be at (4,6) after moving up twice and right"
assert len(t2.moves) == 3, "Turtle should have 3 moves recorded"
assert str(t2) == "Turtle is at position (4,6) and has moved 3 times since start", "String representation after custom moves is incorrect"

# Test Case 6: Test configure_turtle method
config_message = t2.configure_turtle(color="green", thickness=2, size=10)
assert config_message == "Current configuration: color:green | thickness:2 | size:10 |", "Configuration message is incorrect"

# Test Case 7: Test check_for_drawing method with existing drawing
t2.move('down', 'down', 'left')
assert t2.check_for_drawing(['up', 'right', 'down']) is True, "Drawing sequence should match recorded moves"
assert t2.check_for_drawing(['up', 'up', 'right', 'left']) is False, "Invalid drawing sequence should not match recorded moves"

# Test Case 8: Test get_current_position method
assert t2.get_current_position() == (3, 4), "Current position should be (3,4) after initial moves"

print("✅ All OK! +1.25 points")