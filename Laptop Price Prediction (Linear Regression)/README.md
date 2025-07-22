
# Laptop Price Prediction Analysis

## Summary of Notebook Analysis


Summary of Notebook Analysis:

1.  **Data Loading and Exploration:** The analysis began by loading the 'Laptop_price.csv' dataset into a pandas DataFrame. Initial exploration involved displaying the first few rows and checking the data types and non-null counts using `.head()` and `.info()`. The dataset contains 1000 entries with 7 columns: 'Brand', 'Processor_Speed', 'RAM_Size', 'Storage_Capacity', 'Screen_Size', 'Weight', and 'Price'. A check for null values confirmed that there were no missing entries in any column. Descriptive statistics were generated using `.describe()`, providing insights into the central tendency, dispersion, and shape of the numerical features.

2.  **Visualization:** Histograms were plotted for all numerical features ('Processor_Speed', 'RAM_Size', 'Storage_Capacity', 'Screen_Size', 'Weight', and 'Price') to visualize their distributions. Scatter plots were then created to explore the relationships between each of the independent numerical variables and the target variable, 'Price'. These plots visually suggested positive relationships between 'Price' and 'Processor_Speed', 'RAM_Size', and 'Storage_Capacity', while the relationships with 'Screen_Size' and 'Weight' appeared less clear.

3.  **Correlation Analysis:** A correlation matrix was computed for all numerical features to quantify the linear relationships between them. A heatmap was used to visualize this matrix. The analysis of the correlation matrix revealed a very strong positive linear correlation (approximately 0.998) between 'Storage_Capacity' and 'Price'. 'RAM_Size' showed a weak positive correlation, while 'Processor_Speed', 'Screen_Size', and 'Weight' had very weak or negligible correlations with 'Price'. This confirmed the visual findings from the scatter plots, highlighting 'Storage_Capacity' as the dominant feature linearly related to price in this dataset.

4.  **Model Building:** A linear regression model was built to predict laptop prices. The numerical features ('Processor_Speed', 'RAM_Size', 'Storage_Capacity', 'Screen_Size', 'Weight') were selected as independent variables (X), and 'Price' was selected as the target variable (y). The dataset was split into training (80%) and testing (20%) sets using `train_test_split`. A `LinearRegression` model was initialized and trained on the training data.

5.  **Model Evaluation:** The trained model was used to make predictions on the test set. The actual and predicted prices were visualized using a scatter plot and displayed in a DataFrame for comparison. The model's performance was evaluated using Mean Squared Error (MSE) and R-squared (R2) score. The MSE was approximately 32031.54, and the R2 score was approximately 0.9996. The exceptionally high R2 score indicates that the model explains about 99.96% of the variance in laptop prices, largely attributed to the strong correlation between 'Storage_Capacity' and 'Price'.


## Further Steps or Insights

Based on the analysis and the strong performance of the linear regression model (largely driven by the high correlation of Storage Capacity with Price), here are some potential further steps and insights:

*   **Explore Other Algorithms:** While linear regression performed well, exploring other regression algorithms like Random Forest, Gradient Boosting, or even simple models focusing primarily on Storage Capacity could provide comparative performance metrics or reveal different aspects of the data's structure.
*   **Feature Engineering:** Investigate creating interaction terms between features (e.g., RAM size and Processor Speed) to see if combined factors have a significant impact beyond their individual effects. Polynomial features could also be explored if any non-linear relationships are suspected, although the current data suggests strong linearity with Storage Capacity.
*   **Include Categorical Features:** Incorporate the 'Brand' categorical feature into the model using one-hot encoding to assess if specific brands command a price premium or discount after accounting for the numerical specifications.
*   **Regularization:** Apply regularization techniques like Lasso Regression to see if they can help identify which features (beyond Storage Capacity) contribute most significantly to the price, potentially simplifying the model and providing clearer insights into feature importance.
*   **Gather More Diverse Data:** If the goal is to build a model generalizable to a wider market, acquiring a dataset with more varied relationships between features and price, or with a larger number of observations, would be beneficial. The current dataset's strong correlation between Storage Capacity and Price might be a specific characteristic of the data source.
*   **Outlier Analysis:** Conduct a formal outlier analysis to understand if any extreme data points are disproportionately influencing the model, particularly given the strong linear relationship observed.

These steps can help refine the model, gain deeper insights into the factors influencing laptop prices, and build a more robust predictive tool.
