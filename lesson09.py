currency_exchange = {"USD": 0.87, "EUR": 0.92, "UAH": 0.023, "CHF": 1}


class Price:
    def __init__(self, value: float, currency: str):
        self.value: float = value
        self.currency: str = currency

    def __str__(self) -> str:
        return f"Price: {self.value} {self.currency}"

    def convert_to(self, target_currency: str) -> "Price":
        converted_chf = self.value * currency_exchange[self.currency]
        converted_value = converted_chf / currency_exchange[target_currency]
        return Price(value=converted_value, currency=target_currency)

    def __add__(self, other: "Price") -> "Price":
        if self.currency == other.currency:
            return Price(value=self.value + other.value, currency=self.currency)
        else:
            converted_other = other.convert_to(self.currency)
            return Price(
                value=self.value + converted_other.value, currency=self.currency
            )


flight = Price(value=1, currency="USD")
hotel = Price(value=1, currency="UAH")

total = flight + hotel
print(total)  # 1.9456521739130435 USD
