from collections import Counter

def receipt_content(prices_filename, cash_register_filename):
    """Construct contents of a receipt of the cash register events,
    given the store prices."""

    total = 0

    #Get prices from file to dict
    prices_dict = {}
    with open(prices_filename, "r", encoding="utf-8") as file:
        for line in file.read().splitlines():
            data = line.split(";")
            prices_dict[data[0]] = float(data[1])

    #Get register activity from file to dict
    register_dict = {"buy":[], "return":[], "pay":[]}
    with open(cash_register_filename, "r", encoding="utf-8") as file:
        for line in file.read().splitlines():
            data = line.split(";")
            register_dict[data[0]].append(data[1])

    #Get amount, name and total price for each item
    bought = []
    counted_sorted_bought = sorted(Counter(register_dict["buy"]).items())
    for item in counted_sorted_bought:
        price = item[1] * prices_dict[item[0]]
        bought.append((item[1], item[0], price))
        total += float(price)

    #Get amount, name and total return price for each returned item
    returned = []
    counted_sorted_returned = sorted(Counter(register_dict["return"]).items())
    for item in counted_sorted_returned:
        price = -item[1] * prices_dict[item[0]]
        returned.append((-item[1], item[0], price))
        total += float(price)

    vat = round(total - total / 1.25, 2)
    paid = float(register_dict["pay"][0])
    change = total - paid

    return (bought + returned, format(total, ".2f"), vat, format(paid, ".2f"), format(change, ".2f"))


def receipt(prices_filename, cash_register_filename):
    """Construct a receipt of the cash register events,
    given the store prices."""

    # get receipt content from receipt_content()
    purcases_returns, total, vat, payment, change = receipt_content(
        prices_filename, cash_register_filename
    )

    # the formatted lines of the receipt
    receipt_lines = [f"{'Nr.':>4}  {'Item':18}  {'Price':>10}"]

    for nr, item, price in purcases_returns:
        receipt_lines.append(f"{nr:4d}  {item:18}  {price:10.2f}")

    receipt_lines.append(f"Total: {total}")
    receipt_lines.append(f"Of which VAT: {vat:.2f}")
    receipt_lines.append(f"Payment: {payment}")
    receipt_lines.append(f"Change {change}")

    # add some dividers
    max_len = max(len(line) for line in receipt_lines)
    divider = "-" * max_len
    receipt_lines.insert(1, divider)
    receipt_lines.insert(-4, divider)
    receipt_lines.insert(-2, divider)

    return "\n".join(receipt_lines)

print("Tester receipt... ", end="")
expected_value = """\
 Nr.  Item                     Price
------------------------------------
   2  apple                    10.00
   1  chips                    24.30
   1  dish soap                26.20
   1  frozen pizza             54.40
   1  peanuts                  18.50
   1  toilet paper             34.00
   3  tomato                   30.00
  -1  pocket book            -149.00
  -1  toothpaste              -13.70
------------------------------------
Total: 34.70
Of which VAT: 6.94
------------------------------------
Payment: 100.00
Change -65.30"""
assert(expected_value == receipt("prices.txt", "cash_register.txt"))
print("OK")
