from configparser import ConfigParser

def readData(section,key):
    config=ConfigParser()
    config.read('/Users/kavyavijay/PycharmProjects/pythonProject1/ConfigFiles/Config.cfg')
    return config.get(section,key)

def elementsData(section,key):
    config = ConfigParser()
    config.read('/Users/kavyavijay/PycharmProjects/pythonProject1/ConfigFiles/Elements.cfg')
    return config.get(section, key)