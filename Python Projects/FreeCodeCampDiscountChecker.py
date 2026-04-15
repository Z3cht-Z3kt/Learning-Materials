def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return 'The price should be a number'
    elif not isinstance(discount, (int, float)):
        return 'The discount should be a number'
    elif price <= 0:
        return 'The price should be greater than 0'
    elif discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    elif isinstance(price, (int, float)) and isinstance(discount, (int, float)):
        total = price - (price * (discount / 100))
        if isinstance(price, int) and isinstance(discount, int):
            return(int(total))
        elif total <= 0:
            return(int(total))
        else:
            return(total)

print(apply_discount(200, 100))