import json
import logging
from typing import Any, Hashable

from fastapi import FastAPI, Request
from src.config.config_loader import ConfigLoader
from src.games.fallout4 import Fallout4
from src.games.gameable import Gameable
from src.games.skyrim import Skyrim
from src.output_manager import ChatManager
from src.llm.llm_client import LLMClient
from src.game_manager import GameStateManager
from src.http.routes.routeable import routeable
from src.http.communication_constants import communication_constants as comm_consts
from src.tts.ttsable import TTSable
from src.tts.xvasynth import xVASynth
from src.tts.xtts import XTTS
from src.tts.piper import Piper
from src import utils
from src.config.definitions.game_definitions import GameEnum
from src.config.definitions.tts_definitions import TTSEnum

class mantella_route(routeable):
    """Main route for Mantella conversations

    Args:
        routeable (_type_): _description_
    """
    def __init__(self, config: ConfigLoader, stt_secret_key_file: str, image_secret_key_file: str, secret_key_file: str, language_info: dict[Hashable, str], show_debug_messages: bool = False) -> None:
        super().__init__(config, show_debug_messages)
        self.__language_info: dict[Hashable, str] = language_info
        self.__secret_key_file: str = secret_key_file
        self.__stt_secret_key_file = stt_secret_key_file
        self.__image_secret_key_file: str = image_secret_key_file
        self.__game: GameStateManager | None = None

        # if not self._can_route_be_used():
        #     error_message = "MantellaSoftware settings faulty. Please check MantellaSoftware's window or log."
        #     logging.error(error_message)

    @utils.time_it
    def _setup_route(self):
        if self.__game:
            self.__game.end_conversation({})

        game: Gameable
        game_enum = self._config.game
        if game_enum.base_game == GameEnum.FALLOUT4:
            game = Fallout4(self._config)
        else:
            game = Skyrim(self._config)

        tts: TTSable
        if self._config.tts_service == TTSEnum.XVASYNTH:
            tts = xVASynth(self._config)
        elif self._config.tts_service == TTSEnum.XTTS:
            tts = XTTS(self._config, game)
        if self._config.tts_service == TTSEnum.PIPER:
            tts = Piper(self._config, game)

        llm_client = LLMClient(self._config, self.__secret_key_file, self.__image_secret_key_file)
        
        chat_manager = ChatManager(self._config, tts, llm_client)
        self.__game = GameStateManager(game, chat_manager, self._config, self.__language_info, llm_client, self.__stt_secret_key_file, self.__secret_key_file)

    @utils.time_it
    def add_route_to_server(self, app: FastAPI):
        @app.post("/mantella")
        async def mantella(request: Request):
            if not self._can_route_be_used():
                error_message = "MantellaSoftware settings faulty. Please check MantellaSoftware's window or log."
                logging.error(error_message)
                return self.error_message(error_message)
            if not self.__game:
                error_message = "Game manager setup failed. There is most likely an issue with the config.ini."
                logging.error(error_message)
                return self.error_message(error_message)
            reply = {}
            received_json: dict[str, Any] | None = await request.json()
            if received_json:
                logging.debug('Processing request...')
                if self._show_debug_messages:
                    logging.log(self._log_level_http_in, json.dumps(received_json, indent=4))
                request_type: str = received_json[comm_consts.KEY_REQUESTTYPE]
                match request_type:
                    case comm_consts.KEY_REQUESTTYPE_INIT:
                        # nothing needs to be done for this request aside from self._can_route_be_used() being triggered
                        logging.debug('Mantella settings initialized')
                        reply = {comm_consts.KEY_REPLYTYPE: comm_consts.KEY_REPLYTTYPE_INITCOMPLETED}
                    case comm_consts.KEY_REQUESTTYPE_STARTCONVERSATION:
                        reply = self.__game.start_conversation(received_json)
                    case comm_consts.KEY_REQUESTTYPE_CONTINUECONVERSATION:
                        reply = self.__game.continue_conversation(received_json)
                    case comm_consts.KEY_REQUESTTYPE_PLAYERINPUT:
                        reply = self.__game.player_input(received_json)
                    case comm_consts.KEY_REQUESTTYPE_ENDCONVERSATION:
                        reply = self.__game.end_conversation(received_json)
                    case _:
                        reply = self.error_message(f"Request type '{request_type}' was not recognized")
            else:
                reply = self.error_message(f"Request did not contain properly formatted json!")

            if self._show_debug_messages:
                logging.log(self._log_level_http_out, json.dumps(reply, indent=4))
            return reply
