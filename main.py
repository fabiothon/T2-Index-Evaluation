# =============================================================================
# T2 INDEX EVALUATION
# =============================================================================

# DESCRIPTION
# This Python script generates a grouped bar chart visualizing the development
# of the T2 index over time after surgery, based on the cartilage zones
# ("deep," "global," and "superficial") as described by Trattnig et al. (2015).
# The T2 index provides insights into cartilage repair quality, with a 95%
# confidence interval (CI) as a measure of uncertainty.
# The data used includes post-surgery measurements at various time points
# (e.g., 12, 18, and 24 months) with an early post-surgery reference at 1 week.
# Error bars represent the 95% CI for the mean T2 index values, and the number
# of observations per category is displayed directly on the bars.
# The chart is divided into three cartilage zones for comparison, using distinct
# colors to differentiate between them, facilitating the assessment of cartilage
# repair outcomes over time.
# PLEASE NOTE: THIS CODE IS FOR EDUCATIONAL PURPOSES ONLY!
# Additional information is available in the README file.

# =============================================================================
# LIBRARIES
# =============================================================================
import pandas as pd
import plotly.graph_objects as go

# =============================================================================
# DATA IMPORT
# =============================================================================
df = pd.read_excel("/Users/fabiothon/Desktop/Code/T2_Index/data.xlsx")

# =============================================================================
# DATA SUMMARY
# =============================================================================
# Add annotation to the n column
df["n"] = df["n"].apply(lambda x: f'n = {x}')

# Calculation of the absolut CI values
df["yerr_lower"] = df["mean"] - df["lower_ci"]
df["yerr_upper"] = df["upper_ci"] - df["mean"]

# Dataframe separation based on the cartilage zone
df_deep = df[df["zone"] == "deep"]
df_global = df[df["zone"] == "global"]
df_superficial = df[df["zone"] == "superficial"]

# =============================================================================
# VISUALISATION
# =============================================================================
fig = go.Figure()

fig.add_trace(go.Bar(
    x = df_deep["visit"],
    y = df_deep["mean"],
    name = 'deep',
    text = df_deep["n"],
    textposition = "inside",
    insidetextanchor = "middle",
    error_y = dict(
        type = "data",
        array = df_deep["yerr_upper"].tolist(),  
        arrayminus = df_deep["yerr_lower"].tolist()  
    ),
    marker_color = '#E69F00'
))

fig.add_trace(go.Bar(
    x = df_global["visit"],
    y = df_global["mean"],
    name = "global",
    text = df_global["n"],
    textposition = "inside",
    insidetextanchor = "middle",
    error_y = dict(
        type = "data",
        array = df_global["yerr_upper"].tolist(),  
        arrayminus = df_global["yerr_lower"].tolist()  
    ),
    marker_color = '#000000'
))

fig.add_trace(go.Bar(
    x = df_superficial["visit"],
    y = df_superficial["mean"],
    name = "superficial",
    text = df_superficial["n"],
    textposition = "inside",
    insidetextanchor = "middle",
    error_y = dict(
        type = "data",
        array = df_superficial["yerr_upper"].tolist(),  
        arrayminus = df_superficial["yerr_lower"].tolist()
    ),
    marker_color = '#999999'
))

fig.update_layout(barmode = "group",
                title_text = "T<sub>2</sub> Index Development over Time after Surgery",
                xaxis_title = "Post-Surgery Period",
                yaxis_title = "Mean T<sub>2</sub> Index",
                legend_title = "Cartilage Zone")

fig.show()