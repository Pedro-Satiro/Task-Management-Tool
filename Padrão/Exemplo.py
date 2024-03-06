from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

# Definindo o abstract handler
# Definindo a Forma de como os handlers devem ser criados, tipo forma de bolo
class PurchaseHandler(ABC):
    def __init__(self) -> None:
        self.successor: Optional[PurchaseHandler] = None

    @abstractmethod
    def handle_request(self, amount: float) -> Optional[str]:
        raise NotImplementedError("Must implement handle_request method")

    def set_successor(self, successor: PurchaseHandler) -> None:
        self.successor = successor

# Criação de handlers já com suas regras de negócio, tipo bolo de chocolate, bolo de morango 
class ManagerHandler(PurchaseHandler):
    def handle_request(self, amount: float) -> Optional[str]:
        if amount <= 1000:
            return f"Approved by Manager. Amount: ${amount}"
        elif self.successor:
            # Se o valor for maior que 1000, passa para o seu handler sucessor
            return self.successor.handle_request(amount)
        else:
            return None

class DirectorHandler(PurchaseHandler):
    def handle_request(self, amount: float) -> Optional[str]:
        if amount <= 5000:
            return f"Approved by Director. Amount: ${amount}"
        elif self.successor:
            # Se o valor for maior que 5000, passa para o seu handler sucessor
            return self.successor.handle_request(amount)
        else:
            return None

class CEOHandler(PurchaseHandler):
    def handle_request(self, amount: float) -> Optional[str]:
        if amount <= 10000:
            return f"Approved by CEO. Amount: ${amount}"
        elif self.successor:
            # Se o valor for maior que 10000, passa para o seu handler sucessor
            return self.successor.handle_request(amount)
        else:
            return None

# Codigo do cliente (main de onde o programa é executado)
def client_code(handler: PurchaseHandler, amounts: list[float]) -> None:
    for amount in amounts:
        result = handler.handle_request(amount)
        if result is not None:
            print(result)
        else:
            # Se não houver aprovação para o valor, imprime a mensagem
            print(f"No approval found for amount: ${amount}")

if __name__ == "__main__":
    # Cria os handlers e define seus successors
    manager = ManagerHandler()
    director = DirectorHandler()
    ceo = CEOHandler()
    manager.set_successor(director)
    director.set_successor(ceo)

    # Envio de valores para aprovação dos clientes
    purchase_amounts = [500, 1500, 6000, 12000]
    client_code(manager, purchase_amounts)