import tkinter as tk
from typing import List, Callable


class OptionMenu(tk.Frame):
    """OptionMenu
    """

    def __init__(self, root, values: List[str],
                 callback: Callable[[], None] = None,
                 default_idx: int = 0, *args, **kwargs):
        """OptionMenu

        Args:
            root: root or frame where the option menu should be added
            values (List[str]): option menu values
            callback (Callable[[], None]): value change event
            default_idx (int): index of default value
        """
        super().__init__(root, *args, **kwargs)
        self._value = tk.StringVar(self, value=values[default_idx])
        if callback is not None:
            self.set_callback(callback)
        self._om = tk.OptionMenu(self, self._value, *values)
        self._om.config(width=15)
        self._om.pack()

    @property
    def value(self) -> str:
        """Get the option menu state/value
        """
        return self._value.get()

    def set_callback(self, callback: Callable[[], None]):
        """Set callback for value change
        """
        self._value.trace("w", callback)  # w -> write
