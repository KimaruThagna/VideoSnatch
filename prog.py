import time,progressbar


non_interactive_sleep_factor = 100


def sleep(delay):
    '''Make non-interactive examples faster by a factor'''
    if __name__ != '__main__':
        delay /= non_interactive_sleep_factor
    time.sleep(delay)


def basic_widget_example():
    widgets = [progressbar.Percentage(), progressbar.Bar()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
    for i in range(100):
        # do something
        sleep(0.1)
        bar.update(i + 1)
    bar.finish()

def double_bar_example():
    widgets = [
        progressbar.Bar('>'), ' ',
        progressbar.ETA(), ' ',
        progressbar.ReverseBar('<'),
    ]
    bar = progressbar.ProgressBar(widgets=widgets).start()
    for i in range(100):
        # do something
        bar.update(i + 1)
        sleep(0.5)

    bar.finish()
double_bar_example()