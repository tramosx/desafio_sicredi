from src.question1 import Contract, Contracts


def test_contract():
    contract = Contract(1, 100.0)
    assert contract.id == 1
    assert contract.debt == 100.0
    assert str(contract) == 'id=1, debt=100.0'


def test_get_top_N_open_contracts():
    contracts = [Contract(i, i * 100.0) for i in range(1, 6)]
    renegotiated = [1, 3]
    contracts_instance = Contracts()
    max_debts_descending = contracts_instance.get_top_N_open_contracts(contracts, renegotiated, 3)
    assert max_debts_descending == [5, 4, 2]
