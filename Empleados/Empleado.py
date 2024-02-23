class Empleado:
    #aqui va el codigo

    """--------------------------------------------------------------------
    # Atributos
    --------------------------------------------------------------------"""

    nombre=""
    apellido=""

    """--------------------------------------------------------------------
    # 1 = Masculino y 2 = Femenino
    --------------------------------------------------------------------"""
    sexo=0
    salario=0

    """---------------------------------------------------------------------
    #   Mtetodos
    ---------------------------------------------------------------------"""
    def CambiarSalario(self,nSalario):
        #aqui va el codigo
        self.salario = nSalario
        return "Su nuevo salario es:" + self.salario
    
    def ConsultarSalario(self):
        return self.salario
    
    def AumentoSalarial(self):
        aumento = self.salario*0.05
        nSalario = self.salario+aumento
        self.salario = nSalario
        return "Su nuevo salario es:" + self.salario