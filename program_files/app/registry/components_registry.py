
from program_files.app.registry.components_info import ComponentsInfo

class ComponentsRegistry:
    _registry: dict[type, list[ComponentsInfo]] = {}

    @classmethod
    def register(
        cls,
        base: type,
        components_info: ComponentsInfo,
    ) -> None:

        cls._registry.setdefault(
            base,
            []
        ).append(components_info)

    #decorator
    @classmethod
    def component(
        cls,
        base: type, #抽象既定クラスが入る。
        name: str #具体クラスの名前が入る
    ):

        def decorator(
            implementation: type
        ) -> type:

            #components_info生成
            components_info = ComponentsInfo(
                type = implementation,
                name=name
            )

            cls.register(
                base,
                components_info
            )

            return implementation

        return decorator

    @classmethod
    def get_choices(
        cls,
        base: type,
    ) -> list[ComponentsInfo]:

        return cls._registry.get(
            base,
            []
        )

    @classmethod
    def get_name(
        cls,
        implementation: type,
    ) -> str:

        for infos in cls._registry.values():
            for info in infos:
                if info.type is implementation:
                    return info.name

        raise ValueError(
            f"{implementation.__name__} is not registered."
        )

    @classmethod
    def get_choices_name(
        cls,
        implementation: type,
    ) -> list[str]:
    
        for infos in cls._registry.values():
            for info in infos:
                if info.type is implementation:
                    return [
                        choice.name
                        for choice in infos
                    ]

        raise ValueError(
            f"{implementation.__name__} is not registered."
        )

























