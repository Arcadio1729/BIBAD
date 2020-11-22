from Vector import Vector
from Shape import Shape
from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle
from Circle import Circle


class Drawer:
    def __init__(self):
        self.figures = {}

    def run(self):
        input_command = ""
        input_parameters = []
        print("Enter command: ")
        input_command = input()
        input_command_list=input_command.split()
        current_command = input_command_list[0]
        input_parameters = input_command_list[1:]
        while (input_command!= "quit"):
            try:
                if current_command == "add":
                    self.add(input_parameters)
                elif current_command=="remove":
                    self.remove(input_parameters)
                elif current_command=="move":
                    self.move(input_parameters)
                elif current_command=="scale":
                    self.scale(input_parameters)
                elif current_command=="rotate":
                    self.rotate(input_parameters)
                elif current_command=="set_border_color":
                    self.set_border_color(input_parameters)
                elif current_command=="set_background_color":
                    self.set_background_color(input_parameters)
                elif current_command=="help":
                    self.help(input_parameters)
                else:
                    raise Exception(input_command+" is incorrect command.")
            except Exception as e:
                print(str(e))
            print("Enter command: ")
            input_command = input()
            input_command_list=input_command.split()
            current_command = input_command_list[0]
            input_parameters = input_command_list[1:]

        for f in self.figures.values():
            f.draw()


    def add(self,parameters):
        try:
            if len(parameters)>=2:
                figure_type = parameters[0]
                figure_name = parameters[1]
                if not figure_name[0].isnumeric():
                    if figure_name not in self.figures.keys():
                        if figure_type == "circle":
                            try:
                                if len(parameters)==3:
                                    radius = parameters[2]
                                    self.figures[figure_name] = Circle(figure_name,radius)
                                else:
                                    raise Exception("Incorrect amount of parameters")
                            except Exception as e:
                                print(str(e))
                        elif figure_type == "rectangle":
                            try:
                                if len(parameters) == 4:
                                    side_a = parameters[2]
                                    side_b = parameters[3]
                                    self.figures[figure_name] = Rectangle(figure_name,side_a, side_b)
                                else:
                                    raise Exception("Incorrect amount of parameters")
                            except Exception as e:
                                print(str(e))
                        elif figure_type=="square":
                            try:
                                if len(parameters)==3:
                                    side_a = float(parameters[2])
                                    self.figures[figure_name] = Square(figure_name,side_a)
                                else:
                                    raise Exception("Incorrect amount of parameters")
                            except Exception as e:
                                print(str(e))
                        elif figure_type == "triangle":
                            try:
                                if len(parameters)==5:
                                    side_a = parameters[2]
                                    side_b = parameters[3]
                                    side_c = parameters[4]
                                    self.figures[figure_name] = Triangle(figure_name,side_a, side_b, side_c)
                                else:
                                    raise Exception("Incorrect amount of parameters")
                            except Exception as e:
                                print(str(e))
                        else:
                            raise ValueError("Wrong Figure Type.")
                    else:
                        raise ValueError("Name " + figure_name + " already taken.")
                else:
                    raise ValueError("Name cannot start from number.")
            else:
                raise ValueError("Params amount should be greater than 2.")
        except ValueError as ve:
            print(str(ve))
    def remove(self,parameters):
        figure_name=parameters[0]
        try:
            if figure_name not in self.figures.keys():
                raise Exception("Error: "+figure_name+" does not exist.")
            else:
                self.figures.pop(figure_name)
        except Exception as e:
            print(str(e))

    def move(self,parameters):
        try:
            figure_name=parameters[0]
            if figure_name in self.figures.keys():
                move_vector=Vector(float(parameters[1]),float(parameters[2]))
                self.figures[figure_name].move(move_vector)
            else:
                raise ValueError("Error: "+figure_name+" does not exist.")
        except ValueError as ve:
            print(str(ve))

    def scale(self,parameters):
        try:
            figure_name=parameters[0]
            if figure_name in self.figures.keys():
                ratio=parameters[1]
                self.figures[figure_name].scale(float(ratio))
            else:
                raise ValueError("Error: "+figure_name+" does not exist.")
        except ValueError as ve:
            print(str(ve))

    def rotate(self,parameters):
        try:
            figure_name=parameters[0]
            if figure_name in self.figures.keys():
                angle=parameters[1]
                self.figures[figure_name].rotate(angle)
            else:
                raise ValueError("Error: "+figure_name+" does not exist.")
        except ValueError as ve:
            print(str(ve))

    def set_border_color(self,parameters):
        try:
            figure_name = parameters[0]
            if figure_name in self.figures.keys():
                color = parameters[1]
                self.figures[figure_name].set_border_color(color)
            else:
                raise ValueError("Error: " + figure_name + " does not exist.")
        except ValueError as ve:
            print(str(ve))

    def set_background_color(self,parameters):
        try:
            figure_name=parameters[0]
            if figure_name in self.figures.keys():
                color=parameters[1]
                self.figures[figure_name].set_background_color(color)
            else:
                raise ValueError("Error: "+figure_name+" does not exist.")
        except ValueError as ve:
            print(str(ve))