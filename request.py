class Request:
    def __init__(self, request_string):
        self.request_string = request_string
        request_list = request_string.split(' ')
        for index in range(len(request_list)):

            if request_list[index] == 'из':
                self._from = request_list[index + 1]
            if request_list[index] == 'в':
                self._to = request_list[index + 1]
            try:
                amount = int(request_list[index])
                self._amount = amount
                self._product = request_list[index + 1]
            except Exception:
                pass

    def get_source_string(self):
        return self.request_string

    def __repr__(self):
        return f"from - {self._from}\n" \
               f"to - {self._to}\n" \
               f"amount - {self._amount}\n" \
               f"product - {self._product}"

    @property
    def from_place(self):
        return self._from.lower()

    @property
    def to_place(self):
        return self._to.lower()

    @property
    def product_amount(self):
        return self._amount

    @property
    def product_title(self):
        return self._product.lower()


# req = Request('Доставить 3 печеньки из склад')
# print(req)
# print(req.product_amount)