from dataclasses import dataclass

from program_files.app.context.components import Components
from program_files.app.context.user_config import UserConfig


@dataclass(frozen=True)
class AppContext:
    user_id: str
    #差し替え可能なクラス類から、使用するものを決定する
    components: Components
    #PDF, DBなどのpathや、その他設定を決定する
    user_config: UserConfig

    
