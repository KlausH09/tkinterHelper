import tkinter as tk
from abc import ABC, abstractmethod, abstractclassmethod
from typing import Union, Iterable


class ElementHidder:
    """Helper class to show/hide frames, editboxes, buttons, ...
    """

    class _Item(ABC):
        """Helper class to get grid/pack information and grid/pack elements
        """
        @abstractmethod
        def __init__(self, frame: tk.Frame):
            pass

        @abstractclassmethod
        def isValid(cls, frame: tk.Frame):
            pass

        @abstractmethod
        def hide(self):
            pass

        @abstractmethod
        def show(self):
            pass

    class _ItemGrid(ABC):
        def __init__(self, frame: tk.Frame):
            self._frame = frame
            self._settings = frame.grid_info()

        @classmethod
        def isValid(cls, frame: tk.Frame):
            try:
                return len(frame.grid_info()) > 0
            except Exception:
                return False

        def hide(self):
            self._frame.grid_forget()

        def show(self):
            self._frame.grid(self._settings)

    class _ItemPack(ABC):
        def __init__(self, frame: tk.Frame):
            self._frame = frame
            self._settings = frame.pack_info()

        @classmethod
        def isValid(cls, frame: tk.Frame):
            try:
                return len(frame.pack_info()) > 0
            except Exception:
                return False

        def hide(self):
            self._frame.pack_forget()

        def show(self):
            self._frame.pack(self._settings)

    def __init__(self, *frames: tk.Frame):
        """Helper class to show/hide frames, editboxes, buttons, ...

        Args:
            frames (List[tk.Frame]): list of frames
        """
        self._frames = []
        self.add(frames)

    @classmethod
    def _get_item_classes(cls):
        return (cls._ItemGrid, cls._ItemPack)

    def add(self, frame: Union[tk.Frame, Iterable[tk.Frame]]):
        """Add a frame, editbox, button, ...
        """
        if isinstance(frame, Iterable):
            for f in frame:
                self.add(f)
            return

        c = [c for c in self._get_item_classes() if c.isValid(frame)]
        if len(c) == 0:
            raise ValueError("No packing information. "
                             "Call 'frame.pack()' or 'frame.grid()'")
        elif len(c) != 1:
            raise RuntimeError()
        c = c[0]
        self._frames.append(c(frame))

    def show(self):
        """Show all elements
        """
        for f in self._frames:
            f.show()

    def hide(self):
        """Hide all elements
        """
        for f in self._frames:
            f.hide()
