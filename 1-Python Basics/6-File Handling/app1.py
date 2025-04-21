##logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%Y-%m-%d %H:%M:%S',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers = [
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithmeticApp")

def add(a,b):
    return result

def subtract(a,b):
    result = a-b
    logger.debug(f"Subtracting {a}-{b}={result}") 
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f"Multiplying {a}*{b} = {result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Dividing{a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
add(10,15)
subtract(26,8)
multiply(3,4)
divide(10,2)

