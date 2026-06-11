from dataclasses import dataclass

from program_files.app.components import Components
from program_files.app.user_config import UserConfig
from program_files.app._types import (
    DEFAULT_COMPONENTS,
    DEFAULT_USER_ID,
    DEFAULT_USER_CONFIG,
)

@dataclass
class AppContext:
    user_id: str = DEFAULT_USER_ID
    #差し替え可能なクラス類から、使用するものを決定する
    components: Components = DEFAULT_COMPONENTS
    #PDF, DBなどのpathや、その他設定を決定する
    user_config: UserConfig = DEFAULT_USER_CONFIG

    
