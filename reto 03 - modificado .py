
class MenuItem:
    def __init__(self, name: str, price: float, size: str = "regular") -> None:
        self.name: str = name
        self.price: float = price
        self.size: str = size

    def total_price(self, quantity: int = 1) -> float:
        return self.price * quantity

    def calculate_price(self): 
        pass

    def __str__(self) -> str:
        return f"{self.name} (${self.price:.2f})"


class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size: str, is_alcohol: bool = False) -> None:
        super().__init__(name, price, size)
        self._is_alcohol: bool = is_alcohol

    def calculate_price(self) -> None:
        if self.size == "small":
            self.price *= 0.8
        elif self.size == "large":
            self.price *= 1.4

    def get_is_alcohol(self):
        return self._is_alcohol

    def set_is_alcohol(self, value: bool):
        self._is_alcohol = value

    def __str__(self) -> str:
        alcohol: str = ""
        if self._is_alcohol:
            alcohol = "alcoholic"
        return (
            f"{self.name}{alcohol} {self.size.capitalize()} "
            f"- (${self.price:.2f})"
        )


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, with_sauce: bool = False, with_lemon: bool = False) -> None:
        super().__init__(name, price)
        self._with_sauce: bool = with_sauce
        self._with_lemon: bool = with_lemon

    def get_with_sauce(self):
        return self._with_sauce

    def set_with_sauce(self, value: bool):
        self._with_sauce = value

    def get_with_lemon(self):
        return self._with_lemon

    def set_with_lemon(self, value: bool):
        self._with_lemon = value

    def __str__(self) -> str:
        sauce: str = ""
        lemon: str = ""
        if self._with_sauce:
            sauce = "with homemade sauce"
        if self._with_lemon:
            lemon = "and lemon"
        return f"{self.name}{sauce}{lemon} - (${self.price:.2f})"


class Soup(MenuItem):
    def __init__(self, name: str, price: float, size: str, temperature: str = "regular",
                 with_tostacos: bool = False, with_avocado: bool = False) -> None:
        super().__init__(name, price, size)
        self._temperature: str = temperature
        self._with_tostacos: bool = with_tostacos
        self._with_avocado: bool = with_avocado

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        self._temperature = value

    def get_with_tostacos(self):
        return self._with_tostacos

    def set_with_tostacos(self, value: bool):
        self._with_tostacos = value

    def get_with_avocado(self):
        return self._with_avocado

    def set_with_avocado(self, value: bool):
        self._with_avocado = value

    def calculate_price(self) -> None:
        if self.size == "small":
            self.price *= 0.9
        elif self.size == "large":
            self.price *= 1.2
        if self._with_avocado:
            self.price *= 1.05
        if self._with_tostacos:
            self.price *= 1.1

    def __str__(self) -> str:
        avocado: str = ""
        tostacos: str = ""
        if self._with_avocado:
            avocado = "avocado addition"
        if self._with_tostacos:
            tostacos = "tostacos addition"
        return (
            f"{self.name}{self.temperature}{avocado}{tostacos} "
            f" {self.size.capitalize()} "
            f"- (${self.price:.2f})"
        )


class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, size: str, protein: str, carbs: str,
                 is_vegetarian: bool = False, walnut_allergy: bool = False, cereal_allergy: bool = False,
                 egg_allergy: bool = False) -> None:
        super().__init__(name, price, size)
        self._protein: str = protein
        self._carbs: str = carbs
        self._is_vegetarian: bool = is_vegetarian
        self._walnut_allergy: bool = walnut_allergy
        self._cereal_allergy: bool = cereal_allergy
        self._egg_allergy: bool = egg_allergy

    def get_protein(self):
        return self._protein

    def set_protein(self, value):
        self._protein = value

    def get_carbs(self):
        return self._carbs

    def set_carbs(self, value):
        self._carbs = value

    def get_is_vegetarian(self):
        return self._is_vegetarian

    def set_is_vegetarian(self, value: bool):
        self._is_vegetarian = value

    def get_walnut_allergy(self):
        return self._walnut_allergy

    def set_walnut_allergy(self, value: bool):
        self._walnut_allergy = value

    def get_cereal_allergy(self):
        return self._cereal_allergy

    def set_cereal_allergy(self, value: bool):
        self._cereal_allergy = value

    def get_egg_allergy(self):
        return self._egg_allergy

    def set_egg_allergy(self, value: bool):
        self._egg_allergy = value

    def calculate_price(self) -> None:
        if self.size == "small":
            self.price *= 0.9
        elif self.size == "large":
            self.price *= 1.3
        if self._is_vegetarian:
            self.price *= 2
        if self._walnut_allergy or self._cereal_allergy or self._egg_allergy:
            self.price *= 1.05

    def __str__(self) -> str:
        vegetarian: str = ""
        if self._is_vegetarian:
            vegetarian = "vegetarian"
        return (
            f"{self.name}{self._protein}{self._carbs}{vegetarian} "
            f" {self.size.capitalize()} "
            f"- (${self.price:.2f})"
        )


class Dessert(MenuItem):
    def __init__(self, name: str, price: float, lactose_intolerant: bool = False,
                 chocolate_addition: bool = False, ice_cream_addition: bool = False) -> None:
        super().__init__(name, price)
        self._lactose_intolerant: bool = lactose_intolerant
        self._chocolate_addition: bool = chocolate_addition
        self._ice_cream_addition: bool = ice_cream_addition

    def get_lactose_intolerant(self):
        return self._lactose_intolerant

    def set_lactose_intolerant(self, value: bool):
        self._lactose_intolerant = value

    def get_chocolate_addition(self):
        return self._chocolate_addition

    def set_chocolate_addition(self, value: bool):
        self._chocolate_addition = value

    def get_ice_cream_addition(self):
        return self._ice_cream_addition

    def set_ice_cream_addition(self, value: bool):
        self._ice_cream_addition = value

    def calculate_price(self) -> None:
        if self._lactose_intolerant:
            self.price *= 1.4
        if self._chocolate_addition:
            self.price *= 1.1
        if self._ice_cream_addition:
            self.price *= 1.2

    def __str__(self) -> str:
        return f"{self.name} - (${self.price:.2f})"


class SideDish(MenuItem):
    def __init__(self, name: str, price: float, size: str, is_spicy: bool = False, extra_cheese: bool = False) -> None:
        super().__init__(name, price, size)
        self._is_spicy: bool = is_spicy
        self._extra_cheese: bool = extra_cheese

    def get_is_spicy(self):
        return self._is_spicy

    def set_is_spicy(self, value: bool):
        self._is_spicy = value

    def get_extra_cheese(self):
        return self._extra_cheese

    def set_extra_cheese(self, value: bool):
        self._extra_cheese = value

    def calculate_price(self) -> None:  
        if self.size == "small":
            self.price *= 0.7
        elif self.size == "large":
            self.price *= 1.3
        if self._is_spicy:
            self.price *= 1.1
        if self._extra_cheese:
            self.price *= 1.15

    def __str__(self) -> str:
        spicy: str = ""
        cheese: str = ""
        if self._is_spicy:
            spicy = " (spicy)"
        if self._extra_cheese:
            cheese = " (extra cheese)"
        return f"{self.name}{spicy}{cheese} {self.size} - ${self.price:.2f}"


class Salad(MenuItem):
    def __init__(self, name: str, price: float, size: str, dressing_type: str = "house",
                 chicken_addition: bool = False) -> None:
        super().__init__(name, price, size)
        self._dressing_type: str = dressing_type
        self._chicken_addition: bool = chicken_addition

    def get_dressing_type(self):
        return self._dressing_type

    def set_dressing_type(self, value):
        self._dressing_type = value

    def get_chicken_addition(self):
        return self._chicken_addition

    def set_chicken_addition(self, value: bool):
        self._chicken_addition = value

    def calculate_price(self) -> None:
        if self.size == "large":
            self.price *= 1.4
        if self._chicken_addition:
            self.price *= 1.1

    def __str__(self) -> str:
        chicken: str = ""
        if self._chicken_addition:
            chicken = "chicken"
        return (
            f"{self.size} {self.name} with {self._dressing_type} "
            f" dressing - {chicken} ${self.price:.2f}"
        )


class Coffee(MenuItem):
    def __init__(self, name: str, price: float, size: str, coffee_type: str = "espresso",
                 milk_type: str | None = None) -> None:
        super().__init__(name, price, size)
        self._coffee_type: str = coffee_type
        self._milk_type: str | None = milk_type

    def get_coffee_type(self):
        return self._coffee_type

    def set_coffee_type(self, value):
        self._coffee_type = value

    def get_milk_type(self):
        return self._milk_type

    def set_milk_type(self, value):
        self._milk_type = value

    def calculate_price(self) -> None:
        if self.size == "small":
            self.price *= 0.8
        elif self.size == "large":
            self.price *= 1.5
        if self._milk_type in ["almond", "soy"]:
            self.price *= 1.2

    def __str__(self) -> str:
        milk: str = f" with {self._milk_type} milk" if self._milk_type else ""
        return f"{self.size} {self._coffee_type}{milk} - ${self.price:.2f}"


class KidsMeal(MenuItem):
    def __init__(self, name: str, price: float, main_item: str, side_item: str, drink: str, toy: bool = True) -> None:
        super().__init__(name, price)
        self._main_item: str = main_item
        self._side_item: str = side_item
        self._drink: str = drink
        self._toy: bool = toy

    def get_main_item(self):
        return self._main_item

    def set_main_item(self, value):
        self._main_item = value

    def get_side_item(self):
        return self._side_item

    def set_side_item(self, value):
        self._side_item = value

    def get_drink(self):
        return self._drink

    def set_drink(self, value):
        self._drink = value

    def get_toy(self):
        return self._toy

    def set_toy(self, value: bool):
        self._toy = value

    def calculate_price(self) -> None:
        if not self._toy:
            self.price *= 0.9

    def __str__(self) -> str:
        toy: str = " with toy" if self._toy else ""
        return (    
            f"Kids Meal: {self._main_item} + {self._side_item} + "
            f" {self._drink}{toy} - ${self.price:.2f}"
        )


class Special(MenuItem):
    def __init__(self, name: str, price: float, day_of_week: str, is_chef_recommendation: bool = False) -> None:
        super().__init__(name, price)
        self._day_of_week: str = day_of_week
        self._is_chef_recommendation: bool = is_chef_recommendation

    def get_day_of_week(self):
        return self._day_of_week

    def set_day_of_week(self, value):
        self._day_of_week = value

    def get_is_chef_recommendation(self):
        return self._is_chef_recommendation

    def set_is_chef_recommendation(self, value: bool):
        self._is_chef_recommendation = value

    def calculate_price(self) -> None:
        if self._day_of_week in ["Tuesday", "Wednesday"]:
            self.price *= 0.85
        if self._is_chef_recommendation:
            self.price *= 1.1

    def __str__(self) -> str:
        chef: str = " (Chef's Recommendation)" if self._is_chef_recommendation else ""
        return (
            f"Special of the day ({self._day_of_week}): {self.name}{chef} - "
            f" ${self.price:.2f}"
        )



class MedioPago:
  def __init__(self):
    pass

  def pagar(self, monto):
    pass

class Tarjeta(MedioPago):
  def __init__(self, numero, cvv):
    super().__init__()
    self.numero = numero
    self.cvv = cvv

  def pagar(self, monto):
    print(f"Pagando {monto} con tarjeta {self.numero[-4:]}")

class Efectivo(MedioPago):
  def __init__(self, monto_entregado):
    super().__init__()
    self.monto_entregado = monto_entregado

  def pagar(self, monto):
    if self.monto_entregado >= monto:
      print(f"Pago realizado en efectivo. Cambio: {self.monto_entregado - monto}")
    else:
      print(f"Fondos insuficientes. Faltan {monto - self.monto_entregado} para completar el pago.")




class Order:
    def __init__(self, customer_name: str) -> None:
        self.customer_name: str = customer_name
        self.items: list[MenuItem] = []
        self.discount: float = 0
        self.tax_rate: float = 0.08

    def add_item(self, menu_item: MenuItem, quantity: int = 1) -> None:
        for _ in range(quantity):
            menu_item.calculate_price()
            self.items.append(menu_item)

    def calculate_subtotal(self) -> float:
        return sum(item.price for item in self.items)

    def apply_discounts(self) -> None:
        self.discount = 0
        subtotal: float = self.calculate_subtotal()
        if subtotal >= 50:
            self.discount += subtotal * 0.05
        if len(self.items) >= 4:
            self.discount += subtotal * 0.02

    def calculate_tax(self) -> float:
        return (self.calculate_subtotal() - self.discount) * self.tax_rate

    def calculate_total(self) -> float:
        self.apply_discounts()
        subtotal: float = self.calculate_subtotal()
        tax: float = self.calculate_tax()
        return (subtotal - self.discount) + tax

    def bill(self) -> None:
        print("BILL:")
        print(f"{self.customer_name}")
        print("Items:")
        for item in self.items:
            print(item)
        subtotal: float = self.calculate_subtotal()
        tax: float = self.calculate_tax()
        total: float = self.calculate_total()
        print(f"Subtotal: ${subtotal:.2f}")
        if self.discount > 0:
            print(f"Discount ${self.discount:.2f}")
        print(f"Taxes: ({self.tax_rate*100:.0f}%): ${tax:.2f}")
        print(f"Total: ${total:.2f}")


class Payment:
    def __init__(self, order: Order, medio_pago: MedioPago):
        self.order = order
        self.medio_pago = medio_pago
        self.amount = self.order.calculate_total()
        self.is_paid = False

    def process_payment(self):
        print(f"Procesando pago de ${self.amount:.2f} para {self.order.customer_name}")
        self.medio_pago.pagar(self.amount)
        self.is_paid = True

