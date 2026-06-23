


from program_files.interface.profile_run.base import ProfileRunInterface

class CliProfileRunInterface(ProfileRunInterface):
    
    def select_option(
        self,
        ProfileOptionMap: dict
    ) -> str:
        
        while True:
            self._display(ProfileOptionMap)
            
            user_input: str = self._get_input()

            if user_input in ProfileOptionMap.keys():
                break
            else:
                print(f"Invarid input: {user_input}")

        return user_input


    def _display(
        self,
        ProfileOptionMap: dict
    ) -> None:

        print(f"available option: {', '.join(ProfileOptionMap.keys())}")


    def _get_input(self) -> str:
        return self._input(">> ")
