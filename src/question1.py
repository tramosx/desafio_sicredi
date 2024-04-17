class Contract:
    def __init__(self, id: int, debt: float):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:
    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        contract_not_reneg = []
        ids_top_debts = []

        for contract in open_contracts:
            if contract.id not in renegotiated_contracts:
                contract_not_reneg.append(contract)

        contract_not_reneg.sort(key=lambda contract: contract.debt, reverse=True)

        for contract in contract_not_reneg[:top_n]:
            ids_top_debts.append(contract.id)

        return ids_top_debts
