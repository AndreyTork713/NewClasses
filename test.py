class A(object):
    x = 5

    def xx(self):
        return self.x


class AB(A):
    y = 7

    def xx(self):
        return self.x, self.y


ab = AB()
print(ab.xx())
