from game_state_machine.playing_state import PlayingState
from game_state_machine.paused_state import PausedState
from game_state_machine.level_up_state import LevelUpState
from game_state_machine.waves_state import WavesState
from game_state_machine.boss_state import BossState
from game_state_machine.main_menu_state import MainMenuState
from game_state_machine.game_over_state import GameOverState
from game_state_machine.save_score_state import SaveScoreState
from game_state_machine.leaderboard_state import LeaderBoardState
from game_state_machine.saving_game_state import SavingGameState
from game_state_machine.loading_game_state import LoadingGameState
from game_state_machine.options_state import OptionsState
from game_state_machine.changing_bind_state import ChangingBindState
from game_state_machine.boss_key_state import BossKeyState
from game_state_machine.dialogue_state import DialogueState
from game_state_machine.shop_state import ShopState
from time import time


class GameStateManager:
    def __init__(self, map_manager=None, input_handler=None, main_canvas=None):
        print("GAME STATE INIT")
        self.map_manager = map_manager
        self.input_handler = input_handler
        self.main_canvas = main_canvas

        self.PLAYING = PlayingState(self)
        self.PAUSED = PausedState(self)
        self.LEVELUP = LevelUpState(self)
        self.WAVES = WavesState(self)
        self.BOSS = BossState(self)
        self.MAINMENU = MainMenuState(self)
        self.GAMEOVER = GameOverState(self)
        self.SAVESCORE = SaveScoreState(self)
        self.LEADERBOARD = LeaderBoardState(self)
        self.SAVINGGAME = SavingGameState(self)
        self.LOADINGGAME = LoadingGameState(self)
        self.OPTIONS = OptionsState(self)
        self.CHANGINGBIND = ChangingBindState(self)
        self.BOSSKEY = BossKeyState(self)
        self.DIALOGUE = DialogueState(self)
        self.SHOP = ShopState(self)

        self.current_state = self.MAINMENU

        self.PLAYING.initialise_state()
        self.PAUSED.initialise_state()
        self.LEVELUP.initialise_state()
        self.WAVES.initialise_state()
        self.BOSS.initialise_state()
        self.MAINMENU.initialise_state()
        self.GAMEOVER.initialise_state()
        self.SAVESCORE.initialise_state()
        self.LEADERBOARD.initialise_state()
        self.SAVINGGAME.initialise_state()
        self.LOADINGGAME.initialise_state()
        self.OPTIONS.initialise_state()
        self.CHANGINGBIND.initialise_state()
        self.BOSSKEY.initialise_state()
        self.DIALOGUE.initialise_state()
        self.SHOP.initialise_state()

        self.current_state.enter_state()

        self.previous_state = None

    def update(self):
        self.current_state.update_states()

        if self.input_handler.get_pressed_combo("control_l", "b"):  # boss-key
            self.previous_state = self.current_state
            self.current_state.change_state(self.BOSSKEY)
