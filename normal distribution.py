from scipy.stats import truncnorm
import matplotlib.pyplot as plt
%matplotlib notebook

def get_truncated_normal(mean=1, sd=1, low=-3, upp=7):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


X1 = sorted(get_truncated_normal().rvs(10000))
mean, std = stats.norm.fit(X1, loc=0)
pdf_norm = stats.norm.pdf(X1, mean, std)


fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(X1, pdf_norm)

ax.fill_between(X1, 0, pdf_norm,
                where=(np.array(X1)>-1) & (np.array(X1)<=3),
                facecolor='lightgrey')
# ax.fill_betweenx(pdf_norm, 2, x2=7, interpolate=True)