import tkinter
import route


class App:
    def __init__(self):
        self.window = tkinter.Tk()
        self.page: route.Page = route.MainMenu(self, "Un titre", [("Quitter", self.destroy)])

    def main_loop(self):
        self.draw()
        self.window.mainloop()

    def go_to_page(self, page_name):
        pass

    def draw(self):
        route.custom_widget.destroy_widgets(self.window)
        self.page.draw(self.window)

    def destroy(self):
        self.window.destroy()


def main():
    app = App()
    app.main_loop()


if __name__ == "__main__":
    main()
