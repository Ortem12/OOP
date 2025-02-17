class Cryptocurrency:
    """
    Базовый класс для представления криптовалюты.

    Атрибуты:
        name (str): Название криптовалюты.
        symbol (str): Символ-тикер криптовалюты.
        minable (bool): Возможность добычи майнингом.
        rate_to_usd (float): Текущий курс к доллару США.
        anonymous (bool): Наличие анонимных транзакций.
    """

    def __init__(self, name, symbol, minable, rate_to_usd, anonymous):
        self.name = name
        self.symbol = symbol
        self.minable = minable
        self.rate_to_usd = rate_to_usd
        self.anonymous = anonymous

    def mining_reward(self):
        """
        Метод для расчета вознаграждения за майнинг.

        Возвращает:
            float: Размер вознаграждения за майнинг.
        """
        raise NotImplementedError("Метод должен быть переопределен в подклассе")


def minable_required(func):
    """
    Декоратор для проверки возможности майнинга криптовалюты.

    Если криптовалюта не может быть добыта майнингом, выводится сообщение.

    Аргументы:
        func (function): Функция, которую нужно обернуть.

    Возвращает:
        function: Обернутая функция.
    """

    def wrapper(self, *args, **kwargs):
        if not self.minable:
            print(f"{self.name} ({self.symbol}): не майнится")
            return None
        return func(self, *args, **kwargs)

    return wrapper


class Nano(Cryptocurrency):
    """
    Подкласс для представления криптовалюты Nano.

    Атрибуты:
        block_lattice (bool): Наличие блок-решетки.
    """

    def __init__(self, block_lattice, rate_to_usd, anonymous):
        super().__init__("Nano", "NANO", True, rate_to_usd, anonymous)
        self.block_lattice = block_lattice

    @minable_required
    def mining_reward(self):
        """
        Метод для расчета вознаграждения за майнинг Nano.

        Возвращает:
            float: Размер вознаграждения за майнинг.
        """
        return 0.02


class Iota(Cryptocurrency):
    """
    Подкласс для представления криптовалюты Iota.

    Атрибуты:
        tangle (bool): Наличие Tangle.
    """

    def __init__(self, tangle, rate_to_usd, anonymous):
        super().__init__("Iota", "IOTA", True, rate_to_usd, anonymous)
        self.tangle = tangle

    @minable_required
    def mining_reward(self):
        """
        Метод для расчета вознаграждения за майнинг Iota.

        Возвращает:
            float: Размер вознаграждения за майнинг.
        """
        return 0.001


class Stellar(Cryptocurrency):
    """
    Подкласс для представления криптовалюты Stellar.

    Атрибуты:
        distributed (bool): Наличие распределенного реестра.
    """

    def __init__(self, distributed, rate_to_usd, anonymous):
        super().__init__("Stellar", "XLM", False, rate_to_usd, anonymous)
        self.distributed = distributed


def print_info(crypto):
    """
    Функция для вывода информации о криптовалюте.

    Аргументы:
        crypto (Cryptocurrency): Экземпляр криптовалюты.
    """
    info = f"{crypto.name} ({crypto.symbol}): "
    info += "добывают майнингом, " if crypto.minable else "не майнится, "
    info += f"курс к USD: {crypto.rate_to_usd}, "
    info += "анонимные транзакции" if crypto.anonymous else "только публичные транзакции"
    if hasattr(crypto, 'block_lattice') and crypto.block_lattice:
        info += ", блок-решетка"
    if hasattr(crypto, 'tangle') and crypto.tangle:
        info += ", Tangle"
    print(info)


# Пример использования
cryptocurrencies = [Nano(block_lattice=True, rate_to_usd=6, anonymous=False),
                    Iota(tangle=True, rate_to_usd=0.4, anonymous=False),
                    Stellar(distributed=False, rate_to_usd=0.15, anonymous=True)]

for crypto in cryptocurrencies:
    print_info(crypto)
    if crypto.minable:
        print(f"Награда за майнинг: {crypto.mining_reward()} {crypto.symbol}\n")