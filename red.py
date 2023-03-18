class Auto:

    @staticmethod
    def get_class_info1():
        print('Детальная информация о классе')

    def get_class_info2(self):
        print('Детальная информация о классе')


if __name__ == '__main__':
    a = Auto()
    a.get_class_info1()
