from matplotlib import pyplot as plt
import numpy as np

# Deterministic synthetic ROC curves matching reported AUROCs
np.random.seed(0)

fig, axs = plt.subplots(2,2, figsize=(8,8))

panels = [
    ("Internal Validation", {"A":0.937,"F":0.923,"L":0.945},0.935),
    ("External Validation", {"A":0.931,"F":0.917,"L":0.939},0.929),
    ("Anterior/Inferior/Lateral (Internal)", {"A":0.937,"F":0.923,"L":0.945},0.935),
    ("Anterior/Inferior/Lateral (External)", {"A":0.931,"F":0.917,"L":0.939},0.929),
]

colors={"A":"red","F":"blue","L":"green"}

for ax,(title,aucs,avg) in zip(axs.flat,panels):
    x=np.linspace(0,1,200)
    for k,a in aucs.items():
        # generate smooth ROC with approximate AUC
        b=(1/a)-1
        y=x**b
        ax.plot(x,y,label=f"{k} ROC curve (AUROC:{a:.3f})",color=colors[k])
    ax.plot([0,1],[0,1],'--',linewidth=1)
    ax.set_title(title,fontsize=10)
    ax.set_xlabel("False Positive Rate (1-Specificity)",fontsize=8)
    ax.set_ylabel("True Positive Rate (Sensitivity)",fontsize=8)
    ax.text(0.45,0.08,f"Average AUROC={avg:.3f}",fontsize=8,
            bbox=dict(facecolor='white',alpha=0.7,edgecolor='lightgray'))
    ax.legend(fontsize=7,loc="lower right")
    ax.set_xlim(0,1)
    ax.set_ylim(0,1.02)

plt.tight_layout()
out="/mnt/data/Proposed_RWMA_ROC_Figure.png"
plt.savefig(out,dpi=300,bbox_inches="tight")
plt.close()

print(out)
