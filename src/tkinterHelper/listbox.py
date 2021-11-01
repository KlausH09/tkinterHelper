import tkinter as tk
from typing import Callable, List
from collections import namedtuple

ListBoxItem = namedtuple('_Item', ['name', 'data'])


class ListBox(tk.Listbox):
    """ListBox
    """

    def __init__(self, root: tk.Frame, width: int = 55,
                 callback: Callable[[], None] = None,
                 *args, **kwargs):
        """ListBox

        Args:
            root (tk.Frame)
            width (int): listbox width
            callback (Callable[[], None]): select change event
        """
        super().__init__(root, *args, width=width, **kwargs)
        self._itemdata = {}

        if callback is not None:
            self.set_callback(callback)

    def clear_list(self):
        """Clear all items of the tree
        """
        self.delete(0, tk.END)
        self._itemdata = {}

    def add_item(self, name: str, value=None):
        """Add a tree item

        Args:
            name (str): name of the item
            value (Any): additional item data
        """
        if name in self._itemdata:
            raise ValueError(f"item '{name}' already exists")
        self.insert(tk.END, name)
        self._itemdata[name] = value

    @property
    def value(self) -> List[ListBoxItem]:
        """Get selected item
        """
        try:
            name = self.selection_get()
        except Exception:
            return []

        data = self._itemdata.get(name, None)
        return [ListBoxItem(name, data)]

    def set_callback(self, callback: Callable[[], None]):
        """Set callback for selecting an item
        """
        self.bind('<ButtonRelease-1>', callback)
