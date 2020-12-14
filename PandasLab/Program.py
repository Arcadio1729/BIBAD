from DataTooler import DataTooler


if __name__ == "__main__":
    source1="C:\\Users\\arcad\\Desktop\\ja\\college\\IT\\BibliotekiAnalizyDanych\\Lab9\\Plant_1_Generation_Data.csv"
    source2="C:\\Users\\arcad\\Desktop\\ja\\college\\IT\\BibliotekiAnalizyDanych\\Lab9\\Plant_2_Generation_Data.csv"

    D = DataTooler(source1,source2)
    D.remove_nan()
    D.convert_column_to_datetime("DATE_TIME")
    D.plot_generator('2020-05-17','2020-05-24','pkci93gMrogZuBj')
    defects=D.find_below(0.8)
