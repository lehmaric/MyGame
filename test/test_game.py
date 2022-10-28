import pytest
from src.Game import Game

#Scope = "function"
Scope = "package"


class TestGame:

    @pytest.fixture(autouse=True)
    def get_game_instance(self):
        game = Game()
        return game

    @pytest.fixture
    def base(self):
        return 5

    def test_new_game_is_running(self, get_game_instance):
        assert get_game_instance.running == True

    def test_screen_is_255_times_255(self, get_game_instance):
        get_game_instance.running == True

    def test_add(self, base):
        assert base + 2 == 7