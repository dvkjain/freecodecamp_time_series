import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"])
df.set_index("date", inplace=True)

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) &
        (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = df["value"].plot(color="red")

    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")



    fig = plt.gcf()
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')

    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df["year"] = df.index.year
    df["month"] = df.index.month
    df["day"] = df.index.day

    month_average = df.groupby(["year", "month"])["value"].mean().reset_index(name="average_page_views")

    # Draw bar plot
    custom_palette = sns.color_palette("Paired", n_colors=12)
    fig = sns.barplot(data=month_average, x="year", y="average_page_views", hue="month", palette=custom_palette)
    handles, labels = fig.get_legend_handles_labels()
    plt.legend(handles=handles, labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], title="Months")
    plt.xlabel("Year")
    plt.ylabel("Average Page Views")
    plt.title("Average Daily Page Views for Each Month Grouped by Year")


    fig = plt.gcf()
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    fig = sns.boxplot(x='year', y='value', data=df_box)
    plt.title('Year-wise Box Plot (Trend)')
    plt.ylabel('Page Views')
    plt.xlabel('Year')

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    plt.subplot(1, 2, 2)
    fig = sns.boxplot(x='month', y='value', data=df_box, order=months)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.ylabel('Page Views')
    plt.xlabel('Month')


    fig = plt.gcf()
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')

    return fig
