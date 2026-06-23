from abc import ABC, abstractmethod

from program_files.interface.base.base_interface import Interface


class ProfileRunInterface(Interface, ABC):

    @abstractmethod
    def select_option(
        self,
        ProfileOptionMap: dict
    ) -> str:
        ...
