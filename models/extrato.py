class Extrato:
    def __init__(self, Data_Movimento, Valor, Tipo_Movimento, Categoria, Descricao, Futuro):
        self.Data_Movimento = Data_Movimento
        self.Valor = Valor
        self.Tipo_Movimento = Tipo_Movimento
        self.Categoria = Categoria
        self.Descricao = Descricao
        self.Futuro = Futuro
        
    def ToJSON(self):
        json_string = '{"Data_Movimento": {"__type": "Date", "iso": "' + str(self.Data_Movimento) + 'T00:00:00.000Z"},' + \
                        ' "Valor": ' + self.Valor + ',' + \
                        ' "Tipo_Movimento": "' + self.Tipo_Movimento + '",' + \
                        ' "Categoria": "' + self.Categoria + '",' + \
                        ' "Descricao": "' + self.Descricao + '",' + \
                        ' "Futuro": ' + str(self.Futuro).lower() + '}'
                        
        return json_string
        