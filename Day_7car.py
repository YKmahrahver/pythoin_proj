class Car:
  def __init__(self, model, year, color, for_sale): #constructor method (self means the object were creating rn)
    self.model = model
    self.year = year
    self.color = color
    self.for_sale = for_sale

  def drive(self): #self refers to the specific object
    print(f'You drive the {self.model}')