

import tkinter as tk


class MiniSite(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Мой мини-сайт на Tkinter")
        self.geometry("700x600")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.pages = {}

        for Page in (HomePage, AboutPage, ContactPage, SettingsPage, logerUser):
            page = Page(self)
            self.pages[Page] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(HomePage)

    def show_page(self, page):
        self.pages[page].tkraise()


class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="🏠 Главная страница",
                 font=("Arial", 20)).pack(pady=30)

        tk.Button(self, text="О нас", width=15,
                  command=lambda: master.show_page(AboutPage)).pack(pady=10)

        tk.Button(self, text="Контакты", width=15,
                  command=lambda: master.show_page(ContactPage)).pack(pady=10)

        tk.Button(self, text="Настройки", width=15,
                  command=lambda: master.show_page(SettingsPage)).pack(pady=10)
        tk.Button(self, text="logerUser", width=15, command=lambda: master.show_page(logerUser)).pack(pady=10)


class AboutPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="ℹ️ О нас",
                 font=("Arial", 20)).pack(pady=30)

        tk.Label(self, text="Мы создаём крутые").pack(pady=10)

        tk.Button(self, text="Назад",
                  command=lambda: master.show_page(HomePage)).pack(pady=10)


class ContactPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="📞 Контакты",
                 font=("Arial", 20)).pack(pady=30)

        tk.Label(self, text="Почта: example@mail.com").pack(pady=10)

        tk.Button(self, text="Назад",
                  command=lambda: master.show_page(HomePage)).pack(pady=10)


class SettingsPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="🔧 Настройки",
                 font=("Arial", 20)).pack(pady=30)

        tk.Label(self, text="Пользователь: user").pack(pady=10)
        tk.Label(self, text="Пароль: 123456").pack(pady=10)

        tk.Button(self, text="Назад",
                  command=lambda: master.show_page(HomePage)).pack(pady=10)

        tk.Button(self, text="Сохранить",
                  command=lambda: master.show_page(HomePage)).pack(pady=10)

        tk.Button(self, text="Выход",
                  command=master.destroy).pack(pady=10)

class logerUser(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="📝 Лог пользователя",
                 font=("Arial", 20)).pack(pady=30)

        tk.Button(self, text="Назад",
                  command=lambda: master.show_page(HomePage)).pack(pady=10)


if __name__ == "__main__":
    app = MiniSite()
    app.mainloop()

