import matplotlib.pyplot as plt
import pandas as pd

#read csv
elisa = pd.read_csv("/Users/maingocv/Library/CloudStorage/GoogleDrive-ngocmai1812@gmail.com/My Drive/Desktop/datascience/2025_AI_Learning/Kaggle_python_course/mock_ELISA_C57BL6.csv")
#print(elisa.head())

#color different vaccine group
for i, (group, group_df) in enumerate(elisa.groupby("Group")):
    color = f"C{i}"

    # plot individual mosue
    for mouse, mouse_df in group_df.groupby("MouseID"):
        plt.plot(mouse_df["Day"], mouse_df["ELISA_Titre"], marker = "o", linestyle="-", label = group, color = color, linewidth=1, alpha = 0.2)

    #calculate mean and std of mouse by days
    #stat_df = group_df.groupby("Day")["ELISA_Titre"].agg(["mean", "std"]).reset_index()
    stat_df = group_df.groupby("Day").agg(mean=("ELISA_Titre", "mean"), std=("ELISA_Titre", "std")).reset_index()
    #stat_df = mouse_df["ELISA_Titre"].agg(["mean", "std"]).reset_index()

    plt.plot(stat_df["Day"], stat_df["mean"], linestyle="-", linewidth=2, color=color)
    plt.errorbar(stat_df["Day"], stat_df["mean"], yerr=stat_df["std"], fmt="o", color=color)


plt.xlabel("dpi")
plt.ylabel("titre")
plt.title("titre over time")
plt.legend()

plt.show()
