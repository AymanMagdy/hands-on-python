# To check the usage of the lamdna functions

def lambda_multplier(factorX, factorY):
    lambda_multplier_excuter = lambda factorX, factorY: factorX * factorY
    result = lambda_multplier_excuter(factorX, factorY)
    return result

if __name__ == "__main__":
    valueX = int(input("Enter the value x number: "))
    valueY = int(input("Enter the value y number: "))
    result = lambda_multplier(valueX, valueY)
    print(result)