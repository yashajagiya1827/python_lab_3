class company:
    def dis1(self):
        nm = "Y2C"
        city = "Rajkot"
        mobo = 7778935595
        print(f"Company Name :- {nm}\nCity :- {city}\nMobile Number :- {mobo}\n\n")

class employee(company):
    def dis2(self):
        empnm = "Yash Ajagiya"
        desig = "CEO"
        sal = 9000000
        print(f"Employee Name :- {empnm}\nDesignation :- {desig}\nSalary :- {sal}")

dis = employee()
dis.dis1()
dis.dis2()
