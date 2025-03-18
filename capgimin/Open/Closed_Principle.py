from abc import abstractmethod,ABC

class Paymenthmethod(ABC):
    @abstractmethod
    def pay(self):
        pass
class CreditcardPayment(Paymenthmethod):
    def pay(self):
        print("proceesing the cread card payment")

class PayPalPayment(Paymenthmethod):
    def pay(self):
        print("process the pay pal payment")

def process_payment(payment:Paymenthmethod):
    payment.pay()

credit_payment = CreditcardPayment()
paypal_payment = PayPalPayment()

process_payment(credit_payment)  # Output: Processing the credit card payment
process_payment(paypal_payment)
