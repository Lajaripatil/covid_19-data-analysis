import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")


# Load dataset
df = pd.read_csv(r"C:\Users\lajar\Desktop\word data\Anudip ACPCE\covid_19_clean_complete.csv")

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# ---------------- GRAPH 1 -----------------
# Monthly confirmed cases (LINE GRAPH)
monthly_cases = df.resample('M', on='Date')['Confirmed'].sum()

plt.figure(figsize=(8,4))
plt.plot(monthly_cases.index, monthly_cases.values)
plt.title("Monthly Confirmed COVID-19 Cases")
plt.xlabel("Month")
plt.ylabel("Total Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------- GRAPH 2 -----------------
# Daily new case distribution (HISTOGRAM)
if 'Daily New Cases' in df.columns:
    plt.figure(figsize=(8,4))
    plt.hist(df['Daily New Cases'].dropna(), bins=20)
    plt.title("Distribution of Daily New Cases")
    plt.xlabel("New Cases")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# ---------------- GRAPH 3 -----------------
# Top 10 countries by confirmed cases (BAR GRAPH)
country_cases = df.groupby('Country/Region')['Confirmed'].max().sort_values(ascending=False).head(10)

plt.figure(figsize=(8,4))
plt.bar(country_cases.index, country_cases.values)
plt.title("Top 10 Countries by Total Confirmed Cases")
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------- GRAPH 4 -----------------
# Confirmed vs Deaths (SCATTER PLOT)
plt.figure(figsize=(8,4))
plt.scatter(df['Confirmed'], df['Deaths'], s=10)
plt.title("Confirmed vs Deaths")
plt.xlabel("Confirmed Cases")
plt.ylabel("Deaths")
plt.tight_layout()
plt.show()

# ---------------- GRAPH 5 -----------------
# Active cases trend (LINE GRAPH)
daily_active = df.groupby('Date')['Active'].sum()

plt.figure(figsize=(8,4))
plt.plot(daily_active.index, daily_active.values)
plt.title("Daily Active Cases Trend")
plt.xlabel("Date")
plt.ylabel("Active Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------- GRAPH 6 -----------------
# WHO region-wise cases (PIE CHART)
region_cases = df.groupby('WHO Region')['Confirmed'].sum()

plt.figure(figsize=(6,6))
plt.pie(region_cases.values, labels=region_cases.index, autopct="%1.1f%%")
plt.title("WHO Region-wise Confirmed Cases")
plt.tight_layout()
plt.show()

# ---------------- GRAPH 7 -----------------
# Deaths over time (LINE GRAPH)
daily_deaths = df.groupby('Date')['Deaths'].sum()

plt.figure(figsize=(8,4))
plt.plot(daily_deaths.index, daily_deaths.values)
plt.title("Daily COVID-19 Deaths Trend")
plt.xlabel("Date")
plt.ylabel("Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------- GRAPH 8 -----------------
# Top 10 recovered countries (BAR GRAPH)
top_recovered = df.groupby('Country/Region')['Recovered'].max().sort_values(ascending=False).head(10)

plt.figure(figsize=(8,4))
plt.bar(top_recovered.index, top_recovered.values)
plt.title("Top 10 Countries by Recovered Cases")
plt.xlabel("Country")
plt.ylabel("Recovered")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
