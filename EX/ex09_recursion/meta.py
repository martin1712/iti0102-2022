"""Meta-trees and meta-dragons."""
from turtle import Turtle
from sys import setrecursionlimit
setrecursionlimit(10000)


def tree(length):
    """Ok."""
    if length < 5:
        return
    else:
        t.forward(length)
        t.left(60)
        tree(3 * length / 5)
        t.right(120)
        tree(3 * length / 5)
        t.left(60)
        t.backward(length)


def apply_dragon_rules(string: str):
    """
    Write a recursive function that replaces characters in string.

    Like so:
        "a" -> "aRbFR"
        "b" -> "LFaLb"
    apply_dragon_rules("a") -> "aRbFR"
    apply_dragon_rules("aa") -> "aRbFRaRbFR"
    apply_dragon_rules("FRaFRb") -> "FRaRbFRFRLFaLb"

    :param string: sentence with "a" and "b" characters that need to be replaced
    :return: new sentence with "a" and "b" characters replaced
    """
    if string == "":
        return ""
    if string[0] == "a":
        return "aRbFR" + str(apply_dragon_rules(string[1:]))
    if string[0] == "b":
        return "LFaLb" + str(apply_dragon_rules(string[1:]))
    return string[0] + apply_dragon_rules(string[1:])


def curve(string, depth):
    """
    Recursively generate the next depth of rules.

    Calls apply_dragon_rules() function `depth` times.
    curve("Fa", 2) -> "FaRbFRRLFaLbFR"

    :param string: current instruction string
    :param depth: how many times the rules are applied
    :return: instructionset for drawing the dragon at iteration 'depth'
    """
    if depth == 0:
        return ""
    elif depth == 1:
        return apply_dragon_rules(string)
    else:
        return curve(apply_dragon_rules(string), depth - 1)


def format_curve(string):
    """
    Use recursions to remove  a  and  b  symbols from the instruction string.

    format_curve("Fa") -> "F"
    format_curve("FaRbFR") -> "FRFR"

    :param string: instruction string
    :return: clean instructions with only "F", "R", and "L" characters
    """
    if len(string) == 0:
        return ""
    if string[0] == "a":
        return "" + str(format_curve(string[1:]))
    if string[0] == "b":
        return "" + str(format_curve(string[1:]))
    return string[0] + format_curve(string[1:])


def draw_dragon(s, length):
    """Draws the dragon by reading the string recursively.

    Use t.right(), t.left(), t.forward() and draw_dragon() to move turtle.
        L - means turn 90 degrees to left and go forward
        R - means turn 90 degrees to right and go forward
        F - means don't turn just go forward

    :param string: instructions left to process
    :param length: how many pixels to move forward, left or right
    """
    if len(s) == 0:
        return ""
    if s[0] == "L":
        t.left(90)
        t.forward(length)
        return draw_dragon(s[1:], length)
    elif s[0] == "R":
        t.right(90)
        t.forward(length)
        return draw_dragon(s[1:], length)
    elif s[0] == "F":
        t.forward(length)
        return draw_dragon(s[1:], length)


def get_line_length(dragon_width, depth):
    """Return one Turtle step length if the width and depth are known."""
    return dragon_width / (2 ** (1 / 2)) ** depth


def save(t: Turtle):
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    t.ht()  # hide him
    t.getscreen().getcanvas().postscript(file='tree.ps')


if __name__ == '__main__':
    t = Turtle()
    t.getscreen().bgcolor("#1c262b")
    t.color("#96004f")
    t.speed(0)
    t.pensize(2)
    t.left(90)
    s = curve("Fa", 8)
    s = format_curve(s)
    length = get_line_length(100, 8)
    draw_dragon(s, length)

    save(t)
    t.getscreen().exitonclick()

    print(format_curve("FaRbFR"))
