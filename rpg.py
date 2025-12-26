full_dot = '●'
empty_dot = '○'

def create_character(name,strength,intelligence,charisma):
    
  if not isinstance(name, str):
      return "The character name should be a string"
  if not name:
    return "The character should have a name"
  if len(name) > 10 :
    return "The character name is too long"
  if name.count(" ") > 0:
    return "The character name should not contain spaces"
  if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int) :
    return "All stats should be integers"
  if strength < 1 or intelligence < 1 or charisma < 1  :  
    return "All stats should be no less than 1"
  if strength > 4 or intelligence > 4 or charisma > 4  :  
    return  "All stats should be no more than 4"
  if strength+intelligence+charisma != 7 :    
    return "The character should start with 7 points"
  car_strengh = calc_stat_graph(strength)
  car_int = calc_stat_graph(intelligence)
  car_charisma = calc_stat_graph(charisma)
  
  return name+"\nSTR "+car_strengh+"\nINT "+car_int+"\nCHA "+car_charisma

def calc_stat_graph(value):
    empty = 10 - value
    print(full_dot*value + empty_dot*empty)
    return full_dot*value+empty_dot*empty

create_character('ren', 4, 2, 1)