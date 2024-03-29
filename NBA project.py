import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

# import dataframe sourced from 538’s Analysis of the Complete History Of The NBA
nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

# create DataSeries of points each team scored in their games in 2010
knicks_pts = nba_2010.pts[nba_2010.fran_id == 'Knicks']
nets_pts = nba_2010.pts[nba_2010.fran_id == 'Nets']

# calculate the difference between the two teams' average to estimate, if one team was more successful than another
diff_means_2010 = knicks_pts.mean() - nets_pts.mean()
print(diff_means_2010)

# create overlapping histograms of points of each team to analyze deeper the success of each team
plt.hist(knicks_pts, color='blue', label = 'Knicks', normed = True, alpha = 0.5)
plt.hist(nets_pts, color='green', label = 'Nets', normed = True, alpha = 0.5)
plt.legend()
plt.title('2010 Season')
plt.show()
plt.clf()

# repeat the same for two teams in 2014, create DataSeries of points in 2014
knicks_pts_2014 = nba_2014.pts[nba_2014.fran_id == 'Knicks']
nets_pts_2014 = nba_2014.pts[nba_2014.fran_id == 'Nets']

# calculate the difference between means in 2014
diff_means_2014 = knicks_pts_2014.mean() - nets_pts_2014.mean()
print(diff_means_2014)

# create overlapping histograms of points in 2014
plt.hist(knicks_pts_2014, color='red', label = 'Knicks', normed = True, alpha = 0.5)
plt.hist(nets_pts_2014, color='green', label = 'Nets', normed = True, alpha = 0.5)
plt.legend()
plt.title('2014 Season')
plt.show()
plt.clf()

# create side-by-side boxplots of points of each team (there are 5 of them) and compare, if the team and points are associated
sns.boxplot(data = nba_2010, x = 'fran_id', y = 'pts')
plt.title('2010')
plt.show()
plt.clf()

# calculate a contingency table of frequencies to determine if there are association between the game location (home or away) and game result (win or lose)
location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)

# calculate a contingency table of proportions to make numbers look better for humans
location_result_proportions = location_result_freq/len(nba_2010)
print(location_result_proportions)

# calculate expected values in contingency table and then using chi square test check if the difference between expected and actual data is signifficant
chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)

# calculate covariance of forecasted win probability and point difference
point_diff_forecast_cov = np.cov(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_cov)

# calculate linear correlation between forecasted win prob and point difference to see, if there is association
point_diff_forecast_corr, p = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_corr)

# create scatter plot of these values to see association (or no association) visually
plt.scatter(x = nba_2010.forecast, y = nba_2010.point_diff)
plt.xlabel('Forecast')
plt.ylabel('Point difference')
plt.show()
plt.clf()