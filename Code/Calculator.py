#!/usr/bin/python
# -*- coding: utf-8 -*-

class SimpleCalculator():
    """
    This class abstracts a calculator with basic
    arithmetic operations
    """

    def __init__(self):
       self.curr_screen = 0
       self.prev_screen = 0

       # can be either '+' or '-'
       self.operator = None

       # the following boolean variable decides whether the last
       # input was a number or an operator
       # True iff it's a number
       self.input_type = True

    def clear(self):
        """
        Clears the screens and operators
        """
        self.__init__()

    def digest(self):
        """
        This method processes the operation stored in the class' variables,
        that is, performs the binary operation saved in self.operator
        on self.curr_screen and self.prev_screen and saves the result
        in self.curr_screen.
        If self.operator is None, it does nothing.
        """
        if self.operator is not None:
            if self.operator == '+':
                self.curr_screen = int(self.prev_screen) + int(self.curr_screen)
            elif self.operator == '-':
                self.curr_screen = int(self.prev_screen) - int(self.curr_screen)


    def enter_digit(self, digit):
        """
        :param digit in the range [0, 9]:
        """
        if self.input_type:
            self.curr_screen = (self.curr_screen * 10) + int(digit)
        else:
            self.prev_screen = self.curr_screen
            self.curr_screen = int(digit)
        self.input_type = True

    def enter_op(self, op):
        """
        :op can be either '+' or '-' or '=':
        """
        if op == '=':
            if self.input_type:
                self.digest()
                self.prev_screen = 0
            else:
                # the following functionality is based on what the
                # Mac OS X calculator actually does
                self.prev_screen = self.curr_screen
                self.digest()
        else:
            if self.operator is None:
                self.prev_screen = self.curr_screen
            else:
                self.digest()
            self.operator = op
        self.input_type = False
