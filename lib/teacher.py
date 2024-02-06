#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def teach(self):
        pass
        r1 = random.randint(0, len(self.knowledge))
        return self.knowledge[r1]