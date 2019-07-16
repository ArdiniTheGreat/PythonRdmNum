from uagame import Window
from time import sleep

#window here
window = Window("Hacking",1920,1010)
window.set_font_color("green")
window.set_font_name("couriernew")
window.set_bg_color("black")
window.set_font_size(18)

line_y=0
string_height = window.get_font_height()

#display attempts
window.draw_string("ONE ATTEMPT LEFT", 0, line_y)
window.update()
line_y = line_y + string_height
#display password lists
sleep(0.3)
window.draw_string("***?101//1001-DOG/|10", 0, line_y)
window.update()
line_y = line_y + string_height
sleep(0.3)
window.draw_string("01~/-PEPE-10?/", 0, line_y)
window.update()
line_y = line_y + string_height
window.draw_string("0001-YEET-\10", 0, line_y)
window.update()
line_y = line_y + string_height
#password prompt
guess = window.input_string("ENTER PASSWORD >", 0, line_y)
window.clear()

#outcome
if (guess == "PEPE"):
    sleep(0.3)
    window.draw_string("~ACESS GRANTED~", 0, 0)
    window.update()
else:
    sleep(0.3)
    window.draw_string("~INCORRECT~", 0, 0)
    window.update()
    window.clear()
sleep(1)
#prompt for end
window.input_string("PRESS ENTER TO QUIT", 0, line_y)


#close window
window.close()


