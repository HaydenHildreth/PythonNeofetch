import platform
import ctypes
import psutil


def foo():
    # UPTIME CALCULATIONS
    # getting the library in which GetTickCount64() resides
    lib = ctypes.windll.kernel32
    # calling the function and storing the return value
    t = lib.GetTickCount64()
    # since the time is in milliseconds i.e. 1000 * seconds
    # therefore truncating the value
    t = int(str(t)[:-3])
    # extracting hours, minutes, seconds & days from t
    # variable (which stores total time in seconds)
    mins, sec = divmod(t, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)
    # formatting the time in readable form
    # (format = x days, HH:MM:SS)
    os = platform.system()
    kernel = platform.platform()

    # PRINT STATEMENTS
    print('OS:', os)
    print('Kernel:', kernel)
    print(f"Uptime: {days} days, {hour:02}:{mins:02}:{sec:02}")  # Windows only?
    print('CPU:', platform.processor())
    print('GPU:', platform.processor())
    print('Memory:', psutil.virtual_memory().total)


if __name__ == '__main__':
    foo()

