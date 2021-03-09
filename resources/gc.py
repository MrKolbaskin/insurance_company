import copy

def gc_contracts(contracts):
    res = {}
    for key in contracts:
        res[key] = [contract for contract in contracts[key] if contract.duration]
    return res