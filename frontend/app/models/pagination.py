class Pagination():
    def __init__(self, items, page=1, per_page=6):
        self.page = page
        self.per_page = per_page
        self.total = len(items)
        self.max_page = self.define_pages()
        self.items = self.paginate(items)

    def define_pages(self):
        if self.total <= self.per_page:
            return 1
        elif (self.total % self.per_page) == 0:
            return self.total // self.per_page
        else:
            return (self.total // self.per_page) + 1

    def paginate(self, items):
        try:
            if self.page > self.max_page:
                raise ValueError(f"Le nombre de page maximal est {self.total}")
            elif self.page == self.max_page:
                start = (self.page - 1) * self.per_page
                return items[start:]
            else:
                start = (self.page - 1) * self.per_page
                end = start + self.per_page
                return items[start: end]
        except ValueError as e:
            print(f"Erreur de numero de page : {e}")
            return None
