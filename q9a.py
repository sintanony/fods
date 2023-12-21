# Importing library
from scipy.stats import f_oneway

# Performance when each of the engine oil is applied
performance1 = [89, 89, 88, 78, 79]
performance2 = [93, 92, 94, 89, 88]
performance3 = [89, 88, 89, 93, 90]
performance4 = [81, 78, 81, 92, 82]

# Conduct the one-way ANOVA
f_statistic, p_value = f_oneway(performance1, performance2, performance3, performance4)

# Analyze the result
print(f'F Statistic: {f_statistic}')
print(f'P-value: {p_value}')

# Check if the p-value is less than 0.05
if p_value < 0.05:
    print('Reject the null hypothesis. There is a significant difference in performance among the engine oils.')
else:
    print('Fail to reject the null hypothesis. There is not enough evidence to suggest a significant difference in performance.')