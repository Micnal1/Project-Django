import matplotlib.pyplot as plt, mpld3


def get_diagram(last_days_data, type_data='active'):
    if not last_days_data:
        return None
    y = last_days_data[type_data]
    x = last_days_data["time"]

    fig = plt.figure()
    plt.plot(x, y)

    return mpld3.fig_to_html(fig)

