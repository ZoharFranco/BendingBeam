from sympy.plotting import plot


def customized_plot(x, y, title, label, y_axis,x_axis, length):

    p1 = plot(y,  (x, 0, length), show=False, title=title, label=label, ylabel=y_axis, xlabel=x_axis,  legend=True)

    # Show the plot
    p1.show()


def customized_plots(y, title, label, y_axis, x_axis):

    p2 = plot(show=False, title=title, label=label, ylabel=y_axis, xlabel=x_axis )

    for i in range(len(y)):
        p1 = plot(y[i][0], y[i][1], show=False,)
        p2.append(p1[0])

    # Show the plot
    p2.show()
