from preprocessing import *
from processing import *
from file_utils import *
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import filedialog, simpledialog, Tk, messagebox

def analyse_main(file_path, presitumulation_time=3, baseline_time=12, total_time=30, frequency=40, drop=False, show=False, save_path=None):
    """
    Main entrance for analysing data.
    :param file_path:
    :param presitumulation_time:
    :param baseline_time:
    :param total_time:
    :param frequency:
    :param drop:
    :param show:
    :param save_path:
    :return:
    """
    drop_num = presitumulation_time * frequency
    total_num = total_time * frequency
    base_num = baseline_time * frequency

    data_dict = cvt_file2dict(file_path)
    splitted_dict = split_2_events(data_dict, interval=total_num + drop_num)
    if drop:
        splitted_dict = delete_staring_period(splitted_dict, drop_num=drop_num)

    index = 0
    for key in splitted_dict.keys():

        if key != 'No':
            temp_save_dict = {}
            normalized_list = normalize_2d_list(splitted_dict[key], base_num=base_num)
            for i in range(len(normalized_list)):
                temp_key = "sample-%02d"%i
                temp_save_dict[temp_key] = normalized_list[i].tolist()

            average_list = average_2d_list(normalized_list)
            temp_save_dict["average"] = average_list.tolist()
            data_frame = pd.DataFrame(temp_save_dict)
            if save_path is None:
                csv_path = os.path.join(os.path.dirname(file_path), os.path.basename(file_path).replace('.txt', ""))
                if not os.path.isdir(csv_path):
                    os.mkdir(csv_path)
                data_frame.to_csv(index=True, path_or_buf=os.path.join(csv_path, "%s.csv"%key))
            if show:
                x = np.linspace(0, average_list.shape[0], num=average_list.shape[0])
                plt.subplot(310 + index)
                plt.plot(x, average_list)
                plt.title(key)
        index += 1
    plt.show()


def main():
    """
    GUI guide for users to walk them through all the parameters required.
    :return:
    """
    root = Tk()
    root.withdraw()
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select raw txt files",
                                          filetypes=(("Text File", "*.txt"), ("All Files", "*.*")), parent=root)
    prestimulation_time = simpledialog.askinteger(title="Please input pre-stimulation time (s)",
                                                  prompt="Pre-stimulation time", parent=root)
    baseline_time = simpledialog.askinteger(title="Please input baseline time (s)",
                                            prompt="baseline time", parent=root)
    total_time = simpledialog.askinteger(title="Please input total time (s)",
                                         prompt="total time", parent=root)
    frequency = simpledialog.askinteger(title="Please input frequency (hz)",
                                        prompt="frequency", parent=root)
    drop = messagebox.askyesno("Drop or not", "Would you like to drop the points of prestimulation time")
    show = messagebox.askyesno("Show preview", "Would you like to show the preview")

    analyse_main(filename, prestimulation_time, baseline_time, total_time, frequency, drop, show, None)


main()
