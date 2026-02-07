from APP.core.pagination.pagintaion_result import Pagination_result

class Paginator:
    def __init__(self, items, per_page=10):
        self.items = list(items)
        self.per_page = per_page
        self.total = len(self.items)
        self.total_pages = ((self.total - 1)//per_page) + 1

    def get_page(self, page_num):
        res = Pagination_result()

        if page_num < 1:
            page_num = 1

        elif page_num > self.total_pages:
            page_num = self.total_pages

        start = (page_num - 1) * self.per_page
        end = start + self.per_page
        current_items = self.items[start:end]

        res.payload["items"] = current_items
        res.payload["curt_page"] = page_num

        res.meta["per_page"] = self.per_page
        res.meta["total_items"] = self.total
        res.meta["total_pages"] = self.total_pages

        return res.success()

    def next(self, curt_Page):
        res = Pagination_result()

        if curt_Page < self.total_pages:
            res.payload["curt_page"] = curt_Page + 1
            res.meta["can_move"] = True

        else:
            return res.fail("No more pages in that direction.")
        return res.success()
    
    def prev(self, curt_Page):
        res = Pagination_result()

        if 1 < curt_Page <= self.total_pages:
            res.payload["curt_page"] = curt_Page - 1
            res.meta["can_move"] = True

        else:
            return res.fail("No more pages in that direction.")
        return res.success()

    def quit(self):
        raise StopIteration