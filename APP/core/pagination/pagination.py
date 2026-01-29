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
        result = {"page_num":current_page, "can_move": False, "error": None}
        if current_page < self.total_pages:
            result["page_num"] = current_page + 1
            result["can_move"] = True
        else:
            result["error"] = f"No more pages in that direction."
        return result
    
    def prev(self, current_page):
        result = {"page_num":current_page, "can_move": False, "error": None}
        if 1 < current_page <= self.total_pages:
            result["page_num"] = current_page - 1
            result["can_move"] = True
        else:
            result["error"] = f"No more pages in that direction."
        return result

    def quit(self):
        raise StopIteration