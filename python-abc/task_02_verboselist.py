#!/usr/bin/env python3
"""
VerboseList sinfi üçün modul.
Bu sinif list sinfini genişləndirir və hər əməliyyatda mesaj çap edir.
"""


class VerboseList(list):
    """Siyahıya element əlavə edildikdə və ya silindikdə bildiriş verir."""

    def append(self, item):
        """Element əlavə edir və bildiriş çap edir."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Siyahını genişləndirir və neçə element əlavə edildiyini çap edir."""
        items_count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(items_count))

    def remove(self, item):
        """Elementi silməzdən əvvəl bildiriş çap edir."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Elementi çıxarmazdan əvvəl bildiriş çap edir."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
