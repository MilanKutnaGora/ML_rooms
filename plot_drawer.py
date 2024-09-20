import pandas as pd
import matplotlib.pyplot as plt
import os

class PlotDrawer:
    def __init__(self):
        self.output_folder = 'plots'
        os.makedirs(self.output_folder, exist_ok=True)

    def draw_plots(self, json_file):
        df = pd.read_json(json_file)
        plot_paths = []

        # Сравнение Gt_corners и Rb_corners
        plt.figure(figsize=(10, 6))
        plt.bar(df['name'], df['Gt_corners'], label='Gt_corners')
        plt.bar(df['name'], df['Rb_corners'], label='Rb_corners', alpha=0.5)
        plt.title('Сравнение Gt_corners и Rb_corners')
        plt.xlabel('Комната')
        plt.ylabel('Количество углов')
        plt.legend()
        plt.xticks(rotation=45)
        path = os.path.join(self.output_folder, 'corners_comparison.png')
        plt.savefig(path)
        plot_paths.append(path)
        plt.close()

        # Сравнение средних значений отклонений
        plt.figure(figsize=(10, 6))
        plt.bar(df['name'], df['mean'], label='Общее')
        plt.bar(df['name'], df['floor_mean'], label='Пол', alpha=0.5)
        plt.bar(df['name'], df['Ceiling_mean'], label='Потолок', alpha=0.5)
        plt.title('Сравнение средних значений отклонений')
        plt.xlabel('Комната')
        plt.ylabel('Среднее отклонение (градусы)')
        plt.legend()
        plt.xticks(rotation=45)
        path = os.path.join(self.output_folder, 'mean_deviations.png')
        plt.savefig(path)
        plot_paths.append(path)
        plt.close()

        # Сравнение максимальных значений отклонений
        plt.figure(figsize=(10, 6))
        plt.bar(df['name'], df['max'], label='Общее')
        plt.bar(df['name'], df['floor_max'], label='Пол', alpha=0.5)
        plt.bar(df['name'], df['Ceiling_max'], label='Потолок', alpha=0.5)
        plt.title('Сравнение максимальных значений отклонений')
        plt.xlabel('Комната')
        plt.ylabel('Максимальное отклонение (градусы)')
        plt.legend()
        plt.xticks(rotation=45)
        path = os.path.join(self.output_folder, 'max_deviations.png')
        plt.savefig(path)
        plot_paths.append(path)
        plt.close()

        return plot_paths