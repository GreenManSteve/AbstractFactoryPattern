from autos.abs_auto import AbsAuto


class FordLincoln(AbsAuto):
    def start(self):
        print("Starting {}".format(self.__str__()))

    def stop(self):
        print("Stopping {}".format(self.__str__()))