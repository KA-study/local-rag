from datetime import datetime

from program_files.interface.session_manager.base import SessionManagerInterface


class CliSessionManagerInterface(SessionManagerInterface):

    #セッション一覧および新規セッションの選択肢を表示し、選択を受け取る
    def select_session_id(
        self,
        session_ids: list[str]
    ) -> str:

        print("=== session list ===")

        for i, session_id in enumerate(session_ids):
            print(f"{i}: {session_id}")

        print("n: new session")
        print("set_available_cost: update available cost")

        print("Do not start with _")

        while True:
            choice: str = self._input("select: ")


            #set_available_costの時
            if choice == "set_available_cost":
                return "_SETAVAILABLECOST_"
            
            #new_session指定の時
            if choice == "n":
                return "_NEW_"

            #番号指定の時
            if choice.isdigit():
                idx = int(choice)

                if 0 <= idx < len(session_ids):
                    return session_ids[idx]

            #session_id直接指定の時
            if choice in session_ids:

                return choice


            print("Invalid input")


    def create_session_id(self) -> str:
        
        session_name: str = self._input("new session name >> ")

        now: str = datetime.now().isoformat()

        session_id: str = session_name + now

        return session_id



