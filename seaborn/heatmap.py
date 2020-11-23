# サイズ変更
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
sns.set_context("notebook")
plt.figure(figsize=(20, 10))


df_corr = train.corr()
sns.heatmap(df_corr, vmax=1, vmin=-1, center=0)
