import tkinter as tk
from typing import Callable, Union
from enum import IntEnum


class EditField(tk.Frame):
    """EditField
    """
    class ElementType(IntEnum):
        Checkbox = 1
        Editfield = 2

    def __init__(self, root: tk.Frame, name: str,
                 value: Union[bool, int, float, str],
                 callback: Callable[[], None] = None,
                 *args, **kwargs):
        """Editfield

        Args:
            root (tk.Frame): root or frame where the edit field should be added
            name (str): label of the edit field
            value (Union[bool, int, float, str]): default value
            callback (Callable[[], None]): value change event
         """
        super().__init__(root, *args, **kwargs)
        self._varname = name

        if isinstance(value, bool):
            self._elementType = self.ElementType.Checkbox
            # checkbox
            self._value = tk.IntVar(self, value=int(value))
            self._element = tk.Checkbutton(self, variable=self._value,
                                           text=name)
            self._element.pack()
        else:
            self._elementType = self.ElementType.Editfield
            # entry field
            tmp = {
                int: tk.IntVar,
                float: tk.DoubleVar,
                str: tk.StringVar,
            }
            self._value = tmp[type(value)](self, value=value)
            self._element = tk.Entry(self, textvariable=self._value, width=10)
            if name:
                self._element.pack(side="right")
                labelText = tk.StringVar(self, value=name)
                labelDir = tk.Label(self, textvariable=labelText)
                labelDir.pack(side="right", fill='x')
            else:
                self._element.pack()

        if callback is not None:
            self.set_callback(callback)

    @property
    def value(self) -> Union[bool, int, float, str]:
        """Get the edit field value
        """
        return self._value.get()

    @value.setter
    def value(self, value: Union[bool, int, float, str]):
        """Set the edit field value
        """
        self._value.set(value)

    @property
    def name(self) -> str:
        """Name of the edit field
        """
        return self._varname

    def set_callback(self, callback: Callable[[], None],
                     callback_at_return: bool = True):
        """Set callback for value change

        Args
            callback (Callable[[], None]): value change event
            callback_at_return (bool): if 'True', the callback will called when
                                       the user types <Return> in the edit
                                       field. If 'False', the callback will
                                       called at each value change (typing).
                                       This options has no effect for checkbox.
        """
        if self._elementType == self.ElementType.Checkbox:
            self._value.trace("w", callback)  # w -> write
        elif self._elementType == self.ElementType.Editfield:
            if callback_at_return:
                self._element.bind("<Return>", callback)
            else:
                self._value.trace("w", callback)  # w -> write
        else:
            raise NotImplementedError()
