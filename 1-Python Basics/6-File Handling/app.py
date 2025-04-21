import logging 

# logging setting
logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s - %(name)s-%(levelname)s - %(message)s',
    datefmt='%Y-%M-%D %H:%m:%s',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)
logger=logging.getLogger("ArithmethicApp")


def add(a,b):
    result=a+b 
    logger.debug(f"Adding{a}+{b}",result)
    return result

def multiply(a,b):
    result=a*b 
    logger.debug(f"Multiplying {a}*{b}",result)
    return result

def subtract(a,b):
    result=a-b 
    logger.debug(f"Subtracting{a}-{b}",result)
    return result

add(10,15)
multiply(15,20)
subtract(10,20)