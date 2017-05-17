from selenium import webdriver


class Driver(object):
    __instance = None

    @classmethod
    def get(cls, type='ff'):
        if not cls.__instance:
            cls.__instance = webdriver.Firefox()
        return cls.__instance


class BaseTest(object):
    pass
    # def teardown_class(self):
    #     Driver.get().close()
