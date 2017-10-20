from configparser import ConfigParser
def cfgs():
    cfg = ConfigParser()
    cfg.read('config.ini')
    cfg.sections()
    return cfg
#if __name__ =='__main__':
    #cfgs()