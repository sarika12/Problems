import pytest
#
# calculate_discount(price, discount_percentage)
# Apply a discount of 10% on a price of 100.
# Apply a discount of 0% (no discount) on a price of 200.
# Apply a discount of 50% on a price of 50.

class Calcuate:
    def __init__(self,price,discount_percentage):
        self.price=price
        self.discount_percentage=discount_percentage

    def calculate_discount(self,price,discount_percentage):
        if self.price<0:
            raise ValueError("price can not be negative")
        if self.discount_percentage< 0 and self.discount_percentage>100:
            raise ValueError("price must be between 0 to 100 ")

        discount=(price*discount_percentage)/100
        return round(price-discount,2)



# @pytest.mark.parametrize("discount_percentage,price",[(0.01,100),(0,200),(0.5,50)])
def test_calculate_discount():
    assert Calcuate.calculate_discount(10,100)==90.0