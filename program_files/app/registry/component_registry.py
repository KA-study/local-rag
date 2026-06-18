


class ComponentRegistry:
    _registry: dict[type, list[type]] = {}

    @classmethod
    def register(
        cls,
        base: type,
        implementation: type,
    ) -> None:

        cls._registry.setdefault(
            base,
            []
        ).append(implementation)

    #decorator
    @classmethod
    def component(
        cls,
        base: type,
    ):

        def decorator(
            implementation: type
        ) -> type:

            cls.register(
                base,
                implementation
            )

            return implementation

        return decorator

    @classmethod
    def get_choices(
        cls,
        base: type,
    ) -> list[type]:

        return cls._registry.get(
            base,
            []
        )
