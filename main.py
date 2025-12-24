from window import Window
from cell import Cell

def main():
    win = Window(800, 600)
    c1 = Cell(win)
    c1.draw(111,111,222,222)
    c2 = Cell(win)
    c2.draw(444,444,555,555)
    c1.draw_move(c2)
    win.wait_for_close()


if __name__ == "__main__":
    main()