class Paginator:
    def __init__(self, items, per_page=10):
        self.items = list(items)
        self.per_page = per_page
        self.total = len(self.items)
        self.total_pages = ((self.total - 1)//per_page) + 1

    def get_page(self, page_num):
        if page_num < 1:
            page_num = 1
        elif page_num > self.total_pages:
            page_num = self.total_pages

        start = (page_num - 1) * self.per_page
        end = start + self.per_page
        current_items = self.items[start:end]

        return {
            "items": current_items,
            "current_page": page_num,
            "total_pages": self.total_pages,
            "per_page": self.per_page,
            "total_items": self.total
        }

    def next(self, current_page):
        if current_page < self.total_pages:
            return self.get_page(current_page + 1), True
        return self.get_page(current_page), False
    
    def prev(self, current_page):
        if 1 < current_page <= self.total_pages:
            return self.get_page(current_page - 1), True
        return self.get_page(current_page), False
    
    def quit(self):
        raise StopIteration