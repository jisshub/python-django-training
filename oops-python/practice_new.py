class Jobs:
    aim = 'get paid'

    def __init__(self, salary):
        self.salary = salary


class Senior_Asst(Jobs):
    def job_info(self, post_name, salary):
        self.salary = salary
        self.post = post_name

    def features(self, HRA, TA):
        self.hra = HRA
        self.ta = TA


class Juniour_Asst(Senior_Asst, Jobs):
    def job_info(self, post_name, salary):
        self.salary = salary
        self.post = post_name

    def __str__(self):
        return self.aim

    def details(self):
        return f"My jobs is {self.post} and hav salary {self.salary}"

    @classmethod
    def change(cls, aim):
        cls.aim = aim
        return cls.aim

    @staticmethod
    def static():
        ans = input('Whether Satisfied in job?): ')
        # return ans
        if ans:
            return 'Ok'
        return 'Give any Comment'


adharsh = Juniour_Asst(30000)
