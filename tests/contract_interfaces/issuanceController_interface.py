from utils.deployutils import mine_tx

class IssuanceControllerInterface():
    def __init__(self, contract, name):
        self.contract = contract
        self.contract_name = name

        self.getSomeValue = lambda: self.contract.functions.getSomeValue().call()
        self.setSomeValue = lambda sender, someValue: mine_tx(
            self.contract.functions.setSomeValue(someValue).transact({'from': sender}), "setSomeValue", self.contract_name
        )
        self.buy = lambda sender, value: mine_tx(
            self.contract.functions.buy().transact({
                'from': sender,
                'value': value,
            }), "buy", self.contract_name
        )

