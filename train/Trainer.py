import random
from abc import ABC, abstractmethod
from faker import Faker
from datetime import  datetime

fakeUtils = Faker()


class Trainer(ABC):
    def __init__(self,model,config:dict):
        self.model = model
        self.config = config

    @abstractmethod
    def start_train(self,*args,**kwargs):
        raise NotImplemented('start train not implemented')

    @abstractmethod
    def get_predict(self,*args,**kwargs):
        raise NotImplemented('get  predict not implemented')

    @staticmethod
    def get_fake(types,size):
        fake = []
        for i in range(size):
            for t in types:
                if t == 'float':
                    fake.append(random.random())
                elif t == 'datetime':
                    fake_date = fakeUtils.date_time().strftime('%Y-%m-%d %H:%M:%S')
                    fake.append(fake_date)
                else:
                    pass

        return fake

    @abstractmethod
    def write_to_db(self,config:dict|None):
        raise NotImplemented(' write to db not implemented')


class triformer(Trainer):
    def __init__(self, model, config):
        super().__init__(model, config)

    def start_train(self):
        print("start train")

    def get_predict(self):
        print("get predict")