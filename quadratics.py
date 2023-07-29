import random



NUMBER_OF_PROBLEMS = 10  # Adjust the number of problems you want to generate

class Quadratic:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def coefficient_one(self):
        coefficient_1 = 1
        return coefficient_1
    
    def coefficient_two(self):
        coefficient_2 = self.a + self.b
        return coefficient_2

    def constant_one(self):
        constant_1 = self.a * self.b
        return constant_1

def main():

    with open('quadratics.md', 'w') as file1:

        file1.write("<pre>\n")
        file1.write("Name: _______________________________             \
Date: _____________________\n")
        file1.write("Wack Rapper's Class\n")
        file1.write("</pre>\n\n")

        for x in range(0, NUMBER_OF_PROBLEMS):
            random_list = [2, 3, 4, 5, 6, 7, 8, 9]
            a = random.choice(random_list)
            b = random.choice(random_list)
            new_equation = Quadratic(a, b)
            file1.write("<div>\n")
            file1.write(f"<h3>Problem {x + 1}</h3>\n")
            file1.write(f"<p>Factor the following quadratic: &nbsp; \
x<sup>2</sup> + \
{new_equation.coefficient_two()}x + \
{new_equation.constant_one()}. </p>\n"
            )
            file1.write("<br><br><br>\n")
            file1.write("</div>")


if __name__ == "__main__":
    main()
