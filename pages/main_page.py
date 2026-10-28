from .base_page import BasePage


class MainPage(BasePage):
    """Главная страница: все нужные методы уже есть в BasePage."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
