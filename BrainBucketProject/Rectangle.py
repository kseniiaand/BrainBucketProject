class Rectangle():
    """finding the area of a rectangle"""
    length = ""
    width = ""

    def area(self,length, width):
        self.length = length
        self.width = width
        area_of_rec = self.length * self.width
        return area_of_rec
Rectangle1 = Rectangle()

print(Rectangle1.area(10,7))