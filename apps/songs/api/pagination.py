from typing import Optional

from rest_framework.pagination import PageNumberPagination


class OnlyNumbersPagination(PageNumberPagination):
    def get_next_link(self) -> Optional[int]:
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()
        return page_number

    def get_previous_link(self) -> Optional[int]:
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()
        if page_number == 1:
            return None
        return page_number
