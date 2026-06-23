

from program_files.runtime import InterfaceMode
from program_files.interface.profile_run.base import ProfileRunInterface


class ProfileRunInterfaceAdapter:

    def __init__(self):
        self._interface: ProfileRunInterface = InterfaceMode.get_interface().profile_run()

    def select_option(
        self,
        ProfileOptionMap: dict
    ) -> str:

        user_input:str = self._interface.select_option(ProfileOptionMap)

        return user_input
