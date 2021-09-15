# -----Oh Soldier Prettify My Folder-----
import os


def soldier(f_path, f_names, f_ext):
    os.chdir(f_path)
    file_list1 = os.listdir()
    with open(f_names) as f:
        file_list2 = [names.strip() for names in f]
    i = 1
    for file in file_list1:
        if os.path.splitext(file)[0] not in file_list2:
            os.rename(file, file.capitalize())
            if os.path.splitext(file)[1] == f_ext:
                os.rename(file, f"{i}. {file}")
                i += 1
        else:
            continue


if __name__ == '__main__':
    # customizable inputs
    folder_path = r"C:\Users\NALIN KR\Documents\Programs\Python_Tutorials\Exercise\Exercise8\Testing"
    file_names = "don't change.txt"
    file_extension = ".jpg"

    soldier(folder_path, file_names, file_extension)
