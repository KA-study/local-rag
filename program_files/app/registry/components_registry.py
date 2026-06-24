
from program_files.app.registry.components_info import ComponentsInfo

#global
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
    def get_choices_for_base(
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

    #ProfileStorageManagerに使用するために実装する際は、forで_registryのbase_typeを全探索
    @classmethod
    def get_type(
        cls,
        base: type,
        name: str,
    ) -> type:

        for info in cls._registry.get(base, []):
            if info.name == name:
                return info.type

        raise ValueError(
            f"{name} is not registered for {base.__name__}."
        )

    @classmethod
    def get_choices_for_implementation(
        cls,
        implementation: type,
    ) -> list[ComponentsInfo]:
    
        for infos in cls._registry.values():
            for info in infos:
                if info.type is implementation:
                    return infos

        raise ValueError(
            f"{implementation.__name__} is not registered."
        )

























