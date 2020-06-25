# To check the usage of the lamdna functions

def lambda_adder(base_value, add_on):
    lambda_adder_excuter = lambda base:base + base_value
    result = lambda_adder_excuter(add_on)
    return result

if __name__ == "__main__":
    base_value = int(input("Enter the base number: "))
    add_on = int(input("Enter value to add on: "))
    result = lambda_adder(base_value, add_on)
    print(result)